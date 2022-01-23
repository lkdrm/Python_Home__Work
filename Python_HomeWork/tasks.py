#1 Task:
"""
Napište program na počítání deště ve městech
Uživatel postupně zadává jméno města a déšť v milimetrech (nějaké
město se může zadat vícekrát). Pro ukončení zadá prázdný řádek.
Program pak vytiskne, kolik v každém městě napršelo.
Příklad (každý řádek je jedno zadání od uživatele):
Brno
10
Bratislava
15
Brno
20
(enter, tj. prázdný řádek)

Výsledek bude:
Brno: 30
Bratislava: 15
(nápověda: použijte slovník)

"""

def show_rain():
    my_list = {}
    while True:
        key = input("Enter a city:")
        if key == " ":
            break
        value_rain = int(input("Enter a rain milimetr:"))
        if key in my_list:
            my_list[key]+=value_rain
        my_list.setdefault(key,value_rain)
    return my_list   
        
def print_dict(pocasi):
    for key,value in pocasi.items():
        print(key,":", value )

def middle_of_numbs(my_list):
    sum_of_numbs = sum(my_list)
    middle = sum(my_list) / len

print_dict(show_rain())
"""
3.) Těžší verze dvojky:
Místo celkového deště program vypočítá průměrný déšť podle počtu dní.
Tj. v minulém případě by u Bratislavy bylo pořád 15, a u Brna také 15.

4.) And now something completely different
Mám list, ve kterém jsou dvojice čísel, např.: [(1, 2), (3, 7), (9, 5)]
Napište kód, který ten list projde a spočítá součet součinů,
tj. v tomto případě 1 * 2 + 3 * 7 + 9 * 5
"""
##############

my_list = [(1,2),(3,7),(9,5)]

def count(my_list):
    a,b,c = my_list
    sum_of_numb = (a[0]*a[1]) + (b[0]*b[1]) + (c[0]*c[1])
    return sum_of_numb

print(count(my_list))