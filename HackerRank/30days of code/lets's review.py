for i in range(int(input())):
    mystr = input()
    evenstr = ""
    oddstr = ""
    for i in range(len(mystr)):
        if(i%2==0):
            evenstr+=mystr[i]
        else:
            oddstr+=mystr[i]
    print("{} {}".format(evenstr,oddstr))
