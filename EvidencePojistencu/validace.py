
def nacti_text(pozadavek):
        text = input(pozadavek).strip()
        while not text or not text.isalpha():
            print("Zadejte pouze písmena. Pole nesmí být prázdné.")
            text = input(pozadavek).strip()
        return text.capitalize()

def nacti_cislo(pozadavek):
        hodnota = input(pozadavek).strip()
        while not hodnota or not hodnota.isdigit():
            print("Zadejte platné celé číslo. Pole nesmí být prázdné.")
            hodnota = input(pozadavek).strip()
        return int(hodnota)
