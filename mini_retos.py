nums = [6, 3, 7, 2, 9, 4, 6, 6, 1, 3, 2, 8, 5]

# Suma de todos
suma = 0
for n in nums:
    suma += n
print("Suma de todos:", suma)

# Cuál es el máximo
maximo = nums[0]
for n in nums:
    if n > maximo:
        maximo = n
print("Máximo:", maximo)

# Contar ocurrencias de un número
num_buscar = int(input("¿Qué número quieres contar?: "))
ocurrencias = 0
for n in nums:
    if n == num_buscar:
        ocurrencias += 1
print(f"Ocurrencias de {num_buscar}:", ocurrencias)

# Calcula la media de una lista de enteros con for (sin sum)
total = 0
for n in nums:
    total += n
media = total / len(nums)
print("Media:", media)

# Crea una lista solo con los pares de nums
pares = []
for n in nums:
    if n % 2 == 0:
        pares.append(n)
print("Lista de pares:", pares)

# Dado nums, halla max(nums) - min(nums) usando for
maximo = nums[0]
minimo = nums[0]
for n in nums:
    if n > maximo:
        maximo = n
    if n < minimo:
        minimo = n
print("max(nums) - min(nums):", maximo - minimo)

# Pide un número y muestra el primer índice donde aparece (o -1 si no está)
num_indice = int(input("¿Qué número quieres buscar su índice?: "))
indice = -1
for i in range(len(nums)):
    if nums[i] == num_indice:
        indice = i
        break
print(f"Índice de {num_indice}:")