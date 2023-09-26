liste = [1, 0, 0, 4, 0, 1, 2, 0,0,0,0,0, 9, 10]

def sammenhengende_nuller(liste):
  antall_nuller = 0
  lengste_antall = 0
  
  for nummer in liste:
    if nummer == 0:
      antall_nuller += 1
    else:
      if lengste_antall < antall_nuller:
        lengste_antall = antall_nuller
      antall_nuller = 0
      
  return lengste_antall

print(f"Lengden til den lengste sammenhengende sekvensen av 0-ere er {sammenhengende_nuller(liste)}")