from lister_for_del_1 import temperaturer

def sum_av_tall_over_fem(liste):
  total = 0
  for tall in liste:
    if (tall > 5):
      total += tall - 5

  return total

summen = sum_av_tall_over_fem(temperaturer)

print(f"Summen av {temperaturer} er {summen}")