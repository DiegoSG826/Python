def obtener_num(mensaje, minimo=1, maximo=None):  # Funcion para obtener valores enteros validos
    valido = False
    while not valido:
        entrada = input(mensaje)
        if entrada.isdigit():  # Verifica si la entrada es un número
            valor = int(entrada)
            if valor >= minimo and (maximo is None or valor <= maximo):
                return valor
            else:
                if maximo is not None:
                    print(f"Error: El número debe estar entre {minimo} y {maximo}")
                else:
                    print(f"Error: El número debe ser mayor o igual a {minimo}")
        else:
            print("Error: Ingrese un número entero válido")

def calcular_promedio(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    promedio = suma / len(lista)
    return promedio

# Programa principal
estudiantes=[]
calificaciones=[]
print("Sistema de promedios de estudiantes\n")
num_estudiantes = obtener_num("\nIngrese el numero de estudiantes: ")
print("Ingrese las calificaciones de los estudiantes:")

for i in range(num_estudiantes):
    print(f"\nEstudiante {i+1}")
    
    # Validación nombre no vacío
    valido=False
    while valido==False:
        nombre=input("Nombre: ")
        if nombre=="":
            print("Error: El nombre no puede estar vacío")
        else:
            break

    calificaciones = [] #Reinicia la calif. por estudiante    
    
    for j in range(3):
        calificacion = obtener_num(f"Calificación Materia {j + 1} (0-10): ", 0, 10)
        calificaciones.append(calificacion)
    
    promedio = calcular_promedio(calificaciones)
    #estado = evaluar_aprobacion(promedio)

    estudiantes.append({ #se usa un diccionario para estudiantes
        "nombre": nombre,
        "promedio": promedio,
        "estado": "Aprobado"
        if promedio >= 6 else "Reprobado"
    })

#Mostrar resultados
print("\n--- RESULTADOS ---")

for estudiante in estudiantes:
    print(f"{estudiante['nombre']} - Promedio: {estudiante['promedio']:.1f} - {estudiante['estado']}")

print(f"\nTotal de estudiantes aprobados: ")
print(f"Total de estudiantes reprobados: ")