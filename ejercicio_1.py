import random

valor = random.randint(1, 100)
while True:
  numero = int(input("Ingresa un valor entre el 1 y el 100: "))
  if (numero == valor):
    print("Felicidades numero encontrado")
    break

  elif (numero < valor):
    print("El numero ingresado es demasiado bajo\n")

  elif (numero > valor):
    print("El numero ingresado es demasiado alto\n")
