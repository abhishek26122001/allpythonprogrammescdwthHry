#   water(200 mL) in 25 min
#   Eyes in 30 min
#   Exercise in 45 min
import time
from pygame import mixer

p=time.localtime().tm_hour


def wat():
        import time
        print("Please drink 200 mL of water")
        mixer.init()
        mixer.music.load("water.mp3")
        mixer.music.set_volume(0.2)
        mixer.music.play()
        wi = input("enter 'Drank' to stop the audio\n")
        if wi == "Drank":
            mixer.music.stop()


def eye():
        print("Please do eye care routine")
        mixer.init()
        mixer.music.load("eyes.mp3")
        mixer.music.set_volume(0.2)
        mixer.music.play()
        eyi = input("enter 'EyDone' to stop the audio\n")
        if eyi == "EyDone":
            mixer.music.stop()


def phys():
        print("Please do exercise")
        mixer.init()
        mixer.music.load("exercise.mp3")
        mixer.music.set_volume(0.2)
        mixer.music.play()
        exi = input("enter 'ExDone' to stop the audio\n")
        if exi == "ExDone":
            mixer.music.stop()

wtime=0000
eytime=0000
extime=0000

while (p>=9) and (p<=17):
    now = time.time()
    if now-wtime > 25*60:
        wat()
        wtime=time.time()
        with open ("Water.txt","a") as f:
            f.write(f"You Drank Water at--> {time.asctime(time.localtime())}\n\n")
    if now-eytime > 30*60:
        eye()
        eytime=time.time()
        with open ("Eyes.txt","a") as f:
            f.write(f"You Did Eye Exercise at--> {time.asctime(time.localtime())}\n\n")
    if now-extime > 45*60:
        phys()
        extime=time.time()
        with open ("Exercise.txt","a") as f:
            f.write(f"You Did Exercise at--> {time.asctime(time.localtime())}\n\n")
    time.sleep(60)
if p<9:
    print("Your time will start at 9:00 AM localtime.")
    print("Please ReRun the program between 9:00 AM - 5:00 PM")
if p>17:
    print("You are done for the day! Program will start at 9:00 AM localtime tomorrow.")
    print("Please ReRun the program between 9:00 AM - 5:00 PM")