"""
4.) Napište funkci, která vezme čísla v zadaném rozsahu a 
vrátí řetězec, kde jsou daná čísla oddělená čárkami.

5.) Napište funkci, kter vezme řetězec, kde jsou čísla a 
shluky písmenek oddělená mezerami. Funkce vrátí součet čísel 
a písmenka ignoruje.
příklad: "10 abc 20 de44 30 55fg 40" -> 100

6.) Otočte slovník:
Vytvořte funkci, která vezme slovník a vytvoří nový slovník,
kde klíče jsou to, co bylo minule hodnoty a naopak

7.) Vytvočte funkci, která narovná seznam - tj. ze seznamu 
dvě úrovně hlubokého vytvoří seznam jednoúrovňový.
[[1,2], [3,4]] => [1, 2, 3, 4]
Asi budete potřebovat vnořený cyklus - v list comprehensions
lze vnořovat také, jen jsem vám to neukazoval. Zkuste to vymyslet.
"""

# 1 task :
#   Napište funkci, která vrátí seznam s třetími mocninami všech čísel v zadaném rozsahu :

my_numbers = [1,2,3,4,5]

numbers_by_3 = [
    number**3
    for number in my_numbers
    ]
print(numbers_by_3)

my_numbers_2 = [2,4,6,8,10]
numbers_by_3 = [
    number**3
    for number in my_numbers_2
    ]

print(numbers_by_3)

# 2 task:
#   a.) Vytvořte funkci, která vezme seznam čísel (list of ints) a vytvoří z nich řetězce.
#   b.) Vytvoří řetězce jen z těch čísel, co jsou menší než 15.

my_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

def change(my_list):
    change_list = [
        str(letter)
        for letter in my_list
        if letter <=15
    ]
    return "".join(change_list)

print(change(my_numbers))

#3 task:
#   Sečtěte všechna čísla od 15 do 35 (můžete použít funcki sum):

sum_of_numb = [
    i
    for i in range(15,36)    
]

print(sum(sum_of_numb)) 

#4 task:
#   Napište funkci, která vezme čísla v zadaném rozsahu a svrátí řetězec, kde jsou daná čísla oddělená čárkami.

my_number = 22

def letters(my_number):
    my_new_list = [
        str(i)
        for i in range (0,my_number+1)
    ]
    return ",".join(my_new_list)

print(letters(my_number))

#5 task:
#   Napište funkci, kter vezme řetězec, kde jsou čísla a 
#   shluky písmenek oddělená mezerami. Funkce vrátí součet čísel 
#   a písmenka ignoruje.
"""
def find_and_count(text):
    list_of_text = text.split(" ")
    count_numbers = [
        list_of_text = text.split(" ")
        for i in list_of_text
    ]
    return sum(co)

"""

my_text = "Hello today I`have 20 apple & 10 bananas and 100"

def find_and_count_2(text):
    list_of_text = text.split(" ")
    list_of_numbers = [
            int(i)
            for i in list_of_text
            if i.isdigit()
    ]
    return sum(list_of_numbers)

print(find_and_count_2(my_text))

#6 task:
#   Vytvořte funkci, která vezme slovník a vytvoří nový slovník, kde klíče jsou to, co bylo minule hodnoty a naopak

some_dict = {"name":"Vitalik",
             "year":1996,
             "hobby":"leasining song"}

def change_dict(some_dict):
    new_dict = {}
    for key,value in some_dict.items():
        key,value = value, key
        new_dict.setdefault(key,value)
    return new_dict

print(change_dict(some_dict))

# verse 2:
some_dict = {"name":"Vitalik",
             "year":1996,
             "hobby":"leasining song"}

def change_dict(some_dict):
    return {
        value:key
        for key,value in some_dict.items()
    }

print(change_dict(some_dict))





