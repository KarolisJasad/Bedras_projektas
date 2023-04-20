# Komandinis darbas - biudžeto programėlė

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

    def pajamu_sukurimas(self, pajamos):
        self.sarasas.append(pajamos)

    def islaidu_sukurimas(self, islaidos):
        self.sarasas.append(islaidos)

    def info_ataskaita(self,):
        pass

biudzetas = Biudzetas()
pajamos = Pajamos(500, "pajamos", siuntejas="tadas")
biudzetas.pajamu_sukurimas(pajamos)

for pajamos in biudzetas.sarasas:
    print(pajamos.siuntejas, "pajamos yra:", pajamos.suma)

biudzetas = Biudzetas()
islaidos = Islaidos(200, "islaidos", gavejas="petras")
biudzetas.islaidu_sukurimas(islaidos)

for islaidos in biudzetas.sarasas:
    print(islaidos.gavejas, "islaidos yra:", islaidos.suma)

