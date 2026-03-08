def main():
    inicio = int(input("Ingrese el numero de inicio:"))
    iteraciones = int(input("Ingrese el numero de iteraciones:"))
    
    if iteraciones <= 0:
        print("El numero de iteraciones no puede ser negativo")
    else:
        lista = []
        a , b = 0, 1
            
        for i in range(inicio - 1):
            a, b = a + b, a
            
        
        for i in range(iteraciones):
            lista.append(a)
            a , b = a + b, a
            
        
        print("La lista completa es:", lista)
        print("Cantidad de terminos generados:", len(lista))
        print("El ultimo numero generado es:", lista[-1])
        
        # Estas dos lineas son para verificar que si funciona el programa, no se si es necesario dejarlas o no, pero las dejo por si acaso
        print("El numero de inicio es:", inicio)
        print("El numero de iteraciones es:", iteraciones)
        
if __name__ == "__main__":
    main()