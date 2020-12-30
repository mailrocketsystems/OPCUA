# OPCUA

This project contains python script for OPC UA server and client.

When running the scripts, make sure to update the IP address of the system in URL. 
OPC UA server will start the server with default parameters i.e. pressuer and temperature. Edit it as per your requirements.
In opc ua client code, update the node id of the parameters accordingly. You can get the node id from the ua expert software.

OPC UA CLIENT IOT code connected to the opc server code and upload data to thingsboard.io
thingsboard.io is a free to use iot hub platform. In the code, make sure to update the username with access token you get from the device in thingsboard.io

Here is the link to the dashboard which I have created: https://demo.thingsboard.io/dashboard/8d9e6de0-4aad-11eb-b612-b99d709195c3?publicId=abf32860-1f7e-11e8-913e-c3b186e30863

![](/img/img2.PNG)
