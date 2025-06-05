#List to tuple 
#tuple to list 
my_list=[1,2,3,4,4,5,6,'Apple','Banana','Apple']
my_tuple=tuple(my_list)
print(my_tuple)
tuple_to_mylist=list(my_tuple)
print(tuple_to_mylist)


#list to set
#set to list 
my_list=[1,2,3,4,4,5,6,'Apple','Banana','Apple']
my_set=set(my_list)
print(my_set)
set_to_list=list(my_set)
print(set_to_list)


#list to dictionary 
#dictionary to list 

#dictionary is the list of tuples 
#two list 
my_list1 = ['Job','Designation','Salary']
my_list2 = ['Teaching','Assistant Lecturer',50000]
my_dictionary = dict(zip(my_list1,my_list2))
print(my_dictionary,"\n")
#tuples in the list 
my_list = [('Job','Teaching'),('Designation','Assistant Lecturer'),('Salary',50000)]
my_dictionary = dict(my_list)
print(my_dictionary,"\n")
#dictionarty to list 
my_list=list(my_dictionary)
print(my_list,"\n") # this only retrurn the list of keys in python by default 
# if you want just the keys from a dictonary use list(my_dict)
# if you want just the values from a dictonary use list(my_dict.values())
#if you want both then use list(my_dict.items())
my_list=list(my_dictionary.values())
print(my_list,"\n")
my_list=list(my_dictionary.items())
print(my_list)

#tuple to set
#set to tuple
my_tuple = (1, 2, 3, 4, 4, 5)
my_set = set(my_tuple)
print(my_set)
my_tuple = tuple(my_set)
print(my_tuple)

#tuple & set to dictionary?
# NO , You CAN'T convert tuple or set  to dictionary 
# You need to do pair of tuples or  sets to dictioary 
my_set = {'a', 'b', 'c'}
my_dict = dict.fromkeys(my_set, 0)
print(my_dict)

