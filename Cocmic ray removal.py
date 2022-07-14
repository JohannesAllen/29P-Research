# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:40:32 2020
@author: Johannes Allen 
For: Removal of Cosmic Rays for HST WFC3 Observations of Comet 29P

Documentation:
Astropy: https://docs.astropy.org/en/stable/
Astroscrappy: https://astroscrappy.readthedocs.io/_/downloads/en/stable/pdf/
    
"""
# Import packages
# Import fits from Astropy
from astropy.io import fits
# Import detect_cosmics function from astroscrappy (as dc for simplification)
from astroscrappy import detect_cosmics as dc 
from astropy.utils.data import get_pkg_data_filename

data = ['2']
for dat in data:
    # Directory location in which the unprocessed data is located
    image_file = get_pkg_data_filename('D:/29P/RAW/'+dat+'_drz.fits')
    # Load the data information from the fits file
    data = fits.getdata(image_file, ext = 0)
    # Load the header information from the fits file
    head = fits.getheader(image_file, ext = 0)

    # gain = 1.57 for HST WFC3 (Data Handbook (5.1.1))
    # readnoise = approx. 3 for HST WFC3 (Data Handbook 5.1.2)
    # Start at Default values: sigclip=4.5, sigfrac=0.3
    # Decrease sigclip & sigfrac to mark more objects as cosmics
    mask, _clean = dc(data, inmask=None, sigclip=0.0000001, sigfrac=0.01, objlim=10.0, gain=1.57, readnoise=3, satlevel=65535, pssl=0.0, niter=10, sepmed=True, cleantype='meanmask', fsmode='median', psfmodel='gauss', psffwhm=5.5, psfsize =7, psfk=None, psfbeta=4.765, verbose=False)
    
    # Location of folder you want to save the new file in
    fits.writeto('D:/29P/Processed/'+dat+'_cr.fits', _clean, head, overwrite=True)
