"""
Ejercicio 2.3.4

Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
"""


def convertirAEntero(entrada: str) -> int:
    """Convertir una cadena de caracteres en un número entero

    Args:
        entrada (str): una cadena de caracteres

    Returns:
        int: número entero de la conversión de la cadena de caracteres
    """
    num = int(entrada)   
    return num


def main():
    n = input("Introduzca un número:")
    try:
        num = convertirAEntero(n)
    except Exception:
        print("La entrada no es correcta")
    
    
if __name__ == "__main__":
    main()