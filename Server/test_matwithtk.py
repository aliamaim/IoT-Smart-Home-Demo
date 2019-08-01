import glob
import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
matplotlib.use('TkAgg')


class PlotList:
    def __init__(self, master):
        self.master = master
        self.button = Button(master, text="Plot", command=self.plot)
        self.button.pack()

    def plot(self):
        for frame in configuration.frames_g:
            for button in frame.buttons:
                for file in glob.glob(button.topic + ".csv"):
                    print(file)
        x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        p = np.array([16.23697, 17.31653, 17.22094, 17.68631, 17.73641, 18.6368,
                      19.32125, 19.31756, 21.20247, 22.41444, 22.11718, 22.12453])

        fig = Figure(figsize=(3, 3))
        a = fig.add_subplot(111)
        a.plot(p, range(2 + max(x)), color='blue')

        a.set_title("Estimation Grid", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.get_tk_widget().pack(side=LEFT)
        canvas.draw()


window = Tk()
start = PlotList(window)
window.mainloop()
