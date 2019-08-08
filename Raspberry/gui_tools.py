from tkinter import *
import tkinter.font as tkFont
import configuration


class ToggleButton:
    def __init__(self, x, y, text, frame, frame_code):
        self.x = x
        self.y = y
        self.button_state = False
        self.button_prev_state = False

        self.button_canvas = Canvas(master=frame, width=50, height=50, bg='LightGrey', highlightthickness=0)
        self.button_canvas.place(x=self.x+120, y=self.y)
        self.button_oval_id = self.button_canvas.create_oval(10, 10, 30, 30, width=2, fill='red4')

        self.button = Button(frame, text=text, pady=3, command=self.button_callback)
        self.button.configure(font=("Corbert", 10, "bold"))
        self.button.place(x=self.x, y=self.y)

        self.topic = configuration.houseid + "/" + frame_code + "/" + text.lower().replace(" ", "_")

    def button_callback(self):
        self.button_state = not self.button_state
        if self.button_state:
            self.button_canvas.itemconfigure(self.button_oval_id, fill="SpringGreen2")
        else:
            self.button_canvas.itemconfigure(self.button_oval_id, fill="red4")


class ReadingMeter:
    def __init__(self, x, y, text, frame, frame_code):
        self.x = x
        self.y = y
        self.reading = StringVar()
        self.reading.set("0")
        var_name = Label(frame, text=text)
        self.display = Label(frame, textvariable=self.reading)  # we need this Label as a variable
        self.display.place(x=self.x+120, y=self.y)
        var_name.place(x=self.x, y=self.y)

        self.topic = configuration.houseid + "/" + frame_code + "/" + text.lower().replace(" ", "_")


class FrameCreate:
    def __init__(self, width, height, x, y, text, button_names, meter_names, frame_code):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.frame_code = frame_code

        self.button_names = button_names
        self.meter_names = meter_names

        self.frame = None
        self.buttons = []
        self.meters = []
        self.code = frame_code

    def create(self, master):
        # Creating the frame which will be parent to all buttons/meters in it.
        self.frame = Frame(master=master, width=self.width, height=self.height,
                           bd=3, relief=RIDGE, bg="LightGray", colormap="new")
        self.frame.place(x=self.x, y=self.y)
        ##################################

        # Creating the title
        title = Button(master=master, text=self.text, relief=FLAT, state=DISABLED)
        title_font = tkFont.Font(family="Corbert", size=15, weight="bold")
        title.configure(font=title_font)
        # Centering the title according to it's size
        title.place(x=self.x + ((self.width - tkFont.Font.measure(title_font, self.text)) / 2), y=self.y + 10)
        ###################################

        # Creating the toggle buttons
        button_location_y = 100  # Relative to the parent frame
        for button_name in self.button_names:
            button = ToggleButton(10, button_location_y, button_name, self.frame, self.frame_code)
            self.buttons.append(button)
            button_location_y += 70

        # Creating meters (sensors,etc..)
        meter_location_y = button_location_y
        for meter_name in self.meter_names:
            meter = ReadingMeter(10, meter_location_y, meter_name, self.frame, self.frame_code)
            self.meters.append(meter)
            meter_location_y += 50
        ##################################

