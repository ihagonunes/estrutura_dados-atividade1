# (1,5) Um vetor A contém n inteiros retirados do intervalo [0, 4n], com repetições permitidas.
# Implemente um programa em Python contendo uma função para determinar o valor inteiro k
# que ocorre com mais frequência.
# Requisitos 
# 
# a) O programa deve receber como entrada um array contendo n inteiros retirados do intervalo
# [0, 4n]. Os valores deverão ser informados via terminal e não podem estar fora do intervalo
# especificado. O valor de n também deverá ser informado via teclado.
# 
# b) O programa deve imprimir no terminal o elemento com frequência máxima e sua frequência 
# associada.
# 
# c) Caso todos os valores apresentam a mesma frequência imprimir a mensagem "Todos os 
# valores apresentam a mesma frequência".
# 
# d) O programa não pode usar recursividade.

from random import randint

n = int(input(f"Digite a quantidade de inteiros para o vetor"))
a = []
freq = {}
valoresRepetidos = []

for i in range(n):
    aux = int(input(f"Digite um valor para o endereço {i} do vetor"))
    #aux = randint(0, 4*n)
    a.append(aux) 
    freq[a[i]] = freq.get(a[i], 0) + 1
    if i  == 0: 
        valoresRepetidos.append(aux)
    
    elif(freq.get(a[i]) > freq.get(valoresRepetidos[0])): # comparando as frequência puxando o value através das keys
        valoresRepetidos = [] # limpa valores repetidos com freq. menores
        valoresRepetidos.append(a[i])
        
    elif(freq.get(a[i]) == freq.get(valoresRepetidos[0])):
        valoresRepetidos.append(a[i])

if(len(valoresRepetidos) > 1):
    print(f"Há mais de um valor com a maior frequência ({freq.get(valoresRepetidos[0])}). Os valores são: {valoresRepetidos}")

else:
    print(f"A maior frequência é {freq.get(valoresRepetidos[0])} do valor {valoresRepetidos[0]}")
    