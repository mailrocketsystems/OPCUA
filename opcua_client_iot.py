"""
This is the opc ua client IOT python script
Running this code will connect to a opcua server and will start fetching the parameter values of temperature & pressure
Once we have all the values, we then upload it to IOT platform
Make sure to run the opcua_server.py code first.

Install paho-mqtt python package

NOTE: Change the URL with the IP address of your system. Also update the node id's.
"""

from opcua import Client
import paho.mqtt.client as mqtt
import time
import json

url = "opc.tcp://192.168.0.119:4840"
client = Client(url)
client.connect()
print("OPC UA Client connected")

iot_hub = "demo.thingsboard.io"
port = 1883
username = "iGfJvDyP8CCJfvb7eRS8Lz"  # Paste your access token here
password = ""
topic = "v1/devices/me/telemetry"

iot_hub_client = mqtt.Client()
iot_hub_client.username_pw_set(username, password)
iot_hub_client.connect(iot_hub, port)
print("Connected to IOT hub")

data = dict()
while True:
    try:
        temp = client.get_node("ns=2;i=2")
        press = client.get_node("ns=2;i=3")
        temperature = temp.get_value()
        pressure = press.get_value()
        print(temperature, pressure)

        data["temperature"] = int(temperature)
        data["pressure"] = int(pressure)
        data_out = json.dumps(data)
        iot_hub_client.publish(topic, data_out, 0)

        time.sleep(2)
    except Exception as e:
        print(e)
