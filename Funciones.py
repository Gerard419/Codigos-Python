turistas= {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
        "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
        "012": ["Julian Martinez", "Argentina", "19-09-2023"],
        "014": ["Agustin Morales", "Argentina", "28-03-2024"],
        "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
        "006": ["Maria Lopez", "Mexico", "08-12-2023"],
        "007": ["Joao Silva", "Brasil", "20-06-2024"],
        "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
        "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
        "008": ["Ana Santos", "Brasil", "03-10-2023"],
        "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
        "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

def menu():
    print("1. Turistas por pais")
    print("2. Turitas por mes")
    print("3. Eliminar turista")
    print("4. Salir")

def turistas_por_pais(pais):
    hay=False
    can=0
    for codigo,datos in turistas.items():
        if pais in datos[1]:
            print(f"Nombre Turista:{datos[0]}")
            print("-"*10)
            can+=1
            hay=True
    if hay==True:
        print(f"Se ha enontrado {can} turistas")
    elif hay==False:
        print(f"No hay turistas en el pais {pais}")

def turistas_por_mes(mes):
    smes="0"
    if 1<=mes<=9:
        smes+=str(mes)
    else:
        smes+=str(mes)
    can=0
    for codigo,datos in turistas.items():
        if smes[0]==datos[2][3] and smes[1]==datos[2][4]:
            can+=1
    print(f"l numero de turistas equivalen al {round((100*can)/len(turistas),1)} %")

def eliminar_turista():
    tur=input("Ingrese el nombre del turista a eliminar:")
    ntur=tur[0].upper()
    for i in range(1,len(tur)):
        if tur[i-1]==" ":
            ntur+=tur[i].upper()
        else:
            ntur+=tur[i].lower()
    borrar=False
    for codigo,datos in turistas.items():
        if ntur in datos[0]:
            del turistas[codigo]
            borrar=True
            break
    if borrar==True:
        print("Turista eliminado con exito")
    elif borrar==False:
        print("Turista no encontrado. No se puedo eliminar")