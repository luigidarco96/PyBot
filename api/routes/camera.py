from flask import Flask, Response
from flask_restplus import Resource
from api import api
from controllers.camera_controller import Camera

ns = api.namespace('camera', 'Operations related to Robot Camera')


@ns.route('/stream')
class CameraApi(Resource):

    def get(self):
        """
        Return robot camera stream
        """
        return Response(gen(Camera()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
