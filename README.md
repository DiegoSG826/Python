# RegistroDeEstudiantes

## Índice
1. [Descripción del proyecto](#descripción-del-proyecto)
2. [Desarrollo](#desarrollo)
3. [Instrucciones para ejecutar los programas](#instrucciones-para-ejecutar-los-programas)
4. [Estructura del código](#estructura-del-código)
5. [Capturas del Funcionamiento](#Capturas-Funcionamiento)
6. [Enlace al repositorio de GitHub](#Enlace-al-repositorio)

---

## **Descripción del Proyecto**
Este proyecto consiste en un programa que registra estudiantes, calcula sus promedios a partir de 3 calificaciones y determina si están aprobados (promedio ≥ 6.0).  
**Objetivos**:  
- Practicar el manejo de estructuras de datos (listas/diccionarios en Python, arreglos en C++).  
- Implementar funciones para cálculos y validaciones.  
- Convertir un programa de Python a C++ como ejercicio de aprendizaje.  

### **Funcionalidades**
1. Registro dinámico de estudiantes (cantidad definida por el usuario).  
2. Validación de entradas (nombres no vacíos, calificaciones entre 0 y 10).  
3. Cálculo automático de promedios y estado (Aprobado/Reprobado).  
4. Reporte final con resultados individuales y estadísticas globales.  

---

## **Desarrollo**
### **Versión Python (`Promedios.py`)**
- Usa **diccionarios** para almacenar datos de cada estudiante.  
- Incluye funciones reutilizables como `calcular_promedio()` y `obtener_num()` (con validación).  
- Ejemplo de salida:  
  ```python
  Ana - Promedio: 8.0 - Aprobado
  Luis - Promedio: 5.0 - Reprobado

### **Versión C++ (`Promedios.cpp`)**
- Utiliza un **arreglo de estructuras** (Estudiante) para almacenar los datos.
- Replica la lógica de Python, adaptando sintaxis y manejo de memoria.
- Incluye validación de nombres y calificaciones.

---

## **Instrucciones para ejecutar los programas**

### **Versión Python (`Promedios.py`)**
1. **Requisitos**:  
   - Python 3.6 o superior instalado.  

2. **Ejecución**:  
   Abre una terminal en la carpeta del proyecto y ejecuta:  
   ```
   python Promedios.py
   ```

3. **Uso**:
- Ingresa el número de estudiantes a registrar.
- Proporciona el nombre y las 3 calificaciones de cada uno.
- Al finalizar, verás los resultados con promedios y estados.

### **Versión C++ (`Promedios.cpp`)**
1. **Requisitos**:  
   - Compilador g++ instalado (en Linux/macOS) o MinGW (en Windows). 

2. **Compilación**:  
   Desde la terminal, ejecuta:  
   ```
   g++ Promedios.cpp -o Promedios
   ```
   
3. Ejecución:
- Linux/macOS:
   ```
   ./Promedios
   ```
   
- Linux/macOS:
   ```
   Promedios.exe
   ```

4.**Uso**:
- Sigue las mismas instrucciones que en la versión Python.

---

## **Estructura del Código**

### **Python**
- Diccionarios: Almacenan datos de cada estudiante:
```python
estudiantes.append({
    "nombre": nombre,
    "promedio": promedio,
    "estado": "Aprobado" if promedio >= 6 else "Reprobado"
})
```
- Validaciones:
  - Nombre no vacío
  - Calificaciones entre 0 y 10  

### **C++**
- Arreglo de estructuras:
```python
struct Estudiante {
    string nombre;
    float promedio;
    string estado;
    int calificaciones[3];
};
```
- Validaciones:
  - Usa getline() para nombres con espacios.
  - Filtra números fuera del rango 0-10.

---

## **Ejemplo de salida**

### **Python**
- Diccionarios: Almacenan datos de cada estudiante:
```bash
--- RESULTADOS ---
Ana - Promedio: 8.0 - Aprobado
Luis - Promedio: 5.0 - Reprobado

Total de estudiantes aprobados: 1
Total de estudiantes reprobados: 1
```

---

## **Capturas Funcionamiento**

- Ingreso del número de estudiantes y la información del estudiante:

![image](https://github.com/user-attachments/assets/c037d882-6944-42cd-bae2-da2f82758c86)


- Validación de calificaciones:

![image](https://github.com/user-attachments/assets/e44ac7e6-1e39-4871-8128-cd9e020f6a8b)


- Resultados:

![image](https://github.com/user-attachments/assets/6350426a-31ef-41f0-a23a-a76e92f56c68)


--- 

## **Enlace al repositorio**

(https://github.com/DiegoSG826/Python)
