# Komandinis darbas - biudžeto programėlė

import os
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
        self.sarasas = []

    def pajamu_sukurimas(self, pajamos, komentaras, siuntejas):
        self.sarasas.append(pajamos)

    def islaidu_sukurimas(self, islaidos, komentaras, gavejas):
        self.sarasas.append(islaidos)

    def info_balansas(self,):
        pass

    def info_ataskaita(self,):
        for vartotojas in biudzetas.sarasas:
            if isinstance(vartotojas, Pajamos):
                print(f"{vartotojas.siuntejas} pajamos yra: {vartotojas.suma}")
            elif isinstance(vartotojas, Islaidos):
                print(f"{vartotojas.gavejas} isleido: {vartotojas.suma}")
            else:
                print("Nėra tokių įrašų")

biudzetas = Biudzetas()
# pajamos = Pajamos(500, "pajamos", siuntejas="tadas")
# biudzetas.pajamu_sukurimas(pajamos)
# islaidos = Islaidos(200, "islaidos", gavejas="petras")
# biudzetas.islaidu_sukurimas(islaidos)


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
        pajamos = float(input('Iveskite pajamas: '))
        komentaras = input('Iveskite komentarą: ')
        siuntejas = input('Įveskite siuntėją: ')
        biudzetas.pajamu_sukurimas(pajamos, komentaras, siuntejas)
        print ('Pajamų įrašas įvestas')

    if meniu == "2":
        islaidos = float(input('Iveskite išlaidas: '))
        komentaras = input('Iveskite komentarą: ')
        gavejas = input('Įveskite gavėją: ')
        biudzetas.islaidu_sukurimas(islaidos, komentaras, gavejas)
        print ('Išlaidų įrašas įvestas')

    if meniu == "3":
        biudzetas.info_balansas()

    if meniu == "4":
        biudzetas.info_ataskaita()

    elif meniu == "0":
        break

    else:
        print ('Pasirinkite iš meniu')




