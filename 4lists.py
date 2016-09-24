squares = [1, 4, 9, 16, 25]
print( squares )

#get one
print(squares[0])

#get 3 starts from index 0
print(squares[0:3])

#add
print( squares + [36, 49, 64, 81, 100] )

# replace  value
squares[0] = 64
print( squares )

# add the cube of 6
squares.append(216)
print( squares )

#list containing lists
list_a      = ['a', 'b', 'c']
list_b      = [1, 2, 3]
master_list = [list_a, list_b]

print(master_list)
print(master_list[0])
print(master_list[0][1])
