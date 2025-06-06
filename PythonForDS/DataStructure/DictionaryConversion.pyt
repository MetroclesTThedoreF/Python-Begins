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


# three list to dictionary : 
list1=['Apple','Aster','Ape']
list2=['Banana','Bougainvillea','Bear']
list3=['Cherry','Camellia','Cow']
for fruits,flowers,animals in zip(list1,list2,list3) : 
 my_dict =   {
        'fruits':fruits,
        'flowers':flowers,
        'animals':animals,
    }
 print(my_dict)