
# PROBLEMA 2: PROMOCIONES DE UN RESTAURANTE
# Fundamentos de Programacion - UNAD

# 1. Defino los parametros de la promocion

categoria_objetivo = "Comidas rápidas"
umbral = 20000
descuento = 0.15

# 2. Creo la matriz con los productos del restaurante

menu = [
    ["Hamburguesa especial", "Comidas rápidas", 30000],
    ["Perro caliente", "Comidas rápidas", 18000],
    ["Pizza familiar", "Comidas rápidas", 35000],
    ["Ensalada César", "Ensaladas", 22000],
    ["Jugo natural", "Bebidas", 8000],
    ["Sándwich especial", "Comidas rápidas", 25000]
]

# 3. Creo la funcion para calcular el precio final

def calcular_precio_final(categoria, precio_base):

    if categoria == categoria_objetivo and precio_base > umbral:

        valor_descuento = precio_base * descuento
        precio_final = precio_base - valor_descuento

    else:
        precio_final = precio_base
    return precio_final


# 4. Recorro la matriz y presento los resultados

print("======================================")
print("   REPORTE DE PROMOCIONES DEL RESTAURANTE")
print("======================================")

for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(categoria, precio_base)

    print("\nProducto:", nombre)
    print("Categoria:", categoria)
    print("Precio base: $", format(precio_base, ","))
    print("Precio final: $", format(precio_final, ","))
    print("--------------------------------------")

print("\nProceso terminado correctamente.")

