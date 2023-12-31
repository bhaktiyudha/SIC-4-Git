import math
import random
import time

import requests
from ubidots import ApiClient

TOKEN = "BBFF-bOXJfK0ohlRBQ0bOsGE9IXUo3H5eus"  # Put your TOKEN here
DEVICE_LABEL = "machine"  # Put your device label here
VARIABLE_LABEL_1 = "temperature"  # Put your first variable label here
VARIABLE_LABEL_2 = "humidity"  # Put your second variable label here
VARIABLE_LABEL_3 = "position"  # Put your second variable label here

api = ApiClient(token=TOKEN)


def build_payload(variable_1, variable_2, variable_3):
    # Creates two random values for sending data
    value_1 = random.randint(-10, 50)
    value_2 = random.randint(0, 85)

    # Creates a random gps coordinates
    lat = random.randrange(34, 36, 1) + \
        random.randrange(1, 1000, 1) / 1000.0
    lng = random.randrange(-83, -87, -1) + \
        random.randrange(1, 1000, 1) / 1000.0
    payload = {variable_1: value_1,
               variable_2: value_2,
               variable_3: {"value": 1, "context": {"lat": lat, "lng": lng}}}

    return payload


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print("[INFO] Request code :", req.status_code,",Payload :", req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] Request made properly, your device is updated")
    return True


def main():
    payload = build_payload(
        VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3)
    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] Finished send data")


if __name__ == '__main__':
    # Add Switch ID
    switch = api.get_variable('64d712c530002d00104e2199')
    # Add Slider ID
    slider = api.get_variable('64d728a503c304000fa913b4')
    while (True):
        try:
            print("[INFO] ---------------- ")
            main()
            time.sleep(1)
            switch_last_value = switch.get_values(1)
            slider_last_value = slider.get_values(1)
            print("[INFO] Slider Value",slider_last_value[0]['value'])
            # Then you can read this value and do something:
            if switch_last_value[0]['value']:
                print("[INFO] Switch is ON")
            else:
                print("[INFO] Switch is OFF")
        except:
            print("[ERROR] Connection to Ubidots Error")