# A dictionary is collection of key and value pairs
# You have to define first to use a dictionary like,
# my_list=[1,2,3] then my_dictionary ={'my_list':my_list}  or,
# my_dictionary={'my_list'=[1,2,3]}
# dictionary can be refered as list of tuples .
# List of tuples : 
my_list=[('Name','MMD'),('Birth',1824),('Death',1873)]
my_dictionary=dict(my_list)
print(my_dictionary)
# or if there are two list we can use "zip" function 
my_list1 = ['Name','Birth','Death']
my_list2 = ['MMD',1824,1873]
my_dictionary = dict(zip(my_list1,my_list2))
print(my_dictionary)
# if list got no pair like only key or only values we can make the numbers as our keys (1,2,3....)
names =['M','M','D']
my_dict = {i: name for i, name in enumerate(names)}
print(my_dict)
