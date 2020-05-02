from flask import Flask
import os
import time
import calendar
import picamera
import requests
from settings import URL_PYSERVER
from digital_assistant.speaker import Speaker
from settings import PYBOT_LANGUAGE
from measurements import image_timer

app = Flask(__name__)
dir_name = os.path.dirname(__file__)
image_save_path = dir_name + "/images/"


def handle_emotion():
    while True:
        emotion = get_emotion()

        if emotion is not None:
            Speaker(language=PYBOT_LANGUAGE).talk('it seems you are {}. Can I do something for you?'.format(emotion))

        time.sleep(5)


@image_timer
def get_emotion():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)

        timestamp = calendar.timegm(time.gmtime())
        image_name = str(timestamp) + ".jpg"

        # Camera warm-up time
        time.sleep(2)
        camera.capture(os.path.join(image_save_path, image_name))

        url = URL_PYSERVER + "/emotion-recognition"

        files = {'image': open(image_save_path + image_name, 'rb')}
        response = requests.post(url, files=files)

        if response.status_code == 200:
            message = response.json()
            return message['message']
        else:
            return None
