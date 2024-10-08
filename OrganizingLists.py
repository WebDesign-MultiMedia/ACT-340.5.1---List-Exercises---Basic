# The sort() method changes the order 
#  of a list permenately in alphabetical order. 
instruments= ['piano', 'flute', 'guitar', 'trumpet']
print(instruments, ': Original List')
instruments.sort()
print(instruments, ': Sort() method')
print(' ')

# We can also use the sort() method to 
# have our list in reverse alphabetical order 
# by passing the arguement reverse=true
instruments.sort(reverse=True)
print(instruments , ': Sort(reverse=True) method')
print(' ')


# How does this change if all of our 
# values are not strings or not all 
# in the same case?
print('"Mixed_list"')
instruments = ['Piano', 'flute', 'Guitar', 'trumpet']
mixed_list = ['piano', '1', 'trumpet', '5']

example_sorted_function = sorted(instruments)
print(example_sorted_function, ': sorted() function')
print(instruments, ': Original List')
print('')
example_sort_method = instruments.sort()
print(example_sort_method, ': sort() method')
print(instruments, ': Original List')
print('')

# If we only want to sort a list temporarily
#  we can use the sorted function. The sorted
#  function allows us to display the list in
#  alphabetical order, but the original list
#  is unchanged. This function also accepts 
#  the reverse=True arguement.
print(sorted(instruments), ': sorted() function')