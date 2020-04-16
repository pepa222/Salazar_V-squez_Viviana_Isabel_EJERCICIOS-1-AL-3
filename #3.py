print("Ejercicio 3")
aux= True
aux2= True
lista=[]
listaFeos=[1]
i=2

while aux ==True and aux2== True:
    n= int (input())
    if n>=1 and n<=1500:
        lista.append(n)
    elif n==0:
        aux=False
    else:
        aux2= False
if aux2== True:
    while len(listaFeos)< max(lista):
        d=2
        feo=False
        cont=0
        while d<=i:
            if i%2==0 or i%3==0 or i%5==0:
                feo=True
            elif i%d==0:
                cont+=1
            d+=1
        if feo==True and cont<2:
            listaFeos.append(i)
        i+=1
    print()
    for j in range(0,len(lista)):
        print(listaFeos[lista[j]-1])
    

        




