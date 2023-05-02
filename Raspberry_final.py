import paho.mqtt.client as mqtt
import requests
import time
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

servo = GPIO.PWM(25, 50) # Set up PWM on GPIO 25 at 50Hz
servo.start(0) # Start the PWM with a duty cycle of 0

def set_servo_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(25, True)
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(25, False)
    servo.ChangeDutyCycle(0)


# ThingSpeak settings
WRITE_API_KEY = 'PE42EUGGFXS614FT' #EZG57ZK1F6W00ENZ
CHANNEL_ID = '2125585' #2117752

# Global variable to hold the received value
sensor_value = 0

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe("test_topic")

def on_message(client, userdata, msg):
    global sensor_value  # Use the global variable
    print(msg.topic + " " + str(msg.payload))
    sensor_value = int(msg.payload)  # Store the received value

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_start()  # Start the MQTT client loop

# Main loop
while True:
    # Send sensor data to ThingSpeak
    url = f'https://api.thingspeak.com/update?api_key={WRITE_API_KEY}&field1={sensor_value}'
    response = requests.get(url)
    if response.status_code == 200:
        print("sensor value sent") #f'Sent sensor value: {sensor_value}'
    else:
        print('Error sending data')
    
    if sensor_value > 500:
        set_servo_angle(180) # Move the servo to its minimum position
        time.sleep(2)
    else:
        set_servo_angle(0) # Move the servo to its minimum position
        time.sleep(2)
        

    # Wait 15 seconds before sending the next data point
    time.sleep(3)
