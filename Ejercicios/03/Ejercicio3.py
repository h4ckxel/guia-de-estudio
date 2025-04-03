def Datos():
        while True:
                try:
                        nombre = input("Ingresa tu nombre: ")
                        edad = int(input("Ingresa tu edad: "))
                        return nombre, edad
                except ValueError:
                        print ("Debes de ingresar tu edad correcta sin decimales por favor. Lo sieto, intenta de nuevo")
nombre, edad = Datos()
if edad <= 12:
        print ("Tu edad determina que eres un niño. Disfruta tu niñez.")
elif edad >= 15 and edad <= 17:
        print ("Tu edad determina que eres un adolescente. Disfruta tu adolescencia.")
elif edad >= 18 and edad <= 64:
        print ("Tu edad determina que eres un adulto. Disfruta tu Adultez")
elif edad >= 65:
        print ("Tu edad determina que eres un adulto de la tercera edad. Disfrute su vida.")


# Dificultad extra

def Datos():
        while True:
                try:
                        nombre = input("Ingresa tu nombre: ")
                        edad = int(input("Ingresa tu edad: "))
                        return nombre, edad
                except ValueError:
                        print ("Debes de ingresar tu edad correcta sin decimales por favor. Lo sieto, intenta de nuevo")

def Pais():
	while True:
		try:
			pais  = int(input("A que edad se determina la mayoria de edad en tu país, a los 18 ó 21 años? "))
			return pais
		except ValueError:
			print ("Ingrese a que edad te ve como un adulto en tu país por favot. Intentalo de nuevo.")


nombre, edad = Datos()
pais = Pais()
if pais == 18:
	if edad <= 12:
        	print ("Tu edad determina que eres un niño. Disfruta tu niñez.")
	elif edad >= 15 and edad <= 17:
        	print ("Tu edad determina que eres un adolescente. Disfruta tu adolescencia.")
	elif edad >= 18 and edad <= 64:
        	print ("Tu edad determina que eres un adulto. Disfruta tu Adultez")
	elif edad >= 65:
        	print ("Tu edad determina que eres un adulto de la tercera edad. Disfrute su vida.")
elif pais == 21:
        if edad <= 12:
                print ("Tu edad determina que eres un niño. Disfruta tu niñez.")
        elif edad >= 15 and edad <= 20:
                print ("Tu edad determina que eres un adolescente. Disfruta tu adolescencia.")
        elif edad >= 21 and edad <= 64:
                print ("Tu edad determina que eres un adulto. Disfruta tu Adultez")
        elif edad >= 65:
                print ("Tu edad determina que eres un adulto de la tercera edad. Disfrute su vida.")
