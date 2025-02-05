from funciones import *

lectura_de_listas()
prompt = mostrar_menu()
while prompt > 7 or prompt < 0:
	print("Opción inválida. Por favor, escoja una opción que se encuentre en el menú.\n")
	prompt = mostrar_menu()
eleccion(prompt)
