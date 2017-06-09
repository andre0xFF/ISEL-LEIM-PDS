# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:08:40 2017

@author: Danie
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavfile
from SoundPlay import soundPlay
import sys
sys.path.append('../../PySynth')

import notasdic

#color Map
plt.rcParams['image.cmap'] = 'viridis'



sampFreq, snd =wavfile.read('x2.wav') # load the data

x=snd/2.**13

t = np.arange(0, len(x)) /np.float(sampFreq)

#plot do sinal
plt.plot(t[0:1000], x[0:1000], 'k')
plt.show()
plt.plot(x)
plt.savefig("lab2_ex5_Sinal.png", bbox_inches='tight', transparent=False)
plt.show()


plt.figure(facecolor='w', figsize=(30, 20))

NFFT=512*4

[a,b,c,d]=plt.specgram(x, NFFT=NFFT, Fs=sampFreq, noverlap=0)
plt.savefig("lab2_ex5_espectrograma.png", bbox_inches='tight', transparent=False)


#shape do espectrograma(numero de linhas e colunas)
shapeColorSpecgram=np.shape(a)

numRows=shapeColorSpecgram[0]
numCol=shapeColorSpecgram[1]

#array com os tempos médios do espectrograma para cada nfft
arrayTime=c

#array com as frequências do espectrograma para cada nfft
arrayFreq=b

auxColorIntensity=0;
maxColorIntensity=0;

indexIntensity=[]
index=0

notaTime=[]
noteSong=[]
#calcula e guarda os indices com maior intensidade de cor para cada coluna de NFFT do espectrograma
for x in range(0, numCol):
    for y in range(0, numRows):

        auxColorIntensity=a[y][x]
        
        if auxColorIntensity>maxColorIntensity:
            maxColorIntensity=auxColorIntensity

            index=y
    #contêm valores de indice repetidos devido á duração de cada nota [3,3,3,14,14,31,31,31,65,65,65,65]
    indexIntensity.append(index)

    maxColorIntensity=0;
    


#identifica quando começa e acaba uma nota e guarda a respectiva frequência e a sua duração
for x in range(1,len(indexIntensity)):
    
    if(indexIntensity[x] != indexIntensity[x-1]):
        notaTime.append(arrayTime[x-1])
        noteSong.append(arrayFreq[indexIntensity[x-1]])


#guarda a ultima nota e a sua duração
notaTime.append(arrayTime[len(indexIntensity)-1])  
noteSong.append(arrayFreq[indexIntensity[len(indexIntensity)-1]])

  

noteTempo=[]
noteTempo.append(np.int(2./notaTime[0]))
for x in range(1,len(notaTime)):
    noteTempo.append(np.int(np.round(2./(notaTime[x]-notaTime[x-1]))))


#recebe as frequências e durações das notas e retorna a notação ABC da Musica/Composição
def createABC(Freq=[],Time=[]):
    

    dic= notasdic.notasDic();

    song=[]
   
    count=0
    dif=None
    auxTuple=None
    
    #identifica qual a nota a que corresponde a frequência recebida e qual a sua respectiva duração
    for x in range(0, len(Freq)):

        for key, val in dic.items():

            if(dif is None):
                dif=np.abs(Freq[x]-val)
                
            if(np.abs(Freq[x]-val)<=dif):
        
                dif=np.abs(Freq[x]-val)
                auxTuple=(key,Time[count])

        dif=None
        count+=1
        song.append(auxTuple)

    return song
      

print(createABC(noteSong,noteTempo))
