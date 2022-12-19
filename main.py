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

def main():
    print("===============start================")

    recipe_info = pd.read_csv(input_file)

    data = input_data()

    age = child_age[data[0] - 1]
    N = data[1]
    time = alloted_time[data[2] - 1]
    for i in range(len(recipe_info["No"])):
        if recipe_info[recipe_info.keys()[1]][i] == age and recipe_info[recipe_info.keys()[2]][i] == N and \
                recipe_info[recipe_info.keys()[3]][i] == time:
            print('---------For the following information : \n')
            print('                   %s : %s\n' % (recipe_info.keys()[1], age))
            print('                   %s : %d\n' % (recipe_info.keys()[2], N))
            print('                   %s : %s\n' % (recipe_info.keys()[3], time))
            print('---------Recipe No is : %d \n' % (recipe_info[recipe_info.keys()[4]][i]))

            break

    print("===============end================")


if __name__ == "__main__":
    main()