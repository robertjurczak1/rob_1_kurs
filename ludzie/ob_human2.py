class Human2:

    def __init__(self, imie:str, wzrost:float, plec:str):
        self.plec = plec
        self.wzrost = wzrost
        self.imie = imie
        self.kolorOczu = "niebieski"

    def idz_do_roboty(self):
        kasa = 0
        for _ in range(5):
            kasa += 10
        print(f"Zarobiona: {kasa} $ przez {self.imie}")
        return kasa

    def stan_konta(self):
        pass

# czlowiek3 = Human2("Ania", "167.5", "K")
# print(czlowiek3.imie)

