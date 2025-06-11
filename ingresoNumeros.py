def validar(par,impar,numero,numeros,nums):
    try:
        for i in range(len(numeros)+1):
            try:
                if numeros[i] in nums:
                    numero+=numeros[i]
                elif numeros[i]==" ":
                    if int(numero)%2==0:
                        par.append(numero)
                        numero=""
                    else:
                        impar.append(numero)
                        numero=""
            except IndexError:
                if int(numero)%2==0:
                    par.append(numero)
                else:
                    impar.append(numero)
                break
        print(f"Numeros pares:{par}")
        print(f"Numeros impares:{impar}")
        return False
    except ValueError:
        print("Se ha encontrado valores no numericos en el ingreso")
        par.clear()
        impar.clear()
        numero=""
        return True

par=[]
impar=[]
nums=["1","2","3","4","5","6","7","8","9","0"]
numero=""
bucle=True
print("Ingrese numeros")
while bucle:
    numeros=input()
    if len(numeros)==0:
        print("no puede haber nada vacio")
    else:
        bucle=validar(par,impar,numero,numeros,nums)