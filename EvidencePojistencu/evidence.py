
class EvidencePojistenych:
    def __init__(self):
        self.pojisteni = []

    def pridej_pojisteneho(self, pojisteny):
        self.pojisteni.append(pojisteny)

    def vypis_vsechny(self):
        return self.pojisteni

    def vyhledej_pojisteneho(self, jmeno, prijmeni):
        return [
            pojisteny for pojisteny in self.pojisteni
            if pojisteny.jmeno.lower() == jmeno.lower() and pojisteny.prijmeni.lower() == prijmeni.lower()
        ]
