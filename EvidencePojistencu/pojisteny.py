
class Pojisteny:
    """Třída reprezentující pojištěnce v systému evidence pojištěnců."""

    def __init__(self, jmeno, prijmeni, vek, telefon):
        """Inicializuje nového pojištěnce s danými údaji."""
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        """Vrátí řetězec s informacemi o pojištěnci."""
        return f"{self.jmeno} {self.prijmeni}, věk: {self.vek}, telefon: {self.telefon}"