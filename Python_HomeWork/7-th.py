#1 First task:
# The user types in a number from 1 to 7 that represents
# a day of the week. Print its name. For example, if the number
# is 1, then you should display “Monday”; if 2, display
# “Tuesday,” etc:
"""
print("Hello this programm will showe you the day from Monday to Sunday")
print("You just need to write 1 to 7")

day = int(input("Enter please a nuber of day from 1 to 7:"))

if day == 1:
    print("The first day of week is - Monday")
elif day == 2:
    print("The second day of week is - Tuesday")
elif day == 3:
    print("The third day of week is - Wednesday")
elif day == 4:
    print("The fourth day of week is - Thursday")
elif day == 5:
    print("The fifth day of week is - Friday")
elif day == 6:
    print("The sixth day of week is - Saturday")
elif day == 7:
    print("The seventh day of week is - Sunday")
else:
    print("Please enter valid value")

print("End of programm")
"""
# Or a second try is do it from list 
# When the user write a numb its will send to the list 
# and showe him a index of list

# 2 Second task:
# The user types in a number from 1 to 12 that represents
# a month. Print its name. For example, if the number is 1,
# display “January”; if 2, display “February,” etc:
"""
print("Hello this programm will showe you month from January to December")
month = int(input("You need just write a value from 1 to 12:"))

if month == 1:
    print("The first month of year is: January",
          "January have - 31 days",
          sep = "\n")
elif month == 2:
    print("The second month of year is: February",
          "February have - 28 days in a common year and 29 days in leap years",
          sep = "\n")
elif month == 3:
    print("The third month of year is: March",
          "March have - 31 days",
          sep = "\n")
elif month == 4:
    print("The fourth month of year is: April",
          "April have - 30 days",
          sep = "\n")
elif month == 5:
    print("The fifth month of year is: May",
          "May have - 31 days",
          sep = "\n")
elif month == 6:
    print("The sixth month of year is: June",
          "June have - 30 days",
          sep = "\n")
elif month == 7:
    print("The seventh month of year is: July",
          "July have - 31 days",
          sep = "\n")
elif month == 8:
    print("The eighths month of year is: August",
          "August have - 31 days",
          sep = "\n")
elif month == 9:
    print("The ninth month of year is: September",
          "September have - 30 days",
          sep = "\n")
elif month == 10:
    print("The tenth month of year is: October",
          "October have - 31 days",
          sep = "\n")
elif month == 11:
    print("The eleventh month of year is: November",
          "November have - 30 days",
          sep = "\n")
elif month == 12:
    print("The twelfth month of year is: December",
          "December have - 31 days",
          sep = "\n")
else:
    print("Please enter a valid value!")

print("End of programm")
"""

#3 Third task:
# The user types in a number. If the number is greater than
# 0, print “Your number is positive”; if it is less than zero, print
# “Your number is negative”; if it is equal to 0, print “Your
# number is equal to zero.”:
"""
print("Hello it`s program wiil tell if your number is greater than = 0" ,"or",
      "if your number is less than zero", "or",
      "if you number is equal to zero",
      sep="\n")

number = int(input("Enter please your number:"))

if number > 0:
    print("Your number is positive")
elif number < 0:
    print("Your number is negative")
elif number == 0:
    print("Your number is equal to zero.")
else:
    print("Please enter a valid value")

print("End of programm")
"""

#4 Fourth task:
# The user types in two numbers. Determine if these numbers
# are equal. If they are not, print them in ascending order.
"""
print("Hello this programm will tell you if your numbers are equal or not")

a = int(input("Enter the first numb:"))
b = int(input("Enter the second numb:"))

if a == b :
    print("The first number:", a, 
          "and", 
          "The second number:", b,
          "are",
          "equal")
elif a>b:
    print("The first number is bigger:", a)
elif a<b:
    print("The second number is bigger:", b)
else:
    print("Please enter a valid value!")

print("End of programm")
"""