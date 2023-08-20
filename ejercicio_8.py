def circulo(radio):
  return (radio**2)*(3.14)
def cilindro(radio,altura):
  return circulo(radio)*altura
operacion=int(input("¿Que operacion desea realizar?\n1) Area de un Circulo\n2) Volumen de un cilindro\n(Ingrese el numero correspondiente a la operacion):\n"))  
if(operacion==1):
  radio=int(input("Ingrese el radio del circulo: "))
  print("El Area del circulo es de: ", circulo(radio))
elif(operacion==2):
  radio=int(input("Ingrese el radio de la base del cilindro: "))
  altura=int(input("Ingrese la altura del cilindro: "))
  print("El volumen del cilindro es de: ", cilindro(radio,altura))
else:
  print("\nERROR al ingresar la operacion")
