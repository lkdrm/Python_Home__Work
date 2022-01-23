"""
Develop a game of Bulls and Cows. The program chooses
a four-digit number, and the player has to guess it. After
the user enters a number, the program reports how many digits of
the number are guessed (bulls), and how many digits are guessed
and stand in the right place (cows). After guessing the number,
print the number of user’s attempts. Use recursion in your game.

"""
import random

number = str(random.randint(1000,9999))

def list_of_number(number): # create of one long number list 
    list_of_numbers = []
    for i in number: # do the cicle of number 
        list_of_numbers.append(i)
    return list_of_numbers

list_of_number(number)

def user_number(user):
    list_of_user_number = []
    if len(user) == 4:
        for i in user:
            list_of_user_number.append(i)
        return list_of_user_number
    else:
        print("Enter only four numbers")
        return  find_numbers()

cows = 0

while True:
    cows = 0    
    def find_numbers(): 
        pc = list_of_number(number)
        print(pc)  
        user = user_number(input("Enter your numbers:"))   
        a,b,c,d = pc    
        a1,b1,c1,d1 = user
        cows = 0    
        if  a == a1 and b == b1 and c == c1 and d == d1 :
            cows+=1 
            print("You have find all numbers",pc,
            "Here is your cows:",cows, sep="\n")
            return False
        elif a == a1 and b == b1 and c == c1 :
            print("Almost")
            cows +=1   
            return cows
        elif a == a1 and b == b1 :
            print("You have find two numbers!")
            cows+=1    
            return cows
        elif a == a1 :
            print("You have find first number!")
            cows+=1
            return cows 
        else:
            cows+=1
            print("Sorry not anyone")
            return True
    find_numbers() 

####
"""
my_list = [1,2,3,4]

a,b,c,d = my_list

print(a)
"""