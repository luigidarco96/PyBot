import speech_recognition as sr
import time
from measurements import speech_timer

class Listener(object):
    language = 'en_EN'
    r = sr.Recognizer()

    source_offset = 0
    source_type = 0 # 0: Microphone - 1: File
    origin = ""

    def __init__(self, language='en_EN', source=0, audio_file=""):
        self.language = language
        self.source_type = source
        if source == 0:
            self.origin = sr.Microphone()
        else:
            self.origin = sr.AudioFile(audio_file)

    @speech_timer
    def listen(self):
        if self.source_type == 0:
            audio = self.__record_from_microphone()
        else:
            audio = self.__record_from_file()

        data = ""
        try:
            data = self.r.recognize_google(audio, language=self.language)
            print("You said: " + data)
        except sr.UnknownValueError:
            print("Google Speech Recognition did not understand audio")
        except sr.RequestError as e:
            print("Request Failed; {0}".format(e))
        return data

    def __record_from_microphone(self):
        with self.origin as source:
            print("I'm listening...")
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)

            return audio

    def __record_from_file(self):
        with self.origin as source:
            print("I'm listening")
            audio = self.r.record(source, offset=self.source_offset, duration=5)

            self.source_offset = (self.source_offset + 5) % 25
            time.sleep(5)

            return audio

