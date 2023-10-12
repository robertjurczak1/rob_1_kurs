from ludzie import ob_human2 as ob
from kurnik import kury

czlowiek3 = ob.Human2("Andrzej", 186.4, "M")
czlowiek3.idz_do_roboty()
print(czlowiek3.wzrost)

# ptak1 = kury.Ptak("orzeł bielik", 100)
# ptak1.lataj()
ptak1 = kury.Orzel("orzeł bielik", 100)
ptak1.lataj()
ptak1.wydaj_odglos()
ptak2 = kury.Kura("kura nioska", 1)
ptak2.lataj()
ptak2.produkcja_jaja(5)
ptak2.wydaj_odglos()
