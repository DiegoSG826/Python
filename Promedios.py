#FUNCION PARA OBTENER UN NUMERO ENTERO CON VALIDACION
def obtener_num(mensaje, minimo=1, maximo=None):
    valido = False
    while not valido:
        entrada = input(mensaje)
        if entrada.isdigit():
            valor = int(entrada)
            if valor >= minimo and (maximo is None or valor <= maximo):
                return valor
            else:
                if maximo is not None:
                    print(f"Error: El numero debe estar entre {minimo} y {maximo}")
                else:
                    print(f"Error: El numero debe ser mayor o igual a {minimo}")
        else:
            print("Error: Ingrese un nymero entero valido")

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

# INICIO DEL PROGRAMA
estudiantes = []
print("Sistema de promedios de estudiantes\n")
num_estudiantes = obtener_num("\nIngrese el numero de estudiantes: ")
print("Ingrese las calificaciones de los estudiantes:")

for i in range(num_estudiantes):
    print(f"\nEstudiante {i+1}")
    
    
    while True:
        nombre = input("Nombre: ")
        if nombre.strip() == "":
            print("Error: El nombre no puede estar vacio")
        else:
            break

    calificaciones = []
    
    for j in range(3):
        calificacion = obtener_num(f"Calificacion Materia {j + 1} (0-10): ", 0, 10)
        calificaciones.append(calificacion)
    
    promedio = calcular_promedio(calificaciones)

    estudiantes.append({
        "nombre": nombre,
        "promedio": promedio,
        "estado": "Aprobado" if promedio >= 6 else "Reprobado"
    })

#RESULTADOS
print("\n--- RESULTADOS ---")

for estudiante in estudiantes:
    print(f"{estudiante['nombre']} - Promedio: {estudiante['promedio']:.1f} - {estudiante['estado']}")

#CONTEO APROBADOS Y REPROBADOS
aprobados, reprobados = contar_aprobados_reprobados(estudiantes)

print(f"\nTotal de estudiantes aprobados: {aprobados}")
print(f"Total de estudiantes reprobados: {reprobados}")