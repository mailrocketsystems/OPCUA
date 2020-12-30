"""
This is the opc ua client python script
Running this code will connect to a opcua server and will start fetching the parameter values of temperature & pressure
Make sure to run the opcua_server.py code first.

NOTE: Change the URL with the IP address of your system. Also update the node id's.
"""

from opcua import Client
import time

url = "opc.tcp://192.168.0.119:4840"
client = Client(url)
client.connect()

while True:
    temp = client.get_node("ns=2;i=2")
    press = client.get_node("ns=2;i=3")
    temperature = temp.get_value()
    pressure = press.get_value()
    print(temperature, pressure)
    time.sleep(2)
