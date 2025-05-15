#ingresar 3 números
lista = []

print("--->Escriba 3 números<---")

for i in range(3):
    f = int(input(f"Ingrese #{i+1}: "))
    lista.append(f)

imp = [i for i in lista if i % 2!=0]
par = [i for i in lista if i % 2==0]

suma = sum(lista)

print("Se ingresaron ",len(par),"números.")
print("Se ingresaron ", len(imp), "impares." )  

if suma < 100:
    print("La suma es menor a 100!.")
elif suma > 100:
    print("La suma es mayor a 100!.")

if suma % 2==0:
    print("La suma es par")
elif suma % 2!=0:
    print("La suma es impar.")