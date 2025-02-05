partidos = []
fichero = open('partidos.txt','r+')
nuevo_fichero = None

def mostrar_menu():
	prompt = int(input('''1. Añadir un partido
2. Partidos jugados (Local & Visitante)
3. Eliminar un partido
4. Listar los nombres de los equipos participantes
5. Listado de clasificación de los equipos
6. Salir

daemoncibsec@proyecto >> '''))
	return prompt

def lectura_de_listas():
	for linea in fichero:
		entrada = linea.strip().split(", ")
		partido = [
			entrada[0].strip("'"), #Código del partido
			entrada[1].strip("'"), #Equipo local
			entrada[2].strip("'"), #Equipo visitante
			int(entrada[3].strip("'")), #Goles local
			int(entrada[4].strip("'")), #Goles visitante
			entrada[5].strip("'"), #Fecha del partido
			int(entrada[6].strip("'")) #Jornada
		]
		partidos.append(partido)

def eleccion(prompt):
	while prompt != 6:
		if prompt == 1:
			agregar_partido()
		elif prompt == 2:
			local_visitante(partidos)
		elif prompt == 3:
			eliminar_partido()
		elif prompt == 4:
			equipos_participantes()
		elif prompt == 5:
			clasificacion()
		else:
			print("Opción inválida. Por favor, especifique una opción válida que se encuentre en el menú.\n")
		prompt = mostrar_menu()
	salir(fichero,nuevo_fichero)


def agregar_partido():
	try:
		print('El partido se agregará en la última entrada.')
		nuevo_partido = []
		nuevo_partido.append(input('Código del partido: '))
		nuevo_partido.append(input('Equipo local: '))
		nuevo_partido.append(input('Equipo visitante: '))
		nuevo_partido.append(int(input('Goles del equipo local:')))
		nuevo_partido.append(int(input('Goles del equipo visitante: ')))
		nuevo_partido.append(input('Fecha: '))
		nuevo_partido.append(int(input('Jornada: ')))
		nueva_entrada = f"'{nuevo_partido[0]}', '{nuevo_partido[1]}', '{nuevo_partido[2]}', '{nuevo_partido[3]}', '{nuevo_partido[4]}', '{nuevo_partido[5]}', '{nuevo_partido[6]}'\n"
		fichero.write(nueva_entrada)
		print(f"El partido se añadirá exitosamente al cerrar el programa.\n")

	except Exception as e:
		print(f"Error: {e}\n")

def local_visitante(partidos):
	nombre = input('Introduzca el nombre del equipo que desea buscar: ')
	try:
			contador_local = 0
			contador_visitante = 0
			for lista in partidos:
				if nombre == lista[1].strip("'"):
					contador_local += 1
				elif nombre == lista[2].strip("'"):
					contador_visitante += 1
			if contador_local == 0 and contador_visitante == 0:
				print(f"'{nombre}' no ha jugado ningún partido.\n")
			else:
				print(f"El equipo '{nombre}' ha pertenecido {contador_local} veces al equipo local.")
				print(f"El equipo '{nombre}' ha pertenecido {contador_visitante} veces al equipo visitante.\n")

	except Exception as e:
		print(f"Error: {e}\n")

def eliminar_partido():
	cod=input('Escriba el código del partido a eliminar: ')
	try:
		if cod not in fichero:
			print(f"Error: El código '{cod}' no se halla en el fichero.\n")
		if cod in fichero:
			nueva_linea = [linea for linea in partidos if cod not in linea]
			nuevo_fichero = "\n".join(f"'{p[0]}', '{p[1]}', '{p[2]}', '{p[3]}', '{p[4]}', '{p[5]}', '{p[6]}'" for p in nueva_linea)
			with open('partidos.txt','w') as fichero1:
				fichero1.write(nuevo_fichero)
			print(f"El partido con el código '{cod}' ha sido eliminado.\n")
			return nuevo_fichero

	except Exception as e:
		print(f"Error: {e}\n")

def equipos_participantes():
	try:
		participantes = []
		for linea in partidos:
			if linea[1] not in participantes:
				participantes.append(linea[1])
			elif linea[2] not in participantes:
				participantes.append(linea[2])
		print(f"Los equipos participantes son:")
		for equipo in participantes:
			print(equipo)
		print("")

	except Exception as e:
		print(f"Error: {e}\n")

def clasificacion():
        equipos = {}
        for partido in partidos:
                equipo_local = partido[1]
                equipo_visitante = partido[2]
                goles_local = int(partido[3])
                goles_visitante = int(partido[4])

                if equipo_local not in equipos:
                        equipos[equipo_local] = {"ganados": 0, "perdidos": 0, "empatados": 0, "puntos": 0}
                if equipo_visitante not in equipos:
                        equipos[equipo_visitante] = {"ganados": 0, "perdidos": 0, "empatados": 0, "puntos": 0}
                if goles_local > goles_visitante:  # Gana el equipo local
                        equipos[equipo_local]["ganados"] += 1
                        equipos[equipo_local]["puntos"] += 2
                        equipos[equipo_visitante]["perdidos"] += 1

                elif goles_local < goles_visitante:  # Gana el equipo visitante
                        equipos[equipo_visitante]["ganados"] += 1
                        equipos[equipo_visitante]["puntos"] += 2
                        equipos[equipo_local]["perdidos"] += 1

                else:  # Empate
                        equipos[equipo_local]["empatados"] += 1
                        equipos[equipo_local]["puntos"] += 1
                        equipos[equipo_visitante]["empatados"] += 1
                        equipos[equipo_visitante]["puntos"] += 1

        clasificacion = sorted(equipos.items(), key=lambda x: x[1]["puntos"], reverse=True)

        print("\nClasificación de equipos:")
        print(f"{'Equipo':<15}{'Ganados':<10}{'Perdidos':<10}{'Empatados':<10}{'Puntos':<10}")
        print("-" * 55)

        for equipo, stats in clasificacion:
                print(f"{equipo:<15}{stats['ganados']:<10}{stats['perdidos']:<10}{stats['empatados']:<10}{stats['puntos']:<10}")
        print("")

def salir(fichero,nuevo_fichero):
	if nuevo_fichero is not None:
		with open('partidos.txt','w') as fichero1:
			fichero1.write(nuevo_fichero)
	fichero.close()
	exit()
