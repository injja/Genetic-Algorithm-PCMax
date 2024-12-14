import random

#from main import ile_probek, ilosc_zadan, ilosc_procesorow, czasy_zadan


def randomGeny(czasy_zadan, ilosc_procesorow, ilosc_zadan, ile_probek):
    probki=[]
    for i in range(ile_probek-1):
        probka=[]
        for j in range(ilosc_zadan):
            probka.append(random.randrange(1,ilosc_procesorow+1))
        probki.append(probka)

    # probka = [0] * ilosc_zadan
    # obciazenia_procesorow = [0] * ilosc_procesorow
    #
    # for i, czas_zadania in sorted(enumerate(czasy_zadan), key=lambda x: -x[1]):
    #     najlepszy_procesor = obciazenia_procesorow.index(min(obciazenia_procesorow))
    #     probka[i] = najlepszy_procesor + 1
    #     obciazenia_procesorow[najlepszy_procesor] += czas_zadania
    #
    # probki.append(probka)

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