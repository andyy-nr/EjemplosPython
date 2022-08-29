listaEst= []
resp = "si"
while (resp.upper() != "NO"): 
    tam = len(listaEst)
    print(f"Estudiantes registrados: {tam}")
    nombre = input("Escriba el nombre del estudiante: ")
    listaEst.append(nombre)
    resp = input("Desea agregar otro? si/no: ")
    resp.upper()

for est in listaEst:
    print(est)