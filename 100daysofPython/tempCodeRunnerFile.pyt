import time 
def greetusers():
    currenttime = time.localtime().tm_hour 
    
if 5 <= currenttime <= 11 :
    print("Good Morning !")
elif 12 <= currenttime  <= 4:
    print("Good Noon ! ")
elif 4 <= currenttime <= 6:
    print("Good Afternoon !")
elif 6 < currenttime <= 8:
    print("Good Evening ! ")
else print("Good Night !")
    greetusers():