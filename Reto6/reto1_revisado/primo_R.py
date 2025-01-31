def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def filtrar_primos(lista):
    try:
        primos = [num for num in lista if es_primo(num)]
        return primos
    except TypeError:
        print("Error: La lista debe contener únicamente números enteros.")
        return []
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        return []

try:
    # Solicitar lista de números al usuario
    entrada = input("Ingrese una lista de números separados por comas: ")
    if not entrada.strip():
        raise ValueError("La entrada no puede estar vacía.")
    
    # Convertir la entrada en una lista de enteros
    numeros = [int(num.strip()) for num in entrada.split(",")]

    # Filtrar y mostrar los números primos
    primos = filtrar_primos(numeros)
    print("Números primos:", primos)
except ValueError as ve:
    print(f"Error en la entrada: {ve}")
except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")
