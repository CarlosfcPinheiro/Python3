#Reproduz um áudio em .mp3
from pygame import mixer

mixer.init()
mixer.music.load('ex021music.mp3')
mixer.music.play()
input('Escuta?')
