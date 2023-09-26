from lister_for_del_1 import dogn_nedbor

def lengde_periode_uten_nedbør(liste):
  antall_døgn = 0
  lengste_døgn = 0
  
  for nummer in liste:
    if nummer != 0:
      antall_døgn += 1
    else:
      if lengste_døgn < antall_døgn:
        lengste_døgn = antall_døgn
      antall_døgn = 0
      
  return antall_døgn

print(f"Lengste perioden uten nedbør er {lengde_periode_uten_nedbør(dogn_nedbor)}")