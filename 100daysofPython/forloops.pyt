# A for loop is used to iterate over a sequence (like a list, tuple , dictionary , string or set
# a list is a collection of items in a particular order 
# a tuple is a collection of items in a particular order but it is immutable 
# a dictionary is a collection of key value pairs
# a set is a collection of unique items in no particular order 
# a string is a collection of characters in a particular order
# difference between a list and a string is that a list can contain any data type while a string can only contain characters 
# second bracket is used to access the elements of a list , for list slicing 
# fruits = [ Orange]
# x = int (input("Enter a number to continue"))
# for number in range(x): # for i in range(x)
#     print("I like",fruits)
# fruits = [ "Apple", "Banana", "Cherry", "Date", "Elderberry" ]
# for fruit in fruits:
#     print("I like",fruit)
fruits = ["Orange", "Apple", "Banana", "Cherry", "Date", "Elderberry"]

x = int(input("Enter a number to continue: "))

# Print first x fruits, safely
for number in range(min(x, len(fruits))):
    print("I like", fruits[number])

# Print all fruits using a for-each loop
for fruit in fruits:
    print("I like", fruit)

n = int(input("Enter a number : "))
for i in range(n+1): 
 print(i)

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
d = int(input("Enter number d: "))
e = int(input("Enter number e: "))
my_list = [a,b,c,d,e]
total = 0
for n in my_list:
   total += n
   print(total)
   #for each 'thing' in group: do something with the 'thing'
