def main():
    
    base = float(input("Ingrese el valor de la base: " ))
    
    impuesto = base * 0.19
    
    if base >= 200000:
        descuento = base * 0.10
    else:  
        descuento = 0
    
    total = base + impuesto - descuento
    
    print(f"El valor del impuesto es: {impuesto}")
    print(f"El valor del descuento es: {descuento}")
    print(f"El valor total a pagar es: {total}")


if __name__ == "__main__":
    main()