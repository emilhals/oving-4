from lister_for_del_1 import temperaturer

b = 10

def tell_elementer(flyt_tall_liste, enkelt_verdi):
  større = 0
  større_liste = []

  for i in flyt_tall_liste:
    if i >= enkelt_verdi:
      større_liste.append(i)

  return større_liste

sommer_dager = len(tell_elementer(temperaturer, 20))
høysommer_dager = len(tell_elementer(temperaturer, 25))
trope_dager = len(tell_elementer(temperaturer, 30))

print(f"Antall sommerdager: {sommer_dager} | Antall høysommerdager: {høysommer_dager} | Antall tropedager: {trope_dager}")

#print(tell_elementer(temperaturer, b))