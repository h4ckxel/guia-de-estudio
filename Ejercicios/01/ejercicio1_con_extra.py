# Ejercicio 1
nombre = input("Ingresa tu nombre o como te dicen: ")
edad = int(input("Ingresa tu edad por favor: "))

print(f"Hola {nombre} bienvenido a mi primer programa, me alegra que tengas {edad} años :)")

# Extra 


#def validar_edad(edad):
    #return edad<0

#while True:
#   nombre, edad = datos()
    
 #   if not nombre or not edad:
  #      print("Debes de ingresar todos los datos. Intenta de nuevo.")
   # elif validar_edad(edad):
    #    print("La edad debe ser mayor a cero. Intenta de nuevo.")
    #else:
     #   print(f"¡Hola {nombre}! Bienvenido, me alegra que tengas {edad} años.")
      #  break

while True:
    nombre = input("Ingresa tu nombre ó el como te gusta que te digan: ")
    edad = int(input("Ingresa tu edad por favor: "))
    
    if not nombre or not edad:
        print("Debes de ingresar todos los datos. Intenta de nuevo.")
    elif edad < 0:
        print("La edad debe ser mayor a cero. Intenta de nuevo.")
    else:
        print(f"¡Hola {nombre}! Bienvenido, me alegra que tengas {edad} años.")
        break



