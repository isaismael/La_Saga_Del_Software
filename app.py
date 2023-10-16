import tkinter as tk
from tkinter import simpledialog, messagebox,Canvas, PhotoImage


# Crear una ventana principal
root = tk.Tk()
root.title("Juego de Preguntas")

# Establecer el tamaño de la ventana
root.geometry("854x480")

#cambiamos el icon
root.iconbitmap("icon.ico")

#bg color
root.configure(bg='white')

#Logo
img = tk.PhotoImage(file='lss.png')
lbl_img = tk.Label(root, image=img)

# Inicializar variables
puntaje = 0
respuestas_correctas = 0

def exitgame():
    root.destroy()

# Función para iniciar el juego
def iniciogame():
    nombre = simpledialog.askstring("Saludo", "Por favor, ingresa tu nombre:")
    if nombre:
        mensaje = f"Bienvenido/a, {nombre}! a la emocionante Saga del Software. \nPrepárate para poner a prueba tus conocimientos sobre el Desarrollo de Software.\nEn este desafío, te enfrentarás a una serie de preguntas en las que deberás elegir la opción \ncorrecta entre tres posibles respuestas. Cada respuesta correcta te otorgará un punto, \ny si logras acumular 7 puntos, podrás desbloquear el segundo nivel.\n¡Demuestra tus habilidades y conviértete en un verdadero maestro del software!"
        messagebox.showinfo("Saludo", mensaje)
        mostrar_menu()

# Función para mostrar el menú de niveles
def mostrar_menu():
    menu_label.config(text="Elige un nivel:")
    menu_label.pack(pady=5)
    lbl_img.pack(pady=8)
    nivel1_button.pack(pady=8)
    nivel2_button.pack(pady=8)
    salir_button.pack(pady=10)
    salir_button.pack(side=tk.BOTTOM)


# Función para comenzar el nivel 1
def nivel1():
    global pregunta_actual, puntaje, respuestas_correctas
    pregunta_actual = 0
    puntaje = 0
    respuestas_correctas = 0
    mostrar_pregunta()
    borrarniveles()
    

# Función para comenzar el nivel 2 (debes implementar este nivel)
def nivel2():
    global pregunta_actual2, puntaje, respuestas_correctas
    pregunta_actual2 = 0
    puntaje = 0
    respuestas_correctas = 0
    # Utiliza las preguntas del Nivel 2 (preguntas_nivel2)
    mostrar_pregunta2()
    borrarniveles()

def borrarniveles():
    nivel1_button.pack_forget()
    nivel2_button.pack_forget()


