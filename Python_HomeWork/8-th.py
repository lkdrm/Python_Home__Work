#1 First task:
# The user types in a number from 1 to 100. If the number
# is a multiple of 3 (divisible by 3 without remainder), print the
# word Fizz. If the number is a multiple of 5, print the wordBuzz.
# If the word is a multiple of 3 and 5, print Fizz Buzz. If the word
# is not a multiple of 3 and 5, print the number.
# If the user typed in a number out of the range, print an
# error message
"""
print("Hello this programm will tell you the word. \nWhich include the numb.",
     "Try to find this words.",
     "You just need to write numbers from 0 to 100",
     sep ="\n")
numb = int(input("Enter a number:"))

if numb <100 and numb >0:
    if numb %5==0:
        print("Fizz Buzz")    
        if numb %3==0 and numb %5==0:
            print("wordBuzz")
    elif numb %3==0:
        print("Fizz")    
    else:
        print(numb)
else:
    print("Only from 0 to 100")

print("End of programm")
"""
#4 Fourth task:
# The salary of a salesperson is $200 + percentage of sales
# as follows: up to $500 — 3%, from 500 to 1000 — 5%, over
# 1000 — 8%. The user types in the sales for three salespersons.
# Determine their salary, the best salesperson, give him or her
# a $200 bonus, print the result.

"""
print("Hello this programm will count have much your employee","will have a sallary.")
print("First of all you need to write his or her name & than have much she/he sold")

sales_person_1 = input("Enter the name of the first salesperson:")
sold_1= int(input("Enter please how much he/she sold:"))

sales_person_2 = input("Enter the name of the second salesperson:")
sold_2= int(input("Enter please how much he/she sold:"))

sales_person_3 = input("Enter the name of the third salesperson:")
sold_3= int(input("Enter please how much he/she sold:"))


salary = 200

sum_1 = 0
sum_2 = 0
sum_3 = 0

if sold_1 < 500:
        sum = (3/100)*(sold_1)
        sum_1+=sum + salary
elif sold_1 > 500 and sold_1 < 1000:
        sum = (5/100)*(sold_1)
        sum_1+=sum + salary
else:
        sum = (8/100)*(sold_1)
        sum_1+=sum + salary + 200

if sold_2 < 500:
        sum = (3/100)*(sold_2)
        sum_2+=sum + salary
elif sold_2 > 500 and sold_2 < 1000:
        sum = (5/100)*(sold_2)
        sum_2+=sum + salary
else:
        sum = (8/100)*(sold_2)
        sum_2+=sum + salary + 200

if sold_3 < 500:
        sum = (3/100)*(sold_3)
        sum_3+=sum + salary
elif sold_3 > 500 and sold_3 < 1000:
        sum = (5/100)*(sold_3)
        sum_3+=sum + salary
else:
        sum = (8/100)*(sold_3)
        sum_3+=sum + salary + 200 


print("Name:",sales_person_1, "Your salary is:",sum_1)
print("Name:",sales_person_2, "Your salary is:",sum_2)
print("Name:",sales_person_3, "Your salary is:",sum_3)

print("End of programm")
"""