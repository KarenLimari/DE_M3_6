def elegir_salsa():
    print("\nElige el tipo de salsa que quieres para tu pizza: ")
    print("1.Salsa de tomate")
    print("2.Salsa Alfredo")
    print("3.Salsa Barbecue")
    print("4.Salsa Pesto")

    eleccion = input("Ingresa el número de tu elección: ")
    if eleccion == "1":
        return "Salsa de tomate"
    elif eleccion == "2":
        return "Salsa Alfredo"
    elif eleccion == "3":
        return "Salsa Barbecue"
    elif eleccion == "4":
        return "Salsa Pesto"
    else:
        print("Número no válido")
