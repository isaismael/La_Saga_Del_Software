puntaje = 0
respuestas_correctas = 0

print("▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░")
print("▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░")
print("▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░")
print("▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░")
print('░░░░▄▄███▄▄░░░░░█████░')
nombre = input("Ingrese su nombre: ")
print(" - - -")
print("// Bienvenido", nombre, "a la emocionante 'Saga del Software'. Prepárate para poner a prueba tus conocimientos sobre el Desarrollo de Software. En este desafío,\nte enfrentarás a una serie de preguntas en las que deberás elegir la opción correcta entre tres posibles respuestas. Cada respuesta correcta te otorgará un punto, y si logras acumular 7 puntos, podrás desbloquear el segundo nivel. ¡Demuestra tus habilidades y conviértete en un verdadero maestro del software! //")
print(" - - -")
input("Si estás listo presiona Enter para comenzar y mucha suerte!")


def pregunta():
    ###### 1 ########
    print(" - - -")
    print("Nivel 1 – Programación")
    print("¿Que es un Algoritmo?")
    print("1 - Es un método para resolver un problema mediante una secuencia pasos precisos, definidos y finitos")
    print("2 - Es una herramienta que nos permite piratear sistemas informáticos")
    print("3 - Es una palabra reservada que se ingresa en el código")
    print(" - - -")
    ###### 1 ########
    while True:
        try:
            respuesta = int(input("Ingrese una opcion: "))
            if respuesta in range(1, 3):
                break
            else:
                print("Opción inválida. Por favor, elija una opción entre 1 y 3.")
        except ValueError:
            print("Ingrese un número válido.")
    # Pregunta 1
    if respuesta == 1:
        print(" - - -")
        print("Correcto! Sumaste un Punto")
        puntaje = + 1
        respuestas_correctas = + 1
        print("Tu puntaje es de:", puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")
    else:
        print(" - - -")
        print("Incorrecto! ( ˘︹˘ )")
        puntaje = + 0
        respuestas_correctas = + 0
        print("Tu puntaje es de:", puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")

    ###### 2 ########
    print(" - - -")
    print("¿Qué es una Variable?")
    print("1 - Es un código secreto utilizado para acceder a un programa")
    print("2 - Es un espacio en memoria para almacenar un valor")
    print("3 - Es un código para liberarnos de errores en el programa")
    print(" - - -")
    ###### 2 ########
    while True:
        try:
            respuesta = int(input("Ingrese una opcion: "))
            if respuesta in range(1, 3):
                break
            else:
                print("Opción inválida. Por favor, elija una opción entre 1 y 3.")
        except ValueError:
            print("Ingrese un número válido.")
    # Pregunta 2
    if respuesta == 2:
        print(" - - -")
        print("Correcto! Sumaste un Punto")
        puntaje += 1
        respuestas_correctas += 1
        print("Tu puntaje es de:", puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")
    else:
        print(" - - -")
        print("Incorrecto! ( ˘︹˘ )")
        puntaje += 0
        respuestas_correctas += 0
        print("Tu puntaje es de:", puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")

    ###### 3 ########
    print(" - - -")
    print("¿Qué es un Pseudocódigo?")
    print("1 - Son instrucción de nuestro algoritmo pero en lenguaje natural como el español e el ingles")
    print("2 - Es una función para crear 0 y 1")
    print("3 - Es un error en la sintaxis del código")
    print(" - - -")
    ###### 3 ########
    while True:
        try:
            respuesta = int(input("Ingrese una opcion: "))
            if respuesta in range(1, 3):
                break
            else:
                print("Opción inválida. Por favor, elija una opción entre 1 y 3.")
        except ValueError:
            print("Ingrese un número válido.")
    # Pregunta 3
    if respuesta == 1:
        print(" - - -")
        print("Correcto! Sumaste un Punto")
        puntaje += 1
        respuestas_correctas += 1
        print("Tu puntaje es de:", puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")
    else:
        print(" - - -")
        print("Incorrecto! ( ˘︹˘ )")
        puntaje += 0
        respuestas_correctas += 0
        print("Tu puntaje es de:", puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")

    ###### 4 ########
    print(" - - -")
    print("¿Qué es un Diagrama de Flujo?")
    print("1 - Es un motor para hacer bases de datos")
    print("2 - Es un IDLE")
    print("3 - Es un representación gráfica de nuestro algoritmo")
    print(" - - -")
    ###### 4 ########
    while True:
        try:
            respuesta = int(input("Ingrese una opcion: "))
            if respuesta in range(1, 3):
                break
            else:
                print("Opción inválida. Por favor, elija una opción entre 1 y 3.")
        except ValueError:
            print("Ingrese un número válido.")
    # Pregunta 4
    if respuesta == 3:
        print(" - - -")
        print("Correcto! Sumaste un Punto")
        puntaje += 1
        respuestas_correctas += 1
        print("Tu puntaje es de:", puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")
    else:
        print(" - - -")
        print("Incorrecto! ( ˘︹˘ )")
        puntaje += 0
        respuestas_correctas += 0
        print("Tu puntaje es de:", puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")

    ###### 5 ########
    print(" - - -")
    print("¿En un diagrama de flujo encontramos símbolos cómo?")
    print("1 - Java, Python, C++, C#")
    print("2 - Inicio, Lectura, Procesos, Condicional")
    print("3 - interrogación, exclamación, puntos suspensivos")
    print(" - - -")
    ###### 5 ########
    while True:
        try:
            respuesta = int(input("Ingrese una opcion: "))
            if respuesta in range(1, 3):
                break
            else:
                print("Opción inválida. Por favor, elija una opción entre 1 y 3.")
        except ValueError:
            print("Ingrese un número válido.")
    # Pregunta 5
    if respuesta == 2:
        print(" - - -")
        print("Correcto! Sumaste un Punto")
        puntaje += 1
        respuestas_correctas += 1
        print("Tu puntaje es de:",puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")
    else:
        print(" - - -")
        print("Incorrecto! ( ˘︹˘ )")
        puntaje += 0
        respuestas_correctas += 0
        print("Tu puntaje es de:",puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")

    ###### 6 ########
    print(" - - -")
    print("¿Cuál de estos son operadores relacionales?")
    print("1 - +; -; *; /")
    print("2 - and; or; not")
    print("3 - ==; !=; <; >")
    print(" - - -")
    ###### 6 ########
    while True:
        try:
            respuesta = int(input("Ingrese una opcion: "))
            if respuesta in range(1, 3):
                break
            else:
                print("Opción inválida. Por favor, elija una opción entre 1 y 3.")
        except ValueError:
            print("Ingrese un número válido.")
    # Pregunta 6
    if respuesta == 3:
        print(" - - -")
        print("Correcto! Sumaste un Punto")
        puntaje += 1
        respuestas_correctas += 1
        print("Tu puntaje es de:",puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")
    else:
        print(" - - -")
        print("Incorrecto! ( ˘︹˘ )")
        puntaje += 0
        respuestas_correctas += 0
        print("Tu puntaje es de:",puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")

    ###### 7 ########
    print(" - - -")
    print("¿Cuál de estos son operadores aritméticos?")
    print("1 - ==; !=; <; >")
    print("2 - +; -; *; /")
    print("3 - and; or; not")
    print(" - - -")
    ###### 7 ########
    while True:
        try:
            respuesta = int(input("Ingrese una opcion: "))
            if respuesta in range(1, 3):
                break
            else:
                print("Opción inválida. Por favor, elija una opción entre 1 y 3.")
        except ValueError:
            print("Ingrese un número válido.")
    # Pregunta 7
    if respuesta == 2:
        print(" - - -")
        print("Correcto! Sumaste un Punto")
        puntaje += 1
        respuestas_correctas += 1
        print("Tu puntaje es de:",puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")
    else:
        print(" - - -")
        print("Incorrecto! ( ˘︹˘ )")
        puntaje += 0
        respuestas_correctas += 0
        print("Tu puntaje es de:",puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")

    ###### 8 ########
    print(" - - -")
    print("¿Qué es una estructura de Selección o Condicional?")
    print("1 - Es una toma de decisiones que nos permite indicarle a nuestro algoritmo que camino debe elegir ")
    print("2 - Es una variable que no puede modificar su valor")
    print("3 - Es un método que nos permite concatenar valores")
    print(" - - -")
    ###### 8 ########
    while True:
        try:
            respuesta = int(input("Ingrese una opcion: "))
            if respuesta in range(1, 3):
                break
            else:
                print("Opción inválida. Por favor, elija una opción entre 1 y 3.")
        except ValueError:
            print("Ingrese un número válido.")
    # Pregunta 8
    if respuesta == 1:
        print(" - - -")
        print("Correcto! Sumaste un Punto")
        puntaje += 1
        respuestas_correctas += 1
        print("Tu puntaje es de:",puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")
    else:
        print(" - - -")
        print("Incorrecto! ( ˘︹˘ )")
        puntaje += 0
        respuestas_correctas += 0
        print("Tu puntaje es de:",puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")

    ###### 9 ########
    print(" - - -")
    print("¿Qué es una estructura repetitiva (Ciclos, Bucles) o While?")
    print("1 - Es una estructura que nos permite designar valores enteros")
    print("2 - Es una estructura que nos permite designar valores reales")
    print("3 - Es una estructura que permite repetir una secuencia de instrucciones varias veces, de manera controlada ")
    print(" - - -")
    ###### 9 ########
    while True:
        try:
            respuesta = int(input("Ingrese una opcion: "))
            if respuesta in range(1, 3):
                break
            else:
                print("Opción inválida. Por favor, elija una opción entre 1 y 3.")
        except ValueError:
            print("Ingrese un número válido.")
    # Pregunta 9
    if respuesta == 3:
        print(" - - -")
        print("Correcto! Sumaste un Punto")
        puntaje += 1
        respuestas_correctas += 1
        print("Tu puntaje es de:",puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")
    else:
        print(" - - -")
        print("Incorrecto! ( ˘︹˘ )")
        puntaje += 0
        respuestas_correctas += 0
        print("Tu puntaje es de:",puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")

    ###### 10 ########
    print(" - - -")
    print("¿Qué tipos de Bucles o Ciclos existen?")
    print("1 - and; or; not")
    print("2 - For; While")
    print("3 - print(); input()")
    print(" - - -")
    ###### 10 ########
    while True:
        try:
            respuesta = int(input("Ingrese una opcion: "))
            if respuesta in range(1, 3):
                break
            else:
                print("Opción inválida. Por favor, elija una opción entre 1 y 3.")
        except ValueError:
            print("Ingrese un número válido.")
    # Pregunta 10
    if respuesta == 2:
        print(" - - -")
        print("Correcto! Sumaste un Punto")
        puntaje += 1
        respuestas_correctas += 1
        print("Tu puntaje es de:",puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")
    else:
        print(" - - -")
        print("Incorrecto! ( ˘︹˘ )")
        puntaje += 0
        respuestas_correctas += 0
        print("Tu puntaje es de:",puntaje)
        print(" - - -")
        input("Presiona Enter para avanzar a la siguiente pregunta!")

    if respuestas_correctas >= 7:
        print("- - - - - - - - - - - - - - - - - - - - - - - ")
        print("Felicitades pasaste al Nivel 2 – Base de Datos")
        print("- - - - - - - - - - - - - - - - - - - - - - - ")


pregunta()
