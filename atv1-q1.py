"""
Implemente um programa em Python contendo uma função que verifique se um vetor de
inteiros contém pelo menos um elemento A[i] que seja a soma de dois valores anteriores no
próprio vetor. Ou seja, seu programa deve identificar se existem índices j e k (j < i e k < i) tais que:
A[i] = A[j] + A[k]. Após a implementação do seu algoritmo, descreva qual a ordem de
complexidade em notação O da função responsável por fazer a verificação (coloque essa
informação como comentário no início do código).
Requisitos
a) O programa deve receber como entrada um array contendo n inteiros. Os valores deverão
ser informados via terminal.
b) O algoritmo deve verificar, para cada elemento A[i] (a partir do terceiro), se ele pode ser
obtido como soma de dois elementos anteriores.
c) O programa deve imprimir "Existe um elemento que é a soma de dois anteriores." caso
encontre tal valor, ou "Nenhum elemento é a soma de dois anteriores." caso contrário.
d) O programa não pode usar recursividade
"""

#A ordem de complexidade desse codigo e O(n^3), por mais que haja algumas tentativas de diminuir a complexidade no segundo e terceiro for o pior caso ainda permanece em n^3

def IhanBraboSelmineVaimedarDeznaProvaSemCorrigir(lista):
    if(len(lista)>=3):
        for i in range (2,len(lista)):
            for j in range(0,i):
                for k in range (0,j):
                    if lista[j] + lista[k] == lista[i] and (k)!=j:
                        return "Existe um elemento que é a soma de dois anteriores."
            if(i==len(lista)-1):
                return "Não existe um elemento que é a soma de dois anteriores."
    else:
        return "Não há elementos suficientes"


cont = int(input("Insira o numero de elementos: "))

aux = []

for i in range(cont):
    aux.append(int(input(f"Insira o {i+1}º  elemento: ")))

print(IhanBraboSelmineVaimedarDeznaProvaSemCorrigir(aux))