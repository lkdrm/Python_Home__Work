"""
1.) Nadefinujte třídu Motor. Motor má typ a výkon. 
Nadefinujte třídu Auto. Auto má značku a motor. Jako motor se používá instance
třídy motor.

Motor i auto se umí hezky vypisovat.

Vytvořte několik instancí třídy auto a několik instancí třídy motor. Nějaké 
motory uložte do proměnných, nějaké vytvořte přímo při vytváření aut.

Zkuste změnit typ motoru tak, že si na něj sáhnete ne přímo, ale přes auto, 
které ho používá.

2.) Vytvořte třídu Kniha. Kniha má jméno, autora a rok vydání.
Vytvořte třídu PoliceNaKnihy. Do police se vejde neomezené množství knih.
Vytvořte ve třídě metodu na přidávání knih (ať je nemusíte přidávat přímo.)

Zařiďte, ať se Kniha i PoliceNaKnihy hezky vypisuje.

Vytvořte několik instancí knih, aspoň jednu instanci PoliceNaKnihy a 
několik knih do ní uložte.
"""

"""
1.) Nadefinujte třídu Motor. Motor má typ a výkon. 
Nadefinujte třídu Auto. Auto má značku a motor. Jako motor se používá instance
třídy motor.

Motor i auto se umí hezky vypisovat.

Part_2:

Vytvořte několik instancí třídy auto a několik instancí třídy motor. Nějaké 
motory uložte do proměnných, nějaké vytvořte přímo při vytváření aut.

Part_3:

Zkuste změnit typ motoru tak, že si na něj sáhnete ne přímo, ale přes auto, 
které ho používá.

"""

class Motor:
    def __init__(self,type:str, hp:int):
        self.type = type
        self.hp = hp

    def __str__(self):
        return f"the type of motor is {self.type} and this motor have a {self.hp} - horse power"

plyn_power_low = Motor("Plyn", 75)
disel_power_med = Motor("Diesel", 300)
benzin_power_high = Motor("Benzin", 550)

class Car:
    def __init__(self,mark:str,model:str, motor:Motor):
        self.mark = mark
        self.model = model
        self.motor = motor

    def __str__(self):
        return f"The mark of car is {self.mark} and a model is {self.model}. \nThis car have  {self.motor}"

mercedes_car = Car("Mercedes","C-class",benzin_power_high)
volkswagen_car = Car("Volkswagen","Passat-b8",disel_power_med)
skoda_car = Car("Skoda","Fabia",plyn_power_low)

print(mercedes_car)
print(volkswagen_car)
print(skoda_car)

# Part_2:
"""
Vytvořte několik instancí třídy auto a několik instancí třídy motor. Nějaké 
motory uložte do proměnných, nějaké vytvořte přímo při vytváření aut.

"""

hunday_car = Car("hunday","don`t know",Motor("diesel",50))

print(hunday_car)

#Part_3:

"""
Zkuste změnit typ motoru tak, že si na něj sáhnete ne přímo, ale přes auto, 
které ho používá.

"""

hunday_car = Motor("Plyn",30)

print(hunday_car)



########################################################################################

"""
2.) Vytvořte třídu Kniha. Kniha má jméno, autora a rok vydání.
Vytvořte třídu PoliceNaKnihy. Do police se vejde neomezené množství knih.
Vytvořte ve třídě metodu na přidávání knih (ať je nemusíte přidávat přímo.)

Zařiďte, ať se Kniha i PoliceNaKnihy hezky vypisuje.

Vytvořte několik instancí knih, aspoň jednu instanci PoliceNaKnihy a 
několik knih do ní uložte.

"""

class Book:
    def __init__(self,name:str,author:str,year:int):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return f"This book was created by {self.author}. Book named - {self.name} was written in year {self.year}"

the_lord_of_the_rings = Book("The Lord of the Rings","J. R. R. Tolkien",1954)
the_elven_sword = Book("The Elven","Bernhard Hennen",2004)
harry_potter = Book("Harry Potter","J. K. Rowling",1997)

class My_shelve:
    def __init__(self):
        self.books = []

    def insert_books(self,book):
        self.books.append(book)

    def __str__(self):
        str_with_text = ""
        if len(self.books) == 0:
            return "The shelves is empty"
        for text in self.books:
            str_with_text += str(text)
            str_with_text += ".\n"
        return str_with_text
        


my_book = My_shelve()

my_book.insert_books(the_lord_of_the_rings)
my_book.insert_books(the_elven_sword)
my_book.insert_books(harry_potter)

print(my_book)
