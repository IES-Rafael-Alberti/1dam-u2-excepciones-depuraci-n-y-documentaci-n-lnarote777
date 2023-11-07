"""
Ejercicio 2.3.5

Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"
"""


def comprobarPassword(password):
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