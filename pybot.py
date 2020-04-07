from speech_to_text import listener
from text_to_speech import talk
from action_handler import ActionHandler


class PyBot(object):
    name = 'PyBot'
    username = ''
    wake_words = ['hey {}'.format(name)]
    action_handler = ActionHandler(speaker=talk)

    def __init__(self, name='PyBot'):
        self.name = name
        print("Hello, I'm {}. How can I help you?".format(name))
        talk("Hello, I'm {}. How can I help you?".format(name))
        while True:
            data = listener()

            if self.__handle_wake_up(data):
                data = data.replace("hey pybot", "")
                self.action_handler(data)

    def __handle_wake_up(self, text):
        text = text.lower()

        for phrase in self.wake_words:
            if phrase in text:
                return True

        return False









