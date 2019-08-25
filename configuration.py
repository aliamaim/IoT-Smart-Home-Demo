import Raspberry.gui_tools as gui
import csv
from tkinter import *


houseid = "a000"  # To be modified so that it's configured by user/program and saved in the config.csv
# standard frame width & height
frame_width = 250
frame_height = 650
broker_url = "test.mosquitto.org"
broker_port = 1883


# Set up the configuration file according to the user preferences for future use
def initialize_first_time():
    with open("C:/Users/Ali.Amr/PycharmProjects/Smart_Home/config.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        frames_number = convert_input_to_int("How many rooms is your home?: ")
        for i in range(frames_number):
            frame_name = input("What is the name of this room?: ")
            frame_code = frame_name.lower().split()[0]  # If name is Living Room id will be --> living

            devices_number = convert_input_to_int("How many digital(ON/OFF) devices you wish to control?: ")
            frame_info = [frame_name, frame_code, devices_number]
            for j in range(devices_number):
                frame_info.append(input("Device " + str(j + 1) + " name: "))

            meters_number = convert_input_to_int("How many meters(ex: Temperature) do you wish to read?: ")
            frame_info.append(meters_number)
            for j in range(meters_number):
                frame_info.append(input("Meter " + str(j + 1) + " name: "))
            csv_writer.writerow(frame_info)


# Initialize the application from configuration file (already configured)
def initialize_from_save():
    with open("C:/Users/Ali.Amr/PycharmProjects/Smart_Home/config.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        frame_x = 20
        list_of_frames = []
        for row in csv_reader:
            frame_name = row[0]
            frame_code = row[1]
            devices_number = row[2]
            devices_names = []
            meters_names = []
            for device_name in row[3:3+int(devices_number)]:
                devices_names.append(device_name)
            for meter_name in row[3+int(devices_number)+1:]:
                meters_names.append(meter_name)
            frame = gui.FrameCreate(frame_width, frame_height, frame_x, 20, frame_name, devices_names,
                                    meters_names, frame_code)
            list_of_frames.append(frame)
            frame_x += 290
        return list_of_frames


# Try to convert text to int if it's not an int raise a ValueError
def convert_input_to_int(prompt_text):
    try:
        number = int(input(prompt_text))
        return number
    except ValueError:
        print("The input was not a valid number")