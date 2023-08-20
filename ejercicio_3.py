num=int(input("Ingresa un numero para saber si es primo: "))
cont=1
for i in range(2,num//2+1):
  if(num%i==0):
    cont=cont+1
if(cont>1):
  print("el numero no es primo")
else:
  print("El numero es primo")
