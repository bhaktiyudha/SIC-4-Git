import random
import paho.mqtt.client as mqtt
import time

# MQTT broker settings
broker_address = "broker.hivemq.com"
broker_port = 1883
topic = "testtopic/yudha"


# Callback function when a connection to the broker is established
def on_connect(client, userdata, flags, rc):
    # Generate a random integer between 0 and 10
    random_number = random.randint(0, 10)
    print(f"Connected to MQTT broker and send {random_number} ")
    client.publish(topic, random_number, qos=1)  # Publish the random number to the specified topic
    client.disconnect()

# Create an MQTT client instance
client = mqtt.Client()

# Set the callback function for connection
client.on_connect = on_connect

# Connect to the broker
client.connect(broker_address, broker_port, 60)

try:
    while True:
        # Set the callback function for connection
        client.on_connect = on_connect

        # Connect to the broker
        client.connect(broker_address, broker_port, 60)
        
        # Loop to maintain network traffic flow with the broker
        client.loop_start()

        # Allow time for the message to be published
        time.sleep(1)

        # Disconnect from the broker
        client.loop_stop()

except KeyboardInterrupt:
    pass

