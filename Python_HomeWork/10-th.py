#1 First task:
# The user types in two numbers. Find the sum of all even,
# odd numbers and multiples of 9 in the specified range, as well
# as arithmetic mean of each group.

print("Hello the programm wil find the sum of all even,odd numbers & multiples of 9 in the specified range")
print("And as well as arithmetic mean of each group.")
a = int(input("Enter the start of range:"))
b = int(input("Enter the end of range:"))

sum_even = 0 # парні
sum_odd = 0 # не парні

arithmetic_count_even = 0
arithmetic_count_odd = 0

multiples_9 = 0

for i in range(a,b+1):
    if i %2==0:
        sum_even+=i
        arithmetic_count_even+=1
    if i %2 !=0:
        sum_odd+=i
        arithmetic_count_odd+=1
    if i %9==0:
        print("The numb is multiples of 9:",i)
        multiples_9+=1

arithmetic_count_even = sum_even/arithmetic_count_even 
arithmetic_count_odd = sum_odd/arithmetic_count_odd

arithmetic_count_even__round = round(arithmetic_count_even,2)
arithmetic_count_odd__round = round(arithmetic_count_odd,2)

print("The arithmetic even is:",arithmetic_count_even__round)
print("The arithmetic odd is:",arithmetic_count_odd__round)

print("The sum of even numbs:",sum_even)
print("The sum of odd numbs:",sum_odd)

print("End of programm")