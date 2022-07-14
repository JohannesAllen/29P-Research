# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 18:01:38 2021

@author: johan
"""

import numpy as np
from astropy.modeling.models import Gaussian2D
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
from astropy.visualization import simple_norm

file = '1'
file_name = get_pkg_data_filename('C:/Users/Johannes/Box/29P/Data/' + file + '.fits')
hdul = fits.open(file_name)
data = hdul[1].data
head = fits.getheader(file_name, ext = 0)

import matplotlib.pyplot as plt
plt.close('all')
plt.imshow(data, origin='lower')
plt.title("Data")

from astropy.nddata import Cutout2D
from astropy import units as u
position = (2567, 2709)
size = (100, 100)     # pixels
cutout = Cutout2D(data, position, size)
size = u.Quantity((100, 100), u.pixel)
cutout = Cutout2D(data, position, size)
cutout = Cutout2D(data, position, (100, 100))
norm = simple_norm(data, 'sqrt', percent=99)
plt.imshow(cutout.data, origin='lower', norm=norm)
plt.title("Data")
from photutils import find_peaks
peaks_tbl = find_peaks(cutout.data, threshold=5)
peaks_tbl['peak_value'].info.format = '%.8g' # for consistent table output
x_peak = np.array(peaks_tbl['x_peak'])
y_peak = np.array(peaks_tbl['y_peak'])
x_pos = 50
y_pos = 50

import polarTransform

polarImage, ptSettings = polarTransform.convertToPolarImage(cutout.data, center=[x_pos,y_pos], initialRadius = 0., finalRadius = 100., initialAngle = 0, finalAngle = 2*np.pi)
plt.figure()
polarImage1 = polarImage.T
plt.imshow(polarImage1, origin='lower', norm=norm)
plt.title("Polar Image")
#fits.writeto('C:/Users/Johannes/Box/29P/Polar/'+file+'_polar.fits', polarImage, head, overwrite=True) 
cutout2 = Cutout2D(polarImage1, (200,35), (70,400))
plt.figure()
plt.imshow(cutout2.data, origin='lower', norm=norm)
plt.title("Cropped Polar Image")

CartImage1, ptSettings = polarTransform.convertToCartesianImage(polarImage)
#plt.figure()
#plt.imshow(CartImage1, origin='lower', norm=norm)

avg = np.average(polarImage, axis=0)
polarImage_subtract = polarImage - avg
#plt.figure()
#plt.imshow(polarImage_subtract, origin='lower', norm=norm)

Range = []
for i in range(0,139):
    x = float(i)
    Range.append(x)

Range = np.array(Range)
PolarSum = np.sum(polarImage, axis=0)
#plt.figure()
#plt.imshow((Range,PolarSum), origin='lower', norm=norm)

CartImage2, ptSettings = polarTransform.convertToCartesianImage(polarImage_subtract, initialAngle = 0., finalAngle = 2*(np.pi))
#plt.figure()
#plt.xlim([200,900])
#plt.ylim([200,900])
#plt.imshow(CartImage2, origin='lower', norm=norm)
#fits.writeto('C:/Users/Johannes/Box/29P/ComaAvg/'+file+'_avg_subtract.fits', CartImage2, overwrite=True)

med = np.median(polarImage, axis=0)
polarImage_subtractMed = polarImage - med
polarImage_subtractMed = polarImage_subtractMed.T
cutout3 = Cutout2D(polarImage_subtractMed, (200,35), (70,400))
plt.figure()
plt.imshow(cutout3.data, origin='lower', norm=norm)
plt.title("Median Subtracted Polar Image")

CartImage3, ptSettings = polarTransform.convertToCartesianImage(polarImage_subtractMed.T, initialAngle = 0., finalAngle = 2*(np.pi))
plt.figure()
plt.xlim([50,250])
plt.ylim([50,250])
plt.imshow(CartImage3, origin='lower', norm=norm)
plt.title("Azimuthal Median Subtracted")

#CartImage4, ptSettings = polarTransform.convertToCartesianImage(med, initialAngle = 0., finalAngle = 2*(np.pi))
plt.figure()
plt.imshow(med, origin='lower', norm=norm)
plt.title('Azimuthal Median')

