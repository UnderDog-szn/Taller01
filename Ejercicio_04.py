def main():
    flag = True
    while flag:
        print("Seleccione una de las siguientes opciones:")
        print("1. Verificar si un numero es primo")
        print("2. Calcular factorial de un numero")
        print("3. Contar vocales de una cadena de texto")
        print("4. Salir")    

        opcion = int(input("Seleccione una opcion: "))
    
        if opcion == 1:
            numero = int(input("Ingrese un numero: "))
            if numero < 2:
                print("Los numeros menores a 2 no son primos" )
            else:
                es_primo = True
                for i in range(2, numero):
                    if numero % i == 0:
                        es_primo = False
                        break
                if es_primo:
                    print(f"{numero} es un numero primo")
                else:
                    print(f"{numero} no es un numero primo")
        elif opcion == 2:
            numero = int(input("Ingrese un numero: "))
            factorial = 1
            for i in range(1, numero + 1):
                factorial *= i
            print(f"El factorial de {numero} es {factorial}")
        elif opcion == 3:
            conteo = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
            cadena = input("Ingrese una cadena de texto: ")
            for letra in cadena:
                if letra.lower() in conteo:
                    conteo[letra.lower()] +=1
            for vocal, cantidad in conteo.items():
                print(f"{vocal}: {cantidad}")
        elif opcion == 4:
            print("Saliendo del programa...")
            flag = False
        else:    
            print("Opcion no valida")

if __name__ == "__main__":
    main()