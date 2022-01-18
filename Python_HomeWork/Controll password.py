dict_of_keys = {
    "Andy":"adc86",
    "Mike":"post82",
    "Kail":"asdv190"
    }

def user():
    count = 0
    while True:
        key = input("Enter a login: ")
        if key in dict_of_keys:
            value = input("Enter a password: ")
            if value in dict_of_keys[key]:
                print("You are - log in")
            else:
                count+=1
                print("Enter a correct password")
        else:
            print("Enter a correct login")
        if count == 3:
            print("You have write wrong passwords we block your acess!")
            break
 

user()
