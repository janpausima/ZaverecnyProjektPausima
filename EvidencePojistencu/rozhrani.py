
from evidence import EvidencePojistenych
from pojisteny import Pojisteny
from validace import nacti_text, nacti_cislo


class UzivatelskeRozhrani:
    def __init__(self):
        self.evidence = EvidencePojistenych()

    def zobraz_menu(self):
        print("\nZvolte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec programu")

    def pokracuj(self):
        input("\nPokračujte stisknutím klávesy Enter..")

    def vytvor_pojisteneho(self):
        jmeno = nacti_text("Zadejte jméno: ")
        prijmeni = nacti_text("Zadejte příjmení: ")
        vek = nacti_cislo("Zadejte věk: ")
        telefon = nacti_cislo("Zadejte telefonní číslo: ")

        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.evidence.pridej_pojisteneho(pojisteny)
        print(f"Pojištěný {jmeno} {prijmeni} byl přidán.")
        self.pokracuj()

    def vypis_pojistene(self):
        print("\nSeznam všech pojištěných:")
        pojisteni = self.evidence.vypis_vsechny()
        if not pojisteni:
            print("Žádní pojištění nejsou v evidenci.")
        else:
            for pojisteny in pojisteni:
                print(pojisteny)
        self.pokracuj()

    def vyhledej_pojisteneho(self):
        jmeno = nacti_text("Zadejte jméno: ")
        prijmeni = nacti_text("Zadejte příjmení: ")
        nalezeni = self.evidence.vyhledej_pojisteneho(jmeno, prijmeni)

        if not nalezeni:
            print(f"Pojištěný {jmeno} {prijmeni} nebyl nalezen.")
        else:
            print("\nNalezení pojištění:")
            for pojisteny in nalezeni:
                print(pojisteny)
        self.pokracuj()