class Human:
    """
    klasa human opisuje człowieka
    :param plec: typ/str
    :param wzrost: typ/flot
    :param imie: typ/str
    """

    plec = None
    wzrost = 0
    imie = ""

    def idz_do_roboty(self):
        """Metoda symulująca pracę i zarabianie
        :return: wynagrodzenia: typ/float
        """
        kasa = 0
        for _ in range(5):
            kasa += 10
        print(f"Zarobiona: {kasa} $ przez {self.imie}")
        return kasa

    def stan_konta(self):
        pass


czlowiek1 = Human() #instancja
czlowiek1.imie = "Robert"
czlowiek1.wzrost = 170
czlowiek1.plec = "M"
czlowiek1.idz_do_roboty()
print(czlowiek1.imie)
print(czlowiek1.wzrost)
print(czlowiek1.plec)


czlowiek2 = Human() #instancja
czlowiek2.imie = "Marta"
czlowiek2.wzrost = 160
czlowiek2.plec = "K"
czlowiek2.idz_do_roboty()
print(czlowiek2.imie)
print(czlowiek2.wzrost)
print(czlowiek2.plec)

marta_konto = (czlowiek2.idz_do_roboty())
robert_konto = (czlowiek1.idz_do_roboty())
print(marta_konto)
print(robert_konto)

print(id(czlowiek1),id(czlowiek2))
print("Razem mają na koncie:", marta_konto + robert_konto)