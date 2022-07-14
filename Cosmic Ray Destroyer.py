# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 18:59:46 2021

@author: johan
"""

from pathlib import Path
from astropy.utils.data import get_pkg_data_filename
import numpy as np
from matplotlib import pyplot as plt

from astropy.nddata import CCDData
from astropy.nddata.utils import block_replicate
from astropy import units as u
import ccdproc as ccdp
from photutils import detect_sources



#from convenience_functions import show_image, display_cosmic_rays


file = '1_drz.fits'
image_path = Path('D:/29P/RAW/')
ccd = CCDData.read(image_path / file)
# show_image(ccd, cmap='gray')
ccd = ccd * 1.57 * 



new_ccd = ccdp.cosmicray_lacosmic(ccd, readnoise=10, sigclip=7, verbose=True)
cr_mask = new_ccd.mask
new_ccd.mask.sum() 

threshold = 0.5
n_pixels = 3
crs = detect_sources(new_ccd.mask, threshold, n_pixels)

crs.areas
