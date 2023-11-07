"""
Ejercicio 2.3.1

Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

def cumplido(edad):
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
        print("Ha cumplido " , cumplido(edad))
    except ValueError as e:
        print("***ERROR*** - " + str(e))

    
    
if __name__ == "__main__":
    main()