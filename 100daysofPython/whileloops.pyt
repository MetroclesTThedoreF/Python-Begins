#while loop is a control flow statement that allows code to be executed repeatedly based on a given boolean condition
# x = int(input("Enter a number")) 
# while x < 50: 
#     print("The number is =",x,"is less than 50")
#     x += 1 

i = int(input("Enter a number"))
x = i
while x > 0:
    print(x)
    x -= 1
    #Atm pin verification using while loop
    correct_pin = "5417"
    pin = input("Enter your ATM pin: ")
    while pin != correct_pin:
        print("Incorrect pin ! Try Again ")
