#string is a data type in python which is used to store text data 
# double quotes or single quotes are used to create string which one is using doesn't matter 
# for example 
a = "hello world"
b = 'Hello world'
print(a,b)
print("What the hell world",a)
print("What the hell is wrong with the world",b)
#we can also use triple quotes to create string 
# triple quotes are used to create multi line string 
# Accessing Characters in string 
# we can access characters in string using index
# index starts from 0
# for example 
print (a[4]) # this will print 4th index character of string a 
# we can also use negative index to access characters from end of the string
# for example 
print (a[-1]) # this will print last character of string a 
print (a[9]) # this will show index error : string index out of range 
# Looping through string 
# we can loop through string using for loop 
print (" Let's use a for loop to print each character of string a ")
for character in a : 
    print (character)
    for character in b : 
        print ( character)