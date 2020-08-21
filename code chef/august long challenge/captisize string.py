def myfun(teststr): 
    testWords = teststr.split(" ")
    newlist = []
    for x in testWords:
        newtest = x[::-1]
        newtest = newtest.capitalize()
        newlist.append(newtest) 
    result = " ".join(newlist)
    return result
teststr = input()
print(myfun(teststr))