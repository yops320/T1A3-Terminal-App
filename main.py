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
            age = int(input("Age of child. Please input the number(1-4)[ 1(" + lst_age[0] + "), 2(" +
                            lst_age[1] + "), 3(" + lst_age[2] + "), 4(" + lst_age[3] + ") ] :   "))
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
            time = int(input("How much time do you have to cook? Please input the number(1-3)[ 1(" + lst_time[0] +
                             "), 2(" + lst_time[1] + "), 3(" + lst_time[2] + ") ]:   "))
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

    age = lst_age[data[0] - 1]
    N = data[1]
    time = lst_time[data[2] - 1]
    mathced_criteria_df = recipe_info[(recipe_info["Age of child"] == age) & (recipe_info["How many children"] == N) & (recipe_info["How much time do you have to cook"] == time)]
    print("Following recipe(s) matched the criteria ", ', '.join(map(str, mathced_criteria_df['Recipe No'])))
    recipe_number = 0
    while True:
        try:
            recipe_number = int(input("Enter the recipe number to show "))
            if recipe_number in mathced_criteria_df['Recipe No'].to_list():
                break
        except:
            continue
    print('---------For the following information : \n')
    print('                   %s : %s\n' % (recipe_info.keys()[1], age))
    print('                   %s : %d\n' % (recipe_info.keys()[2], N))
    print('                   %s : %s\n' % (recipe_info.keys()[3], time))
    print('---------Recipe No is : %d \n' % recipe_number)

    while True:
        add_rows = input('Do you want to add rows ? Yes/No ')
        if add_rows == 'Yes':
            data = input_data()
            recipe_number = input('Enter Recipe Number : ')
            recipe_info.loc[len(recipe_info)] = [recipe_info['No'].iloc[len(recipe_info)-1] + 1, lst_age[data[0]], data[1], lst_time[data[2]], recipe_number]
            print('Recipe has been added ! ')
        elif add_rows == 'No':
            break
        else:
            continue
    recipe_info.to_csv('recipe.csv', index=False)

    print("===============end================")


if __name__ == "__main__":
    main()