def main():
    estudiante = {
        "nombre": "Juan",
        "edad": 20,
        "carrera": "Ingeniería",
        "activo": True,
        "materias": ["Calculo Vectorial", "Física Moderna", "Programación 2"],
        "notas": {
            "Calculo Vectorial": 3.3,
            "Física Moderna": 3.1,
            "Programación 2": 4.5
        }
    }

    
    if len(estudiante["materias"]) < 3:
        print("Error: debe haber al menos 3 materias.")
        return


    for materia, nota in estudiante["notas"].items():    
        if nota < 0.0 or nota > 5.0:
            print(f"Error: la nota de {materia} está fuera del rango válido.")
            return

    promedio = (estudiante["notas"]["Calculo Vectorial"] + estudiante["notas"]["Física Moderna"] + estudiante["notas"]["Programación 2"]) / len(estudiante["notas"])
    print("El promedio de las notas es", promedio)

    mejorMateria = max(estudiante["notas"], key=estudiante["notas"].get)
    print("La mejor materia es:", mejorMateria, "con una nota de", estudiante["notas"][mejorMateria])

    peorMateria = min(estudiante["notas"], key=estudiante["notas"].get)
    print("La peor materia es:", peorMateria, "con una nota de", estudiante["notas"][peorMateria])
    
    if promedio >= 3.0:
        aprobar = True
        print("El estudiante ha aprobado.")
    else: 
        print("El estudiante no ha aprobado")



if __name__ == "__main__":
    main()

