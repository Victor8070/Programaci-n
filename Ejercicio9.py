secreto = 7

while True:
    intento = int(input("Adivina el número (entre 1 y 10): "))
    if intento == secreto:
        print("¡Correcto! Has adivinado el número.")
        break
    elif intento > secreto:
        print("Muy alto.")
    else:
        print("Muy bajo.")