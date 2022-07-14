# -*- coding: utf-8 -*-
"""
Author: Johannes Allen

Purpose: Script to calculate the Flux and Afrho from fits images

For: Comparative coma morhpology and search for cometary fragments of 29P from HST WFC3 data collected in 2019 and 2021
"""

# Import required libraries and functions
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits
from astropy.stats import sigma_clipped_stats
from photutils import aperture_photometry
from photutils import CircularAperture
import numpy as np
import astropy.units as u
from sbpy.activity import Afrho
from sbpy.data import Ephem
from sbpy.calib import solar_fluxd
import pandas as pd
import math
import openpyxl

# Import data
for x in range(30,31):
    # Open Fits Files
    file = str(x)
    file_name = get_pkg_data_filename('C:/Users/Johannes/Box/29P/2021Data/' + file + '.fits')
    hdul = fits.open(file_name)
    data = hdul[1].data

    # Open Excel files
    i = int(file) - 1
    df = pd.read_excel('C:/Users/Johannes/Box/29P/29P 2021 Log.xlsx', sheet_name=2)
    df2 = pd.read_excel('C:/Users/Johannes/Box/29P/29P 2021 Log.xlsx', sheet_name=1)
    wb = openpyxl.load_workbook('C:/Users/Johannes/Box/29P/29P 2021 Log.xlsx')
    ws = wb.active
    ws2 = wb["Obs Log"]
    ws3 = wb["Afrho"]
    
    #############################################################
    # ~~~~~~~~ Perform aperture photometry to get flux ~~~~~~~~ #
    #############################################################
    
    # Coordinates of Comet Center from Excel sheet (Brightest pixel (manually located in DS9) near the RA & Dec specified in image header)
    position = [(df2.iat[i,9],df2.iat[i,10])]

    # Sigma Clipped Stats
    # Sigma is the clipping threshold, the median background value changes very little as you increase the threshold past 10, so the lowest threshold value of 10 was chosen
    mean, median, std = sigma_clipped_stats(data,sigma=10.0)
    
    # The median pixel value (flux in e-/s) of the image, excluding any pixels that are clipped by the sigma clipped stats 
    bkg_mean = median
    
    # Radius in Pixels 
    radius = 10
    
    # Create a circular aperture centered at 'position' with radius 'radius'
    aperture = CircularAperture(position, r=radius)

    # Open photometry table
    phot = aperture_photometry(data, aperture)
    # Define background median in the table as the mean background value found above
    phot['aper_median'] = bkg_mean 
    # Multiply the median background pixel value (e-/s) by the aperature area (pixels) to get the flux sum of just the background
    phot['aper_bkg'] = bkg_mean * aperture.area
    # Subtract the estimated background flux sum from the measured sum from Aperture Photometry
    phot['aper_sum_bkgsub'] = phot['aperture_sum'] - phot['aper_bkg']
    # Define the Aperture Sum as a variable
    aperture_sum = np.array(phot['aper_sum_bkgsub'])
    # Maintain consistent formatting within the Photometry table
    for col in phot.colnames:
        phot[col].info.format = '%.8g'
        
    # Flux from aperture sum (e-/s)
    flux = aperture_sum[0]
    # Angular radius conversion from pixel radius to arcsec (0.04 factor from HST WFC3 doumentation)
    angRadius = 0.04 * radius
    # Surface brightness
    bright = flux / (np.pi*angRadius**2)
    
    # Error Estimation
    from photutils.utils import calc_total_error
    bkg_only = bkg_mean * np.ones(data.shape)
    effective_gain = 1.5  # seconds
    error = calc_total_error(data, bkg_only, effective_gain)  
    phot_table = aperture_photometry(data - bkg_only, aperture, error=error)  

    #print("Surface Brightness:", bright, "e-/s/arcsec")
    
    #############################################
    # ~~~~~~~~~ Calculate Afrho ~~~~~~~~~~~~~~~ #
    #############################################
    
    # Solar flux from excel sheet (integrated solar flux from HST WFC3 documentation)
    Solar = float(df.iat[i,9])
    # Filter pivot wavelength (integrated wavelength from HST WFC3 documentation)
    Wavelength = float(df.iat[i,8])
    # Inverse sensitivity (converts flux units from image units e-/s to ergs/cm2/A/s)
    PHOTFLAM = float(df.iat[i,7])
    # Comet heliocentric distance from JPL horizons
    rh = float(df.iat[i,4])
    # Distance between the comet and HST from JPL Horizons
    delta = float(df.iat[i,5])
    # angle between the direction to the Sun and the direction to the observer, as seen at the object being observed (from JPL Horizons)
    Phase = float(df.iat[i,3])
    # Calculate the Radius in km given the angular radius and distance between the comet and HST
    Radius = math.tan((angRadius*(np.pi/648000)))*delta*1.496E+8
    # Specify the flux you want to have inputted into the Afrho calculation
    Flux = 600
    
    # Use input parameters from above to calculate Afrho from calculated flux
    solar_fluxd.set({
        'λ8431': Solar * u.Unit('erg/(s cm2 AA)'),
        'λ8431(lambda pivot)': Wavelength * u.AA
        })
    flam = Flux * PHOTFLAM * u.Unit('erg/(s cm2 AA)')
    aper = Radius * u.km
    # Specify comet epheremis
    eph = Ephem.from_dict({'rh': rh * u.au, 'delta': delta * u.au, 'phase': Phase * u.deg})

    afrho = Afrho.from_fluxd('λ8431', flam, aper, eph)

    # Get flux error and afrho error from photometric table 
    flux_error = float(phot_table['aperture_sum_err'])
    flux_err_percent = (flux_error/flux)*100
    afrho_error = afrho*(flux_error/flux)
    afrho_err_percent = (afrho_error/afrho)*100
    
    # Print all desired outputs
    print("File:",x)
    print ("Aperture Radius:", format(radius,".2f"), "pixels /", format(Radius,".2f"), "km")
    print("Flux:", format(flux,".2f"), "e-/s")
    print("Flux error:", format(flux_error,".2f"), "e-/s","(", format(flux_err_percent,".2f"), "%)")
    print("Afrho:", format(afrho,".2f"))
    print("Afrho error:", format(afrho_error,".2f"),"(", format(afrho_err_percent,".2f"), "%)")
    
    # Overwrite excel file in include Flux, Radius, Afrho, and Afrho error
    Row = str(i + 2)
    ws3['K' + Row] = flux
    ws3['L' + Row] = Radius
    ws3['M' + Row] = int(afrho.value)
    ws3['N' + Row] = int(afrho_error.value)
    wb.save('29P 2021 Log.xlsx')
    



