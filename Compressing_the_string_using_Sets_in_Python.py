# File: Compressing_the_string_using_Sets_in_Python.py
# Description: Compressing the string using Sets in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Compressing the string using Sets in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Compressing_the_string_using_Sets_in_Python (date of access: XX.XX.XXXX)


# Implementing the task
# Input string with elements divided by gaps
# Output the elements and the number they are found in the string
# Algorithm isn't sensitive to upper or lowcase letters
string = input().lower().split()  # Creating the string with low case latters
# It is important to use 'split()' method in order to write in the string elements divided be gaps
print(string)  # Checking if the string was created properly with elements divided by gap
s = set(string)  # Creating the set with elements from the string, but it will not add repeated elements
for x in s:
    print(x + str(string.count(x)), end=' ')
    # We use here + str() + instead of comma in order to connect them without gaps
