
from crossing import podzial_na_grupy, turniej, crossing
from initiation import randomGeny, maxCzasZadan, czasyZadanWProbkach, najlepszyCzas

ile_probek=30 #ile genow się krzyzuje
prob_mutacji=0.1
ile_w_grupie=5 #ile genow w grupie turniejowej
limit_generacji=100
wspolczynnik_poprawy=0
granica_stagnacji=50


ilosc_procesorow=int(input())
ilosc_zadan=int(input())
czasy_zadan=[]
czasy_wykonywania=[]

for i in range(ilosc_zadan):
    pom=int(input())
    czasy_zadan.append(pom)

minimum_czas_przewidywany=sum(czasy_zadan)//ilosc_procesorow+1
geny=randomGeny(czasy_zadan, ilosc_procesorow, ilosc_zadan, ile_probek)
czas=najlepszyCzas(geny, ilosc_procesorow, czasy_zadan)
ostatnie_czasy=[]
liczba_generacji=0
licznik_stagnacji=0
najlepszy_wynik=czas
najlepszy_gen = min(geny, key=lambda x: maxCzasZadan(x, ilosc_procesorow, czasy_zadan))


i=0
while  1:

    if liczba_generacji==0:
        ostatnie_czasy.append(czas)

    czas=najlepszyCzas(geny, ilosc_procesorow, czasy_zadan)

    if czas < najlepszy_wynik:
        najlepszy_wynik = czas
        najlepszy_gen = min(geny, key=lambda x: maxCzasZadan(x, ilosc_procesorow, czasy_zadan)).copy()
        print(najlepszy_gen)

    ostatnie_czasy.append(czas)

    if len(ostatnie_czasy)> 2:
        poprawa = ostatnie_czasy[-2] - najlepszy_wynik
        if poprawa <= wspolczynnik_poprawy:
            licznik_stagnacji += 1
            if licznik_stagnacji >= granica_stagnacji:
                print(f"Zatrzymano z powodu stagnacji.")
                break
        else:
            licznik_stagnacji = 0



    grupy=podzial_na_grupy(geny, ile_w_grupie)
    najlepsi=turniej(grupy, ilosc_procesorow, czasy_zadan)
    geny=crossing(geny, ile_probek, prob_mutacji, ilosc_procesorow, ile_w_grupie, czasy_zadan)
    liczba_generacji+=1


print(f"Najlepszy czas: {najlepszy_wynik}")
print(f"Ostatni wynik: {najlepszy_gen}")



