#from main import ile_probek, prob_mutacji, ilosc_procesorow, czasy_zadan, ile_w_grupie
import random

def maxCzasZadan(probka,ilosc_procesorow,czasy_zadan):
    czasy_procesorow=[]
    for i in range(ilosc_procesorow):
        czasy_procesorow.append(0)
    for i in range(len(probka)):
        czasy_procesorow[probka[i]-1]+=czasy_zadan[i]
    return max(czasy_procesorow)

def podzial_na_grupy(geny, ile_w_grupie):

    ile_grup = (len(geny) + ile_w_grupie - 1) // ile_w_grupie
    return [geny[i * ile_w_grupie:(i + 1) * ile_w_grupie] for i in range(ile_grup)]

def turniej(grupy, ilosc_procesorow, czasy_zadan):

    najlepsi = []
    for grupa in grupy:
        najlepszy = min(grupa, key=lambda gen: maxCzasZadan(gen, ilosc_procesorow, czasy_zadan))
        najlepsi.append(najlepszy)
    return najlepsi

def cross_geny(gen1, gen2):

    geny = []
    gen3 = gen1[:len(gen1) // 2] + gen2[len(gen1) // 2:]
    gen4 = gen2[:len(gen1) // 2] + gen1[len(gen1) // 2:]
    geny.append(gen3)
    geny.append(gen4)
    return geny

def crossing(geny, ile_probek, prob_mutacji, ilosc_procesorow, ile_w_grupie, czasy_zadan):
    nowe_geny = []
    grupy = podzial_na_grupy(geny, ile_w_grupie)
    najlepsi = turniej(grupy, ilosc_procesorow, czasy_zadan)
    najlepsi=mutacja(najlepsi, prob_mutacji, ilosc_procesorow)
    nowe_geny+=najlepsi
    while len(nowe_geny) < ile_probek:
        gen1 = random.choice(najlepsi)
        gen2 = random.choice(najlepsi)
        nowe_geny+=cross_geny(gen1, gen2)
    return nowe_geny
        
def mutacja(geny, prob_mutacji, ilosc_procesorow):
    for gen in geny:
        if random.random() < prob_mutacji:
            gen[random.randrange(len(gen))] = random.randrange(1, ilosc_procesorow + 1)
    return geny
        




