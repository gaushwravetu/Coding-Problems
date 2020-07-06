def mystery(l):
    if l==[]:
        return(1)
    else:
        return(l[-1] + mystery(l[:-1]))
