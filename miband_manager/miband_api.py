from flask import Blueprint, render_template, request, redirect, url_for
from .auth import MiBand3

miband_app = Blueprint('', __name__, template_folder="templates")
miband = None


@miband_app.route('/home')
def home():
    global miband
    if miband is None:
        return render_template("home_log.html")
    else:
        steps, meters, fatgram, calorie = get_fitness_data()
        return render_template("home.html", steps=steps, meters=meters, calorie=fatgram)


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


def get_fitness_data():
    global miband
    values = miband.get_steps()
    heart_rate = 0
    return values['steps'], values['meters'], values['fat_grams'], values['calories']
