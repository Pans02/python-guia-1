palabra = input("Ingrese una palabra: ")
palabra2 = input(
  "Ingresa una segunda palabra para saber si rima con la anterior: ")
if (len(palabra) > 2 and len(palabra2) > 2):
  if(palabra[-3:]==palabra2[-3:]):
    print("Las palabras riman")
  elif(palabra[-2:]==palabra2[-2:]):
    print("Las palabras riman un poco")
  else:
    print("Las palabras no riman")
else:
  print("Las palabras no tienen elñ tamaño sufieciente")
