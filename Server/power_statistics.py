import csv
import configuration
from datetime import datetime
import matplotlib
matplotlib.use('TkAgg')


class PowerCalculations:
    def __init__(self):
        with open('C:/Users/Ali.Amr/PycharmProjects/Smart_Home/config.csv', 'r') as config_file:
            config_reader = csv.reader(config_file)

            for row_in_config in config_file:
                buttons = row_in_config.split(',')
                for item in buttons[3:3+int(buttons[2])]:
                    # in he config CSV file
                    # 2nd column in the row represents frame code and 3rd column represents number of devices in frame
                    # The preceding columns are the devices names (that's where we start iterating)
                    # so houseid_frameid_devicename.csv gives us the CSV file name
                    with open(configuration.houseid + '_' + buttons[1] + '_'
                              + item.lower().replace(' ', '_').rstrip() + '.csv', 'r') as button_data_file:
                        button_data_reader = csv.reader(button_data_file)
                        on_datetime = None       # Time at which the lights were turned on
                        off_datetime = None      # Time at which the lights were turned off
                        accumulated_time_hr = 0  # Overall lights on time
                        # in the CSV that contains the data of the intended device there are 2 columns, first is the
                        # datetime and the second is the value of the order (ON/OFF)
                        for row_in_button in button_data_reader:
                            if row_in_button[1] is '1':
                                on_datetime = datetime.strptime(row_in_button[0], "%Y-%m-%d %H:%M:%S.%f")
                            else:
                                off_datetime = datetime.strptime(row_in_button[0], "%Y-%m-%d %H:%M:%S.%f")
                            # Make sure we have the first on_datetime & off_datetime readings (None initially)
                            # Also make sure the on_datetime is bigger than the off_datetime to avoid
                            # desync between readings (for example ON OFF ON OFF)
                            # We want the first 2 to be paired with each other and same for the second without allowing
                            # the middle OFF ON to be considered valid related readings
                            if on_datetime and off_datetime and on_datetime < off_datetime:
                                difference_time = off_datetime - on_datetime
                                difference_time = difference_time.total_seconds() / 3600  # Seconds to hours
                                accumulated_time_hr += difference_time
                        print("Your " + item.rstrip() + " in your " + buttons[0] + " in house id " + configuration.houseid
                              + " has consumed " + str(accumulated_time_hr * 2) + " kWh of electricity.")
