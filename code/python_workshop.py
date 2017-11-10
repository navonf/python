# Python programming workshop

# Just some introductory things, explaining data types.

sam_age = 20            # integer
jordan_age = 24.1       # float
is_jordan_sick = True   # boolean
derger = "ben"          # string
percentage = 0.5

# A list! Commonly know as an unordered list, an array.. etc.
# Lists are awesome.

list = [100, 200, 225, 250, 300]

# A sweet taste of list comprehension
#
# We see here that we take each element in the list, list[i]
# and multiply it by a centrain percentage, for all indecies,
# in one sweet sweet line.
#
# This would be equivalent to making a loop, iterating though each
# index, and setting the new value to each index in the list. A tedious
# task (using loops, if's, etc) made very simple with list comprehension.

mySuperList = [list[i] * percentage for i in range(len(list))]

# The introductory
print("How old is sam", sam_age)
print("How old is jordan exactly", jordan_age)
print("Is this guy sick rn?", is_jordan_sick)
print("Is a derger:", derger)

# Our super cool super list my dudes
print(mySuperList)
