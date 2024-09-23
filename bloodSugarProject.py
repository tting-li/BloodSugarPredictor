#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 20:53:26 2023

@author: tingtingli
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import CubicSpline

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#carb
carb = input("what is the total carb value of your meal?")
while isfloat(carb) != True or (float(carb) < 0):
    carb = input("Enter a valid number: what is the total carb value of your meal?")

carb = float(carb)

#gi
gi = input("what is the gi value of your meal?")
while isfloat(gi) != True or (float(gi) < 0):
    gi = input("Enter a valid number: what is the gi value of your meal?")

gi = float(gi)
if gi <= 55:
    giLevel = "LOW"
elif gi <= 69:
    giLevel = "MEDIUM"
else:
    giLevel = "HIGH"

#fiber
fiber = input("what is the fiber value of your meal?")

while isfloat(fiber) != True or (float(fiber) < 0):
    fiber = input("Enter a valid number: what is the fiber value of your meal?")

fiber = float(fiber)

#net carb and gl values
netCarb = carb - fiber
while netCarb < 0:
    print("Fiber value should be greater than total carb value. Please restart the program.")
gl = (gi * netCarb)/100

#gl values
if gl <= 10:
    print("GL value of your meal: " + str(gl) + ". This is a LOW value.")
    glLevel = "LOW"
elif gl <= 19:
    print("GL value of your meal: " + str(gl) + ". This is a MEDIUM value.")
    glLevel = "MEDIUM"
else:
    print("GL value of your meal: " + str(gl) + ". This is a HIGH value.")
    glLevel = "HIGH"

print("GI value of your meal: " + str(gi) + ". This is a " + giLevel + " value.")

#data sets -- personal experiment
if glLevel == "HIGH" and giLevel == "MEDIUM":
    print("Example blood sugar change from Ting Ting's personal study")
    print("Increasing Rate: 0.622 (mg/dL)/min, Decreasing Rate: 0.400 (mg/dL)/min, Max Blood Sugar: 154 mg/dL")
    y = np.array([98, 110, 119, 154, 127, 119, 118])
    edition = "GL: High, GI: Medium"

if glLevel == "LOW" and giLevel == "LOW":
    print("Example blood sugar change from Ting Ting's personal study")
    print("Increasing Rate: 1.25 (mg/dL)/min, Decreasing Rate: 0.533 (mg/dL)/min, Max Blood Sugar: 143 mg/dL")
    y = np.array([68, 118, 143, 109, 107, 78, 79])
    edition = "GL: Low, GI: Low"
    
if glLevel == "MEDIUM" and giLevel == "LOW":
    print("Example blood sugar change from Ting Ting's personal study")
    print("Increasing Rate: 1.533 (mg/dL)/min, Decreasing Rate: 0.842 (mg/dL)/min, Max Blood Sugar: 188 mg/dL")
    y = np.array([96, 151, 188, 138, 145, 117, 87])
    edition = "GL: Medium, GI: Low"
    
if glLevel == "HIGH" and giLevel == "HIGH":
    print("Example blood sugar change from Ting Ting's personal study")
    print("Increasing Rate: 0.844 (mg/dL)/min, Decreasing Rate: 0.844 (mg/dL)/min, Max Blood Sugar: 181 mg/dL")
    y = np.array([105, 113, 156, 181, 168, 165, 105])
    edition = "GL: High, GI: High"
    
if glLevel == "MEDIUM" and giLevel == "MEDIUM":
    print("Example blood sugar change from Ting Ting's personal study")
    print("Increasing Rate: 0.533 (mg/dL)/min, Decreasing Rate: 0.844 (mg/dL)/min, Max Blood Sugar: 153 mg/dL")
    y = np.array([105, 115, 151, 153, 125, 142, 122])
    edition = "GL: Medium, GI: Medium"
    
#plotting
x = np.array([0, 30, 60, 90, 120, 150, 180])
func = CubicSpline(x, y, bc_type='clamped')
model = np.linspace(x.min(), x.max(), 100)
fig = plt.figure(num=1, clear=True)
plt.plot(model, func(model),'m-')
plt.xlabel("Time After Insulin Injection (Min)")
plt.xticks(np.arange(0,210, step=30))
plt.xlim(0,180)
plt.ylabel("Blood Sugar (mg/dL)")
plt.yticks(np.arange(0,250, 30))
plt.legend()
plt.grid()
plt.title("Blood Sugar (mg/dL) Change Over Time (min) -- " + edition + " Edition")





    
    
