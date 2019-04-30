# start - starting integer where the slicing of the object starts
# stop - integer until which the slicing takes place. The slicing stops at index stop - 1.
# step - integer value which determines the increment between each index for slicing

list1 = [1,2,6,4,234,623]

# ok something I understand now that I didn't before is, the new slice will CONTAIN
# the value at the start index! :D
# also since the max index was 5 and I wanted to go until the end of the list, I put 6 for 'stop' value.
slice1 = list1[1:6:1]
print(slice1)
