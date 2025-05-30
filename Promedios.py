def obtener_num(mensaje, minimo=1, maximo=None):  # Función para obtener valores enteros válidos
    valido = False
    while not valido:
        entrada = input(mensaje)
        if entrada.isdigit():
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

def contar_aprobados_reprobados(lista_estudiantes):
    aprobados = 0
    reprobados = 0
    for est in lista_estudiantes:
        if est["estado"] == "Aprobado":
            aprobados += 1
        else:
            reprobados += 1
    return aprobados, reprobados

# Programa principal
estudiantes = []
print("Sistema de promedios de estudiantes\n")
num_estudiantes = obtener_num("\nIngrese el número de estudiantes: ")
print("Ingrese las calificaciones de los estudiantes:")

for i in range(num_estudiantes):
    print(f"\nEstudiante {i+1}")
    
    # Validación nombre no vacío
    while True:
        nombre = input("Nombre: ")
        if nombre.strip() == "":
            print("Error: El nombre no puede estar vacío")
        else:
            break

    calificaciones = []  # Reinicia la lista de calificaciones por estudiante    
    
    for j in range(3):
        calificacion = obtener_num(f"Calificación Materia {j + 1} (0-10): ", 0, 10)
        calificaciones.append(calificacion)
    
    promedio = calcular_promedio(calificaciones)

    estudiantes.append({
        "nombre": nombre,
        "promedio": promedio,
        "estado": "Aprobado" if promedio >= 6 else "Reprobado"
    })

# Mostrar resultados
print("\n--- RESULTADOS ---")

for estudiante in estudiantes:
    print(f"{estudiante['nombre']} - Promedio: {estudiante['promedio']:.1f} - {estudiante['estado']}")

# Contar aprobados y reprobados
aprobados, reprobados = contar_aprobados_reprobados(estudiantes)

print(f"\nTotal de estudiantes aprobados: {aprobados}")
print(f"Total de estudiantes reprobados: {reprobados}")
