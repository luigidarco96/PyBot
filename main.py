from flask import Flask
from api import api
from api.routes import initialise_routes
from digital_assistant.pybot import PyBot
import settings
from multiprocessing import Process, Queue
from ui_manager.manager import miband_app
from emotion_manager import handle_emotion

app = Flask(__name__)
app.register_blueprint(miband_app)


def init_pybot():
    bot = PyBot(language=settings.PYBOT_LANGUAGE)


def init_miband():
    print('')
    # webview.create_window('PyBot', 'http://0.0.0.0/hello')
    # webview.start()


def init_emotion():
    handle_emotion()


def configure_app(flask_app):
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialise_app(flask_app):
    configure_app(flask_app)

    api.init_app(flask_app)
    initialise_routes(api)

    flask_app.run(host='0.0.0.0', port=80, debug=True, use_reloader=False)


class MiBandWorker(Process):

    def __init__(self):
        super(MiBandWorker, self).__init__()

    def run(self):
        print("===== Start MiBand =====")
        init_miband()


class PyBotWorker(Process):

    def __init__(self):
        super(PyBotWorker, self).__init__()

    def run(self):
        print("===== Start PyBot =====")
        initialise_app(app)


class AppWorker(Process):

    def __init__(self):
        super(AppWorker, self).__init__()

    def run(self):
        print("===== Start App =====")
        init_pybot()


class EmotionWorker(Process):

    def __init__(self):
        super(EmotionWorker, self).__init__()

    def run(self):
        print("===== Start Emotion Recognition =====")
        init_emotion()


if __name__ == "__main__":
    request_queue = Queue()

    PyBotWorker().start()
    AppWorker().start()
    MiBandWorker().start()
    EmotionWorker().start()


