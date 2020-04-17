from flask import Flask, render_template
from api import api
from api.routes import initialise_routes
from digital_assistant.pybot import PyBot
import settings
from multiprocessing import Process, Queue
from miband_manager.miband_api import miband_app
import webbrowser

app = Flask(__name__)
app.register_blueprint(miband_app)

'''
@app.route("/home")
def home():
    steps = 10
    meters = 20
    calorie = 50
    heart_rate = 72
    return render_template("home.html", steps=steps, meters=meters, calorie=calorie, heart_rate=heart_rate)
'''

def init_pybot():
    bot = PyBot(language='en_EN')


def init_miband():
    chrome_path = '/usr/lib/chromium-browser/chromium-browser'
    webbrowser.get(chrome_path).open('http://0.0.0.0/home')


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


if __name__ == "__main__":
    request_queue = Queue()

    PyBotWorker().start()
    AppWorker().start()
    MiBandWorker().start()


