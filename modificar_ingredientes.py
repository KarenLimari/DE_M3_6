def modificar_ingredientes(ingredientes):
    while True:
        print("\n¿Quieres modificar o agregar algún ingrediente?")
        print("1.Agregar ingrediente")
        print("2.Eliminar ingrediente")
        print("3.No quiero modificar ni agregar nada")

        eleccion = input("Ingrese el número de tu elección: ")

        if eleccion == "1":
            print("\nIngrendientes disponibles para agregar:")
            print(
                "Tomate, Champiñones, Aceituna, Cebolla, Pollo, Jamón, Carne, Tocino, Queso"
            )
            nuevo_ingrediente = input(
                "Ingresa el ingrediente que deseas agregar: "
            ).capitalize()

            if nuevo_ingrediente in ingredientes:
                print(f"{nuevo_ingrediente} ya está en la pizza.")
            else:
                ingredientes.append(nuevo_ingrediente)
                print(f"{nuevo_ingrediente} agregado a la pizza.")

        elif eleccion == "2":
            print("\nIngredientes actuales:", ingredientes)
            eliminar_ingrediente = input(
                "Ingresa ingrediente que deseas eliminar: "
            ).capitalize()
            if eliminar_ingrediente in ingredientes:
                ingredientes.remove(eliminar_ingrediente)
                print(f"{eliminar_ingrediente} ha sido eliminado de la pizza")
            else:
                print(f"{eliminar_ingrediente} no está en la pizza")

        elif eleccion == "3":
            break

        else:
            print("Opción no váida. Intenta de nuevo")

            return ingredientes


ingredientes = ["Queso"]
modificar_ingredientes(ingredientes)
