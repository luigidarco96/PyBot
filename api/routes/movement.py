from flask_restplus import Resource
from easygopigo3 import EasyGoPiGo3
from api import api
import time

gpg = EasyGoPiGo3()
distance_sensor = gpg.init_distance_sensor()
min_distance = 100
GPG_SPEED = 150

ns = api.namespace('', "Operations related to movements")


@ns.route('/forward')
class MoveForward(Resource):

    def get(self):
        """
        Move the robot forward
        """
        gpg.set_speed(GPG_SPEED)

        distance = distance_sensor.read_mm()
        while distance > min_distance:
            print("Distance: {}".format(distance))
            try:
                distance = distance_sensor.read_mm()
                time.sleep(.1)
                gpg.backward()
            except IOError:
                gpg.stop()
                return "Error"
        gpg.stop()


@ns.route('/backward')
class MoveBackward(Resource):

    def get(self):
        """
        Move the robot backward
        """
        gpg.set_speed(GPG_SPEED)
        for i in range(0, 5000):
            gpg.forward()
        gpg.stop()


@ns.route('/leftward')
class MoveLeftward(Resource):

    def get(self):
        """
        Move the robot leftward
        """
        gpg.set_speed(GPG_SPEED)
        gpg.turn_degrees(-30)
        gpg.stop()


@ns.route('/rightward')
class MoveRightward(Resource):

    def get(self):
        """
        Move the robot rightward
        """
        gpg.set_speed(GPG_SPEED)
        gpg.turn_degrees(30)
        gpg.stop()
