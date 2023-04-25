# Komandinis darbas - biudžeto programėlė

import os
import pickle
def clear(): 
    if os.name == 'nt':
        os.system('cls') 
    else:
        os.system('clear')

# savybės: suma ir komentaras
class Irasas():
    def __init__(self, suma, komentaras):
        self.suma = suma
        self.komentaras = komentaras

# savybė: gavejas
class Islaidos(Irasas):
    def __init__(self, suma, komentaras, gavejas):
        super().__init__(suma, komentaras)
        self.gavejas = gavejas

# savybė: siuntejas
class Pajamos(Irasas):
    def __init__(self, suma, komentaras, siuntejas):
        super().__init__(suma, komentaras)
        self.siuntejas = siuntejas

# savybe: zurnalas: sąrašas įrašų
# turi turėti metodus:**
# Ataskaitai, balansui
# pajamų įrašo sukūrimas ir įtraukimui į žurnalą
# išlaidų įrašo sukūrimas ir įtraukimui į žurnalą
class Biudzetas():
    def __init__(self):
        self.__sarasas = []

    def biudzeto_sukurimas(self):
        return self.__sarasas

    def pajamu_sukurimas(self, pajamos):
        self.__sarasas.append(pajamos)

    def islaidu_sukurimas(self, islaidos):
        self.__sarasas.append(islaidos)

    def info_balansas(self,):
        bendros_pajamos = 0
        bendros_islaidos = 0
        for irasas in self.__sarasas:
            if isinstance(irasas, Pajamos):
                bendros_pajamos += irasas.suma 
            elif isinstance(irasas, Islaidos):
                bendros_islaidos += irasas.suma 
        print(f'Bendros pajamos yra: {bendros_pajamos}')
        print(f'Bendros islaidos yra: {bendros_islaidos}')
        print(f'Balansas: {bendros_pajamos - bendros_islaidos}') 

    def info_pajamos(self):
        for vartotojas in self.__sarasas:
            if isinstance(vartotojas, Pajamos):
                print(f"{vartotojas.siuntejas} pajamos yra: {vartotojas.suma} ({vartotojas.komentaras})")

    def info_islaidos(self):
        for vartotojas in self.__sarasas:
            if isinstance(vartotojas, Islaidos):
                print(f"{vartotojas.gavejas} isleido: {vartotojas.suma} ({vartotojas.komentaras})")

    def info_ataskaita(self):
        for vartotojas in self.__sarasas:
            if isinstance(vartotojas, Pajamos):
                print(f"{vartotojas.siuntejas} pajamos yra: {vartotojas.suma} ({vartotojas.komentaras})")
            elif isinstance(vartotojas, Islaidos):
                print(f"{vartotojas.gavejas} isleido: {vartotojas.suma} ({vartotojas.komentaras})")
            else:
                print("Nėra tokių įrašų")

    def pickle_sukurimas(biudzetas):
        with open("irasas.pickle", "wb") as file:
            pickle.dump(biudzetas, file)
        return biudzetas
    
    def pickle_nuskaitymas(biudzetas):
        with open('irasas.pickle', 'rb') as f:
            biudzetas = pickle.load(f)
        return biudzetas
    

biudzetas = Biudzetas()
biudzetas = Biudzetas.pickle_nuskaitymas(biudzetas)

while True:
    clear()
    print('\n-------- MENIU --------')
    print('1. Naujas pajamų įrašas')
    print('2. Naujas išlaidų įrašas')
    print('3. Balansas')
    print('4. Ataskaita')
    print('0. Išeiti iš programos')
    meniu = input("Pasirinkite: ")

    if meniu == "1":
        irasas = float(input('Iveskite pajamas: '))
        komentaras = input('Iveskite komentarą: ')
        siuntejas = input('Įveskite siuntėją: ')
        irasas = Pajamos(irasas, komentaras, siuntejas=siuntejas)
        biudzetas.pajamu_sukurimas(irasas)
        Biudzetas.pickle_sukurimas(biudzetas)
        print ('Pajamų įrašas įvestas')

    if meniu == "2":
        islaidos = float(input('Iveskite išlaidas: '))
        komentaras = input('Iveskite komentarą: ')
        gavejas = input('Įveskite gavėją: ')
        islaidos = Islaidos(islaidos, komentaras, gavejas=gavejas)
        biudzetas.islaidu_sukurimas(islaidos)
        Biudzetas.pickle_sukurimas(biudzetas)
        print ('Išlaidų įrašas įvestas')

    if meniu == "3":
        biudzetas.info_balansas()
        input("Paspauskite ENTER, kad grįžti į meniu")

    if meniu == "4":
        print("Pasirinkite ką norite peržiūrėti")
        print("1.Pajamas")
        print("2.Islaidas")
        print("3.Bendras")
        pasirinkimas = input("Įveskite skaičių: ")
        if pasirinkimas == "1":
            biudzetas.info_pajamos()
            input("Paspauskite ENTER, kad grįžti į meniu")
        elif pasirinkimas == "2":
            biudzetas.info_islaidos()
            input("Paspauskite ENTER, kad grįžti į meniu")
        elif pasirinkimas == "3":
            biudzetas.info_ataskaita()
            input("Paspauskite ENTER, kad grįžti į meniu")
        else:
            input("Neteisingai pasirinkote, paspauskite ENTER, kad grįžti į meniu")
        
    elif meniu == "0":
        break

    else:
        print ('Pasirinkite iš meniu')





