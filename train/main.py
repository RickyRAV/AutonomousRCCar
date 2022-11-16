import serial
import time
import requests
from PIL import Image
from io import BytesIO
import uuid

arduino = serial.Serial('COM3', 9600)
time.sleep(2)

#TODO: IMPORT FLASK & FLASK_CORS
from flask import Flask
from flask import Blueprint
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

#start checking
#testTime = 1
#arduino.write(b'forward_on\n')
#time.sleep(testTime)
#arduino.write(b'forward_off\n')
#time.sleep(testTime)
#arduino.write(b'backward_on\n')
#time.sleep(testTime)
#arduino.write(b'backward_off\n')
#time.sleep(testTime)
#arduino.write(b'left_on\n')
#time.sleep(testTime)
#arduino.write(b'left_off\n')
#time.sleep(testTime)
#arduino.write(b'right_on\n')
#time.sleep(testTime)
#arduino.write(b'right_off\n')
#time.sleep(testTime)

def save_data(command):
    for _ in range(0, 10):
        response = requests.get('CameraURL')
    Image.OPEN(BytesIO(response.content)).convert('L').save('../data_tmp/{}_{}.jpg'.format(uuid.uuid1(), command))

@app.route("/forward")
def forward():
    save_data(0)
    arduino.write(b'forward_on\n')
    time.sleep(0.10)
    arduino.write(b'forward_off\n')
    return 'forward'

@app.route("/left")
def left():
    save_data(1)
    arduino.write(b'left_on\n')
    time.sleep(0.5)
    arduino.write(b'forward_on\n')
    time.sleep(0.10)
    arduino.write(b'forward_off\n')
    time.sleep(0.5)
    arduino.write(b'left_off\n')
    return 'left'

@app.route("/right")
def right():
    save_data(2)
    arduino.write(b'right_on\n')
    time.sleep(0.5)
    arduino.write(b'forward_on\n')
    time.sleep(0.10)
    arduino.write(b'forward_off\n')
    time.sleep(0.5)
    arduino.write(b'right_off\n')
    return 'right'

#TODO: MAKE FLASK GET REDIRECTED TO INDEX.HTML & INDEX.JS
if __name__ == "__main__":
    app.run(host='0.0.0.0')
