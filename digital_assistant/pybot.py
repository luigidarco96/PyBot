from digital_assistant.speaker import Speaker
from digital_assistant.listener import Listener
from digital_assistant.action_manager import ActionManager
import os
import sys


class PyBot(object):
    name = 'PyBot'
    wake_words = ['hey {}'.format(name)]
    language = 'en_EN'
    speaker = None
    listener = None
    action_handler = None

    def __init__(self, name='PyBot', language='en_EN'):
        print("Hello I'm {}, My language is: {}".format(name, language))
        self.name = name
        self.language = language
        self.speaker = Speaker(language=language)
        self.listener = Listener(language=language, source=1, audio_file="digital_assistant/AudioCommands.wav")
        self.action_handler = ActionManager(speaker=self.speaker, language=language)

        self.__start()

    def __start(self):
        self.speaker.talk("Hello, I'm {}".format(self.name))
        while True:

            # if self.__handle_wake_up(data):
            # data = data.replace("hey pybot", "")
            # self.action_handler(data)

            data = self.listener.listen()
            self.action_handler.handle_decision(data)

    def __handle_wake_up(self, text):
        text = text.lower()

        for phrase in self.wake_words:
            if phrase in text:
                return True

        return False
