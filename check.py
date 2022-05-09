dict_of_logs = {'user':'1234',}
count = 1

while True:
    print("Hello this is my programm if you want login",
          "Enter please a Login.",
          "But if you`re first time, enter New.",
          "And we will created a new user",
          "",
    sep="\n")
    first_user = input("Enter here please: ")
    if first_user == "Login":
        user = input("Enter a login: ")
        if count == 3:
            break
        if user in dict_of_logs:
            pass_word = input("Enter a password:")
            print("Look:",pass_word)
            if pass_word == dict_of_logs[user]:
                print("You`re login")
                break
            else:
                print("Incorrect password\n")
                count+=1
        else:
            print("Incorrect login\n")
            count +=1
    elif first_user == "New":
        print()
        print("Below you can create a login")
        user = dict_of_logs.setdefault(input("Enter here a login which you will be use: "))
        print("We have save it")
        new_user_password = input("Enter here your new password: ")
        print(new_user_password)
        if len(new_user_password) >= 8:# check a long
            if len({"q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x",
                "c","v","b","n","m",'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',} & set(new_user_password)) >=3: # check if there are a letters
                if not new_user_password.islower() and not new_user_password.isupper(): # check a lower and upper 
                    if len({'1','2','3','4','5','6','7','8','9','0'} & set(new_user_password)) >=3: # check if there are a numbers
                        if len({'!','@','#','$','?','*'} & set(new_user_password)) >=1: # check if there is one symbol
                            dict_of_logs[input("Enter again you login: ")]=new_user_password
                            print("You have been create a new account\n")
                            print(dict_of_logs)
                        else:
                            print("You have not a special symbol like ('!','@','#','$','?','*',)\n\n")
                    else:
                        print("You have not a numbers, enter at least 3 numbers\n\n")
                else:
                    print("Pleas enter a lower and upper words\n\n")
            else:
                print("You have not a letters\n\n")
        else:
            print("You`re pass it too short!\n\n")