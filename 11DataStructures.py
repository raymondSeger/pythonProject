list_object = [66.25, 333, 333, 1, 1234.5]
#inset
list_object.insert(2, -1)
#you can delete too
del list_object[0]
print(list_object)



# now we test tuple
tuple_object = 12345, 54321, 'hello!'
print(tuple_object)
# Tuples are immutable:
# t[0] = 88888 # <- will cause error



# now we test sets, which only have unique values
set_object = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(set_object) #notice the double values disappeared



# dictionary, think of it as keyed array
dictionary_object = {'jack': 4098, 'sape': 4139}


#looping dictionary
for key, value in dictionary_object.items():
    print(key, value)

#looping list
for index, value in enumerate(tuple_object):
    print(index, value)

for index, value in enumerate(list_object):
    print(index, value)

for index, value in enumerate(set_object):
    print(index, value)