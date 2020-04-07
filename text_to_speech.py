from gtts import gTTS
from pygame import mixer


def talk(string):
    tts = gTTS(text=string, lang="en", slow=False)
    tts.save("speech.mp3")
    mixer.init()
    mixer.music.load("speech.mp3")
    mixer.music.play()

