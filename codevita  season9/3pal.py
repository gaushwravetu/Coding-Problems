# cook your dish here
def checker(text):
    size=len(text)
    if size==1:
        return True
    else:
        pass
    k=size//2
    for x in range(k):
        if text[-x-1]!=text[x]:
            return False
    return True
    
text=input(); solved=False
for x in range(1,len(text)-2):
        if checker(text[:x]):
            for y in range(x+1,len(text)):
                if checker(text[x:y]) and checker(text[y:]):
                    print(text[:x],text[x:y],text[y:],sep="\n")
                    solved=True
                    break
            if solved:
                break
if not solved:
    print("impossible")
