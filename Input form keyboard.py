while(True):
    try:
        username = input("Enter your id: ")
        userid = int(username)
    except ValueError:
        print("Not a correct user id \n Try again!")
    else:
        print("Your user id accepted:", userid)
        break
