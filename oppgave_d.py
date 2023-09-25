
a = [1.2, 2.4, 5.2, 8.4, 10.39, 11.7, 12.7]
b = 10

def tell_elementer(flyt_tall_liste, enkelt_verdi):
  større = 0
  større_liste = []

  for i in flyt_tall_liste:
    if i >= enkelt_verdi:
      større_liste.append(i)

  return større_liste

print(tell_elementer(a, b))