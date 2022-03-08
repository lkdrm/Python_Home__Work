class Human:
    peoples = 0
    
    def __init__(self, name:str, year:int):
        self.name = name
        self.year = year
        self.__class__.peoples+=1
    
    def __str__(self):
        return f"My name is {self.name} & I`m {self.year} years old."

    @classmethod # class method
    def count_peoples(cls):
            print(f"We have spawn : {cls.peoples} peoples")
    
    @staticmethod # statik method
    def count_peoples_2():
        print(f"We have spawn : {__class__.peoples} peoples")

first_human = Human("Tommy",25)
second_human = Human("Joe",34)
third_human = Human("Mike",40)

Human.count_peoples()
Human.count_peoples_2()
print(first_human,second_human,third_human, sep="\n")


"""
4.) Otázky z TEORIE:
a) Jak se liší statická a třídní metoda, vzhledem k počtu parametrů?

Ze staticka metoda neprijima zadny parametr a tridni ma aspon jeden parametr "cls"

b) K čemu je dobrý parametr "cls" ve třídní metodě?

Ze ukazuje primo na class - cls. Nezalezi jak se jmenuje trida primo na nej ukazuje 

c) Na co se odkazuji pomocí "self.__class__"?

Okdazuje se primo na tridu ve ktere se nachazi eventualnim odkaz.

napr:

class Human:
    pocet = 0
        def__init__(self,neco_neco):
        self.neco = neco_neco
        pocet +=1


class vypis:
    def _neco:
        return f"{__class__.self.pocet}"

    jestli zmenime jmeno class tak styjne vytiskne to co potrebuje , at kterekoliv bude jmeno

"""