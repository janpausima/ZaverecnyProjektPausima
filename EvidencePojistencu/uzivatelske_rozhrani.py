
from evidence_pojistenych import EvidencePojistencu
from pojistenec import Pojistenec
from validace_vstupu import nacti_text, nacti_cislo


class UzivatelskeRozhrani:
    """Třída pro interakci s uživatelským rozhraním."""

    def __init__(self):
        """Inicializace uživatelského rozhraní."""
        self.evidence_pojistenych = EvidencePojistencu()

    def zobraz_menu(self):
        """Zobrazí hlavní menu programu."""
        print("\nZvolte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec programu")

    def pokracuj_dale(self):
        """Požádá uživatele o pokračování k hlavnímu menu."""
        input("\nPokračujte stisknutím klávesy Enter..")

    def vytvor_pojisteneho(self):
        """Vytvoří nového pojištěného a přidá ho do evidence."""
        jmeno = nacti_text("Zadejte jméno: ")
        prijmeni = nacti_text("Zadejte příjmení: ")
        vek = nacti_cislo("Zadejte věk: ")
        telefon = nacti_cislo("Zadejte telefonní číslo: ")

        pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
        self.evidence_pojistenych.pridej_pojisteneho(pojistenec)
        print(f"Pojištěný {jmeno} {prijmeni} byl přidán.")
        self.pokracuj_dale()

    def vypis_pojistene(self):
        """Vypíše všechny pojištěné v evidenci."""
        print("\nSeznam všech pojištěných:")
        pojistenci = self.evidence_pojistenych.vypis_vsechny()
        if not pojistenci:
            print("Žádní pojištění nejsou v evidenci.")
        else:
            for pojistenec in pojistenci:
                print(pojistenec)
        self.pokracuj_dale()

    def vyhledej_pojisteneho(self):
        """Vyhledá pojištěného podle jména a příjmení."""
        jmeno = nacti_text("Zadejte jméno: ")
        prijmeni = nacti_text("Zadejte příjmení: ")
        nalezeni = self.evidence_pojistenych.vyhledej_pojisteneho(jmeno, prijmeni)

        if not nalezeni:
            print(f"Pojištěný {jmeno} {prijmeni} nebyl nalezen.")
        else:
            print("\nNalezení pojištění:")
            for pojistenec in nalezeni:
                print(pojistenec)
        self.pokracuj_dale()