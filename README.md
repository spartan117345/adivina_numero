# adivina_numero

un juego para adivinar un numero y que el programa te de pistas y en cuantos intentos adivinaste
 
# analisis

## input

### variables
 
g = nivel de dificultad

 n = el numero que dijita el jugador

 z = numero generado por la maquina

 i = numero de intentos para acertar el numero

 r = respuesta de "ganaste o una pista"

 # processing

        z = random.randint(1, 100)
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
 
 # diseño

 ![diagrama de flujo](diagrama.png "diagrama de flujo")

 # construccion