import time 
def greetusers():
current time = time.localtime().tm_hour 
if 5 <= current time <= 11 :
print("Good Morning !")
elif 12 <= current time  <= 4:
print("Good Noon ! ")
elif 4 <= current time <= 6:
print("Good Afternoon !")
elif 6 < current time <= 8:
print("Good Evening ! ")
else print("Good Night !")
greetusers():