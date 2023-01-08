import Title
from colorama import Fore, Back, Style
import time
import menu
import pandas as pd

input_file = "/Users/liam/Desktop/T1A3/recipe.csv"
child_age = ["under 6 months", "6-12 months", "12-18months", "18-24months"]
max_children = 4
alloted_time = ["30 mins or less", "30-60 mins", "1-1.5hrs"]


def input_data():
    data = []

    age = -1
    while 1:
        try:
            age = int(input("Age of youngest child? \nPlease input the number(1-4)\n[ 1(" + child_age[0] + "), 2(" +
                            child_age[1] + "), 3(" + child_age[2] + "), 4(" + child_age[3] + ") ] :   "))
            if isinstance(age, int) and 1 <= age <= 4:
                break
        except:
            continue
    data.append(age)

    N = -1
    while 1:
        try:
            N = int(input("How many serves?\n(Please input the number between 1 and " + str(max_children) + ") :   "))
            if isinstance(N, int) and 1 <= N <= max_children:
                break
        except:
            continue
    data.append(N)

    time = -1
    while 1:
        try:
            time = int(input("How much time do you have to cook? \nPlease input the number(1-3)\n[ 1(" + alloted_time[0] +
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
    #print("this is recipe info ______", recipe_info)
    #print(recipe_info["Age of child"])
    data = input_data()

    age = child_age[data[0] - 1]
    print("age: ", age)
    N = data[1]
    time = alloted_time[data[2] - 1]
    mathced_criteria_df = recipe_info[(recipe_info["Age of child"] == age) & (recipe_info["How many children"] == N) & (recipe_info["How much time do you have to cook"] == time)]
    print("Following recipe(s) matched the criteria ", ', '.join(map(str, mathced_criteria_df['Recipe name'])))
    recipe_number = 0
    while True:
        a=mathced_criteria_df['Recipe name'].to_list()
        try:
            recipe_name = input("Enter the recipe name to show ")
            if recipe_name in a:
                break
        except:
            continue
    Rcp_Name=mathced_criteria_df['Recipe name'].to_list()
    #print("this is len of rcp_names:    ", Rcp_Names)
    Rcp_Method=mathced_criteria_df['Recipe method'].to_list()
    print('---------For the following information : \n')
    print('                   %s : %s\n' % (recipe_info.keys()[1], age))
    print('                   %s : %d\n' % (recipe_info.keys()[2], N))
    print('                   %s : %s\n' % (recipe_info.keys()[3], time))
    a=mathced_criteria_df['Recipe name'].to_list()
    b=a.index(recipe_name)
    print('---------Recipe Name is : %s \n' % Rcp_Name[b])
    print('---------Here\'s how to make it : %s \n' % Rcp_Method[b])


    #print('len recipe_info  :', len(recipe_info))
    #print (recipe_info)
    while True:
        add_rows = input('Do you want to add your own recipe? Yes/No ')
        if add_rows == 'Yes':
            data = input_data()
            print(data)
            
            newrecipe_name = input('Enter Recipe Name  : ')
            newrecipe_method = input('how do you make it : ')
            recipe_info.loc[len(recipe_info)+2] = [recipe_info['No'].iloc[len(recipe_info)-1] + 1, child_age[data[0]-1], data[1], alloted_time[data[2]-1], recipe_number, newrecipe_name, newrecipe_method]
            print('Recipe has been added ! ')
        elif add_rows == 'No':
            break
        else:
            continue
    recipe_info.to_csv("/Users/liam/Desktop/T1A3/recipe.csv", index=False)

    print("===============end================")


if __name__ == "__main__":
    main()