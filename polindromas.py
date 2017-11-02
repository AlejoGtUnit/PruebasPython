def quitarEspaciosTildes(entrada):
    palabra = entrada.lower()
    return palabra.replace(" ","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")

with open("entrada.csv") as entrada:
	with open("salida.csv", "w") as salida:
		polindromas = []
		lineas = entrada.readlines()
		
		for linea in lineas:
			for palabra in linea.split(","):
				if palabra != "":
					if quitarEspaciosTildes(palabra) == quitarEspaciosTildes(palabra[::-1]):
						polindromas.append(palabra)
				
		for elemento in ",".join(polindromas):
			salida.write(elemento);
	salida.close()
entrada.close()

