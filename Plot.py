# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:22:54 2022

@author: Johannes
"""
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('C:/Users/Johannes/Box/29P/29P 2019 Log.xlsx', sheet_name=4)
a1 = 39
a2 = 37
a3 =38
y1 = 33
y2 = 28
y3 = 30
Color1_3 = [df.iat[52,y1], df.iat[53,y1], df.iat[56,y1], df.iat[57,y1], df.iat[60,y1], df.iat[61,y1], df.iat[64,y1], df.iat[65,y1]]
error1_3 = [df.iat[52,a1], df.iat[53,a1], df.iat[56,a1], df.iat[57,a1], df.iat[60,a1], df.iat[61,a1], df.iat[64,a1], df.iat[65,a1]]
Color1_5 = [df.iat[52,y2], df.iat[53,y2], df.iat[56,y2], df.iat[57,y2], df.iat[60,y2], df.iat[61,y2], df.iat[64,y2], df.iat[65,y2]]
error1_5 = [df.iat[52,a2], df.iat[53,a2], df.iat[56,a2], df.iat[57,a2], df.iat[60,a2], df.iat[61,a2], df.iat[64,a2], df.iat[65,a2]]
Color1_7 = [df.iat[52,y3], df.iat[53,y3], df.iat[56,y3], df.iat[57,y3], df.iat[60,y3], df.iat[61,y3], df.iat[64,y3], df.iat[65,y3]]
error1_7 = [df.iat[52,a3], df.iat[53,a3], df.iat[56,a3], df.iat[57,a3], df.iat[60,a3], df.iat[61,a3], df.iat[64,a3], df.iat[65,a3]]
date1 = [1,2,3,4,5,6,7,8]
plt.rcParams.update({'font.size': 22})
plt.figure()
plt.scatter(date1,Color1_3)
plt.errorbar(date1,Color1_3,yerr=error1_3, fmt="o")
plt.scatter(date1,Color1_5)
plt.errorbar(date1,Color1_5,yerr=error1_5, fmt="o")
plt.scatter(date1,Color1_7)
plt.errorbar(date1,Color1_7,yerr=error1_7, fmt="o")
plt.title("F689M-F487N")

Color2_3 = [df.iat[54,y1], df.iat[58,y1], df.iat[62,y1], df.iat[66,y1]]
error2_3 = [df.iat[54,a1], df.iat[58,a1], df.iat[62,a1], df.iat[66,a1]]
Color2_5 = [df.iat[54,y2], df.iat[58,y2], df.iat[62,y2], df.iat[66,y2]]
error2_5 = [df.iat[54,a2], df.iat[58,a2], df.iat[62,a2], df.iat[66,a2]]
Color2_7 = [df.iat[54,y3], df.iat[58,y3], df.iat[62,y3], df.iat[66,y3]]
error2_7 = [df.iat[54,a3], df.iat[58,a3], df.iat[62,a3], df.iat[66,a3]]
date2 = [1,2,3,4]
plt.figure()
plt.scatter(date2,Color2_3)
plt.errorbar(date2,Color2_3,yerr=error2_3, fmt="o")
plt.scatter(date2,Color2_5)
plt.errorbar(date2,Color2_5,yerr=error2_5, fmt="o")
plt.scatter(date2,Color2_7)
plt.errorbar(date2,Color2_7,yerr=error2_7, fmt="o")
plt.title("F487N-F845M")

Color3_3 = [df.iat[55,y1], df.iat[59,y1], df.iat[63,y1], df.iat[67,y1]]
error3_3 = [df.iat[55,a1], df.iat[59,a1], df.iat[63,a1], df.iat[67,a1]]
Color3_5 = [df.iat[55,y2], df.iat[59,y2], df.iat[63,y2], df.iat[67,y2]]
error3_5 = [df.iat[55,a2], df.iat[59,a2], df.iat[63,a2], df.iat[67,a2]]
Color3_7 = [df.iat[55,y3], df.iat[59,y3], df.iat[63,y3], df.iat[67,y3]]
error3_7 = [df.iat[55,a3], df.iat[59,a3], df.iat[63,a3], df.iat[67,a3]]
date3 = [1,2,3,4]
plt.figure()
plt.scatter(date3,Color3_3)
plt.errorbar(date3,Color3_3,yerr=error3_3, fmt="o")
plt.scatter(date3,Color3_5)
plt.errorbar(date3,Color3_5,yerr=error3_5, fmt="o")
plt.scatter(date3,Color3_7)
plt.errorbar(date3,Color3_7,yerr=error3_7, fmt="o")
plt.title("F689M-F845M")