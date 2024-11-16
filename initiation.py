import random

#from main import ile_probek, ilosc_zadan, ilosc_procesorow, czasy_zadan


def randomGeny(czasy_zadan, ilosc_procesorow, ilosc_zadan, ile_probek):
    probki=[]
    for i in range(ile_probek):
        probka=[]
        for j in range(ilosc_zadan):
            probka.append(random.randrange(1,ilosc_procesorow+1))
        probki.append(probka)

    return probki

def maxCzasZadan(probka,ilosc_procesorow,czasy_zadan):
    czasy_procesorow=[]
    for i in range(ilosc_procesorow):
        czasy_procesorow.append(0)
    for i in range(len(probka)):
        czasy_procesorow[probka[i]-1]+=czasy_zadan[i]
    return max(czasy_procesorow)

def czasyZadanWProbkach(probki,ilosc_procesorow,czasy_zadan):
    czasy=[]
    for probka in probki:
        czasy.append(maxCzasZadan(probka,ilosc_procesorow,czasy_zadan))
    return czasy

def najlepszyCzas(probki,ilosc_procesorow,czasy_zadan):
    return min(czasyZadanWProbkach(probki,ilosc_procesorow,czasy_zadan))