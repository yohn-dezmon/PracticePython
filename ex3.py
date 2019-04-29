# Take a list and write a program that prints out all the elemtns of the list that are
# less than 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
empty_list = []

for x in a:
    if x < 5:
        empty_list.append(x)
    else:
        continue

for y in empty_list:
    # python's print function comes with a parameter called 'end'
    print(y, end =" ")

print(" ")


# Write this in one line of Python.

[print(x, end=" ") for x in a if x < 5]
