import random
import time

def juego_adivina():
    print("\n-- Adivina (1–20) — 5 intentos --")
    secreto = random.randint(1, 20)
    inicio = time.time()
    max_intentos = 5
    intentos = 0

    while intentos < max_intentos:
        entrada = input(f"Intento {intentos+1}/{max_intentos} - Tu número: ").strip()
        try:
            intento = int(entrada)
        except ValueError:
            print("Introduce un número entero.")
            continue

        if not 1 <= intento <= 20:
            print("Número fuera de rango (1-20).")
            continue

        intentos += 1

        if intento == secreto:
            duracion = time.time() - inicio
            print("¡Correcto! Has adivinado el número.")
            print(f"Intentos: {intentos}  Duración: {duracion:.2f} s")
            return
        elif intento < secreto:
            print("↑ Muy bajo.", f"Quedan {max_intentos - intentos} intentos.")
        else:
            print("↓ Muy alto.", f"Quedan {max_intentos - intentos} intentos.")
        time.sleep(0.25)

    duracion = time.time() - inicio
    print("Se han agotado los intentos.")
    print(f"El número era: {secreto}. Duración: {duracion:.2f} s")

def juego_ppt():
    print("\n-- Piedra, Papel o Tijera --")
    opciones = ("piedra", "papel", "tijera")
    maquina = random.choice(opciones)
    while True:
        jugador = input("Elige piedra/papel/tijera: ").strip().lower()
        if jugador in opciones:
            break
        print("Opción no válida. Intenta de nuevo.")
    print(f"Tú: {jugador}  —  Bot: {maquina}")
    if jugador == maquina:
        print("Empate.")
    else:
        gana = (
            (jugador == "piedra" and maquina == "tijera") or
            (jugador == "tijera" and maquina == "papel") or
            (jugador == "papel" and maquina == "piedra")
        )
        print("Has ganado." if gana else "Has perdido.")
    time.sleep(0.5)

def juego_calculo_mental():
    print("\n-- Cálculo mental (5 operaciones, tiempo total límite 12s) --")
    operaciones = ['+', '-', '*']
    preguntas = 5
    limite = 12.0
    inicio = time.time()
    aciertos = 0

    for i in range(1, preguntas + 1):
        if time.time() - inicio > limite:
            print("Se ha agotado el tiempo total.")
            break
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        op = random.choice(operaciones)
        if op == '+':
            respuesta_correcta = a + b
        elif op == '-':
            respuesta_correcta = a - b
        else:
            respuesta_correcta = a * b

        entrada = input(f"{i}) {a} {op} {b} = ").strip()
        # si se pasa tiempo mientras escribe, comprobar igualmente
        if time.time() - inicio > limite:
            print("Se ha agotado el tiempo total.")
            break
        try:
            respuesta = int(entrada)
        except ValueError:
            print("Respuesta no válida, se cuenta como error.")
            continue

        if respuesta == respuesta_correcta:
            aciertos += 1
            print("Correcto.")
        else:
            print("Incorrecto.")
    duracion = time.time() - inicio
    print(f"Puntuación: {aciertos}/{preguntas}. Duración: {duracion:.2f} s")

def juego_eco_loco():
    print("\n-- Eco loco --")
    print("Escribe líneas. Vacío o 'salir' para volver al menú.")
    while True:
        linea = input("Texto: ")
        if linea.strip() == "" or linea.strip().lower() == "salir":
            break
        invertida = linea[::-1]
        num_chars = len(linea)
        num_vocales = sum(1 for c in linea.lower() if c in "aeiouáéíóúü")
        print(f"Invertida: {invertida}")
        print(f"Caracteres: {num_chars}  Vocales: {num_vocales}")

def pedir_opcion():
    menu = (
        "\n--- ARCADE ---\n"
        "1) Adivina el número (1-20, 5 intentos)\n"
        "2) Piedra, Papel o Tijera\n"
        "3) Cálculo mental\n"
        "4) Eco loco\n"
        "5) Salir\n"
    )
    while True:
        print(menu)
        opcion = input("Elige una opción (1-5): ").strip()
        if opcion in {"1","2","3","4","5"}:
            return int(opcion)
        print("Opción no válida. Inténtalo de nuevo.")

def main():
    while True:
        opcion = pedir_opcion()
        if opcion == 1:
            juego_adivina()
        elif opcion == 2:
            juego_ppt()
        elif opcion == 3:
            juego_calculo_mental()
        elif opcion == 4:
            juego_eco_loco()
        else:
            print("Adiós.")
            break
        time.sleep(0.3)

