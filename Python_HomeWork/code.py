def sifr():
    text = input("Enter your text :") # user enter a text
    number = int(input("Enter a value 1 or 3 to coded:")) # user enter in which letter wiil coded every third or first letter
    code = input("Do you want to code this or decoded?:") # user will write what he want code or decoded
    coded_abc = [] # Here coded_abc will append
    abc = ["a","b","c","d","e",
            "f","g","h","i","j","k","l",
            "m","n","o","p","q","r","s",
            "t","u","v","w","x","y","z"] # Here the find_index will search a letter 
    if  code == "code":     # If you write code , programm will coded your text
        if  number == 3:    # That means every third letter
            for i in text:
                find_index = abc.index(i) # Will find a index of my letter
                new_append = coded_abc.append(abc[find_index+3]) # Send a index +3 to coded_abc
            return "".join(coded_abc) # Created as a text
        elif number == 1:   # That means every one letter
            for i in text:
                find_index = abc.index(i)
                new_append = coded_abc.append(abc[find_index+1])
            return "".join(coded_abc)
    elif code == "decoded":   #If you write decoded, program will decode your text
        if  number == 3:    # That means every third letter
            for i in text:
                find_index = abc.index(i)
                new_append = coded_abc.append(abc[find_index-3])
            return "".join(coded_abc)
        elif number == 1:   # That means every one letter
            for i in text:
                find_index = abc.index(i)
                new_append = coded_abc.append(abc[find_index-1])
            return "".join(coded_abc)
    return "".join(coded_abc)

print(sifr())
