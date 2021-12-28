#1 First task:
# The user types in two numbers. Find the sum and average
# of numbers in the specified range:
"""
print("Hello this program is count the sum of range")
a = int(input("Enter the start of range:"))
b = int(input("Enter the end of range:"))

sum = 0

for i in range(a, b+1):
    sum+=i
print("The sum of numbers of range are:", sum)
print("End of programm")
"""

#2 Second task:
#The user types in a number. Calculate the factorial of
#a number. For instance, if the user typed in 3, the factorial is
#1*2*3 = 6
#The formula for calculating the factorial: n! = 1*2*3…*n,
#where n is the user-defined number:
"""
print("Hello the programm will find the factorial of your value")
b = int(input("Enter value of n-factorial we will count it:"))

n = 1

for i in range(n,b+1):
    n*=i

print("The factorial of:", b , "is", n, sep="\n\t")
print("End of programm")
"""

#3 Third task:
#The user types in the line length. Print a horizontal line
#made out of * of the specified length.
#For instance, if the typed in number is 7, the output will
#be as follows: *******.
"""
print("Hello this program will created the line of starts")
b = int(input("Enter the value of stars:"))
n="*"

for i in range(1,b+1):
    n*i
    print(n,end="")
print("\nEnd of programm")
"""

#4 Fourth task:
#The user types in the length of a line and a symbol to fill the
#line. Print a horizontal line made out of the typed in symbol
#of the specified length.
#If the typed in number and symbol are 5 and &, the output
#will be as follows: &&&&&.
"""
print("Hello this program will created the line of your symbols")
b = int(input("Enter the value of symbols:"))
s = input("Please enter a symbol:")

for i in range(1,b+1):
    s*i
    print(s,end="")
print("\nEnd of programm")
"""