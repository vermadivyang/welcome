password = input("Please state the password to continue.   ")
if password == "Nothing":
    name = input("What is your full name?   
    email = input("What is your email?   ")
    print("Your name is " + name + " ,and your email is " + email)
    conf = input("Is this correct? Y/N   ")
    if conf == "Y":
        userN = input("Please tell us what your username is.   ")
        passW = input("Please tell us what your password is.   ")
        print("Your password is " + passW + " and your username is " + userN)
        print("") 
        TRUE=input("Was that correct? Y/N   ")
        if TRUE == "Y":
            print("Thank you for your time, have a nice day.")
            print("bye")
