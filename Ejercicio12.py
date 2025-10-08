entrada = input("Introduce números separados por espacios: ").strip()

if not entrada:
    print("Suma total: 0")
else:
    total = 0.0
    for token in entrada.split():
        try:
            total += float(token)
        except ValueError:
            print(f"'{token}' no es un número. Se omite.")
    
    
    if total.is_integer():
        total = int(total)
    print("Suma total:", total)