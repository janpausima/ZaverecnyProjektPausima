
def nacti_text(pozadavek):
        """Funkce pro načtení textového vstupu od uživatele."""
        text = input(pozadavek).strip()
        while not text or not text.isalpha():
            print("Zadejte pouze písmena. Pole nesmí být prázdné.")
            text = input(pozadavek).strip()
        return text.capitalize()

def nacti_cislo(pozadavek):
        """Funkce pro načtení číselného vstupu od uživatele."""
        hodnota = input(pozadavek).strip()
        while not hodnota or not hodnota.isdigit():
            print("Zadejte platné celé číslo. Pole nesmí být prázdné.")
            hodnota = input(pozadavek).strip()
        return int(hodnota)
