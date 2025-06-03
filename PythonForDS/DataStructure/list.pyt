#Here we are learning Data structure for DS
#MLDS_MejV_Rec
#(1) list is ordered,changelble,repeat value is allowed 
my_list=[1,2,3,4,'a','Rifat']
my_list[5]
my_list.append('Ireland')
my_list.append('Lithunia')
my_list.remove(4) #(n)-here it search for value n , don't look for n index . For indexing search you have to use del[]
del my_list[5]
print(my_list)
print(len(my_list))
print(my_list.count('Rifat'))