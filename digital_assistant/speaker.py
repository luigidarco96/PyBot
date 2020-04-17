from gtts import gTTS
from pygame import mixer
from googletrans import Translator


class Speaker(object):
    language = 'en'
    translator = Translator()

    def __init__(self, language='en'):
        if len(language) > 2:
            self.language = language[0:2]
        else:
            self.language = language

    def talk(self, string):
        phrase = self.translator.translate(string, dest=self.language).text
        tts = gTTS(text=phrase, lang=self.language, slow=False)
        tts.save("speech.mp3")
        mixer.init()
        mixer.music.load("speech.mp3")
        mixer.music.play()
