
# We can remove a(n) element(s) from a 
# list either by either the position or the value.

new_list = ['apple', 'orange', 12, ['peanut', 'butter', 'jelly', 'time']]
new_list[0] = 'banana'
new_list.insert(0, 'grape')
print(new_list)

# If we know the position of the element 
# we want to remove from a list we can use the del statement
del new_list[2]
del new_list[-1]
print(new_list)
print('')
# 
food= ['burger', 'fries', 'pizza', 'hotdog']
print(food)
food_item = food.pop()
food_item2 = food.pop(1)
print(food_item)
print(food_item2)
print('')

# We can also remove an item from a 
# list by value using the remove() method.
transportation = ['planes', 'trains', 'automobiles', 'boats']

transportation.remove('automobiles')
item_remove = 'trains'
transportation.remove(item_remove)
print(transportation)
print(item_remove) 