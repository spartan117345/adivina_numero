import random

print("===========================================================")
print("=======================adivina=un=numero===================")
print("===========================================================")

n = int(input("dijite el numero para jugar: "))

i = 1

z = random.randint(1, 100)  # Genera un número entre 1 y 100

if n == z:
    r="ganaste el juego"
else:
    while n < z or n> z:
        i = i + 1
        if n < z:
            r = "el numero es mas grande"
        else:
            r = "el numero es mas pequeño"
        print(r)
        n = int(input("dijite otra ves el numero: "))
 
# output

print("acertaste a: "+ str(i)+" intentos,")