# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.

#doing it like this isn't working so...
usr_nmbr = int(input("Please give me a number: "))


if usr_nmbr % 2 == 1:
    print("Your number is odd!")
elif usr_nmbr % 4 == 0:
    print("Your number is a multiple of 4!")
else:
    print("Your number is even!")

# Ask the user for two numbers: one number to check (call it num) and one number to
# divide by (check). If check divides evenly into num, tell that to the user.
# If not, print a different appropriate message.

num = int(input("Please provide a number that you will divide by: "))
divisee = int(input(f"Please provide a number that will be divided by {num}: "))

if divisee % num == 0:
    print(f"{num} divides evenly into {divisee}")
else:
    print(f"{num} does not divide evenly into {divisee}")
