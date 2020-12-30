"""
This is the opc ua demo server python script.
Running this script will start a demo opc ua server with default parameters i.e. temperature & pressure.
You can edit the code to add more parameters as per your requirement

NOTE: Change the URL with the IP address of your system. If 4840 port is blocked, you can use any other port

"""

from opcua import Server
from random import randint
import time


server = Server()
url = "opc.tcp://192.168.0.119:4840"
server.set_endpoint(url)
name = "Rocket_Systems_OPCUA_Simulation_Server"
add_space = server.register_namespace(name)

node = server.get_objects_node()
param = node.add_object(add_space, "Parameters")

temp = param.add_variable(add_space, "Temperature", 0)
press = param.add_variable(add_space, "Pressure", 0)
temp.set_writable()
press.set_writable()

server.start()
print("Server started at {}".format(url))

while True:
    temperature = randint(10, 50)
    pressure = randint(200, 999)
    print(temperature, pressure)

    temp.set_value(temperature)
    press.set_value(pressure)

    time.sleep(3)
