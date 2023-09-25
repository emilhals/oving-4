temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
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