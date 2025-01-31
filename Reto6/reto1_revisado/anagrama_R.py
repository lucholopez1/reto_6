def filtrar_anagramas(lista_palabras):
    try:
        anagramas = []
        for palabra in lista_palabras:
            for otra_palabra in lista_palabras:
                if palabra != otra_palabra and sorted(palabra) == sorted(otra_palabra):
                    anagramas.append(palabra)
                    break
        return anagramas
    except TypeError:
        print("Error: La lista debe contener únicamente cadenas de texto.")
        return []
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        return []

try:
    # Solicitar lista de palabras al usuario
    entrada = input("Ingrese una lista de palabras separadas por comas: ")
    if not entrada.strip():
        raise ValueError("La entrada no puede estar vacía.")
    
    lista_palabras = [palabra.strip() for palabra in entrada.split(",")]

    # Validar que la lista no esté vacía después de procesarla
    if not lista_palabras:
        raise ValueError("La lista de palabras no puede estar vacía.")

    # Llamar a la función y mostrar el resultado
    resultado = filtrar_anagramas(lista_palabras)
    print("Palabras que tienen los mismos caracteres:", resultado)
except ValueError as ve:
    print(f"Entrada no válida: {ve}")
except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")
