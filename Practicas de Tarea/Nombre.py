nombre = input("Ingrese el nombre de usuario: ")
ingreso= nombre.split()
y=""

if len(nombre.split()) > 1:
    print("El nombre ingresado es muy largo")
else:
    for x in ingreso[-1]:
        y= x+y
    print("Hola,", y.capitalize())
