from os import listdir
from os.path import isfile, join
import random
from pygame import mixer
import os
import sys

dir_name = os.path.dirname(sys.modules['__main__'].__file__)
music_dir = dir_name + "/music"  # change to music
onlyfiles = [f for f in listdir(music_dir) if isfile(join(music_dir, f))]


def play_music():
    index = random.randrange(0, len(onlyfiles), 1)
    music = onlyfiles[index]

    print(music)

    music_path = "{}/{}".format(music_dir, music)
    mixer.init()
    mixer.music.load(music_path)
    mixer.music.play()


if __name__=='__main__':
    play_music()