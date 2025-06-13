import Funciones as Fn

print("*"*3,"MENU PRINCIPAL","*"*3)
print("Que desea hacer")
Fn.menu()
while True:
    op=input()
    if op=="1":
        print("Ingrese nombre de pais:")
        print("La primera letra siempre on mayuscula")
        print("Ej: Hong Kong")
        pais=input()
        Fn.turistas_por_pais(pais)
        print("Desea algo mas")
        print("-"*10)
        Fn.menu()
    elif op=="2":
        print("Ingrese el mes a buscar")
        print("Debe ser un numero valido entre 1 y 12")
        print("Numeos de 1 cifra inrese olo 1 numero")
        print("Ej: Si:4;11 No:Cuatro;Once")
        while True:
            try:
                mes=int(input())
                if 1<=mes<=12:
                    Fn.turistas_por_mes(mes)
                    break
                else:
                    print("El mes debe ser entre 1 y 12")
            except ValueError:
                print("Porfavor ingrese un numero")
        print("Desea algo mas")
        print("-"*10)
        Fn.menu()
    elif op=="3":
        Fn.eliminar_turista()
        print("Desea algo mas")
        print("-"*10)
        Fn.menu()
    elif op=="4":
        print("Programa terminado...")
        break
    else:
        print("mal")
