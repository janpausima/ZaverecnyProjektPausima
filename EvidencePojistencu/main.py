
from uzivatelske_rozhrani import UzivatelskeRozhrani

uzivatelske_rozhrani = UzivatelskeRozhrani()
volba_cisla = 0

print("\nEvidence pojištěných")
print("---------------------")

while volba_cisla != 4:
    uzivatelske_rozhrani.zobraz_menu()
    try:
        volba_cisla = int(input("\nZadejte číslo volby: "))
    except ValueError:
        print("Zadejte platné číslo.")
        continue

    if volba_cisla == 1:
        uzivatelske_rozhrani.vytvor_pojisteneho()

    elif volba_cisla == 2:
        uzivatelske_rozhrani.vypis_pojistene()

    elif volba_cisla == 3:
        uzivatelske_rozhrani.vyhledej_pojisteneho()

    elif volba_cisla == 4:
        print("Ukončuji program.")
        break

    else:
        print("Neplatná volba, zkuste to znovu.")