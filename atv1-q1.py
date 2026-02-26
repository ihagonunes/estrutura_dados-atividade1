def IhanBraboSelmineVaimedarDeznaProvaSemCorrigir(lista):
    for i in range (2,len(lista)):
        for j in range(0,i):
            if lista[j] + lista[i-1] == lista[i] and (i-1)!=j:
                return "Existe um elemento que é a soma de dois anteriores."
        if(i==len(lista)-1):
            return "Não existe um elemento que é a soma de dois anteriores."


print(IhanBraboSelmineVaimedarDeznaProvaSemCorrigir([8, 1, 6, 2, 9]))#atencion
