
from crossing import podzial_na_grupy, turniej, crossing
from initiation import randomGeny, maxCzasZadan, czasyZadanWProbkach, najlepszyCzas

ile_probek=30#ile genow się krzyzuje
prob_mutacji=0.1
stare_prob_mutacji=0.1
ile_w_grupie=2 #ile genow w grupie turniejowej
limit_generacji=100
wspolczynnik_poprawy=0
granica_stagnacji=100000


czasy_wykonywania=[]

with open("dane.txt", "r") as dane:
    temp=dane.readlines()
    ilosc_procesorow=int(temp[0])
    ilosc_zadan=int(temp[1])
    czasy_zadan=[int(temp[i]) for i in range(2,ilosc_zadan+2)]

minimum_czas_przewidywany=sum(czasy_zadan)//ilosc_procesorow+1
geny=randomGeny(czasy_zadan, ilosc_procesorow, ilosc_zadan, ile_probek)
czas=najlepszyCzas(geny, ilosc_procesorow, czasy_zadan)
ostatnie_czasy=[]
liczba_generacji=0
licznik_stagnacji=0
najlepszy_wynik=czas
najlepszy_gen = min(geny, key=lambda x: maxCzasZadan(x, ilosc_procesorow, czasy_zadan))


i=0
while 1:

    if liczba_generacji==0:
        ostatnie_czasy.append(czas)

    czas=najlepszyCzas(geny, ilosc_procesorow, czasy_zadan)
    print(czas)
    if czas < najlepszy_wynik:
        najlepszy_wynik = czas
        najlepszy_gen = min(geny, key=lambda x: maxCzasZadan(x, ilosc_procesorow, czasy_zadan)).copy()
        print(najlepszy_gen)

    ostatnie_czasy.append(czas)

    if len(ostatnie_czasy)> 2:
        poprawa = ostatnie_czasy[-2] - najlepszy_wynik
        if poprawa <= wspolczynnik_poprawy:
            licznik_stagnacji += 1
            if licznik_stagnacji%100==50 and prob_mutacji<0.5:
                prob_mutacji += 0.05
                ile_probek += 1
                geny+=randomGeny(czasy_zadan, ilosc_procesorow, ilosc_zadan, 1)
            if licznik_stagnacji >= granica_stagnacji:
                print(f"Zatrzymano z powodu stagnacji.")
                break
        else:
            licznik_stagnacji = 0
            prob_mutacji = stare_prob_mutacji

    geny=crossing(geny, ile_probek, prob_mutacji, ilosc_procesorow, ile_w_grupie, czasy_zadan)
    liczba_generacji+=1


print(f"Najlepszy czas: {najlepszy_wynik}")
print(f"Ostatni wynik: {najlepszy_gen}")