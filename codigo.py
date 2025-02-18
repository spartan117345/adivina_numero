import random

print("===========================================================")
print("=======================adivina=un=numero===================")
print("===========================================================")
print("==========================dificultades=====================")
print("1. la dificultad es de 100 numeros ")
print("2. la dificultad es de 200 numeros ")
print("===========================================================")
g = int(input("dijite el numero de dificultad: "))
print("===========================================================")
n = int(input("dijite el numero para jugar: "))
print("===========================================================")

i = 1

if g == 1:

    p="facil"

    z = random.randint(1, 100)
    if n == z:
            r="ganaste el juego"
            print("===========================================================")
    else:
        while n < z or n> z:
            i = i + 1
            if n < z:
                r = "el numero es mas grande"
                print("===========================================================")
            else:
               r = "el numero es mas pequeño"
               print("===========================================================")
            print(r)
            n = int(input("dijite otra ves el numero: "))

elif g == 2:

    p="dificil"

    z = random.randint(1, 200)
    
    if n == z:
            r="ganaste el juego"
    else:
        while n < z or n > z:
            i = i + 1
            
            if n < z:
                print("===========================================================")
                r = "el numero es mas grande"
            else:
                r = "el numero es mas pequeño"
                print("===========================================================")
            print(r)
            n = int(input("dijite otra ves el numero: "))
            print("===========================================================")

else:
    p ="el numero  no es valido"


# output
print("===========================================================")
print("acertaste a "+ str(i)+" intentos, con la dificultad "+ str(p))
print("===========================================================")