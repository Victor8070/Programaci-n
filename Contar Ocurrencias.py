#Contar ocurrencias
nums = [6, 3, 7, 2, 9, 4, 6, 6, 1, 3, 2, 8, 5]

num_buscar = int(input("¿Qué número quieres contar?: "))
ocurrencias = 0
for n in nums:
    if n == num_buscar:
        ocurrencias += 1
print(f"Ocurrencias de {num_buscar}:", ocurrencias)