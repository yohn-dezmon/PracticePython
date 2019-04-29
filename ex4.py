# Create a program that asks the user for a number and then prints out a list of all
# the divisors of that number.

nmb = int(input("Please give me a number: "))
len_list = nmb*[0]
less_list = []
org_num = nmb

while len(len_list) > 0:
    num_to_add = nmb - 1
    if num_to_add > 0:
        less_list.append(num_to_add)
        nmb = nmb - 1
        del len_list[0]
    else:
        break

divisor_list = []

for x in less_list:
    if org_num % x == 0:
        divisor_list.append(x)
    else:
        continue
        
divisor_list.sort()

print(divisor_list)
