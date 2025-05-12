# create a program that asks the user to enter a time and then greets them with the time table for the time the user entered 
# import time 
# def greetusers():
# current_time = time.localtime().tm_hour 
# if 5 <= current_time <= 11 :
# print("Good Morning !")
# elif 12 == current_time
# print("Good Noon ! ")
# elif 4 <= current_time <= 6:
# print("Good Afternoon !")
# elif 6 < current_time <= 8:
# print("Good Evening ! ")
# else print("Good Night !"):
# greetusers()
import time

def greetusers():
    current_time = time.localtime().tm_hour  # Get the current hour

    if 5 <= current_time <= 11:
        print("Good Morning!")
    elif current_time == 12:
        print("Good Noon!")
    elif 13 <= current_time <= 16:
        print("Good Afternoon!")
    elif 17 <= current_time <= 20:
        print("Good Evening!")
    else:
        print("Good Night!")

greetusers()

