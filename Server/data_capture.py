import paho.mqtt.client as mqtt
import configuration
import csv
from datetime import datetime

broker_url = "iot.eclipse.org"
broker_port = 1883


def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " + rc)


def on_message(client, userdata, message):
    timestamp = datetime.now()
    print(timestamp)
    print(message.topic + " Received: " + message.payload.decode())
    # Store temperature readings in a csv file with the format [datetime, temperature]
    # Each room temperature data is stored in a separate file with file code indicating who it belongs to
    if configuration.houseid in message.topic and \
            "temperature" in message.topic:
        parsed_filename = message.topic.replace("/", "_")  # Replace each / with _ since / is not allowed in filenames
        with open(parsed_filename + ".csv", "a", newline='') as csv_file:
            write_file = csv.writer(csv_file)
            write_file.writerow([timestamp, message.payload.decode()])

    if configuration.houseid in message.topic and \
            "light" in message.topic:
        parsed_filename = message.topic.replace("/", "_")
        with open(parsed_filename + ".csv", "a", newline='') as csv_file:
            write_file = csv.writer(csv_file)
            write_file.writerow([timestamp, message.payload.decode()])


client = mqtt.Client("G2K_Server_Analytics")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_url, broker_port)
client.subscribe(configuration.houseid + "/#")
client.loop_forever()
