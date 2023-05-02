# COMP_CE_450_Intellignet_Gate_System_Project_G22

This project is about the Intelligent Gate System.The project was designed to collect data from a sensor connected to an ESP microcontroller and transmit that data to a Raspberry Pi using MQTT protocol. The Raspberry Pi was configured as a broker to receive the data and make decisions based on that data to control a servo motor. The data was also uploaded to the cloud for remote monitoring and analysis.

To implement this system, the following steps were taken:

Sensor data collection: A sensor was connected to an ESP microcontroller to collect data. The data was read by the ESP microcontroller and transmitted to the Raspberry Pi using MQTT protocol.

MQTT Broker setup: The Raspberry Pi was configured as an MQTT broker using a software like Mosquitto. The broker was set up to listen to a specific topic where the sensor data was being transmitted from the ESP microcontroller.

Decision making and servo motor control: A Python script was written to process the incoming data on the Raspberry Pi. The script made decisions based on the data received and controlled the servo motor accordingly.

Cloud data upload: The data collected from the sensor and the servo motor was uploaded to the cloud for remote monitoring and analysis. This was achieved by configuring the Python script to upload the data to a cloud platform like AWS IoT Core, Azure IoT Hub or Google Cloud IoT Core.

Overall, this project demonstrated how data can be collected from a sensor, transmitted using MQTT protocol, and processed on a Raspberry Pi to make decisions and control a servo motor. The integration of cloud data upload allowed for remote monitoring and analysis of the system.