# Preguntas y respuestas (las mismas preguntas que tenías)
preguntas = [
    # Pregunta 1
    {
        "pregunta": "1) - ¿Qué es un Algoritmo?",
        "respuestas": [
            "Es un método para resolver un problema mediante una secuencia pasos precisos, definidos y finitos",
            "Es una herramienta que nos permite piratear sistemas informáticos",
            "Es una palabra reservada que se ingresa en el código"
        ],
        "correcta": 0
    },
    # Pregunta 2
    {
        "pregunta": "2) - ¿Qué es una Variable?",
        "respuestas": [
            "Es un espacio en memoria para almacenar un valor",
            "Es un código secreto utilizado para acceder a un programa",
            "Es un código para liberarnos de errores en el programa"
        ],
        "correcta": 0
    },
    # Pregunta 3
    {
        "pregunta": "3) - ¿Qué es un Pseudocódigo?",
        "respuestas": [
            "Es una función para crear 0 y 1",
            "Son instrucción de nuestro algoritmo pero en lenguaje natural como el español e el ingles",
            "Es un error en la sintaxis del código"
        ],
        "correcta": 1
    },
    # Pregunta 4
    {
        "pregunta": "4) -¿Qué es un Diagrama de Flujo?",
        "respuestas": [
            "Es un motor para hacer bases de datos",
            "Es un IDLE",
            "Es un representación gráfica de nuestro algoritmo"
        ],
        "correcta": 2
    },
    # Pregunta 5
    {
        "pregunta": "5) - ¿En un diagrama de flujo encontramos símbolos cómo?",
        "respuestas": [
            "Java, Python, C++, C#",
            "Inicio, Lectura, Procesos, Condicional",
            "interrogación, exclamación, puntos suspensivos"
        ],
        "correcta": 1
    },
    # Pregunta 6
    {
        "pregunta": "6) - ¿Cuál de estos son operadores relacionales?",
        "respuestas": [
            "+; -; *; /",
            "and; or; not",
            "==; !=; <; >"
        ],
        "correcta": 2
    },
    # Pregunta 7
    {
        "pregunta": "7) - ¿Cuál de estos son operadores aritméticos?",
        "respuestas": [
            "==; !=; <; >",
            "+; -; *; /",
            "and; or; not"
        ],
        "correcta": 1
    },
    # Pregunta 8
    {
        "pregunta": "8) - ¿Qué es una estructura de Selección o Condicional?",
        "respuestas": [
            "Es una toma de decisiones que nos permite indicarle a nuestro algoritmo que camino debe elegir ",
            "Es una variable que no puede modificar su valor",
            "Es un método que nos permite concatenar valores"
        ],
        "correcta": 0
    },
    # Pregunta 9
    {
        "pregunta": "9) - ¿Qué es una estructura repetitiva (Ciclos, Bucles) o While?",
        "respuestas": [
            "Es una estructura que nos permite designar valores enteros",
            "Es una estructura que nos permite designar valores reales",
            "Es una estructura que permite repetir una secuencia de instrucciones varias veces, de manera controlada "
        ],
        "correcta": 2
    },
    # Pregunta 10
    {
        "pregunta": "10) - ¿Qué tipos de Bucles o Ciclos existen?",
        "respuestas": [
            "and; or; not",
            "For; While",
            "print(); input()"
        ],
        "correcta": 1
    },
]

