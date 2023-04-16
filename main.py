import pandas as pd
import random


dict = {'data': None, 'percent': None} #creating dict to input the values from the user. 
while 1: #to again take the value of the data 
    try:
        path = input(
            "Please Enter The Path of The DataFrame (.csv File Only): \n")
        dict["data"] = pd.read_csv(path)
    except:
        print("Please ensure that the path of the dataframe Should be correct And File should be in .csv format.")
        continue
    while 1:
        try:
            dict['percent'] = float(input(
                "Enter the Percentage value(i.e. how much percentage of missing value you want to generate in your data): \n"))
            break
        except:
            print['Please Enter the correct value.']
            continue
    break

def generate_missing():
    shape = dict["data"].shape
    print("Shape of the your Dataframe is ", shape)
    print("Total no. of values in the dataFrame is ", shape[0]*shape[1])
    missing_value = shape[0]*shape[1]*dict["percent"]/100
    missing_value = round(missing_value)
    print("Total no. of missing that are going to be generated in the Dataframe is ", missing_value)
    for a in range(missing_value-1):
        row = random.randint(0,shape[0]-1)
        col = random.randint(0,shape[1]-1)
        dict["data"].iloc[row,col] = None

    print("Missing Values are generated Successfully Generated.")
    name = input("Enter the name of the folder:\n")
    dict["data"].to_csv(name)
    print("Your DataFrame is saved in the current folder with name: ", name)
    dict["data"].info()

generate_missing()