palabra=input("Ingrese una palabra: ")
letra= input("Ingrese una letra: ")
cont=0
if(len(letra)>1):
  print("ERROR")
else:
  for i in palabra:
    if(i==letra):
      cont=cont+1
print("La letra ",letra,"se encuentra ",cont," veces en la palabra")
