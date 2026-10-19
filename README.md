# Simulated Device Monitoring and Alert System
 
**Student Name:** Jon Danielle G. Pizarro

**Student Number:** 2601279

**Section:** 1CPE-B
 
## Project Description
The Simulated Device Monitoring and Alert System is a Python program that stores and monitors simulated device temperature readings. It allows users to view readings, add valid readings, classify temperatures, and generate a numerical summary. It also determines the overall device status based on the temperature classifications. 
 
## Objectives
- To practice using core Python features—such as variables, lists, loops, conditions, and functions all in a single project
- To let users view existing temperature records and input new ones.
- To validate temperature readings and accept only whole numbers from 0 to 100.
- To classify temperatures as NORMAL, WARNING, or CRITICAL.
- To calculate the total, average, minimum, maximum, category counts, and overall status.
- To develop skills in testing, debugging, documentation, and version control.
 
## Features
1. Displays the initial temperature readings: 28, 31, 35, 37, and 29.
2. Allows users to add valid temperature readings.
3. Rejects empty, non-numeric, decimal, negative, and above-100 inputs.
4. Classifies readings below 30 °C as NORMAL.
5. Classifies readings from 30 °C to 35 °C as WARNING.
6. Classifies readings above 35 °C as CRITICAL.
7. Generates a numerical summary with category counts and percentages.
8. Determines the overall device status.
9. Repeats the menu until the user selects Exit.
10. Handles invalid menu choices without terminating the program.

## Requirements
- Python 3
- Visual Studio Code
- Git and Github account
 
## How to Run
1. Save the Python program as device_monitor.py.
2. Open the project folder in a code editor.
3. Run the program using Python 3.
4. Select an option from the menu.
5. Follow the instructions displayed by the program.
6. Select option 5 to exit.
 
## Sample Output
```
SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: _

CURRENT READINGS
----------------
Reading 1: 28 °C
Reading 2: 31 °C
Reading 3: 35 °C
Reading 4: 37 °C

READING CLASSIFICATION
----------------------
28 °C -> NORMAL
31 °C -> WARNING
35 °C -> WARNING
37 °C -> CRITICAL
29 °C -> NORMAL

MONITORING SUMMARY
------------------
Number of readings : 5
Total of readings : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL : 2 (40.00%)
WARNING : 2 (40.00%)
CRITICAL : 1 (20.00%)

Thank you for using the Device Monitoring System.
```
 
## Test Cases
I performed 10 tests.  10 passed and 0 failed.
Full details are in test_cases.md.
 
## Known Limitations
- The program stores readings only while it is running.
- Added readings are lost when the program closes.
- The program does not maintain a permanent history of readings.
 
## Reflection
Putting all the pieces together—the menu, input validation, temperature classification, and calculations—was definitely the most challenging part. I realized how important input validation is to protect the dataset from incorrect numbers. Testing exact boundaries, such as 30 °C and 35 °C, really deepened my understanding of conditional statements. If i were to improve  it somehow, I would try to add a file saving so data isn't lost when the program closes.