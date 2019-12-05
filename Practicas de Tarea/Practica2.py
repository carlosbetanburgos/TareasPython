##Ver elementos iguales en ambas listas##

a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,89]
iguales = 0

def programa(a, b):
    for x in a:
        for z in b:
            if x == z:
                iguales = x
                print(iguales)
                iguales = 0

programa(a, b)
