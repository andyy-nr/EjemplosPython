# Sumar los elementos de un arreglo

arreglo = []
cant = int(input("Dime cuantos numeros: "))
cont  = 0 
while (cont < cant):
    num = int(input("Dime un numero: "))
    cont += 1
    arreglo.append(num)

suma = 0
for num in arreglo: 
    suma += num
print(f"El resultado de la suma de todos los elementos es: {suma}")
