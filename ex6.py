# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
usr_str = input("Please provide a string: ")

# list[start:stop:step] -1 step means decreasing, null for start means start at the end, null for stop means stop at the beginning
reversed_str = usr_str[::-1]

if usr_str == reversed_str:
    print("Palindrome!")
else:
    print("Not a palindrome!")


# STRINGS ARE LISTS! :D 
