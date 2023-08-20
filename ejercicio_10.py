diccionario={}
while(True):
  articulo=input("Ingrese el articulo que desea comprar: ")
  precio=int(input("Ingrese el precio del articulo: "))
  diccionario[articulo]=precio
  seguir=int(input("¿Desea ingresar otra articulo? 1=>si 2=>no: "))
  if(seguir==2):
    break
print("Lista de compra:\n")    
print("Articulo|  Precio:")
total=0
for a,p in diccionario.items():
  print(a,"|  ",p)
  total=total+p
print("Total: ",total)
