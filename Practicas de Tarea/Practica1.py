##Programa que saque los dividendos de cada uno##

numero = int(input("Ingrese el número entero que desea sacar: " ))

if numero <= 0:
    print("Ingrese un número entero correcto")
else:
    print(f"Los divisores para el número {numero} son:")
    for i in range(1, numero+1):
        if numero % i == 0:
            print(i)
