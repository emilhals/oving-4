liste = [4, 7, 15]

def sum_av_tall_over_fem(liste):
  total = 0
  for tall in liste:
    if (tall > 5):
      total += tall - 5

  return total

summen = sum_av_tall_over_fem(liste)

print(f"Summen av {liste} er {summen}")