if __name__ == "__main__":
    main()

import random
import time

def juego_adivina():
    print("\n-- Adivina (1–20) — 5 intentos --")
    secreto = random.randint(1, 20)
    inicio = time.time()
    max_intentos = 5
    intentos = 0

    while intentos < max_intentos:
        entrada = input(f"Intento {intentos+1}/{max_intentos} - Tu número: ").strip()
        try:
            intento = int(entrada)
        except ValueError:
            print("Introduce un número entero.")
            continue

        if not 1 <= intento <= 20:
            print("Número fuera de rango (1-20).")
            continue

        intentos += 1

        if intento == secreto:
            duracion = time.time() - inicio
            print("¡Correcto! Has adivinado el número.")
            print(f"Intentos: {intentos}  Duración: {duracion:.2f} s")
            return
        elif intento < secreto:
            print("↑ Muy bajo.", f"Quedan {max_intentos - intentos} intentos.")
        else:
            print("↓ Muy alto.", f"Quedan {max_intentos - intentos} intentos.")
        time.sleep(0.25)

    duracion = time.time() - inicio
    print("Se han agotado los intentos.")
    print(f"El número era: {secreto}. Duración: {duracion:.2f} s")

def juego_ppt():
    print("\n-- Piedra, Papel o Tijera --")
    opciones = ("piedra", "papel", "tijera")
    maquina = random.choice(opciones)
    while True:
        jugador = input("Elige piedra/papel/tijera: ").strip().lower()
        if jugador in opciones:
            break
        print("Opción no válida. Intenta de nuevo.")
    print(f"Tú: {jugador}  —  Bot: {maquina}")
    if jugador == maquina:
        print("Empate.")
    else:
        gana = (
            (jugador == "piedra" and maquina == "tijera") or
            (jugador == "tijera" and maquina == "papel") or
            (jugador == "papel" and maquina == "piedra")
        )
        print("Has ganado." if gana else "Has perdido.")
    time.sleep(0.5)

def juego_calculo_mental():
    print("\n-- Cálculo mental (5 operaciones, tiempo total límite 12s) --")
    operaciones = ['+', '-', '*']
    preguntas = 5
    limite = 12.0
    inicio = time.time()
    aciertos = 0

    for i in range(1, preguntas + 1):
        if time.time() - inicio > limite:
            print("Se ha agotado el tiempo total.")
            break
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        op = random.choice(operaciones)
        if op == '+':
            respuesta_correcta = a + b
        elif op == '-':
            respuesta_correcta = a - b
        else:
            respuesta_correcta = a * b

        entrada = input(f"{i}) {a} {op} {b} = ").strip()
        
        if time.time() - inicio > limite:
            print("Se ha agotado el tiempo total.")
            break
        try:
            respuesta = int(entrada)
        except ValueError:
            print("Respuesta no válida, se cuenta como error.")
            continue

        if respuesta == respuesta_correcta:
            aciertos += 1
            print("Correcto.")
        else:
            print("Incorrecto.")
    duracion = time.time() - inicio
    print(f"Puntuación: {aciertos}/{preguntas}. Duración: {duracion:.2f} s")

def juego_eco_loco():
    print("\n-- Eco loco --")
    print("Escribe líneas. Vacío o 'salir' para volver al menú.")
    while True:
        linea = input("Texto: ")
        if linea.strip() == "" or linea.strip().lower() == "salir":
            break
        invertida = linea[::-1]
        num_chars = len(linea)
        num_vocales = sum(1 for c in linea.lower() if c in "aeiouáéíóúü")
        print(f"Invertida: {invertida}")
        print(f"Caracteres: {num_chars}  Vocales: {num_vocales}")

def pedir_opcion():
    menu = (
        "\n--- ARCADE ---\n"
        "1) Adivina el número (1-20, 5 intentos)\n"
        "2) Piedra, Papel o Tijera\n"
        "3) Cálculo mental\n"
        "4) Eco loco\n"
        "5) Salir\n"
    )
    while True:
        print(menu)
        opcion = input("Elige una opción (1-5): ").strip()
        if opcion in {"1","2","3","4","5"}:
            return int(opcion)
        print("Opción no válida. Inténtalo de nuevo.")

def main():
    while True:
        opcion = pedir_opcion()
        if opcion == 1:
            juego_adivina()
        elif opcion == 2:
            juego_ppt()
        elif opcion == 3:
            juego_calculo_mental()
        elif opcion == 4:
            juego_eco_loco()
        else:
            print("Adiós.")
            break
        time.sleep(0.3)

if __name__ == "__main__":
    main()