# Nuevas preguntas para el Nivel 2
preguntas_nivel2 = [
    #Pregunta 1
    {
        "pregunta": "1) - ¿Qué es un Dato?",
        "respuestas": [
            "Un dato es un pequeño programa informático diseñado para ejecutar\ntareas específicas en un sistema operativo.",
            "Un dato es una herramienta de diseño gráfico utilizada para crear \nelementos visuales y efectos especiales en el desarrollo de software",
            "Es una representación simbólica de un atributo o una variable cuantitativa"
        ],
        "correcta": 2
    },
    #Pregunta 2
    {
        "pregunta": "2) - ¿Qué es la Información?",
        "respuestas": [
            "Es un conjunto organizado de datos procesados que constituyen un mensaje",
            "La información es un tipo de archivo de imagen utilizado en el diseño \nde interfaces gráficas para mejorar la apariencia visual de las aplicaciones de software.",
            "La información es un conjunto de sonidos o melodías que se utilizan para \ncrear música en los programas de desarrollo de software"
        ],
        "correcta": 0
    },
    #Pregunta 3
    {
        "pregunta": "3) - ¿Qué es una base de datos?",
        "respuestas": [
            "Una base de datos es un tipo de hardware especializado utilizado en el \ndesarrollo de software para almacenar y procesar información.",
            "Una base de datos es un lenguaje de programación utilizado en el \ndesarrollo de software para crear interfaces de usuario interactivas.",
            "Es una colección de datos interrelacionados, almacenados en conjunto \nsin redundancias perjudiciales o innecesarias"
        ],
        "correcta": 2
    },
    #Pregunta 4
    {
        "pregunta": "4) - ¿Qué es BBMS o SGBD?",
        "respuestas": [
            "Sistema de Gestión De Base de Datos",
            "Base de Búsqueda y Manipulación de Segmentos",
            "Sistema de Gestión de Búsquedas y Descargas"
        ],
        "correcta": 0
    },
    #Pregunta 5
    {
        "pregunta": "5) - ¿Qué es SQL?",
        "respuestas": [
            "Es una tecnología utilizada en el desarrollo de software para controlar \ny monitorear el suministro de energía eléctrica en los centros de datos.",
            "Es un protocolo de comunicación utilizado en el desarrollo de software \npara transferir datos entre diferentes dispositivos de red.",
            "Es un lenguaje de programación utilizado para administrar y manipular bases de datos relacionales"
        ],
        "correcta": 2
    },
    #Pregunta 6
    {
        "pregunta": "6) - ¿Cuáles son los niveles de independencia de datos, según Karth?",
        "respuestas": [
            "Independencia Física y Lógica",
            "Independencia Mayor y Menor",
            "Independencia Conceptual y Lógica "
        ],
        "correcta": 0
    },
    #Pregunta 7
    {
        "pregunta": "7) - ¿Qué es POO?",
        "respuestas": [
            "Es un enfoque de desarrollo de software que se centra en la ejecución \nde operaciones matemáticas complejas para resolver problemas en aplicaciones científicas",
            "Es un paradigma de la programación que la idea principal es combinar \nen una única unidad o modulo, tanto los datos como las funciones que operan sobre esos datos",
            "Es un paradigma de programación que se basa en la creación y manipulación \nde objetos físicos en un entorno virtual, como juegos de realidad virtual"
        ],
        "correcta": 1
    },
    #Pregunta 8
    {
        "pregunta": "8) - ¿Qué es Modelo Entidad-Relación?",
        "respuestas": [
            "Es un método utilizado en el desarrollo de software para diseñar interfaces \nde usuario y definir la interacción entre diferentes elementos visuales",
            "Es una técnica utilizada en modelado de datos para representar la estructura de una base de datos",
            "Es una herramienta utilizada en el desarrollo de software para simular \ny predecir el comportamiento de sistemas de inteligencia artificial en entornos virtuales"
        ],
        "correcta": 1
    },
    #Pregunta 9
    {
        "pregunta": "9) - ¿Qué es una Entidad?",
        "respuestas": [
            "Una entidad se refiere a un programa informático capaz de tomar \ndecisiones y ejecutar tareas de manera autónoma.",
            "Una entidad es una representación gráfica utilizada para visualizar \ndatos complejos en forma de diagramas interactivos",
            "Una entidad pueden ser objetos con existencias físicas o con existencias conceptuales"
        ],
        "correcta": 2
    },
    #Pregunta 10
    {
        "pregunta": "10) - ¿Qué tipos de Entidades existen?",
        "respuestas": [
            "Entidades Abstractas e Reales",
            "Entidades Primarias y Secundarias",
            "Entidades Fuertes y Débiles"
        ],
        "correcta": 2
    },
]


pregunta_actual = 0
pregunta_actual2 = 0


# Función para verificar la respuesta
# Función para verificar la respuesta
def verificar_respuesta(respuesta):
    global pregunta_actual, puntaje, respuestas_correctas
    pregunta = preguntas[pregunta_actual]
    if respuesta == pregunta["correcta"]:
        puntaje += 1
        respuestas_correctas += 1
        messagebox.showinfo("Respuesta Correcta", "¡Respuesta correcta!")
    else:
        messagebox.showinfo("Respuesta Incorrecta", "Respuesta incorrecta. La respuesta correcta es:\n" + pregunta["respuestas"][pregunta["correcta"]])

    pregunta_actual += 1

    if pregunta_actual < len(preguntas):
        mostrar_pregunta()
    else:
        if respuestas_correctas >= 7:
            menu_label.config(text=f"¡Has completado todas las preguntas!\nPuntaje total: {puntaje}\n¡Desbloqueaste el el siguiente nivel")
            limpiar_pantalla()
            nivel2_button.config(state=tk.NORMAL)
            nivel2_button.pack()
        else:
            menu_label.config(text=f"¡Has completado todas las preguntas!\nPuntaje total: {puntaje}\nPero no Desbloqueaste el el siguiente nivel\nVuelve a intentarlo")
            limpiar_pantalla()
            nivel1_button.pack()
            nivel2_button.config(state=tk.DISABLED)


