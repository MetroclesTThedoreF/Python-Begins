# GOAL: Turn 3+ lists into a dictionary
# Let's say we have a list like 
keys = ['name', 'age', 'country']
values1 = ['Alice', 25, 'USA']
values2 = ['Bob', 30, 'UK']
values3 = ['Charlie', 35, 'Canada']
# METHOD 1: Use zip() to combine lists into a dictionary
# Case A: One list as keys, others as values in tuples
# What to do:
# Use zip() to combine the key list with multiple value lists as tuples.
my_dictionary=dict(zip(keys,zip(values1,values2,values3)))
print(my_dictionary)