# 1 first task: 
# The user types in a two-digit number. For example, 26.
# Display the value of the first and second digit on different
# lines. In our case, it will be as follows :
"""
a = input("Enter the first numb: ")
b = input("Enter the second numb: ")

print( a, b, sep="\n")
print("End of program")
"""
#2 second task: 
# The user types in a three-digit number. For instance, 891.
# Print the value of the first, second, and third digit each on a
# new line. Also, print the sum of these numbers on a new line.
# In our case, it will be as follows:
"""
a = int(input("Enter the first numb: "))
b = int(input("Enter the second numb: "))
c = int(input("Enter the third numb: "))

print("The numb on a new line:", a, b, c, sep="\n")
print("The sum of this numbs are:", a+b+c)
print("End of program")
"""
#3 third task:
# The user types in two digits. Create a number containing
# these digits. If the typed in digits are 9 and 7, the created
# number will be 97:
"""
a=input("Enter the first numb: ")
b=input("Enter the second numb: ")

print("Numb together: ", a+b)
print("End of program")
"""
#4 fourth task:
# The user types in Celsius temperature. Convert it to Fahrenheit
# and display the result on the screen:
"""
print("Hello this is a converter which change temperature of Celsius to Fahrenheit")
numb = int(input("Firts you need to write a value:"))
conv = input("You have?\n"+
             "Celsius = C\n"+
             "Fahrenheit = F\n" )

if conv == "F":
    numb = (numb - int(32))//1.8
    print("We convert value in Celsius:",numb)
elif conv == "C":
    numb = ((numb * 1.8) + int(32))
    print("We convert value in Fahrenheit:",numb)
else:
    print("Please write correct value")
print("End of program")
"""