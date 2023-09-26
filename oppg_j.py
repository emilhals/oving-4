from oppg_e import numberList
from lister_for_del_1 import temperaturer

def endring(a):
    if a>0:return"stigende"
    elif a<0: return "synkende"
    else: return "uforandret"

templist = numberList(temperaturer)
tempEndring = [endring(templist[i]) for i in range(len(templist))]

#print(tempEndring)