def elegir_masa():
    print("\nElige el tipo de masa que quieres para tu pizza: ")
    print("1.Masa tradicional")
    print("2.Masa delgada")
    print("3.Masa con bordes de queso")

    eleccion = input("Ingresa el número de tu elección: ")
    if eleccion == "1":
        return "Masa tradicional"
    elif eleccion == "2":
        return "Masa delgada"
    elif eleccion == "3":
        return "Masa con bordes de queso"
    else:
        print("Número no válido")
