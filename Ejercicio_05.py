def validar_campos():
        
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre) > 3:
            break
        print("El nombre debe tener más de 3 caracteres. Intente nuevamente.")
        
    while True:
        edad = int(input("Ingrese su edad"))
        
        if 0 <= edad <= 120:
            break
        print("La edad debe ser un número entre 0 y 120. Intente nuevamente.")

    while True:
        correo = input("Ingrese su correo electrónico: ")
        if "@" in correo and (".com" in correo or "edu.co" in correo):
            break
        print("El correo electrónico debe contener '@' y '.com/.edu.co'. Intente nuevamente.")

    return {"nombre": nombre, "edad": edad, "correo": correo}

def main():
    estudiantes = []
    
    datos = validar_campos()
    estudiantes.append(datos)
    print("Datos ingresados:", estudiantes)
    
if __name__ == "__main__":
    main()