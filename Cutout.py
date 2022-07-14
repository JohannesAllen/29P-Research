# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 12:12:43 2022

@author: Johannes
"""
from astropy.nddata.utils import Cutout2D
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
import polarTransform

file1 = '2'
file_name1 = get_pkg_data_filename('C:/Users/Johannes/Box/29P/2021Data/' + file1 + '.fits')
hdul1 = fits.open(file_name1)
data1 = hdul1[1].data
i1 = int(file1) - 1
df_1 = pd.read_excel('C:/Users/Johannes/Box/29P/29P 2021 Log.xlsx', sheet_name=2)
df2_1 = pd.read_excel('C:/Users/Johannes/Box/29P/29P 2021 Log.xlsx', sheet_name=1)

#file2 = '3'
#file_name2 = get_pkg_data_filename('C:/Users/Johannes/Box/29P/Data/' + file2 + '.fits')
#hdul2 = fits.open(file_name2)
#data2 = hdul2[1].data
#i2 = int(file2) - 1
#df_2 = pd.read_excel('C:/Users/Johannes/Box/29P/Comet 29P.xlsx', sheet_name=3)
#df2_2 = pd.read_excel('C:/Users/Johannes/Box/29P/Comet 29P.xlsx', sheet_name=0)

#file3 = '6'
#file_name3 = get_pkg_data_filename('C:/Users/Johannes/Box/29P/Data/' + file3 + '.fits')
#hdul3 = fits.open(file_name3)
#data3 = hdul3[1].data
#i3 = int(file3) - 1
#df_3 = pd.read_excel('C:/Users/Johannes/Box/29P/Comet 29P.xlsx', sheet_name=3)
#df2_3 = pd.read_excel('C:/Users/Johannes/Box/29P/Comet 29P.xlsx', sheet_name=0)

#file4 = '7'
#file_name4 = get_pkg_data_filename('C:/Users/Johannes/Box/29P/Data/' + file4 + '.fits')
#hdul4 = fits.open(file_name4)
#data4 = hdul4[1].data
#i4 = int(file4) - 1
#df_4 = pd.read_excel('C:/Users/Johannes/Box/29P/Comet 29P.xlsx', sheet_name=3)
#df2_4 = pd.read_excel('C:/Users/Johannes/Box/29P/Comet 29P.xlsx', sheet_name=0)

position_1 = (df2_1.iat[i1,9],df2_1.iat[i1,10])
#position_2 = (df2_2.iat[i2,9],df2_2.iat[i2,10])
#position_3 = (df2_3.iat[i3,9],df2_3.iat[i3,10])
#position_4 = (df2_4.iat[i4,9],df2_4.iat[i4,10])

size = (100, 100)     # pixels
cutout1 = Cutout2D(data1, position_1, size)
plt.figure()
norm = simple_norm(data1, 'sqrt', percent=99)
plt.imshow(cutout1.data, origin='lower', norm=norm)

polarImage, ptSettings = polarTransform.convertToPolarImage(cutout1.data, center=[50,50], initialRadius = 0., finalRadius = 100., initialAngle = 0, finalAngle = 2*np.pi)
plt.figure()
plt.imshow(polarImage, origin='lower', norm=norm)

avg = np.average(polarImage, axis=0)
polarImage_subtract = polarImage - avg

width = []
for i in range(1,114):
    width.append(i)

#plt.figure()
#plt.imshow((avg,width), origin = 'lower', norm=norm)

# Creating histogram
fig, axs = plt.subplots(1, 1,
                        figsize =(10, 7),
                        tight_layout = True)
 
n_bins=100
axs.hist(avg, bins = n_bins)
 
# Show plot
plt.show()
np.savetxt("avg.csv", avg, delimiter=",")

#cutout2 = Cutout2D(data2, position_2, size)
#plt.figure()
#norm = simple_norm(data2, 'sqrt', percent=99)
#plt.imshow(cutout2.data, origin='lower', norm=norm)

#cutout3 = Cutout2D(data3, position_3, size)
#plt.figure()
#norm = simple_norm(data2, 'sqrt', percent=99)
#plt.imshow(cutout3.data, origin='lower', norm=norm)

#cutout4 = Cutout2D(data4, position_4, size)
#plt.figure()
#norm = simple_norm(data4, 'sqrt', percent=99)
#plt.imshow(cutout4.data, origin='lower', norm=norm)

#stack = np.array(cutout1.data) + np.array(cutout2.data) + np.array(cutout3.data) + np.array(cutout4.data)

#plt.figure()
#norm = simple_norm(stack, 'sqrt', percent=99)
#plt.imshow(stack, origin='lower', norm=norm)

#fits.writeto('C:/Users/Johannes/Box/29P/ComaAvg/F487ND1_sum.fits', cutout1.data, overwrite=True)



