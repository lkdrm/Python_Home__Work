"""
Velký úkol na OOP:
Vytvořte třídu zvíře. Zvíře má počet nohou, barvu a metodu vydej_zvuk 
(metoda nebude nic dělat, obecné zvíře zvuk nevydává).

Vytvořte několik tříd na konkrétní zvířata. Např. třída pes, kočka, nebo taky
žirafa a slon. Zajímavá je třída had - ten má 0 nohou.

Každá nová třída bude mít něco navíc (atribut nebo metodu), např. pes může mít atribut rasu nebo
metodu hlidej_barak. (Dohromady vytvořte aspoň jednu metodu a aspoň jeden atribut.)
Každý potomek zvířete zároveň přepíše (přetíží) metodu vydej_zvuk po svém (např. pes zaštěká).
Vytvořte několik instancí různých zvířat.

Vytvořte si seznam (list) a uložte do něj několik instancí různých zvířat. Pak seznam projděte 
cyklem a nechte každé zvíře dát o sobě nahlas vědět (tedy vždy zavolejte metodu vydej_zvuk).

Dodělejte ke zvířatům metodu __str__ nebo __repr__, aby se hezky vypisovala. Zamyslete se, jestli 
se hodí víc k předkovi Zvire nebo k potomkům.

Vytvořte třídu Klec. Do klece se vejde několik zvířat. Vytvořte metodu 
pridej_zvire na přidání zvířete do klece.

(Vsuvka pro velmi pokročilé - tohle jsme nedělali, ale můžete si to zkusit vygooglit:
 Metoda pridej_zvire může mít víc parametrů (více různých zvířat) a přidá je všechny.)

Zařiďte, aby se hezky vypisovala včetně zvířat vevnitř (budeme to potřebovat později).
Můžete vytvořit několik instancí klecí a umístit do nich některé z už vytvořených zvířat.

Vytvořte třídu Zoo. Do zoo se vejde několik klecí. Vytvořte metodu pridej_klec na přidání klece do zoo.

(Vsuvka pro pokročilé: metoda pridej_klec umí přidat několik klecí najednou.)

Třída Zoo se umí hezky vypisovat (vypíše klece i zvířata v nich).
Vytvořte metodu vypis_podle_barvy, která projde celé zoo (všechny klece a zvířata v nich) a vypíše jen
zvířata s určitou barvou (barvu dostane jako parametr).
Vytvořte metodu vypis_podle_nohou, která projde celé zoo (všechny klece a zvířata v nich) a vypíše jen
zvířata s určitým počtem nohou (ten dostane jako parametr).

Do zoo přijel sponzor. Chce všem zvířatům koupit ponožky. Vytvořte metodu spocitej_nohy, která projde
všechny klece a zvířata v nich a spočítá počet nohou v celé zoo.

Vytvořte instanci třídy Zoo a užijte si ji. Vytvořte instance zvířat (pokud je už nemáte), 
do klecí dejte zvířata a klece dejte do zoo. Vypište si zvířata podle barev, podle počtu nohou 
a nezapomeňte spočítat počet ponožek pro sponzora!
"""
# 1 task:
"""
Vytvořte třídu zvíře. Zvíře má počet nohou, barvu a metodu vydej_zvuk 
(metoda nebude nic dělat, obecné zvíře zvuk nevydává).

"""

from unicodedata import name


class Animals:
    def __init__(self,legs:int,color:str):
        self.legs = legs
        self.color = color

    def a_voice(self):
        raise Exception("Animals can`t make a voice")

    def __str__(self):
        return f""

"""
Každá nová třída bude mít něco navíc (atribut nebo metodu), např. pes může mít atribut rasu nebo
metodu hlidej_barak. (Dohromady vytvořte aspoň jednu metodu a aspoň jeden atribut.)
Každý potomek zvířete zároveň přepíše (přetíží) metodu vydej_zvuk po svém (např. pes zaštěká).
Vytvořte několik instancí různých zvířat.

""" 
class HomePets(Animals):
    def __init__(self, legs: int, color: str,race:str,name:str):
        super().__init__(legs, color)
        self.name = name
        self.race = race

class Dog(HomePets):
    def __init__(self,color: str, race: str, name: str):
        super().__init__(4, color, race, name)

    def find_a_house(self):
        return f"Okay i go to find our house"

    def a_voice(self):
        return f"Waf waf"

    def __str__(self):
        return f"This my dog {self.name}" 
    
frank = Dog("black","shepherd","Frank")
Djack = Dog("black & green","shepherd","Djeck")

print(frank)
print(frank.a_voice())

class Cat(HomePets):
    def __init__(self, color: str, race: str, name: str, like_u:bool):
        super().__init__(4, color, race, name)
        self.like_u = like_u

    def a_voice(self):
        return f"Give me a food"

    def wake_up(self):
        return f"Jump on you"

    def __str__(self):
        return f"My cat {self.name}. He always want a food. He like me ? {self.like_u}"

flokie = Cat("black & white","mein coon","Flokie",False)
chubaka = Cat("orange","classick","Chubaka",True)
print(flokie)


class Snake(Animals):
    def __init__(self, color:str, change_color:bool,poison:str,name:str):
        super().__init__(0, color)
        self.change_color = change_color
        self.poison = poison
        self.name = name

    def a_voice(self):
        return f"Ssss"

    def __str__(self):
        return f"This snake have a name {self.name} & have a poison? {self.poison}. He change a colour {self.change_color}"

severus = Snake("green",True,"Yes he have a poison","Severus")
okar = Snake("Yellov",False,"No he didn`t have a poison","Okar")

print(severus)

"""
Vytvořte třídu Klec. Do klece se vejde několik zvířat. Vytvořte metodu 
pridej_zvire na přidání zvířete do klece.
"""

class Cage:
    def __init__(self):
        self.cage = []

    def insert_pet(self,animal):
        self.cage.append(animal)

    def __str__(self):
        """
        animal = ""  
        for pet in self.cage:
            animal += "This is my animal and have a name:"
            animal += str(pet.name)
            animal +="\n"
        return  animal 
        """
        compr = [
            " " +"\n" +"This is my animal and have a name: "+str(pet.name) 
            for pet in self.cage
            ] # compr
        return "".join(" " +"\n" +"This is my animal and have a name: "+str(pet.name) 
            for pet in self.cage) # generator
        

my_cage = Cage()

my_cage.insert_pet(frank)
my_cage.insert_pet(flokie)
my_cage.insert_pet(severus)

print(my_cage)

"""

Vytvořte třídu Zoo. Do zoo se vejde několik klecí. Vytvořte metodu pridej_klec na přidání klece do zoo.

(Vsuvka pro pokročilé: metoda pridej_klec umí přidat několik klecí najednou.)

Třída Zoo se umí hezky vypisovat (vypíše klece i zvířata v nich).
Vytvořte metodu vypis_podle_barvy, která projde celé zoo (všechny klece a zvířata v nich) a vypíše jen
zvířata s určitou barvou (barvu dostane jako parametr).
Vytvořte metodu vypis_podle_nohou, která projde celé zoo (všechny klece a zvířata v nich) a vypíše jen
zvířata s určitým počtem nohou (ten dostane jako parametr).

"""
class Zoo():
    def __init__(self):
        self.cage_for_dogs = []
        self.cage_for_cats = []
        self.cage_for_snakes = []
    
    def insert_animal(self,pet):
        if isinstance(pet,Dog):
            self.cage_for_dogs.append(pet)

        
    