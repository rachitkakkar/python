from time import sleep
from os import system

pomodoros = 0
minutes = 0
while True:
    system('clear')
    print(f'Keep working! {25-minutes} minutes remaining!')

    sleep(60)
    minutes += 1

    if minutes >= 25:
        pomodoros += 1
        minutes = 0

        if pomodoros % 4 == 0:
            system('clear')
            print("Take a 15 minute break!")
            sleep(60 * 15)
        else:
            system('clear')
            print("Take a brief 5 minute break!")
            sleep(60 * 5)
