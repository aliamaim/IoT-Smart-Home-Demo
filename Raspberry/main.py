from tkinter import *
from tkinter import ttk
import paho.mqtt.client as mqtt
import configuration
import Raspberry.visualization as vis
import sys
import os

# Page number is used for the periodic updating of the windows
# to avoid trying to update(access) a non-existent/destroyed frame
page = 0

running = True


def exit_app():
    global running
    running = False
    master.destroy()


# Called when the python application successfully connects to the MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " + rc)


def on_publish(client, userdata, result):
    print("data published \n")
    pass


# Called when an MQTT message is received
def on_message(client, userdata, message):
    if configuration.houseid in message.topic:
        if "/filesendm" in message.topic:
            topic = message.topic.split('/')[2]
            f = open(topic+".csv", "w", newline='')
            f.write(message.payload.decode())
            f.close()
            vis.GraphCreate(topic, topic)
            os.remove(topic+".csv")
            return
        elif "/filesendp" in message.topic:
            print(message.payload.decode())
            return
        main_page.update_meters(message.topic, message.payload.decode())


# Establishing MQTT Connection
client = mqtt.Client("G2K_RaspberryPie3_x01")
client.on_connect = on_connect
client.on_message = on_message
client.connect(configuration.broker_url, configuration.broker_port)
client.subscribe(configuration.houseid + "/#", qos=1)
###########


class MainPage:
    def __init__(self, root):
        self.frames = []
        self.root = root
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.focus_set()
        self.root.title("Smart Home")
        if os.path.exists('C:/Users/Ali.Amr/PycharmProjects/Smart_Home/config.csv'):
            self.list_of_frames = configuration.initialize_from_save()
        else:
            configuration.initialize_first_time()
            self.list_of_frames = configuration.initialize_from_save()

        for frame in self.list_of_frames:
            frame.create(self.root, self.vis_callback, self.power_callback)

    def vis_callback(self, topic):
        client.publish(topic=configuration.houseid + "/filerequestm" + "/" + topic.replace("/", "_"),
                       payload=str(1), qos=0, retain=False)  # m in filerequestm stands for meter
        self.power_callback("bed")

    def power_callback(self, topic):
        client.publish(topic=configuration.houseid + "/filerequestp" + "/" + topic,
                       payload=str(1), qos=0, retain=False)  # d in filerequestd stands for device

    def update_meters(self, topic, value):
        for frame in self.list_of_frames:
            for meter in frame.meters:
                if topic == meter.topic:
                    meter.reading.set(value)
                    break

    def update(self):
        # constantly update the GUI
        self.root.update()

        for frame in self.list_of_frames:
            for button in frame.buttons:
                # Check if visualize_button states changed (ignore redundant)
                if button.button_state != button.button_prev_state:
                    client.publish(topic=button.topic, payload=int(button.button_state), qos=1, retain=False)
                    button.button_prev_state = button.button_state


master = Tk()
master.protocol("WM_DELETE_WINDOW", exit_app)
main_page = MainPage(master)

while 1:
    if running:
        main_page.update()
    else:
        sys.exit(0)
    # constantly check if any messages arrived on subscribed topics
    client.loop()


'''
class StartPage:
    def __init__(self, root):
        self.root = root

        # Initiating the configuration page
        self.config_page = Toplevel(root)
        self.setup = None

        # Initiating the main page
        self.mapp = Toplevel(root)
        self.main = None

        # Initializing the master
        self.master = root
        self.master.geometry("{0}x{1}+0+0".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.master.focus_set()
        self.master.title("Welcome to G2K: Smart Home")

        # Ask the user if he wants to configure the app or not
        msg = Label(self.master, text="Do you want to configure your house?")
        msg.place(x=500, y=500)
        self.yes_button = Button(self.master, text="Yes", pady=3, command=self.yes_callback)
        self.yes_button.configure(font=("Corbert", 10, "bold"))
        self.yes_button.place(x=550, y=550)
        self.no_button = Button(self.master, text="No", pady=3, command=self.no_callback)
        self.no_button.configure(font=("Corbert", 10, "bold"))
        self.no_button.place(x=600, y=550)

    def yes_callback(self):
        global page
        page = 1
        self.setup = ConfigurationPage(self.config_page, self.root)
        self.config_page.update()
        self.master.withdraw()

    def no_callback(self):
        global page
        page = 2
        self.main = MainPage(self.mapp, self.root)
        self.mapp.tkraise()
        self.master.withdraw()

    def update(self):
        # constantly update the GUI
        self.master.update()
'''
'''
class ConfigurationPage:

    def __init__(self, root, master):
        self.master = master
        self.frames = []
        self.root = root
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.focus_set()
        self.root.title("Configuration")

        self.back_button = Button(self.root, text="Back", pady=3, command=self.go_back)
        self.back_button.configure(font=("Corbert", 10, "bold"))
        self.back_button.place(x=1300, y=20)

    def go_back(self):
        global page
        page = 0
        self.root.withdraw()
        self.master.deiconify()

    def update(self):
        # constantly update the GUI
        self.root.update()
'''
