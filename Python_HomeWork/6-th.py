#1 First task:
# The user types in three numbers. The program prints
# the sum or product of these numbers based on the user’s
# choice:
"""
print("Hello the programm will count the sum of numbers.",
      "First you need to write a values",sep="\n")
a = int(input("Enter the first numb:"))
b = int(input("Enter the second numb:"))
c = int(input("Enter the third numb:"))

print("Do you want to count all numbers or only two?",
      "Yes or No",
      "If Yes - the programm will count all 3 values", 
      "If No - the programm will count only 2 values", 
      sep="\n")
user = input("Enter here Yes or No:").capitalize()

if user == "Yes":
    count = a + b + c
    print("The sum of 3 values are:", count)
elif user == "No":
    count = a + b
    print("The sum of 2 values are:", count)
else:
    print("Please enter Yes of No")

print("End of programm")

"""

#2 Second task:
# The user types in three numbers. Based on the user’s
# choice, the program prints a maximum of three, a minimum
# of three, or arithmetic mean of three numbers:
"""
print("Hello, this program will find max & min or if you want, will find the arithmetic mean of three numbers")
print("First of all you need to write a values")

a = int(input("Enter the first value:"))
b = int(input("Enter the second value:"))
c = int(input("Enter the third value:"))

print("Now you need to chose",
             "1 - is a max & minimum of your numbers",
             "or",
             "2 - is arithmetic mean of three numbers",
             sep = "\n")

user = input("1 or 2?")

list_of_numbs = [a,b,c]

if user == "1":
    max_of_numbs = max(list_of_numbs)
    min_of_numbs = min(list_of_numbs)
    print("The maximum of numbers is:",max_of_numbs,
          "The minimum of numbers is:",min_of_numbs,
          sep="\n")
elif user == "2":
    arithmetic = (a + b + c)/3
    arithmetic_round = round(arithmetic,2)
    print("The arithmetic mean of three numbers is:",arithmetic_round)
else:
    print("Please enter 1 or 2. Another not work.")

print("End of programm")
"""

#3 Third task:
# The user types in the number of meters. Based on the
# user’s choice, the program converts meters to miles, inches,
# or yards:
"""
print("Hello this programm will converts meters to miles, inches,or yards.")

a = int(input("Enter a value of meters:"))

print("We convert in:",
      "Miles == mls",
      "Inches == inch",
      "Yards == yrds",
      sep="\n")

conv = input("In which form do you prefer to convert:")

if conv == "mls":
    a *= 0.00062137
    a_round = round(a,2)
    print("We have been convert in:",
          "Miles",a_round,
          sep="\n")
elif conv == "inch":
    a *= 39.370
    a_round = round(a,2)
    print("We have been convert in:",
    "Inches",a_round,
    sep="\n")
elif conv == "yrds":
    a *= 1.0936
    a_round = round(a,2)
    print("We have been convert in:",
    "Yards",a_round,
    sep="\n")
else:
    print("Please enter a correct convert!")

print("End of programm")
"""