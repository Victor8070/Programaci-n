#Maximo
nums = [6, 3, 7, 2, 9, 4, 6, 6, 1, 3, 2, 8, 5]

maximo = nums[0]
for n in nums:
    if n > maximo:
        maximo = n
print("Máximo:", maximo)