while True:
    try:
        Salario=int(input("Digite Salario trabajador"))
        break
    except:
        print("Ingrese un num")
Patrono=0.30
Trabajador=0.10
Total=int((Salario*Patrono)+(Salario*Trabajador))
print("El total es",Total)