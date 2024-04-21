from abc import ABC, abstractmethod
from datetime import datetime

# Szoba absztrakt osztály létrehozása
class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    @abstractmethod
    def szoba_tipus(self):
        pass
# EgyágyasSzoba osztály létrehozása
class EgyagyasSzoba(Szoba):
    def szoba_tipus(self):
        return "Egyágyas szoba"
# KétágyasSzoba osztály létrehozása
class KetagyasSzoba(Szoba):
    def szoba_tipus(self):
        return "Kétágyas szoba"
# Foglalas osztály létrehozása
class Foglalas:
    def __init__(self, szoba, vendeg_nev, foglalas_datum, veg_datum):
        self.szoba = szoba
        self.vendeg_nev = vendeg_nev
        self.foglalas_datum = foglalas_datum
        self.veg_datum = veg_datum
# Foglalás teljes árának kiszámolása
    def teljes_ar(self):
        delta = self.veg_datum - self.foglalas_datum
        napok = delta.days
        return self.szoba.ar * napok
# Szalloda osztály létrehozása
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []
# Új szoba hozzáadása a szállodához
    def uj_szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)
# Szobák listázása
    def szobak_listazasa(self):
        print("A szálloda szobái:")
        for szoba in self.szobak:
            print(f"Szobaszám: {szoba.szobaszam}, Típus: {szoba.szoba_tipus()}, Ár: {szoba.ar}")
 # Szoba foglalása
    def szoba_foglalasa(self, szobaszam, vendeg_nev, foglalas_datum, veg_datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, vendeg_nev, foglalas_datum, veg_datum)
                self.foglalasok.append(foglalas)
                return foglalas.teljes_ar()
        return None
# Foglalás lemondása
    def foglalas_lemondasa(self, vendeg_nev, foglalas_datum):
        for foglalas in self.foglalasok:
            if foglalas.vendeg_nev == vendeg_nev and foglalas.foglalas_datum == foglalas_datum:
                self.foglalasok.remove(foglalas)
                return True
        return False
# Foglalások listázása
    def foglalasok_listazasa(self):
        print("A szálloda foglalásai:")
        for foglalas in self.foglalasok:
            print(f"Szobaszám: {foglalas.szoba.szobaszam}, Vendég: {foglalas.vendeg_nev}, Foglalás dátuma: {foglalas.foglalas_datum}, Vég dátum: {foglalas.veg_datum}")

def main():
    szalloda = Szalloda("Gyula apartman")

    szoba1 = EgyagyasSzoba(szobaszam=1, ar=5500)
    szoba2 = KetagyasSzoba(szobaszam=2, ar=8000)
    szoba3 = EgyagyasSzoba(szobaszam=3, ar=5500)
    szalloda.uj_szoba_hozzaadasa(szoba1)
    szalloda.uj_szoba_hozzaadasa(szoba2)
    szalloda.uj_szoba_hozzaadasa(szoba3)

    szalloda.szoba_foglalasa(szobaszam=1, vendeg_nev="Kiss József", foglalas_datum=datetime(2024, 5, 1), veg_datum=datetime(2024, 5, 3))
    szalloda.szoba_foglalasa(szobaszam=2, vendeg_nev="Nagy Béla", foglalas_datum=datetime(2024, 5, 3), veg_datum=datetime(2024, 5, 7))
    szalloda.szoba_foglalasa(szobaszam=3, vendeg_nev="Nagy Aladár", foglalas_datum=datetime(2024, 5, 5), veg_datum=datetime(2024, 5, 9))
    szalloda.szoba_foglalasa(szobaszam=2, vendeg_nev="Kiss József", foglalas_datum=datetime(2024, 5, 7), veg_datum=datetime(2024, 5, 10))
    szalloda.szoba_foglalasa(szobaszam=1, vendeg_nev="Szabó Károly", foglalas_datum=datetime(2024, 5, 9), veg_datum=datetime(2024, 5, 12))

    while True:
        print("\nÜdvözöljük a Gyula aparmanban***!")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Kérlek, válassz egy műveletet (1-4): ")

        if valasztas == "1":
            szobaszam = int(input("Kérlek, add meg a szobaszámot: (1-egyágyas, 2-kétágyas, 3-egyágyas)"))
            vendeg_nev = input("Kérlek, add meg a neved: ")
            foglalas_datum = input("Kérlek, add meg a foglalás kezdeti dátumát (ÉÉÉÉ-HH-NN): ")
            foglalas_datum = datetime.strptime(foglalas_datum, "%Y-%m-%d")
            veg_datum = input("Kérlek, add meg a foglalás végső dátumát (ÉÉÉÉ-HH-NN): ")
            veg_datum = datetime.strptime(veg_datum, "%Y-%m-%d")
            if foglalas_datum < datetime.now() or foglalas_datum >= veg_datum:
                print("Hibás dátum! Kérlek, adj meg érvényes időpontokat.")
                continue
            ar = szalloda.szoba_foglalasa(szobaszam, vendeg_nev, foglalas_datum, veg_datum)
            if ar:
                print(f"A foglalás sikeres. A teljes ár: {ar}Ft.")
            else:
                print("Hibás szobaszám! Kérlek, válassz egy létező szobát.")
        elif valasztas == "2":
            vendeg_nev = input("Kérlek, add meg a vendég nevét: ")
            foglalas_datum = input("Kérlek, add meg a foglalás kezdeti dátumát (ÉÉÉÉ-HH-NN): ")
            foglalas_datum = datetime.strptime(foglalas_datum, "%Y-%m-%d")
            sikeres = szalloda.foglalas_lemondasa(vendeg_nev, foglalas_datum)
            if sikeres:
                print("A foglalás sikeresen le lett mondva.")
            else:
                print("Hibás adatok! Kérlek, adj meg egy létező foglalást.")
        elif valasztas == "3":
            szalloda.foglalasok_listazasa()
        elif valasztas == "4":
            print("Köszönjük, hogy meglátogatta az oldalunkat! Viszlát!")
            break
        else:
            print("Hibás választás! Kérlek, válassz egy érvényes műveletet.")

if __name__ == "__main__":
    main()
