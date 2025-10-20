# Calcula la media de una lista de enteros con for
nums = [6, 3, 7, 2, 9, 4, 6, 6, 1, 3, 2, 8, 5]
total = 0
for n in nums:
    total += n
media = total / len(nums)
print("Media:", media)