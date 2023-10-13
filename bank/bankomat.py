"""
Klasa bankomat ma mieć możliwości
1. stan konta jako pole
2. metody do: sprawdzania stanu, wpłaty gotówki oraz wypłaty
"""

class Bankomat:
    stan_konta = 0
    wplata = 0
    wyplata = 0
    pin ="1234"

    def sprawdzanie_stanu(self):
        print(f"Aktualny stan konta wynosi: {self.stan_konta}")

    def wplata_gotowki(self):
        print(f"Wypłacono kwotę: {self.wplata}")

    def wyplata(self):
        kod = input("Jaki jest pin?")
        if kod == {self.pin}:
        print(f"Wypłacono kwotę: {self.wyplata}")

        return print(f"błędny pin")

stan1 = Bankomat()
stan1.wplata = 100
stan1.wyplata = 20
print(stan1.stan_konta)
print(stan1.wplata)
print(stan1.wyplata)


