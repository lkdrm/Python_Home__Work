#Task of parts 3


"""
#First task:

a = input("Enter a first numb:")
b = input("Enter a second numb:")
c = input("Enter a third numb:")

print("Your numbs is:",a+b+c)
print("End of program")
"""

"""
#Second task:

a = int(input("Enter the first numb:"))
b = int(input("Enter the second numb:"))
c = int(input("Enter the third numb:"))
d = int(input("Enter the fourth numb:"))

print("Plural of numbs is:",a*b*c*d)
print("End of program")
"""
"""
#Third task:
print("This is a program which convert",
        "First you need to write a number and than in what you want to convert", sep="\n")
numb = int(input("Enter the numb in meters:"))
conv = input("In which form you want to convert?\n"+ 
                "\ncentimeter = cm "+
                "\ndecimeters = dec "+
                "\nmillimeters = ml "+
                "\nmiles = mls:" "\n", )

if conv == "cm" :
    print("You have been convert in centimeter:", numb*100)
elif conv == "dec" :
    print("You have been convert in decimeters:", numb*10)
elif conv == "ml":
    print("You have been convert in millimeters:", numb*1000)
elif conv == "mls" :
    print("You have been convert in miles:", numb*0.00062137)
else :
    print("You wrote incorect convert!")
print("End of program")
"""
"""
#Fourth task:
print("This program is cunt the sum of a area of a triangle")
a = int(input("Please enter the length of base:"))

h = int(input("Please enter the height:"))

S = (1/2*a)*h

print("The area of a triangle is:", "S =", S)
print("End of program")
"""
#fifth task:
"""
print("The program will reverse you numbs & words")
numb = input("Enter the numbs:")

print("Reverse",numb[::-1])
print("End of program")
"""