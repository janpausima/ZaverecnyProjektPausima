
class EvidencePojistencu:
    """Třída sloužící k evidenci pojištěných osob."""

    def __init__(self):
        """Inicializuje prázdnou evidenci pojištěných."""
        self.pojistenci = []

    def pridej_pojisteneho(self, pojistenec):
        """Přidá pojištěného do evidence."""
        self.pojistenci.append(pojistenec)

    def vypis_vsechny(self):
        """Vypíše všechny pojištěné osoby."""
        return self.pojistenci

    def vyhledej_pojisteneho(self, jmeno, prijmeni):
        """Vyhledá pojištěného podle jména a příjmení."""
        return [
            pojistenec for pojistenec in self.pojistenci
            if pojistenec.jmeno.lower() == jmeno.lower() and pojistenec.prijmeni.lower() == prijmeni.lower()
        ]
