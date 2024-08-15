def modificar_ingredientes(ingredientes):
    while True:
        print("\n¿Quieres modificar o agregar algún ingrediente?")
        print("1.Agregar ingrediente")
        print("2.Eliminar ingrediente")
        print("No quiero modificar ni agregar nada")

        eleccion = input("Ingrese el número de tu elección: ")

        if eleccion == "1":
            print("\nIngrendientes disponibles para agregar:")
            print(
                "Tomate, Champiñones, Aceituna, Cebolla, Pollo, Jamón, Carne, Tocino, Queso"
            )
            nuevo_ingrediente = input("Ingresa el ingrediente que deseas agregar: ")

            if nuevo_ingrediente in ingredientes:
                print(f"{nuevo_ingrediente} ya está en la pizza.")
            else:
                ingredientes.append(nuevo_ingrediente)
                print(f"{nuevo_ingrediente} agregado a la pizza.")
