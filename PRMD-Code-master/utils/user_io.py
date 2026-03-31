"""
Created in part by Martin McLaren c2645410
No AI was used in the creation of this code
"""
import os
import time
import settings
from utils import file_io, server
import gyro_accel
import strain_gauge

gyro_accel_measured = False
strain_gauge_measured = False

def ask_sensor_type():
    print("in ask sensor type")
    global gyro_accel_measured
    global strain_gauge_measured
    choice = -1

    valid_answers = [0,3] # 0 for exit, 3 for upload

    print("Please choose a sensor type:")
    if gyro_accel_measured == False:
        print("[1] Gyroscope & Accelerometer")
        valid_answers.append(1)
    if strain_gauge_measured == False:
        print("[2] Strain Gauge")
        valid_answers.append(2)
    print("[0] Exit and save data")

    while not input_valid(valid_answers, choice):
        choice = int(input())
        if input_valid(valid_answers, choice):
            break
        print(f"Input of {choice} is not valid. Try again.")


    return choice

def input_valid(valid_inputs, choice):
    if choice not in valid_inputs:
        return False
    return True



def user_flow():
    global gyro_accel_measured
    global strain_gauge_measured
    print("In user_flow")
    choice = -1
    session_start = time.time()
    gyro_accel_data = {}
    strain_gauge_data = {}
    while True:
        if gyro_accel_measured is False or strain_gauge_measured is False:
            choice = ask_sensor_type()
            print(f"You chose: {choice}")
        if choice == 0:
            break
        if choice == 1:
            gyro_accel_data = gyro_accel.run_session()
            gyro_accel_measured = True
            print("Gyro Accel data:")
            print(gyro_accel_data)
        if choice == 2:
            strain_gauge_data = strain_gauge_data = strain_gauge.run_session()
            strain_gauge_measured = True
            print("Strain Gauge data:")
            print(strain_gauge_data)
    final_readings = {}
    # final_readings["session_start"] = session_start

    print("Gyro Accel data:")
    print(gyro_accel_data)

    print("Strain Gauge data:")
    print(strain_gauge_data)

    if gyro_accel_data:
        final_readings["gyro_accel"] = gyro_accel_data
    if strain_gauge_data:
        final_readings["strain_gauge"] = strain_gauge_data

    if not final_readings:
        print("No data gathered or written.")
        return

    print("Final Readings:")
    print(final_readings)

    file_name = f"{session_start}.json"
    path_to_write = os.path.join(os.getcwd(), settings.SESSION_DIR, file_name)
    file_io.write_to_json_file(path_to_write, final_readings)

