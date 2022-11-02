# skaitļa minēšanas spēle
# bibliotēka random funkcijai
import random
# noteikumi
print("Spēles noteikumi:")
print(45*'-')
print("Dators "iedomājas"pozitīvu skaitli no 1 līdz 10. Lietotājs mēģina šo skaitli atminēt, katrā minēšanas reizē dators uzrāda, vai minējums ir lielāks vai mazāks par uzdoto skaitli. Ja skaitlis uzminēts, var redzēt ar cik minēšanas reizēm. Var izvēlēties spēlēt vēl.")
print(45*'-')
spele='true'   #nosacījums spēles atkārtošanai
#spēles atkārtošanas cikls

while spele:
#minēšanas cikls
# datora minējums
  r=random.randint(1,10)
# atminamā skaitļa ievade
#minēšanas reižu skaitītājs
  n=0
  while i>0:
  i=int(input("Ievadi veselu pozitīvu skaitli no 1-10: "))
# palielinu skaitītāja vērtību 
    if i==r:
      print("skaitlis uzminēts ar", n, "minēšanas reizēm")
      break
    else:
      if i<r: 
        print ("skaitlis:",i, "mazāks par minējumu:",r)
      else: 
        if i>r: 
          print ("skaitlis",i, "lielāks par minējumu:",r)
        else:
          break
    n+=1
  print(45*"-")
  rep=input("Vai vēlies spēli atkārtot (Jā/Nē): ")
  if rep=="Nē":
    spele='false'
    break
print ("Spēle beigusies.")
  