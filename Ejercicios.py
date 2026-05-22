# Suma
Suma = 5+5;
print("La suma de los números es: " + str(Suma));


# Ecuacion
print("Ingrese el valor de a con 4 decimales: ");
a = float(input());
print("Ingrese el valor de b con 4 decimales: ");
b = float(input());
Resultado = ((a+b/5)**2)/2; 
print("El resultado es: " + str("{:.4f}".format(Resultado)));


# Valores de cada fruta
mango = 10
manzana = 5
aguacate = 15

# La ecuación del problema
# 2 aguacates + 4 manzanas + 1 mango y medio
resultado = (2 * aguacate) + (4 * manzana) + (1 * mango) +(mango / 2)

print(f"2 aguacates: {2*aguacate}")
print(f"3 manzanas:  {4*manzana}")
print(f"1 mango ½:   {1*mango + mango/2}")
print(f"\nResultado: {resultado}")
