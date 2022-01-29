"""
1.) Vytvořte funkci, která vezme slovo # ready
a vytvoří z něj slovo v Pig Latin
a) Když slovo začíná samohláskou, přidá se na konec "way"
b) Když slovo začíná souhláskou, souhláska se odebere, přidá se na konec 
a za ní se přidá "ay"
air => airway
ear => earway
elephant => elephantway
computer => omputercay
cat => atcay
papaya => apayapay

2.) Těžší verze: # ready
Pokud je v daném slově první písmeno velké, 
bude velké první písmeno i ve výsledku
Computer => Omputercay

3.) Ještě těžší verze: # ready
Slovo může mít na konci tečku nebo čárku -
pokud tam je, bude na konci i ve výsledku
"computer," => "omputercay,"

4.) To samé, ale s celou větou (věta se nejdříve
rozdělí na slova, nakonec se zase spojí)
- můžete použít funkci ze cvičení jedna,
nemusíte uvažovat diakritiku a velká písmena

5.) Ještě jeden tajný dětský jazyk, tentokrát se jmenuje Ubbi Dubbi
Napište funkci, která vezme slovo, vytvoří
z něj nové slovo a před každou samohlásku přidá písmena "ub"
octopus => uboctubopubus

-----------------------------------------------------------------------------------------------------------------------

Pokud chcete další cvičení, tak zde (ale spíše jako domácí úkol):
1.) Spočítejte, kolik je ve slově samohlásek (ale pokud jste zvládli 
to předtím, tak tohle bude dost lehké)
"elephant" => 3

2.) Spočítejte, kolikrát se ve slově vyskytuje sekvence "bob"
'azcbobobegghakl' => 2

3.) Napište funkci, která vezme řetězec a seřadí písmena v něm 
podle abecedy

4.) Těžší úkol:
Napište funkci, která vezme řetězec, a najde nejdelší podřetězec, 
ve kterém jsou písmena řazená podle abecedy
'azcbobobegghakl' => 'beggh'

5.) Caesarova šifra - písmenka se posunou na další písmenko v abecedě
a => b
b => c
c => d
z => a

ahoj => bipk (posun o jedna)
ahoj => dkrm (posun o tři)

6.) Ceasarova šifra naopak - rozkódovat
"""
# samohlasky =  a, e, i,y, o, u;
# souhlásky = h, ch, k, r, d, t, n, b, f, l, m;

#------------------------#
#1 First task:

word = "elephant"

def find_and_count(word):
    count = 0
    for i in word :
        if i in "aeiyou":
            count+=1
    return count

print(find_and_count(word))

#2 Second task:

word_2 = "azcbobbobegghakl"

print(word_2.count("bob"))

#3 third task:

my_text = "Hello this is my line which will be sorted"

def sort_text(text):
    text_list = text.split(" ")
    return sorted(text_list)
    

print(sort_text(my_text))

#4 fourth task:
# Caeserova sifra:

text = "hello"
text_2 = "ahoj"

text_3 = "bipk"
text_4 = "dkrm"

def sifr(text,number,code):
    coded_abc = []
    abc = ["a","b","c","d","e",
            "f","g","h","i","j","k","l",
            "m","n","o","p","q","r","s",
            "t","u","v","w","x","y","z"]
    if  code == "code":     
        if  number == 3:    
            for i in text:
                find_index = abc.index(i)
                new_append = coded_abc.append(abc[find_index+3])
            return "".join(coded_abc)
        elif number == 1:
            for i in text:
                find_index = abc.index(i)
                new_append = coded_abc.append(abc[find_index+1])
            return "".join(coded_abc)
    elif code == "decoded":
        if  number == 3:    
            for i in text:
                find_index = abc.index(i)
                new_append = coded_abc.append(abc[find_index-3])
            return "".join(coded_abc)
        elif number == 1:
            for i in text:
                find_index = abc.index(i)
                new_append = coded_abc.append(abc[find_index-1])
            return "".join(coded_abc)
    return "".join(coded_abc)

print(sifr(text,3,"code"))
