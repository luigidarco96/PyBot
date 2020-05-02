from flask import Blueprint, render_template, request, redirect, url_for
from miband_manager.auth import MiBand3
from controllers.http_controller import is_auth, login, logout, get_username, send_data
import threading

miband_app = Blueprint('', __name__, template_folder="templates")
miband = None

heart_rate_value = '--'


@miband_app.route('/home')
def home():
    if is_auth():
        global miband
        if miband is None:
            return render_template("home_log.html", name=get_username())
        else:
            steps, meters, fatgram, calorie = get_fitness_data()
            global heart_rate_value
            return render_template("home.html", name=get_username(), steps=steps, meters=meters, calorie=calorie, heart_rate=heart_rate_value)
    else:
        return redirect(url_for('.login_view'))


@miband_app.route('/login')
def login_view():
    return render_template('login.html')


@miband_app.route('/login/error')
def login_error():
    return render_template('login.html', message='Username or Password wrong')


@miband_app.route('/login_server', methods=['POST'])
def login_server():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if login(username, password):
        return redirect(url_for('.home'))
    else:
        return redirect(url_for('.login_error'))


@miband_app.route('/connect', methods=["POST"])
def connect_miband():
    mac_address = request.form.get('macAddress', "")
    if mac_address == "":
        return "Something goes wrong. Try again!"
    else:
        global miband
        miband = MiBand3(mac_address, debug=True)
        miband.setSecurityLevel(level='medium')
        miband.initialize()
        miband.authenticate()
        return redirect(url_for('.home'))


@miband_app.route('/logout')
def logout_view():
    logout()
    global  miband
    miband = None
    return redirect(url_for('.login_view'))


def get_fitness_data():
    global miband
    values = miband.get_steps()
    send_data('steps', values['steps'])
    send_data('meters', values['meters'])
    send_data('calories', values['calories'])
    get_heart_rate()
    return values['steps'], values['meters'], values['fat_grams'], values['calories']


def hr_callback(x):
    global heart_rate_value
    heart_rate_value = x
    print(x)


def hr():
    miband.get_heart_rate(heart_measure_callback=hr_callback)


def get_heart_rate():
    thread1 = threading.Thread(target=hr, args=())

    thread1.start()

    thread1.join()

    global heart_rate_value
    print(heart_rate_value)
