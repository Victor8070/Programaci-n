#lista con los pares de nums
nums = [6, 3, 7, 2, 9, 4, 6, 6, 1, 3, 2, 8, 5]

pares = []
for n in nums:
    if n % 2 == 0:
        pares.append(n)
print("Lista de pares:", pares)