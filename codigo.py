import random

print("===========================================================")
print("=======================adivina=un=numero===================")
print("===========================================================")
print("==========================dificultades=====================")
print("1. la dificultad es de 100 numeros ")
print("2. la dificultad es de 200 numeros ")
print("3. la dificultad es de 300 numeros ")
print("4. la dificultad es de 400 numeros ")
print("5. la dificultad es de 500 numeros ")
print("6. la dificultad es de 1000 numeros ")
print("7. la dificultad es de 10000 numeros ")
print("8. la dificultad es de 20000 numeros ")
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
            print("===========================================================")
            n = int(input("dijite otra ves el numero: "))

elif g == 2:

    p="normal"

    z = random.randint(1, 200)
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

elif g == 3:

    p="medio"

    z = random.randint(1, 300)
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

elif g == 4:

    p="dificil"

    z = random.randint(1, 400)
    
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

elif g == 5:

    p="extremo"

    z = random.randint(1, 500)
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

elif g == 6:

    p="imposible"

    z = random.randint(1, 1000)
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
            
elif g == 7:

    p="legendario"

    z = random.randint(1, 10000)
    
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

elif g == 8:

    p="extrema"

    z = random.randint(1, 20000)
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


else:
    p ="el numero  no es valido"


# output
print("===========================================================")
print("acertaste a "+ str(i)+" intentos, con la dificultad "+ str(p))
print("===========================================================")