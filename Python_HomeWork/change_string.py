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

#First task:
# samohlasky =  a, e, i/y, o, u;
# souhlásky = h, ch, k, r, d, t, n, b, f, l, m;
word = "air"
word_2 = "computer"
def find_and_change(word):
    change = list(word)
    if change[0] in "aeiyou":
        change[-1] += "way"
        return "".join(change)
    else:
        change[-1] += change[0]
        change[0] = ""
        change[-1] += "ay"
        return "".join(change)
# computer => omputercay
# Better version from teacher:

word = "air,"
word_2 = "computer."
def find_and_change_2(word):
    if word[0] in "aeiyou" and ".,":
        change = word[0:-1] + "way" + word[-1]
        return change.title()
    elif word[0] in "aeiyou" :
        word +="way"
        return word.title()
    if word[0] in "hckrdtnbflm" and ".,":
        change = word[1:-1] + word[0] + "ay" + word[-1]
        return change.title()
    elif word[0] in "hckrdtnbflm":
        change = word[1:-1] + word[0] + "ay" + word[-1]

print(find_and_change_2(word_2))
print(find_and_change_2(word))


my_text = "I love air and computer"

def change_text(text):
    my_text = text.split()
    for i in my_text:   
        if i[0].lower() in "aeiyou":
            find = my_text.index(i) 
            change = my_text.pop(find) + "way"
            my_text.insert(find,change)
        if i[0].lower() in "hckrdtnbflm":
             find = my_text.index(i)
             change = my_text.pop(find)
             change_2 = change[1:] + change[0] + "ay" #+ #change[-1]
             my_text.insert(find,change_2) 
    return " ".join(my_text)

print(change_text(my_text))

