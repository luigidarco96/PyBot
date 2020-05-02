import requests
from settings import URL_PYSERVER
import pickle

store_file = 'controllers/store.data'


def login(username, password):
    url = URL_PYSERVER + "/sign-in"
    body = {
        'username': username,
        'password': password
    }
    r = requests.post(url, json=body)

    if r.status_code == 200:
        response = r.json()
        response = response['data']
        user = {
            'username': username,
            'access_token': response['access_token'],
            'refresh_token': response['refresh_token']
        }
        fw = open(store_file, 'wb')
        pickle.dump(user, fw)
        fw.close()
        return True
    else:
        return False


def logout():
    fw = open(store_file, 'wb')
    pickle.dump('', fw)
    fw.close()


def is_auth():
    try:
        fd = open(store_file, 'rb')
        user = pickle.load(fd)
        if user['access_token'] != '':
            return True
        else:
            return False
    except:
        print("Store doesn't exist")
        return False


def get_username():
    try:
        fd = open(store_file, 'rb')
        user = pickle.load(fd)
        if user['username'] != '':
            return user['username']
        else:
            return ''
    except:
        return ''


def send_data(type, value):
    url = URL_PYSERVER + "/" + type
    body = {
        'value': value,
    }
    try:
        fd = open(store_file, 'rb')
        user = pickle.load(fd)
        if user['access_token'] != '':
            headers = {'Authorization': 'Bearer {}'.format(user['access_token'])}
            r = requests.post(url, json=body, headers=headers)
            if r.status_code == 200:
                return True
            else:
                return False
        else:
            return False
    except:
        return False
