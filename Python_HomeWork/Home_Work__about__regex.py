#1 task: ready
#  Napište regex, který najde slovo LES, LED nebo LEV.
import re

my_text = "This notebook have a ledlight and les and lev"

regex = re.compile(r"le(s|d|v)")
result = regex.search(my_text)

print(result.group())

#2 task:
#    Napište regex, který najde slovo HAD nebo HRAD.
import re

my_text_2 = "Some people say - hrad. But I have a had(snake)"

regex_2 = re.compile(r"hr?ad?")
result_2 = regex_2.search(my_text_2)

print(result_2.group())

#3 task:
#   Napište regex, který najde slovo ZAHRADA, OHRADA, PODHRADÍ nebo HRADBY.
import re

my_text_3 = "Napište regex, který najde slovo zahrada, ohrada, podhradi nebo hradby"

#regex_3 = re.compile(r"((za|o|pod)?hrad(a|i|by))")# or [zaopd]*hrad[aiby]+
regex_3 = re.compile(r"[zaopd]*hrad[aiby]+")
result_3 = regex_3.search(my_text_3)

print(result_3.group())

#4 task:
#   Napište regex, který najde slovo končící na -NOST (např. spravedlnost).
import re

my_text_4 = "Napište regex, který najde slovo končící na -nost (např. spravedlnost)."

regex_4 = re.compile(r"\w+nost\b")
result_4 = regex_4.search(my_text_4)

print(result_4.group())

#5 task:
#   Napište regex, který najde mezeru (nebo i jiný bílý znak) následující po čárce, tečce, dvojtečce nebo středníku.
import re

my_text_5 = "Edit the Expression & Text to see matches. Roll over matches or the expression for details. PCRE & JavaScript flavors of !RegEx are! supported. Valid? ate your expression with Tests mode."

regex_5 = re.compile(r"[,.:?!]\s")
result_5 = regex_5.split(my_text_5)

print(result_5)

#6 task:
#   Napište regex, který najde slovo o délce minimálně 7 znaků.
import re

my_text_6 = "RegExr was created by gskinner.com, and is proudly hosted by Media Temple."

regex_6 = re.compile(r"[A-Za-z]{7}")
result_6 = regex_6.search(my_text_6)

print(result_6.group())

#7 task:
#   Napište regex, který najde slovo neobsahující písmeno o (nebo O).
import re

my_text_7 = "Napište regex, který najde slovo neobsahující písmeno o (nebo O)."

regex_7 = re.compile(r"\b[^oO\s]+\b")
result_7 = regex_7.search(my_text_7)

print(result_7.group())

#8 task:
#   8. Napište regex, který najde telefonní číslo ve formátu tři číslice, mezera,Stři číslice, znovu mezera a nakonec znovu tři číslice.
import re

my_text_8 = "my number is - 777 645 789"

regex_8 = re.compile(r"(\b(\d{3}) (\d{3} \d{3}))\b")
result_8 = regex_8.search(my_text_8)

print(result_8.group())

#9 task:
#   Napište regex, který ověří email. Pojďme se domluvit, že emaily zjednodušíme -
#   email začíná na písmena včetně číslic a teček, pak je zavináč, pak opět číslice a písmena,
#   přesně jedna tečka a nakonec dva nebo tři písmenné znaky. (Skutečné regexy pro emaily bývají 
#   mnohem složitější, tím se nebudeme zabývat - dají se vygooglit.)

import re


my_email = "bork322gmail.com"
my_email_2 = ""

regex_9 = re.compile(r"[\w?\d]+@+\w\D[^?!].+[com|net]\b")
result = regex.search(my_email)

print(result.group())
