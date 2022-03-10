"""
1.) Vytvořte třídu DomaciZvire. DomaciZvire ma jmeno a metodu vydej_zvuk. Metoda vydej zvuk může 
být prázdná (obecné zvíře žádný zvuk nevydává).

2.) Vytvořte třídu Pes jako potomka třídy DomaciZvire. Pes má kromě jména navíc rasu. Přepište 
ve třídě pes metodu vydej_zvuk (jaký zvuk vydává pes asi víte). Vytvořte ve třídě pes ještě jednu 
metodu (něco pseicfického pro psy).

3.) Vytvořte třídu Kocka jako potomka třídy DomaciZvire. Vymyslete nějaký atribut a nějakou metodu,
kterou má kočka navíc oproti domácímu zvířeti. Přepište  ve třídě kočka metodu vydej_zvuk
(jaký zvuk vydává kočka asi víte). 

4.) Stejným způsobem můžete vytvořit i třídu Slepice (jeden nový atribut, jedna nová metoda,
přepsat metodu vydej_zvuk).

5.) Vytvořte několik instancí, aspoň jednoho psa, jednu kočku a jednu slepici.

BONUS:
6.) Vytvořte seznam, a instance do něj uložte. Projdětě seznam cyklem a na každém zvířeti
v seznamu zavolejte vydej_zvuk.

"""
# 1.) Vytvořte třídu DomaciZvire. DomaciZvire ma jmeno a metodu vydej_zvuk. Metoda vydej zvuk může 
# být prázdná (obecné zvíře žádný zvuk nevydává).

class HomePet:
    # class created a home pet gave him a name & one move
    def __init__(self,name:str):
        self.name = name

    def a_voice(self):
        return f"I`ve a voice"

    def __str__(self):
        return f"Hi my name is {self.name}"

joe = HomePet("Joe")
print(joe)
# 2.) Vytvořte třídu Pes jako potomka třídy DomaciZvire. Pes má kromě jména navíc rasu. Přepište 
# ve třídě pes metodu vydej_zvuk (jaký zvuk vydává pes asi víte). Vytvořte ve třídě pes ještě jednu 
# metodu (něco pseicfického pro psy).

class Dog(HomePet):
    # the class created a pet a take from superclass a name
    def __init__(self, name: str, race:str):
        super().__init__(name)
        self.race = race

    def a_voice(self):
        return f"Waf-waf"

    def find_a_friend(self):
        return f"I go to find my friend where did h hide?"

    def __str__(self):
        return f"This is my dog & he have a name - {self.name}. And his race is - {self.race}"

pakie = Dog("Pakie","shepherd")

print(pakie)
print(pakie.a_voice())

# 3.) Vytvořte třídu Kocka jako potomka třídy DomaciZvire. Vymyslete nějaký atribut a nějakou metodu,
# kterou má kočka navíc oproti domácímu zvířeti. Přepište  ve třídě kočka metodu vydej_zvuk
# (jaký zvuk vydává kočka asi víte). 

class Cat(HomePet):
    #the class created a cat take a name from super class
    def __init__(self, name: str,race:str,color:str):
        super().__init__(name)
        self.race = race
        self.color = color
    
    def a_voice(self):
        return f"Where is my foood"

    def go_outside(self):
        return f"Go to the door & wait.. until my slave don`t go to the doors. And than go to another side"

    def __str__(self):
        return f"This is my cat {self.name}, he is {self.race} and have a {self.color}"

flokie = Cat("Flokie","Mein-Coon","Black & white")
print(flokie)
print(flokie.a_voice())
print(flokie.go_outside())

# 4.) Stejným způsobem můžete vytvořit i třídu Slepice (jeden nový atribut, jedna nová metoda,
# přepsat metodu vydej_zvuk).

class Turtle(HomePet):
    #the class created a turtle take a name from super class
    def __init__(self, name: str,year:int,hobby:str):
        super().__init__(name)
        self.year = year
        self.hobby = hobby

    def a_voice(self):
        return f"I don`t know"
    
    def run(self):
        return f"I go too slowly to you like a raggy boy)"

    def __str__(self):
        return f"This is my turtle {self.name} and have a {self.year} years old. And have a hobby - {self.hobby}"

cartman = Turtle("Cartman",30,"Look how your gone old")

print(cartman)
print(cartman.hobby)
print(cartman.run())

# 6.) Vytvořte seznam, a instance do něj uložte. Projdětě seznam cyklem a na každém zvířeti
# v seznamu zavolejte vydej_zvuk.

class AllHomePets:
    # the class just print your all pets 
    def __init__(self):
        self.my_list = []

    def insert_a_HomePet(self,pet):
        self.my_list.append(pet)

    def __str__(self):
        str_with_text = ""
        if len(self.my_list) == 0:
            return f"Your list is empty" 
        for pet in self.my_list:
            str_with_text += str(pet)
            str_with_text += ".\n"
        return str_with_text

my_pets = AllHomePets()

my_pets.insert_a_HomePet(joe)
my_pets.insert_a_HomePet(pakie)
my_pets.insert_a_HomePet(flokie)
my_pets.insert_a_HomePet(cartman)

print(my_pets)

list_of_my_pets = []

list_of_my_pets.append(joe)
list_of_my_pets.append(pakie)
list_of_my_pets.append(flokie)
list_of_my_pets.append(cartman)

for pet in list_of_my_pets:
    print(pet.a_voice())