# match case statements are like more powerfull versions of if elif else statements 
# they are used to match a value against a set of patterns and execute the corresponding block of code ]
# like if this happen then do this else if this happen then do that...


# map(int, input("Enter x and y coordinates: ").split())
# point = ( x, y)
# match point:
#     case (0,0):
#         print("Origin") 
#         case (0,y): 
#         print("Y axis")
#         case (x,0): 
#         print("X axis")
#         case (x,y):
#         print ("Point in Quadrant 1")
#         case (-x,y):
#         print ("Point in Quadrant 2")
#         case (-x,-y):
#         print ("Point in Quadrant 3")
#         case (x,-y):
#         print ("Point in Quadrant 4")

    
x, y = map(int, input("Enter x and y coordinates: ").split())
point = (x, y)

match point:
    case (0, 0):
        print("Origin")
    case (0, _):
        print("Y axis")
    case (_, 0):
        print("X axis")
    case (x, y) if x > 0 and y > 0:
        print("Point in Quadrant 1")
    case (x, y) if x < 0 and y > 0:
        print("Point in Quadrant 2")
    case (x, y) if x < 0 and y < 0:
        print("Point in Quadrant 3")
    case (x, y) if x > 0 and y < 0:
        print("Point in Quadrant 4")

#a, b = map(int, input("Enter two numbers: ").split())
# input() → "22 -2"

# .split() → ["22", "-2"]

# map(int, ...) → [22, -2]

# a, b = ... → assigns 22 to a and -2 to b

