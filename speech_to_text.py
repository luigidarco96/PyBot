import speech_recognition as sr

r = sr.Recognizer()


def listener():
    with sr.Microphone() as source:
        print("I'm listening...")
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data
