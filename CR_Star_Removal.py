# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 11:58:04 2022

@author: Johannes
"""
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits
from astropy.stats import sigma_clipped_stats
from photutils import aperture_photometry
from photutils import CircularAperture
import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import simple_norm
import astropy.units as u
from sbpy.activity import Afrho
from sbpy.data import Ephem
from sbpy.calib import solar_fluxd
import pandas as pd
import math
import openpyxl

# Open Fits Files
x=2
file = str(x)
file_name = get_pkg_data_filename('C:/Users/Johannes/Box/29P/Data/' + file + '.fits')
hdul = fits.open(file_name)
data = hdul[1].data

# Open Excel files
i = int(file) - 1
df = pd.read_excel('C:/Users/Johannes/Box/29P/29P 2019 Log.xlsx', sheet_name=2)
df2 = pd.read_excel('C:/Users/Johannes/Box/29P/29P 2019 Log.xlsx', sheet_name=1)
wb = openpyxl.load_workbook('C:/Users/Johannes/Box/29P/29P 2019 Log.xlsx')

    
#############################################################
# ~~~~~~~~ Perform aperture photometry to get flux ~~~~~~~~ #
#############################################################
    
# Coordinates of Comet Center from Excel sheet (Brightest pixel (manually located in DS9) near the RA & Dec specified in image header)

data[2716,2545] = 0.01
data[2715,2545] = 0.01
data[2716,2546] = 0.01
data[2715,2546] = 0.01
for x in range(2555,2560):
    data[2713,x] = 0.01
    data[2714,x] = 0.01
    data[2715,x] = 0.01
    data[2716,x] = 0.01
    data[2717,x] = 0.01
    data[2718,x] = 0.01
    data[2719,x] = 0.01
for x in range(2548,2552):
    data[2710,x] = 0.01
    data[2711,x] = 0.01
    data[2712,x] = 0.01
    data[2713,x] = 0.01
    data[2714,x] = 0.01
    data[2715,x] = 0.01



fits.writeto('C:/Users/Johannes/Box/29P/Processed/2.fits', data, overwrite=True)

