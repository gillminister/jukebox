from pygame import mixer # Load the required library
import mutagen.mp3, mutagen.asf
import RPi.GPIO as GPIO
import time, os, random

GPIO.setmode(GPIO.BCM)
playing = False

bands = [""]*40
bands[17] = "BeachBoys"


#mixer.init()
#mixer.music.load(song_file)
#mixer.music.play()
#print("playing")


def playMusic(pin):
    if mixer.get_init():
        mixer.quit()

    songFile = "Music/" + bands[pin] + "/" + random.choice(os.listdir("/home/pi/Desktop/jukebox/Music/" + bands[pin]))
    print("attempting to play " + songFile.split('/')[-1] )

    fileExt = songFile.split('.')[-1]
    if fileExt == "mp3":
        mp3 = mutagen.mp3.MP3(songFile)
        mixer.init(frequency=mp3.info.sample_rate)
    elif fileExt == "wma":
        asf = mutagen.asf.ASF(songFile)
        mixer.init(asf.info.sample_rate)

    mixer.music.load(songFile)
    mixer.music.play()
    print("Playing song...")

def stopMusic():
    mixer.music.stop()
    print("Stopping music")



GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#print("init")
#playMusic(22)


while True:
    buttonResting = GPIO.input(17)
    if not buttonResting:
        playing = not playing
        #if playing:
        playMusic(17)
        #else:
            #stopMusic()
        time.sleep(0.8)

