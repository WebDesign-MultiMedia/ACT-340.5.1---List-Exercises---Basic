new_list = ['apple', 'orange', 12, ['peanut', 'butter', 'jelly', 'time']]
new_list[0] = 'banana'
print(new_list)
print(' ')

#The simplest way to add a new element 
# to a list is to use the append() method
print('"append() method"')
new_list.append(23)
print(new_list)
print('')

print('"for loop"')
list1 = []
for i in range(10):
    list1.append(i)
    print(list1)
print('')
# You can also add a new element at any 
# position in a list by using the insert() method.