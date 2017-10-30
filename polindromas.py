with open("entrada.csv") as entrada:
	with open("salida.csv", "w") as salida:
		polindromas = []
		lineas = entrada.readlines()
		
		for linea in lineas:
			for palabra in linea.split(","):
				palabra = palabra.rstrip();
				if palabra != "":
					if palabra == palabra[::-1]:
						polindromas.append(palabra)
				
		for elemento in ",".join(polindromas):
			salida.write(elemento);
	salida.close()
entrada.close()