from videoDetector import *
from pictureDetector import *


def start_system():
    first_option = menu()
    second_option = select_function()
    controller(first_option, second_option)
    start_system()
    

def menu():
    print(" Select one of the options below: \n")
    print(" Enter 1 to detect a hand: ")
    print(" Enter 2 to detect people: ")
    print(" Enter 3 to detect a truck: ")
    try:
        option = int(input("Select the option above: "))
        if option > 3:
            print("Invalid option...")
            return menu()
        else:
            return option
    except ValueError:
        print("Try one of the options above!")
        return menu()


def select_function():
    print("\n Select one of the functions below: \n")
    print(" Enter 1 to select a picture: ")
    print(" Enter 2 to use your camera: \n")
    try:
        option = int(input("Select the option above: "))
        if option > 2:
            print("Invalid option...")
            return select_function()
        else:
            return option
    except ValueError:
        print("Try one of the options above!")
        return select_function()


def controller(first_option, second_option):

    path_to_truck_training = "truckFiles/training/cascade.xml"
    path_to_hands_training = "handFiles/training/cascade.xml"
    path_to_people_training = "peopleFiles/training/cascade.xml"

    if first_option == 1:
        path = path_to_hands_training
    elif first_option == 2:
        path = path_to_people_training
    else:
        path = path_to_truck_training

    if second_option == 1:        
        file_path = input("Enter the picture path below: \n")
        pic_detector(file_path, path)
    else:
        vi_detector(path)


if __name__ == "__main__":
    start_system()