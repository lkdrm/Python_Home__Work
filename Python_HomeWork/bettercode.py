def sifr():
    text = input("Enter your text :").lower() # user enter a text
    number = int(input("Enter a value 1 or 3 to coded:")) # user enter in which letter wiil coded every third or first letter
    code = input("Do you want to code this or decoded?:") # user will write what he want code or decoded
    coded_abc = [] # Here coded_abc will append
    abc = ["a","b","c","d","e",
            "f","g","h","i","j","k","l",
            "m","n","o","p","q","r","s", 
            "t","u","v","w","x","y","z"] # Here the find_index will search a letter 
    for i in text:
        find_index = abc.index(i) # Will find a index of my letter 
        if  code == "code":     # If you write code , programm will coded your text
            coded_abc.append(abc[find_index+number]) # Send a index +number to coded_abc
        elif code == "decoded":   #If you write decoded, program will decode your text
            coded_abc.append(abc[find_index-number]) # modulo
    return "".join(coded_abc)

print(sifr())
