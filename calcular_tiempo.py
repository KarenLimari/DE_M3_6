def calcular_tiempo(ingredientes):
    """
    Permite calcular el tiempo de preparación de la pizza basado en la cantidad de ingredientes.
    Parámetros:
    -----------
    ingredientes: list
        Lista de ingredeintes de la pizza. Cada ingrediente adicional suma 2 minutos.
    Returns:
    --------
    int
        El tiempo total estimado en minutos de preparación de la pizza.
    """
    tiempo_base = 20  # tiempo base en minutos.
    tiempo_total = tiempo_base + 2 * len(
        ingredientes
    )  # Cada ingrediente adicional suma 2 minutos.
    return tiempo_total
