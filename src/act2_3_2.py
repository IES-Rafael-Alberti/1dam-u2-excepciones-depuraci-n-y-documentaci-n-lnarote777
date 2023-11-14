"""
Ejercicio 2.3.2

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

def impares(num):
    """Contador de números impares.

    Args:
        num (int): Número que introduce el usuario para contar los impares hasta llegar a él.

    Raises:
        ValueError: error que salta cuando se introduce un número negativo

    Returns:
        str: cadena de caracteres de números impares.
    """
    if num < 0 :
        raise ValueError ("El número no puede ser negativo.")
    
    cont = 1
    suma = str()
    for i in range(1, num + 1, 2) :
        cont += i
        if i != num:
            suma += str(f"{i}, ")
        else:
            suma += str(f"{num}. ")
    return suma
    
    
    
def main(): 
    n = int(input("Introduzca un número: "))
    try: 
        print(impares(n))
    except ValueError as e:
        print("ERROR - " + str(e))

    
    
if __name__ == "__main__":
    main()