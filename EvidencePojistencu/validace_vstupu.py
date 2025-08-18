
def nacti_vstup(pozadavek, validace, chyba_zprava):
        """Funkce pro načtení vstupu od uživatele s validací."""
        nactena_hodnota = input(pozadavek).strip()
        while not nactena_hodnota or not validace(nactena_hodnota):
            print(chyba_zprava)
            nactena_hodnota = input(pozadavek).strip()
        return nactena_hodnota

def nacti_text(pozadavek):
        """Funkce pro načtení textového vstupu od uživatele."""
        return nacti_vstup(
            pozadavek,
            validace=str.isalpha,
            chyba_zprava="Zadejte pouze písmena. Pole nesmí být prázdné."
        )

def nacti_cislo(pozadavek):
        """Funkce pro načtení číselného vstupu od uživatele."""
        return nacti_vstup(
            pozadavek,
            validace=str.isdigit,
            chyba_zprava="Zadejte pouze čísla. Pole nesmí být prázdné."
        )
