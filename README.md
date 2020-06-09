# PyBot

PyBot is a robot infrastructure that aims to collect data from the user's wristband, to interact with the user and to take decisions according to user's emotion. The interaction with the user is provided using speech and speech recognition facilities.

PyBot is developed in Python and it is designed to run on Raspberry Pi 3.

## Installation

In this section are described all the steps required to install and deploy the PyBot

### Step 1 - Software requirements

All the commands in this step must be run in the terminal.

- Install the latest version of Raspian OS
- Install the latest version of Python3
- Install the latest version of pip3
- Install the GoPigo2 Software

```bash
sudo curl -kL dexterindustries.com/update_gopigo3 | bash
sudo reboot
```

- Install sensors library

```bash
curl -kL dexterindustries.com/update_sensors | bash
```

- Install pyaudio

```bash
sudo apt-get install python3-pyaudio
```

- Install flac

```bash
sudo apt-get install flac
```

- Install libhdf5-dev

```bash
sudo apt-get install libhdf5-dev
```

- Move into the project root folder

- Install python requirements

```bash
sudo pip3 install -r requirements.txt
```

### Step 2 - Configuration

- In the project root folder open the file "settings.py"

```python
URL_PYSERVER = 'http://192.168.43.115:3000'

PYBOT_LANGUAGE = 'en_EN'
```

- Change the **URL\_PYSERVER** with the URL of your PyServer instance
- Change the **PYBOT\_LANGUAGE** with the language that you prefer. The languages availabe are:
  - **en\_EN**: English
  - **it\_IT**: Italian
  - **es\_ES**: Spanish
  - **zh-cn**: Chinese

### Step 3 - Deployment

- From the terminal app move into the root folder of the project
- Run the command:

```bash
sudo python3 main.py
```
