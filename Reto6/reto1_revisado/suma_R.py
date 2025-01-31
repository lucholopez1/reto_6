def mayor_suma_consecutivos(numeros):
    try:
        if not isinstance(numeros, list):
            raise TypeError("El argumento debe ser una lista.")
        if len(numeros) < 2:
            raise ValueError("La lista debe tener al menos dos elementos.")

        suma_maxima = numeros[0] + numeros[1]
        for i in range(1, len(numeros) - 1):
            suma_actual = numeros[i] + numeros[i + 1]
            if suma_actual > suma_maxima:
                suma_maxima = suma_actual

        return suma_maxima
    except TypeError as te:
        return f"Error: {te}"
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"Ha ocurrido un error inesperado: {e}"


# Solicitar lista de números al usuario
try:
    entrada = input("Ingrese una lista de números separados por comas: ").strip()
    if not entrada:
        raise ValueError("La entrada no puede estar vacía.")
    
    # Convertir la entrada en una lista de números enteros
    numeros = [int(num.strip()) for num in entrada.split(",")]

    # Llamar a la función y mostrar el resultado
    resultado = mayor_suma_consecutivos(numeros)
    print("La mayor suma entre elementos consecutivos es:", resultado)
except ValueError as ve:
    print(f"Error en la entrada: {ve}")
except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")
