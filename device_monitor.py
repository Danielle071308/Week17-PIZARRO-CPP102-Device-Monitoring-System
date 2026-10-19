#Week 17 - Device Monitoring and Alert System
"""Simulated Device Monitoring and Alert System for CPP102 Week 17."""

def get_initial_readings():
    """Return the initial simulated temperature readings."""
    initial_readings = [28, 31, 35, 37, 29]
    return initial_readings

def is_whole_number(text):
    """Return True when text represents a whole number, including negatives."""
    if len(text) == 0:
        return False

    start = 0
    if text[0] == "-":
        start = 1

    if start == len(text):
        return False

    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False

    return True

def get_valid_integer(prompt, lowest, highest):
    """Keep asking until the user enters a whole number within the range."""
    while True:
        text = input(prompt)

        if len(text) == 0:
            print("Invalid input. The reading cannot be empty.")
        elif not is_whole_number(text):
            print("Invalid input. Enter a whole number only.")
        else:
            value = int(text)

            if value < lowest or value > highest:
                print(f"Invalid reading. Enter a value from {lowest} to {highest}.")
            else:
                return value

def add_reading(readings):
    """Validate one new reading and append it only when valid."""
    text = input("Enter new reading: ")

    if len(text) == 0:
        print("Invalid input. The reading cannot be empty.")
    elif not is_whole_number(text):
        print("Invalid input. Enter a whole number only.")
    else:
        reading = int(text)

        if reading < 0 or reading > 100:
            print("Invalid reading. Enter a value from 0 to 100.")
        else:
            readings.append(reading)
            print("Reading added successfully.")

def classify_reading(reading, warning_limit, critical_limit):
    """Return the classification for one temperature reading."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"

def compute_total(readings):
    """Return the total of all readings using a loop."""
    total = 0

    for reading in readings:
        total = total + reading

    return total

def compute_average(readings):
    """Return the average of the readings."""
    if len(readings) == 0:
        return 0

    total = compute_total(readings)
    number_of_readings = len(readings)
    average = total / number_of_readings

    return average

def find_minimum(readings):
    """Return the smallest reading using a loop."""
    minimum = readings[0]

    for reading in readings:
        if reading < minimum:
            minimum = reading

    return minimum

def find_maximum(readings):
    """Return the largest reading using a loop."""
    maximum = readings[0]

    for reading in readings:
        if reading > maximum:
            maximum = reading

    return maximum
