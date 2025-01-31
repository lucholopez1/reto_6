def calculadora(a, b, operador):
    try:
        if operador == "+":
            return a + b
        elif operador == "-":
            return a - b
        elif operador == "*":
            return a * b
        elif operador == "/":
            if b != 0:
                return a / b
            else:
                raise ZeroDivisionError("No se puede dividir entre cero.")
        else:
            raise ValueError("Operador no válido. Use +, -, *, o /.")
    except ZeroDivisionError as zde:
        return f"Error: {zde}"
    except ValueError as ve:
        return f"Error: {ve}"

# Solicitar datos al usuario
while True:
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        operador = input("Ingrese el operador (+, -, *, /): ").strip()

        # Llamar a la función y mostrar el resultado
        resultado = calculadora(a, b, operador)
        print("Resultado:", resultado)

        # Preguntar si quiere realizar otra operación
        continuar = input("¿Desea realizar otra operación? (s/n): ").strip().lower()
        if continuar != "s":
            print("Gracias por usar la calculadora. ¡Adiós!")
            break
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
