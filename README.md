# health-analytics
This assignment is a primer for HHA 504/507.

## Summary of Variables
This document represents a lab report with some value interpretations and calculations.

The variables created represent the patient's name, age, sex and fasting blood glucose values.
The dictionary defines additional lab values: patient's weight, HbA1c values and Cholesterol Panel.
The Cholesterol panel is a nesting dictionary that also defines Total Cholesterol, LDL, HDL and Triglycerides values.
The if/elif statements print an interpretation of the patient's fasting blood glucose values.

## Explanation of Function
The function is an Absolute Neutrophil Count (ANC) calculator that uses the White Blood Cell(WBC), Neutrophil, and Band lab results as inputs.
The calculator adds the Neutrophil and Band results together, divides by 100, then multiplies by the White Blood Cell count.
Depending on the calculated result, a different if/else statement will print.

## Expected Output
Based on the input values of 11,000 WBC, 30 Neutrophil and 3 Bands, the expected output is 3,630.
The if/else statment will indicate that this is a normal ANC value.

