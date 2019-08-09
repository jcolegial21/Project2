lista=[]
while True:
    seleccionar=input()
    if seleccionar=="1":
        estudiante=input()
        lista.append(estudiante)
    elif seleccionar=="2":
        print(lista)
        opcion=int(input())
        lista.pop=(opcion)
    elif seleccionar=="3":
        break
    print(lista)