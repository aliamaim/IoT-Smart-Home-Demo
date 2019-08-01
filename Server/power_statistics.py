import csv
import configuration
from datetime import datetime
import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
matplotlib.use('TkAgg')


class PowerCalculations:
    def __init__(self):
        with open('C:/Users/Ali.Amr/PycharmProjects/Smart_Home/config.csv', 'r') as config_file:
            config_reader = csv.reader(config_file)

            for row_in_config in config_file:
                buttons = row_in_config.split(',')
                for item in buttons[3:]:
                    with open(configuration.houseid + '_' + buttons[1] + '_'
                              + item.lower().replace(' ', '_').rstrip() + '.csv', 'r') as button_data_file:
                        button_data_reader = csv.reader(button_data_file)
                        on_datetime = None
                        off_datetime = None
                        accumulated_time_hr = 0
                        for row_in_button in button_data_reader:
                            difference_time = 0
                            if row_in_button[1] is '1':
                                on_datetime = datetime.strptime(row_in_button[0], "%Y-%m-%d %H:%M:%S.%f")
                            else:
                                off_datetime = datetime.strptime(row_in_button[0], "%Y-%m-%d %H:%M:%S.%f")
                            if on_datetime and off_datetime and on_datetime < off_datetime:
                                difference_time = off_datetime - on_datetime
                                difference_time = difference_time.total_seconds() / 3600  # Seconds to hours
                                accumulated_time_hr += difference_time
                        print("Your " + item + " in your " + buttons[0] + " in house id " + configuration.houseid
                              + " has consumed " + str(accumulated_time_hr * 2) + " kWh of electricity.")

mypower = PowerCalculations()
