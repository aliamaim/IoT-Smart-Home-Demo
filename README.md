# IoT-Smart-Home-Demo
This project is a smart home demo, in which the **Raspberry Pie** represents the **Controller** that the user is gonna directly interface with. (readings are sent to it and control over the house is through it), the **NodeMCU ESP8266** is the **IoT Platform** used at home to perform the orders sent by the Raspberry Pie and to send back the readings from different sensors, and a regular **PC** is used as a simulation of a **server** which listens to the readings sent by the NodeMCU and saves the data for statistics and analysis.
All these nodes are connected through the MQTT channel.

Data is saved in CSV files (comma seperated values) since it's very light and simple so it can be transfered easily.
The server has a data capture script that always listens to the house published messages so it records the following: sensors values with the datetime (ex: office_temperature 37 18/3/2018:1:34:12) and digital device action with the datetime (ex: office_light ON 14/7/2018:12:00:00).


- Sensor values are graphed using matplotlib.
- Power statistics is calculated using a script and displayed for user.
- Application has been tested on Raspberry Pie Model 3 (with Raspbian OS on it) and it works.

#### Hardware:
- Raspberry Pie (Control)
- NodeMCU ESP8266 (IoT Platform to perform the orders)
- a regular PC

#### Communication Protocol used:
- Mosquitto MQTT broker

#### GUI:
- Created by Tkinter
- The GUI is dynamic, you can start it for the first time in which you choose how many rooms, room names, digital devices and sensors in each room which will generate the GUI     suitable for your choices dynamically then a configuration file is created with the info you entered so that next times the system would check for it and if found it will just   start the GUI without asking you again for the data (Loading)


> **Note**: Turning on/off devices was simulated by turning on/off LEDS on the NodeMCU by sending a signal from the Raspberry Pie using the GUI. due to the unavailability of any sensors, readings were hardcoded to be sent from the NodeMCU ESP8266 on the MQTT channel on which the Raspberry Pie and the Server are listening to.


[![Watch the video](https://img.youtube.com/vi/fDDsRHOdZU8/1.jpg)](https://youtu.be/fDDsRHOdZU8)
