new_list = ['apple', 'orange', 12, ['peanut', 'butter', 'jelly', 'time']]
print(new_list[2])
print(new_list[-1])
print(' ')

print('[Slicing :3]')
print(new_list[:3])
print('[for Loop]')
for item in new_list[:3]:
    print(item)
print(' ')

new_list[0] = 'banana'
print(new_list)