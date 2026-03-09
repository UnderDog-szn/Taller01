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
            cadena = input("Ingrese una cadena de texto: ")
            vocales = "aeiouAEIOU"
            contador_vocales = 0
            for letra in cadena:
                if letra in vocales:
                    contador_vocales += 1
            print(f"La cantidad de vocales en la cadena es: {contador_vocales}")
        elif opcion == 4:
            flag = False
        else:    
            print("Opcion no valida")

if __name__ == "__main__":
    main()