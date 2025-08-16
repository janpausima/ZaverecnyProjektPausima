
def nacti_text(pozadavek):
        """Funkce pro načtení textového vstupu od uživatele."""
        nacteny_text = input(pozadavek).strip()
        while not nacteny_text or not nacteny_text.isalpha():
            print("Zadejte pouze písmena. Pole nesmí být prázdné.")
            nacteny_text = input(pozadavek).strip()
        return nacteny_text.capitalize()

def nacti_cislo(pozadavek):
        """Funkce pro načtení číselného vstupu od uživatele."""
        nactena_hodnota = input(pozadavek).strip()
        while not nactena_hodnota or not nactena_hodnota.isdigit():
            print("Zadejte platné celé číslo. Pole nesmí být prázdné.")
            nactena_hodnota = input(pozadavek).strip()
        return int(nactena_hodnota)
