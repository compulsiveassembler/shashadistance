import pandas as pd
import math
import sys


#loads csv into dataframe
df = pd.read_csv('locations.csv')



#gets user input, tests input for quit prompt and then tries conversion in a try block. Will reset prompt if invalid input.
#only leaves while loop if q is detected

def get_choice():
    
    print("Enter 1 if you would like to view the current list of locations in tabulated form")
    print("Enter 2 if you would like to calculate the distance between two manually entered coordinates")
    print("Enter 3 if you would like to calculate the distance between a listed location and a coordinate point")
    print("Enter 4 if you would like to calculate the distance between two listed locations")
    print("Enter q to quit :)") 
    
    choice = input()    
    print("\n\n")

    return choice




#calculates the distance through the distance formula. Parameters will have already been parsed to floats.
def calc_distance(x1, y1, x2, y2):
    
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

    return distance






#grabs the coordinates of the location entered by the user, loops through csv file and fetches the associated latitude and longitude when the name is matched
def fetch_location(location_name):
    
    length = df.shape[0]

    (x,y) = (-100.0,-100.0)
    
    for k in range(0,length):
         if df.loc[k].at["Name"] == location_name:
            (x,y) = (df.loc[k].at["Longitude"],df.loc[k].at["Latitude"])
                         
    return (x,y)




#gets raw coordinates from input, testing them to make sure they are valid coords
def raw_coords():

    print("Enter x coordinate (Longitude):")
    inx = input()
    print("\n")
    test_coords(inx)
    x = float(inx)    

    print("Enter y coordinate (Latitude):")
    iny = input()
    print("\n")
    test_coords(iny)
    y = float(iny)
    
    return (x,y)




#Ensures that user input in main prompt is valid, and doesn't crash program
def test_choice(choice):


#if 'choice' can't be converted to an int, it's either the quit prompt or a mistype. This try-except block tests for which it is.
    try:
        int(choice)
    except:
        if choice == 'q':
            print("Goodbye!")            
            sys.exit()
        else:
            print("Invalid entry, now returning to main prompt")
            print("\n\n")
            eval_choice(get_choice())

    return



#tests coordinates to ensure that coordinates are not negative, and they are able to be converted to floats.
def test_coords(coordinate):

    try:
        float(coordinate)
    except:
        print("Coordinate entered is invalid, redirecting to main prompt")
        print("\n\n")
        eval_choice(get_choice())

    if float(coordinate) < 0:
        print("Coordinate entered is invalid (negative coordinates not defined for map), redirecting to main prompt")
        print("\n\n")
        eval_choice(get_choice())

    return






#evaluates the user choice, sending control flow to the relevant functions in the appropriate order
def eval_choice(choice):
    
    test_choice(choice)
    
    if int(choice) == 1:
#This branch of the conditional prints the tabulated data loaded in via the locations.csv file       
        print(df)
        
        print("\n\n")

    elif int(choice) == 2:
#this handles option 2, and handles raw coordinates input by the user        
        print("Let's enter the first pair of coordinates!")
        print("\n")
        (x1,y1) = raw_coords()

        print("Let's get the second pair of coordinates!")
        print("\n")
        (x2,y2) = raw_coords()

        distance = round(calc_distance(x1,y1,x2,y2), 4)

        print(f"The DISTANCE between these two points IS -----> {distance}")

    
    elif int(choice) == 3:
#This branch deals with option 3, and handles the distance between a tabulated location and a pair of raw coordinates       
        print("First, enter your listed location's name!")
        print("INPUT IS CASE SENSITIVE!!")
        location_name1 = input()
        print("\n")
        (x1,y1) = fetch_location(location_name1)
        
        if x1 == -100.0:
            print("Location not found, exiting to main prompt")
            print("\n\n")
            eval_choice(get_choice())
        
        print("Next, enter the pair of coordinates you are traveling to from this location!")
        print("\n")
        (x2,y2) = raw_coords()
        
        distance = round(calc_distance(x1,y1,x2,y2), 4)

        print(f"The DISTANCE between {location_name1} and the point you entered IS ------>  {distance}")
        

    elif int(choice) == 4:
#this conditional branch evalutes option 4, the distance between two tabulated entries

        print("Enter first location's name: ")
        print("INPUT IS CASE SENSITIVE!!")
        location_name1 = input()
        print("\n")

        (x1,y1) = fetch_location(location_name1)

        if x1 == -100.0:
            print("Location not found, exiting to main prompt")
            print("\n\n")
            eval_choice(get_choice())

        
        print("Enter second location's name: ")
        location_name2 = input()
        print("\n")

        (x2,y2) = fetch_location(location_name2)

        if x2 == -100.0:
            print("Location not found, exiting to main prompt")
            print("\n\n")
            eval_choice(get_choice())

        distance = round(calc_distance(x1,y1,x2,y2), 4)

        print(f"The DISTANCE from {location_name1} to {location_name2} IS ------>  {distance}")
        print("\n\n")

    else:
    
        print("Invalid entry, now returning to main prompt")
        print("\n\n")

    print("\n\n")
    eval_choice(get_choice())

    return








eval_choice(get_choice())











