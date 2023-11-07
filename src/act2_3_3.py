"""
Ejercicio 2.3.3

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. 
Deberá solicitar el número hasta introducir uno correcto.
"""

def cuenta_atras(num):
    if num < 0 :
        raise ValueError ("El número no puede ser negativo. " )
    
    cuenta = str()
    for i in range(num, -1, -1):
        if i != 0:
            cuenta += f"{i}, "
        else:
            cuenta += f"{i}. "
    return cuenta
        
        
                   
def main():
    numeroCorrecto = False
    n = None
    while not numeroCorrecto  :
        try:  
            n= int(input("Introduzca un número: "))
            atras =cuenta_atras(n)
            numeroCorrecto = True
        except ValueError as e:
            print(e)
            
    print(atras)
    
if __name__ == "__main__":
    main()