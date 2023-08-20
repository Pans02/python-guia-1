def mas_largo(lista):
  mayor=lista[0]
  for i in lista:
    if(len(i)>len(mayor)):
      mayor=i
  return mayor
Palabras=[]  
while(True):
  palabra=input("Ingrese una palabra para añadir a la lista: ")
  Palabras.append(palabra)
  seguir=int(input("¿Desea ingresar otra palabra? 1=>si 2=>no: "))
  if(seguir==2):
    break
print("La palabra mas larga es: ",mas_largo(Palabras))
