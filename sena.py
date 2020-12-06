# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 12:51:38 2017

@author: Dr_viper
"""
import numpy as np
import matplotlib.pyplot as plt
#==============================================================================
ref_arquivo = open("dados.dat","r")
SENA=[]
SENAFULL=[]
a1=0
#==============================================================================



for linha in ref_arquivo:
    valores = linha.split()
#    print('N', valores[0],'Data',valores[1],'Soteiro', valores[2],valores[3],valores[4],valores[5],valores[6],valores[7])
    SENA.append([int(valores[2]),int(valores[3]),int(valores[4]),int(valores[5]),int(valores[6]),int(valores[7])])
    SENAFULL.append(int(valores[2]))
    SENAFULL.append(int(valores[3]))
    SENAFULL.append(int(valores[4]))
    SENAFULL.append(int(valores[5]))
    SENAFULL.append(int(valores[6]))
    SENAFULL.append(int(valores[7]))
    
#gerando distribuição de probabilidade.    
sena_est=np.asarray(SENAFULL)

#his_a=plt.hist(sena_est, bins=60, normed=True)
cum=np.cumsum(his_a[0])
# sortei do jogo.
pre_sena=[]
for j in range(0,6):
    sem=np.random.rand() 
    for i in range(0,59):
        if i==0:
            if sem < cum[0]:
                a1=1
        if (sem > cum[i] and sem < cum[i+1]):
            a1=i+1
    pre_sena.append(a1)

for j in range(0,len(SENA)):
   SENA[j].sort()
   pre_sena.sort()
   
   if SENA[j]==pre_sena :
        print "Ja Sorteado"


if SENA[j]!=pre_sena :
    print "bilhete da mega sorte: ", pre_sena

ref_arquivo.close()