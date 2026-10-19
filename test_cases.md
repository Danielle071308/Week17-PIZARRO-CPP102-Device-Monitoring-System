# Test Cases: Simulated Device Monitoring and Alert System

Name: Jon Danielle G. Pizarro  
Student Number: 2601279  
Section: 1CPE-B  
Date Tested: October 18, 2026  

## Test Cases

I made these test cases to check if my program works correctly. I tested valid and invalid inputs to see if the program displays the correct results and handles mistakes properly.

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Select option 1 to view readings. | The program displays 28, 31, 35, 37, and 29. | The program displayed all five readings. | Pass |
| TC02 | Select option 2 and enter 33, then select option 1. | The program accepts 33 and adds it to the readings. | Reading added successfully. | Pass |
| TC03 | Select option 2 and enter abc. | The program rejects the input and displays an error message. | Invalid choice. Please enter a number from 1 to 5. | Pass |
| TC04 | Select option 2 and enter -5. | The program rejects the input. | Invalid reading. Enter a value from 0 to 100. | Pass |
| TC05 | Select option 2 and enter 120. | The program rejects the input. | Invalid reading. Enter a value from 0 to 100. | Pass |
| TC06 | Add the reading 30, then select option 3. | 30 °C -> WARNING | 30 °C -> WARNING | Pass |
| TC07 | Choose 3, check boundary 35 | 35 °C -> WARNING | 35 °C -> WARNING | Pass |
| TC08 | Restart the program and select option 4. | CountNumber of readings: 5, Total of readings: 160, Average: 32.00, Minimum: 28, Maximum: 37, NORMAL: 2, WARNING: 2, CRITICAL: 1, Overall Status: ATTENTION REQUIRED. | The program displayed the correct summary and overall status. | Pass |
| TC09 | Enter 9 at the menu. | The program displays an invalid choice message and shows the menu again. | Invalid choice. Please enter a number from 1 to 5. | Pass |
| TC10 | Select option 5. | The program displays an exit message and stops running. | Thank you for using the Device Monitoring System. | Pass |

## Bugs Found and Fixed

During testing, I did not find any bugs in the ten test cases. The program displayed the expected results for valid readings, rejected invalid readings, classified temperatures correctly, generated the correct summary, and exited when I selected option 5.

## Testing Notes

1. I ran each test case and compared the actual result with the expected result.
2. I marked each test as Pass because the results matched the expected results.