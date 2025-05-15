#tesoro de la isla aleatoria.
import random

while True:
    try:
        limite_inferior = int(input("Ingresa el límite inferior del rango: "))
        limite_superior = int(input("Ingresa el límite superior del rango: "))
        
        # Verificamos que el inferior sea menor que el superior
        if limite_inferior >= limite_superior:
            print("El límite inferior debe ser menor que el límite superior. Inténtalo de nuevo.")
        else:
            break  # Todo está bien, salimos del bucle
    except ValueError:
        print("Debes ingresar números enteros. Inténtalo de nuevo.")

while True:
    try:
        intento = int(input("Ingrese limite de intentos: "))
        if intento <=0:
            print("La cantidad de intentos debe ser mayor que 0!")
        else:
            break
    except ValueError:
        print("Valor no valido intentelo denuuevo!") 

area = random.randint(limite_inferior,limite_superior)

i = 0
for i in range(intento):
    while True:
        try:
            eleccion = int(input(f"Elige una zona - Intento #{i+1}: "))
            if eleccion < limite_inferior or eleccion > limite_superior:
                print("Fuera de la zona")
            else:
                break
        except ValueError:
            print("Ingresa un valor valido!.")
            
    distancia = abs(eleccion - area)
    
    if eleccion == area:
        print("Felicidades lo encontraste!!.")
        break
    else:
        print(f"Cerca: {distancia} de distancia.")