# Healthy Programmer by Abhishek
# 9am - 5pm
# Water - water.mp3 (3.5 litres = 15 - 18 glasses) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules: Pygame module to play audio
from pygame import mixer
import time

mixer.init()
hour = int(time.asctime()[11:13])
a = time.time() - 20 * 60
b = time.time() - 5 * 60
c = time.time() - 25 * 60

while 9 <= hour <= 17:
    while time.time() - a >= 30 * 60:
        mixer.music.load('water.mp3')
        mixer.music.play(-1)
        if input("Its time to drink water.\n Have You Drank water? \n"
                 " if Yes , Please enter drank:\n").lower() == "drank":
            mixer.music.stop()

            a = time.time()
            f = open("water_log.txt", "a")
            f.write(f"You Drank Water at--> {time.asctime(time.localtime(a))}\n\n")
            f.close()
            break
        else:
            continue

    while time.time() - b >= 30 * 60:
        print(time.time())
        mixer.music.load('eyes.mp3')
        mixer.music.play(-1)
        if input("Its time to do eyes exercise.\n Have You Done? \n"
                 " if Yes , Please enter eyedone:\n").lower() == "eyedone":
            mixer.music.stop()
            b = time.time()
            f = open("Eye_exercise_log.txt", "a")
            f.write(f"You did eye exercise on - {time.asctime(time.localtime(b))}\n\n")
            f.close()
            break
        else:
            continue

    while time.time() - c >= 45 * 60:
        mixer.music.load('exercise.mp3')
        mixer.music.play(-1)
        if input("Its time to do some exercise Dance/something.\n Have You Done? \n"
                 " if Yes , Please enter exdone:\n").lower() == "exdone":
            mixer.music.stop()
            b = time.time()
            f = open("Physical_exercise_log.txt", "a")
            f.write(f"You did eye exercise on - {time.asctime(time.localtime(c))}\n\n")
            f.close()
            break
        else:
            continue
