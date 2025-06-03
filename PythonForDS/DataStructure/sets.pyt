# sets only holds unique items 
# sets remove all the duplicate items 
# sets can perform Union & Intesection operations 
# sets are unordered it means we can not get each items by indexing unlike list and tuple 
my_set={1,2,3,4,'Apple','Apple','Banana'}
print(my_set)
my_set.add('Orange')
my_set.remove(4)
print(my_set)
print(len(my_set))
my_set1={5,5,6,7,9,'Guava','Berry'}
print(my_set.union(my_set1))
print(my_set.intersection(my_set1))