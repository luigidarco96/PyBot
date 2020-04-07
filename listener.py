import speech_recognition as sr


class Listener(object):
    language = 'en_EN'
    r = sr.Recognizer()
    mic = sr.Microphone()

    def __init__(self, language='en_EN'):
        self.language = language

    def listen(self):
        with self.mic as source:
            print("I'm listening...")
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)

        data = ""
        try:
            data = self.r.recognize_google(audio, language=self.language)
            print("You said: " + data)
        except sr.UnknownValueError:
            print("Google Speech Recognition did not understand audio")
        except sr.RequestError as e:
            print("Request Failed; {0}".format(e))
        return data
