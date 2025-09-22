print('Dame el numero de chicos')
chicos=int(input())
print('Dame el numero de chicas de la clase')
chicas=int(input())
TOTAL = chicos+chicas
pchicas = (chicas/total)*100
pchicos = (chicos/total)*100

print('RESUMEN')
print(f'el numero total de alumnos es {total}')

print("El porcentaje de las chicas es de %.2f %% "%(pchicas))

print('el porcentaje de los chicos es de {pchicos:.2f}%')