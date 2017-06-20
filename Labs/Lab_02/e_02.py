import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wavfile
from SoundPlay import soundPlay


#from notasdic import notasDicionario
import notasdic


FS = 11025

NFFT = 512 * 2

dur = 2.
plt.close("all")


#Musica1
song = ["c",4],["d2",4],["e3",4],["f4",2]


#Musica2
marioSong = (
	('e5', 8), ('e5', 8), ('e5', 8), ('c5', 8), ('e5', 8),
	('g5', 4), ('g4', 4),
	('c5', 4), ('g4', 4), ('e4', 4),
	('a4', 4), ('b4', 4), ('bb4', 8), ('a4', 4),
	('g4', 4), ('e5', 4), ('g5', 4), ('a5', 4), ('f5', 8), ('g5', 8),
	('e5', 8), ('c5', 8), ('d5', 8), ('b4', 8)
)



def music(song):

    noteList6 = []
    notedur6 = []
    for i, x in enumerate(song):
        #guarda na lista noteList6 o nome das notas
        noteList6 = np.hstack((noteList6,x[0]))
        
        #guarda na lista notedur6 a duração de cada uma das notas da musica
        notedur6 = np.hstack((notedur6,dur/x[1]))
    
    
    intDur = 0.05
    #define o tipo de onda das notas musicais
    wavType = 1
    #frequência de cada nota(11025 para se conseguir reproduzir no mediaplayer etc..)
    FS = 11025
    
    x = np.array([])
    
    #ciclo responsável por criar cada nota musical com a sua 
    for i in range(0,len(noteList6)):
        xtmp = Note_tone(noteList6[i], notedur6[i], intDur, wavType, FS)
        
        t = np.arange(0, notedur6[i], 1 / FS)
        
        
        x = np.hstack((x,xtmp))
        
        
        #print de cada nota individualmente
        plt.plot(t[0:1000], x[0:1000], 'k')
        plt.title('Sinal Nota -'+noteList6[i])
        plt.xlabel(r'$t$ (segundos)')
        plt.ylabel('Intensidade')
        plt.show()  
        
    return x


    
#retorna a sinal da nota
def Note_tone(nota = [], notaDur = [], intDur = [], wavType = [], Fs = []):



    #dicionario das notas com as respectivas frequências
    notasDic = notasdic.notasDic()

    #passa apenas a primeira letra da musica para Maiuscula
    for i in range(len(nota)):
        if(i == 0):
            strTmp = nota[0][0].upper()
        else:
            strTmp = strTmp+nota[i]
   
    
    #frequência da nota
    fc = notasDic[strTmp]

    #numero de pontos(duração) que a nota tem
    t = np.arange(0, notaDur, 1 / Fs)
    
    #tip de onda a ser usada para construir o sinal
    if wavType == 1:
        x = np.cos(2 * np.pi * fc * t)
        
    elif wavType == 2:
        x = np.square(2 * np.pi * fc * t)
    elif wavType == 3:
        x = np.sawtooth(2 * np.pi * fc * t, 0.5)
    elif wavType == 4:
        x = np.sawtooth(2 * np.pi * fc * t)
    else:
        print ('\n wave type (%d) not available (only ints 1-4)\n'%wavType)
    
    return x




x=music(song)
#reprodução áudio do som e gravação da musica em formato wav
soundPlay.soundPlay(x,FS)
filename = 'x2.wav'
x1Int = np.int16(x * 2**13)
wavfile.write(filename, FS, x1Int)
#plt.plot(x)
#plt.show()

plt.figure(facecolor='w', figsize=(30, 30))
plt.title(" Sinal Musica")
plt.plot( x, 'k')
plt.xlabel(r'$t$ (segundos)')
plt.ylabel('Intensidade')
plt.axis([0,28000,-1.02,1.02])
plt.grid()
plt.savefig("lab2_ex2_Sinal.png", bbox_inches='tight', transparent=False)
plt.show()  



#calculo de fft(transformada rápida de fourier)
N = 4096

xfft = np.fft.fft(x[0:N])

freq1 = np.fft.fftfreq(len(xfft)) * FS
x1mag = np.abs(xfft) / N
Xfase = np.angle(xfft)


#Espectro amplitude
plt.figure(facecolor = 'w', figsize = (10, 20))
plt.title("Espectro amplitude")
plt.stem(freq1, x1mag, 'k', linewidth = 3)
plt.ylabel('Espectro amplitude', fontsize = 18)
plt.xlabel('f(Hz)', fontsize=18)

plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.grid()
plt.savefig("lab2_ex2_espectroAmplitude.png", bbox_inches = 'tight', transparent = False)
plt.show()


#Espectro Fase
plt.figure(facecolor = 'w', figsize = (10, 20))
plt.title("Espectro Fase")
Xfase = np.angle(xfft)
plt.stem(freq1, Xfase, 'k', linewidth = 3)
plt.axis([-5800, 5800, -np.pi, np.pi])
plt.ylabel('Espectro de fase', fontsize = 18)
plt.xlabel('f(Hz)', fontsize = 18)
plt.xticks(fontsize = 22)
plt.yticks(fontsize = 22)
plt.grid()
plt.savefig("lab2ex2_espectroFase.png", bbox_inches = 'tight', transparent = False)
plt.show()

#Espectrograma
plt.figure(facecolor = 'w', figsize = (30, 20))
plt.specgram(x, NFFT = NFFT, Fs = FS, noverlap = 0)
plt.savefig("lab2_ex2_espectrograma.png", bbox_inches = 'tight', transparent = False)


