import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()


def listener():

    with mic as source:
        print("I'm listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_sphinx(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data
