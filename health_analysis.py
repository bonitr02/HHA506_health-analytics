# import pandas and rename to pd
import pandas as pd 
# import numpy and rename to np
import numpy as np


patientAge = 55
patientName = 'Harry Smith'
patientSex = 'male'
bloodGlucose = [85, 90, 105, 123]
print('\n')
print('Patient',patientName,'is a', patientAge,'year old', patientSex, 'who has \
provided the following blood glucose results in mg/dL on 5/12/23, 6/19/23, 7/17/23 and 8/10/23:', bloodGlucose)

# dictionary
additional_labs = {
    'Patient Weight in lbs': 192,
    'HbA1c in %': [12,13,9],
    'Cholesterol Panel': {
        'Total Cholesterol': 300,
        'LDL': 260,
        'HDL': 25,
        'Triglycerides': 1000, 
    },
}
print('\n')
print(patientName, 'also presents with', additional_labs)
print('\n')

#if-else statement
print("Please see below for fasting blood glucose interpretations:")
for FBG in bloodGlucose:
    if FBG <= 55:
        print('\n')
        print('You have severe hypoglycemia and should receive medical attention at:', FBG, 'mg/dL')
    elif FBG > 55 and FBG < 70:
        print('\n')
        print('You have hypoglycemia and should eat a snack soon at:', FBG, 'mg/dL')
    elif FBG >= 70 and FBG < 100:
        print('\n')
        print('You have a normal level: ', FBG, 'mg/dL')
    elif FBG >= 100 and FBG <= 125:
        print('\n')
        print('You may have prediabetes at:', FBG, 'mg/dL')
    elif FBG >125 and FBG <= 400:
        print('\n')
        print('You may be diagnosed with diabetes at:', FBG, 'mg/dL')
    elif FBG > 400:
        print('You should seek urgent medical attention at:', FBG, 'mg/dL')

# function calculation and printing
def ANC_Calculator(WBC, Neutrophils, Bands):
    calculatedOutcome = ((Neutrophils + Bands)/ 100) * WBC
    return calculatedOutcome

print('\n')
print("A normal ANC count is between 2,500 and 6,000 cells/mcL")
print('\n')
ANCresult = ANC_Calculator(11000, 30, 3)
print("This is the calculated Absolute Neutrophil Count for",patientName,": " ,ANCresult, "cells/mcL")
print('\n')

print("End of Report")
print('\n')
