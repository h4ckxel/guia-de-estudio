def Numeros ():
        while True:
                try:
                        num_uno = int(input("Ingresa el primer numero: "))
                        num_dos = int(input("Ingresa el segundo numero: "))
                        return num_uno, num_dos
                except ValueError:
                        prit("Debes de ingresar los numero lo siento. Intenta de nuevo")

num_uno, num_dos = Numeros()
print (f"La suma  de {num_uno} + {num_dos} = ",  num_uno + num_dos)
print (f"La resta  de {num_uno} - {num_dos} = ", num_uno - num_dos)
if num_uno == 0 or num_dos == 0:
        print ("La division no se puede hacer")
else:
        print (f"La divicion  de {num_uno} / {num_dos} = ", num_uno / num_dos)


# Dificultad extra


def Numeros ():
        while True:
                try:
                        num_uno = int(input("Ingresa el primer numero: "))
                        num_dos = int(input("Ingresa el segundo numero: "))
                        return num_uno, num_dos
                except ValueError:
                        prit("Debes de ingresar los numero lo siento. Intenta de nuevo")

num_uno, num_dos = Numeros()
operacion = (input ("Que operación deseas realizar con los numeros anteriores suma, resta, ó division? "))
if operacion == "suma":
        print (f"La suma  de {num_uno} + {num_dos} = ",  num_uno + num_dos)
elif operacion == "resta":
        print (f"La resta  de {num_uno} - {num_dos} = ", num_uno - num_dos)
elif operacion == "division":
        if num_uno == 0 or num_dos == 0:
                print ("La division no se puede hacer")
        else:
                print (f"La divicion  de {num_uno} / {num_dos} = ", num_uno / num_dos)

