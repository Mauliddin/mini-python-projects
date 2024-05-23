import time
import os

def coutdown(second):
    while second > 0:
        os.system("cls")
        hour = second // 360
        minute = second // 60
        print(f"{hour:02}:{minute:02}:{second:02}")
        second -= 1
        time.sleep(1)
    if second == 0:
        print("Time is Up")

def input_check(text) -> int:
    variabel = input(f"Enter {text} : ")
    if variabel.isnumeric():
        return int(variabel)
    else:
        return input_check(text)

def main():
    hour = input_check("Hour")
    minute = input_check("Minutes")
    second = input_check("Second")
    timer = (hour*360) + (minute*60) + second
    coutdown(timer)

main()