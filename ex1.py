#Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
import datetime

print("Hello! Please tell me your name and age")
usr_name = input("Name: ")
usr_age = int(input("Age: "))
print(f"Thanks {usr_name}!")

def year_100(usr_age):
    this_year = datetime.date.today().year
    print(f"{this_year}")
    year_born = this_year - usr_age
    print(f"{year_born} +/- one year")
    year_100_ = year_born + 100
    print(f"you will turn 100 in the year {year_100_}")

year_100(usr_age)
