# IoT-Smart-Home-Demo
This project is a smart home demo, in which the **Raspberry Pie** represents the **Controller** that the user is gonna directly interface with. (readings are sent to it and control over the house is through it), the **NodeMCU ESP8266** is the **IoT Platform** used at home to perform the orders sent by the Raspberry Pie and to send back the readings from different sensors, and a regular **PC** is used as a simulation to of a **server** which listens to the readings sent by the NodeMCU and saves the data for statistics and analysis.


Hardware:
- Raspberry Pie (Control)
- NodeMCU ESP8266 (IoT Platform to perform the orders)
- a regular PC

Communication Protocol used:
- Mosquitto MQTT broker

GUI:
- Created by Tkinter


<br/>
> **Note**: Turning on/off devices was simulated by turning on/off LEDS on the NodeMCU by sending a signal from the Raspberry Pie using the GUI. due to the unavailability of any sensors, readings were hardcoded to be sent from the NodeMCU ESP8266 on the MQTT channel on which the Raspberry Pie and the Server are listening to.
