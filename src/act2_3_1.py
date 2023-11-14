"""
Ejercicio 2.3.1

Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

def edad_cumplida(edad):
    """Recuento de años que ha cumplido el usuario.

    Args:
        edad (int): edad que tiene el usuario.

    Raises:
        ValueError: Error que salta cuando se introduce un número negativo.

    Returns:
        str: Cadena de caracteres con los años que ha cumplido el usuario.
    """
    if edad < 0 :
        raise ValueError ("La edad no puede ser negativa.")
     
    cont = 1
    years = str()
    for i in range(1, edad + 1):
        cont += i
        if i != edad:
            years += str(f"{i}, ")
        else:
            years += str(f"{edad} años. ")
    return years   
    
def main(): 
    edad = int(input("Introduzca su edad: "))
    try: 
        print("Ha cumplido " , edad_cumplida(edad))
    except ValueError as e:
        print("ERROR - ", e)

    
    
if __name__ == "__main__":
    main()