def numberList(inlist):
    newlist = [inlist[x+1]-inlist[x] for x in range(0,len(inlist)-1)]
    return newlist