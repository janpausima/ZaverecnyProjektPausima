
class EvidencePojistenych:
    """Třída sloužící k evidenci pojištěných osob."""

    def __init__(self):
        """Inicializuje prázdnou evidenci pojištěných."""
        self.pojisteni = []

    def pridej_pojisteneho(self, pojisteny):
        """Přidá pojištěného do evidence."""
        self.pojisteni.append(pojisteny)

    def vypis_vsechny(self):
        """Vypíše všechny pojištěné osoby."""
        return self.pojisteni

    def vyhledej_pojisteneho(self, jmeno, prijmeni):
        """Vyhledá pojištěného podle jména a příjmení."""
        return [
            pojisteny for pojisteny in self.pojisteni
            if pojisteny.jmeno.lower() == jmeno.lower() and pojisteny.prijmeni.lower() == prijmeni.lower()
        ]
