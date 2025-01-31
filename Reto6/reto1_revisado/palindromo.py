def es_palindromo(palabra):
    try:
        if not isinstance(palabra, str):
            raise ValueError("La entrada debe ser una cadena de texto.")
        
        palabra = palabra.lower()  # Convertir a minúsculas
        longitud = len(palabra)

        for i in range(longitud // 2):  # Iterar hasta la mitad de la palabra
            if palabra[i] != palabra[longitud - i - 1]:  # Comparar extremos opuestos
                return False

        return True  # Si se completó el bucle sin diferencias, es palíndromo
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        return False


# Ejemplo de uso
try:
    palabra = input("Ingrese una palabra: ").strip()
    
    # Validar que no esté vacía
    if not palabra:
        raise ValueError("La palabra no puede estar vacía.")

    # Verificar si es palíndromo
    if es_palindromo(palabra):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")
except ValueError as ve:
    print(f"Error en la entrada: {ve}")
except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")
