import matplotlib.pyplot as plt
import csv
from datetime import datetime


class GraphVisualize:
    def __init__(self, filename, label):
        self.list_of_datetimes = []
        self.list_of_readings = []
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                self.list_of_datetimes.append(datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f"))
                self.list_of_readings.append(int(row[1]))

            plt.figure(label)
            plt.plot_date(self.list_of_datetimes, self.list_of_readings, linestyle='--')
            plt.gcf().autofmt_xdate()
