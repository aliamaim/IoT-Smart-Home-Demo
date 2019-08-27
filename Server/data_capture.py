import paho.mqtt.client as mqtt
import configuration
import Server.power_statistics as ps
import csv
from datetime import datetime
import os.path


def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " + rc)


def on_message(client, userdata, message):
    timestamp = datetime.now()
    # Each file contains data related to only 1 meter/switch(history)
    # For example the lights in the bedroom in house a000 is stored in a file named a000_bed_light.csv
    if configuration.houseid in message.topic:
        if "filerequestm" in message.topic:
            topic = message.topic.split('/')[2]
            f = open(topic+'.csv', "rb")
            file_content = f.read()
            byte_arr = bytearray(file_content)
            client.publish(topic=configuration.houseid + "/filesendm" + "/" + topic, payload=byte_arr,
                           qos=0, retain=False)
            return
        elif "filerequestp" in message.topic:
            print("Entered here")
            topic = message.topic.split('/')[2]
            myPower = ps.PowerCalculations(topic)
            calculations = myPower.calculate()
            for item in calculations:
                client.publish(topic=configuration.houseid + "/filesendp" + "/" + topic, payload=item,
                               qos=0, retain=False)

        if "filesendm" or "filesendd" in message.topic:
            return

        if os.path.exists('C:/Users/Ali.Amr/PycharmProjects/Smart_Home/config.csv'):
            with open("C:/Users/Ali.Amr/PycharmProjects/Smart_Home/config.csv", 'r') as config_file:
                csv_reader = csv.reader(config_file)
                for row in csv_reader:
                    devices_number = int(row[2])
                    for device_name in row[3:3+devices_number]:
                        # If the topic contains the houseid & device_name, store the data
                        # Store device ON/OFF commands in a csv file with the format [datetime, ON/OFF]
                        if device_name.lower().replace(" ", "_") in message.topic:
                            # Replace each / with _ since / is not allowed in filenames
                            parsed_filename = message.topic.replace("/", "_")
                            with open(parsed_filename + ".csv", "a", newline='') as data_file:
                                write_file = csv.writer(data_file)
                                write_file.writerow([timestamp, message.payload.decode()])

                    for meter_name in row[3+devices_number+1:]:
                        # If the topic contains the houseid & meter_name, store the data
                        # Store meter readings in a csv file with the format [datetime, readings]
                        if meter_name.lower().replace(" ", "_") in message.topic:
                            # Replace each / with _ since / is not allowed in filenames
                            parsed_filename = message.topic.replace("/", "_")
                            with open(parsed_filename + ".csv", "a", newline='') as data_file:
                                write_file = csv.writer(data_file)
                                write_file.writerow([timestamp, message.payload.decode()])
    else:
        print("Configuration file is not found!")


client = mqtt.Client("G2K_Server_Analytics")
client.on_connect = on_connect
client.on_message = on_message
client.connect(configuration.broker_url, configuration.broker_port)
client.subscribe(configuration.houseid + "/#")
client.loop_forever()
