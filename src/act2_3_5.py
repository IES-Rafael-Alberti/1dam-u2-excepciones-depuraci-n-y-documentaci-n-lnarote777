"""
Ejercicio 2.3.5

Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"
"""


def comprobarPassword(password):
    """Comprobación de la contraseña introducida.

    Args:
        password (str): contraseña introducida por el usuario.

    Raises:
        NameError: Salta el error cuando la contraseña del usuario no es correcta.

    Returns:
        str: devuelve un mensaje confirmando que la contraseña es correcta.
    """
    miPassWord = "contraseña" 
    
    if password.lower() == miPassWord.lower():
        return "Tu contraseña coincide con la mía."
    else:
        raise NameError ("ERROR - Incorrect Password!!")


def main():
    password = input("Introduzca contraseña: ")
    try:
        print(comprobarPassword(password))
    except NameError as e:
        print(e)

if __name__ == "__main__":
    main()