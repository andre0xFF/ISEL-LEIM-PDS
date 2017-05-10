import sys
sys.path.append('../../PySynth')
import pysynth_s as pysynth

# E' necessario adaptar este script para PySynth


def ADSR_env0(N=[]):
    xEnv = np.ones(N)
    return xEnv


def ADSR_env1(N=[]):
    Dur = (0.1, 0.2, 0.6, 0.1)
    nA = np.floor(N * Dur[0])
    nD = np.floor(N * Dur[1])
    nS = np.floor(N * Dur[2])
    nR = N - nA - nD - nS
    zA = np.linspace(0, 1, nA)
    # faltam aqui coisas
    xD = np.linspace(1, .8, nD)
    xS = np.ones(nS) * 0.8
    xR = np.linspace(0.8, 0, nR)
    # faltam aqui coisas
    xEnv = np.hstack()
    return xEnv


def F2P3(noteList, notaDur):
    intDur = 0.05
    wavType = 3
    Fs = 22050/2

    x = np.array([])
    for i in range(0, len(noteList)):
        xtmp = Note_tone(noteList[i], notaDur[i], intDur, wavType, Fs)
        x = np.hstack((x, xtmp))

    return (x)


def Note_tone(nota=[], notaDur=[], intDur=[], wavType=[], Fs=[]):

    NotasDir = {}
    strTmp = nota.upper()

    print strTmp

    fc = NotasDic[strTmp]
    t = np.arange(0, notaDur, 1 / Fs)

    if wavType == 1:
        x = np.cos(2 * np.pi * fc * t)
    elif wavType == 2:
        x = sg.square(2 * np.pi * fc * t)
    elif wavType == 3:
        x = sg.sawtooth(2 * np.pi * fc * t, 0.5)
    elif == 4:
        x = sg.sawtooth(2 * np.pi * fc * t)
    else:
        print '\n wave type (%d) not available (only ints 1-4)\n'%wavType

    xEnv = ADSR_env2(len(x))
    plt.figure(facecolor='w')
    plt.plot(xEnv)

    # faltam aqui coisas
