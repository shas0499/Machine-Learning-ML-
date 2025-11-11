# List Comprehension
square = [x**2 for x in range(11)]
print(square)

cube = [y**3 for y in range(6)]
print(cube)

#even = [x%2 == 0 for x in range(20)]
#print(even)

even = [x for x in range(21) if x%2==0]
print(even)

# Dictionary Comprehension
square_dic = {x:x**2 for x in range(11)}
print(square_dic)

#Set Comprehension
NonDuplicate_Num = {x for x in [1,2,2,1,4,3,6,5,6,4,3,8,2]}
print(NonDuplicate_Num)