import Title
from colorama import Fore, Back, Style
import time
import menu
import pandas as pd

input_file = "recipe.csv"
child_age = ["under 6 months", "6-12 months", "12-18months", "18-24months"]
max_children = 4
alloted_time = ["30 mins or less", "30-60 mins", "1-1.5hrs"]


def input_data():
    data = []

    age = -1
    while 1:
        try:
            age = int(input("Age of child. Please input the number(1-4)[ 1(" + child_age[0] + "), 2(" +
                            child_age[1] + "), 3(" + child_age[2] + "), 4(" + child_age[3] + ") ] :   "))
            if isinstance(age, int) and 1 <= age <= 4:
                break
        except:
            continue
    data.append(age)

    N = -1
    while 1:
        try:
            N = int(input("How many children(Please input the number between 1 and " + str(max_children) + ") :   "))
            if isinstance(N, int) and 1 <= N <= max_children:
                break
        except:
            continue
    data.append(N)

    time = -1
    while 1:
        try:
            time = int(input("How much time do you have to cook? Please input the number(1-3)[ 1(" + alloted_time[0] +
                             "), 2(" + alloted_time[1] + "), 3(" + alloted_time[2] + ") ]:   "))
            if isinstance(time, int) and 1 <= time <= 3:
                break
        except:
            continue
    data.append(time)

    return data