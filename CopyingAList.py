# Copy options
original_list = ["A", "B", "C"]
copied_lsit = original_list.copy()  # Using the copy() method
print(copied_lsit, ": Using the copy() method")

copied_lsit.append(4)
print('')
print(original_list, ": Original List")
print(copied_lsit, ": Copied List")
print(original_list == copied_lsit)
print('')


transportation = ['planes', 'trains', 'automobiles', 'boats']
new_transportation = transportation[:]
new_transportation.append('bicycle')

print(new_transportation, ": Using the [:] method")
print(transportation, ": Original List")
print(new_transportation == transportation)
