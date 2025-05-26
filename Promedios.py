def obtener_num(mensaje): #Funcion para obtener valores enteros validos
    valido=False
    while valido==False:
        entrada = input(mensaje)
        if entrada.isdigit():  #Verifica si la entrada es un numero
            valor = int(entrada)
            if 1 <= valor:
                return valor
            print("Error: Debe ser mayor a 1")
        else:
            print("Error: Ingrese un numero entero valido")

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
    
    for j in range(3):
        calificacion = obtener_num(f"Calificación Materia {j + 1} (0-10): ", 0, 10)
        calificaciones.append(calificacion)
    
    #promedio = calcular_promedio(calificaciones)
    #estado = evaluar_aprobacion(promedio)

    estudiantes.append({ #se usa un diccionario para estudiantes
        "nombre": nombre,
        #"promedio": promedio,
        #"estado": estado
    })

#Mostrar resultados
print("\n--- RESULTADOS ---")

for estudiante in estudiantes:
    print(f"{estudiante['nombre']} - Promedio: {estudiante['promedio']:.1f} - {estudiante['estado']}")

print(f"\nTotal de estudiantes aprobados: ")
print(f"Total de estudiantes reprobados: ")