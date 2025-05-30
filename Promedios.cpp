#include <iostream>
#include <string>

using namespace std;

struct Estudiante {
    string nombre;
    float promedio;
    string estado;
    int calificaciones[3];
};

int obtener_num(string mensaje, int minimo = 1, int maximo = -1) {
    string entrada;
    int valor;
    
    while(true) {
        cout << mensaje;
        getline(cin, entrada);
        
        bool es_numero = true;
        for(char c : entrada) {
            if(!isdigit(c)) {
                es_numero = false;
                break;
            }
        }
        
        if(es_numero) {
            valor = stoi(entrada);
            if(valor >= minimo && (maximo == -1 || valor <= maximo)) {
                return valor;
            } else {
                if(maximo != -1) {
                    cout << "Error: Debe estar entre " << minimo << " y " << maximo << endl;
                } else {
                    cout << "Error: Debe ser mayor o igual a " << minimo << endl;
                }
            }
        } else {
            cout << "Error: Ingrese un número entero válido" << endl;
        }
    }
}

float calcular_promedio(int calificaciones[3]) {
    float suma = 0;
    for(int i = 0; i < 3; i++) {
        suma += static_cast<float>(calificaciones[i]);
    }
    return suma / 3;
}

int main() {
    Estudiante estudiantes[100];
    int num_estudiantes;
    
    cout << "Sistema de promedios de estudiantes\n" << endl;
    num_estudiantes = obtener_num("\nIngrese el numero de estudiantes: ");
    
    for(int i = 0; i < num_estudiantes; i++) {
        cout << "\nEstudiante " << i+1 << endl;
        
        //Validar nombre
        while(true) {
            cout << "Nombre: ";
            getline(cin, estudiantes[i].nombre);
            
            string nombre_sin_espacios;
            for(char c : estudiantes[i].nombre) {
                if(c != ' ' && c != '\t' && c != '\n') {
                    nombre_sin_espacios += c;
                }
            }
            
            if(!nombre_sin_espacios.empty()) {
                estudiantes[i].nombre = nombre_sin_espacios;
                break;
            }
            cout << "Error: El nombre no puede estar vacio" << endl;
        }
        
        //OBTENER CALIFICACIONES
        for(int j = 0; j < 3; j++) {
            estudiantes[i].calificaciones[j] = obtener_num(
                "Calificacion Materia " + to_string(j+1) + " (0-10): ", 0, 10
            );
        }
        
        //CALCULAR PROMEDIO Y ESTADO
        estudiantes[i].promedio = calcular_promedio(estudiantes[i].calificaciones);
        estudiantes[i].estado = (estudiantes[i].promedio >= 6) ? "Aprobado" : "Reprobado";
    }
    
    cout << "\n--- RESULTADOS ---" << endl;
    int aprobados = 0, reprobados = 0;
    
    for(int i = 0; i < num_estudiantes; i++) {
        cout << estudiantes[i].nombre << " - Promedio: " << estudiantes[i].promedio;
        cout << " - " << estudiantes[i].estado << endl;
        
        if(estudiantes[i].estado == "Aprobado") {
            aprobados++;
        } else {
            reprobados++;
        }
    }
    
    cout << "\nTotal de estudiantes aprobados: " << aprobados << endl;
    cout << "Total de estudiantes reprobados: " << reprobados << endl;
    
    return 0;
}