while (True):
  operacion = int(
    input(
      "¿Que conversion desea realizar?: \n 1) centrimetros->pulgadas \n 2) metros->kilometros\n 3) onzas->gramos \n 4) milla->kilometro \n 5) celcius->farenheit \n 6) Salir  \n (Ingrese el numero de la operacion a realizar)\n:"
    ))
  if(operacion==1):
    num_a_convertir = float(input("Ingrese el valor en CM que desea convertir a In: "))
    print("El resultado de la conversion es de: ",num_a_convertir/2.54)
  elif(operacion==2):
    num_a_convertir = float(input("Ingrese el valor M que desea convertir a KM: "))
    print("El resultado de la conversion es de: ",num_a_convertir/1000)
  elif(operacion==3):
    num_a_convertir = float(input("Ingrese el valor en OZ que desea convertir a GR: "))
    print("El resultado de la conversion es de: ",num_a_convertir/0.035274)
  elif(operacion==4):
    num_a_convertir = float(input("Ingrese el valor en MI que desea convertir a KM: "))
    print("El resultado de la conversion es de: ",num_a_convertir/0.621371)
  elif(operacion==5):
    num_a_convertir = float(input("Ingrese el valor en CELSIUS que desea convertir a FARENHEIT: "))
    resultado=(9/5)*num_a_convertir+32
    print("El resultado de la conversion es de: ",resultado)
  elif(operacion==6):
    break
  else:
    print("ERROR AL INGRESAR LA OPCION")