#verificar 2
def verificar_respuesta2(respuesta):
    global pregunta_actual2, puntaje, respuestas_correctas
    pregunta = preguntas_nivel2[pregunta_actual2]
    if respuesta == pregunta["correcta"]:
        puntaje += 1
        respuestas_correctas += 1
        messagebox.showinfo("Respuesta Correcta", "¡Respuesta correcta!")
    else:
        messagebox.showinfo("Respuesta Incorrecta", "Respuesta incorrecta. La respuesta correcta es:\n" + pregunta["respuestas"][pregunta["correcta"]])

    pregunta_actual2 += 1

    if pregunta_actual2 < len(preguntas_nivel2):
        mostrar_pregunta2()
    else:
        if respuestas_correctas >= 7:
            menu_label.config(text=f"¡Has completado todas las preguntas!\nPuntaje total: {puntaje}\n¡Desbloqueaste el siguiente nivel")
            limpiar_pantalla()
            nivel1_button.config(state=tk.NORMAL)
            nivel1_button.pack()
        else:
            menu_label.config(text=f"¡Has completado todas las preguntas!\nPuntaje total: {puntaje}\nPero no Desbloqueaste el el siguiente nivel\nVuelve a intentarlo")
            limpiar_pantalla()
            nivel2_button.pack()
            nivel1_button.config(state=tk.DISABLED)

# Función para mostrar la pregunta actual
def mostrar_pregunta():
    global pregunta_actual
    if pregunta_actual < len(preguntas):
        pregunta = preguntas[pregunta_actual]["pregunta"]
        respuestas = preguntas[pregunta_actual]["respuestas"]
        limpiar_pantalla()
        menu_label.config(text=pregunta)

        puntajelbl = tk.Label(text=f'Puntaje: {puntaje}', font=("consolas", 15))
        puntajelbl.pack(pady=5)

        # Crear botones de respuesta
        respuesta_buttons = []
        for i, respuesta in enumerate(respuestas):
            respuesta_buttons.append(tk.Button(root, font=("consolas", 10), text=respuesta, padx=10, pady=5, command=lambda i=i: verificar_respuesta(i)))
            respuesta_buttons[-1].pack()
    else:
        menu_label.config(text="¡Has completado todas las preguntas!")

#mostrar preguntas 2
def mostrar_pregunta2():
    global pregunta_actual2
    if pregunta_actual2 < len(preguntas_nivel2):
        pregunta = preguntas_nivel2[pregunta_actual2]["pregunta"]
        respuestas = preguntas_nivel2[pregunta_actual2]["respuestas"]
        limpiar_pantalla()
        menu_label.config(text=pregunta)

        puntajelbl = tk.Label(text=f'Puntaje: {puntaje}', font=("consolas", 15))
        puntajelbl.pack()

        # Crear botones de respuesta
        respuesta_buttons = []
        for i, respuesta in enumerate(respuestas):
            respuesta_buttons.append(tk.Button(root, font=("consolas", 10), text=respuesta, padx=10, pady=5, command=lambda i=i: verificar_respuesta2(i)))
            respuesta_buttons[-1].pack()
    else:
        menu_label.config(text="¡Has completado todas las preguntas!")        


def limpiar_pantalla():
    # Eliminar los botones de respuesta de la pregunta anterior
    for widget in root.winfo_children():
        if widget != menu_label and widget != nivel1_button and widget != nivel2_button and widget != salir_button:
            widget.destroy()


# Crear widgets
menu_label = tk.Label(root, text="", padx=10, pady=10, font=("consolas", 15))
menu_label.pack()

nivel1_button = tk.Button(root, text="Nivel 1 - Programacion", padx=10, pady=5, command=nivel1, font=("consolas", 10))
nivel2_button = tk.Button(root, text="Nivel 2 - Base de Datos", padx=10, pady=5,  command=nivel2, font=("consolas", 10))
salir_button = tk.Button(root, text="Salir del juego", padx=10, pady=5, command=exitgame, font=("consolas", 10))

# Comenzar el juego mostrando el menú
iniciogame()

root.mainloop()
