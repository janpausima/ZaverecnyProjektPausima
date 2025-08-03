
from rozhrani import UzivatelskeRozhrani

rozhrani = UzivatelskeRozhrani()
volba = 0

print("\nEvidence pojištěných")
print("---------------------")

while volba != 4:
    rozhrani.zobraz_menu()
    try:
        volba = int(input("\nZadejte číslo volby: "))
    except ValueError:
        print("Zadejte platné číslo.")
        continue

    if volba == 1:
        rozhrani.vytvor_pojisteneho()

    elif volba == 2:
        rozhrani.vypis_pojistene()

    elif volba == 3:
        rozhrani.vyhledej_pojisteneho()

    elif volba == 4:
        print("Ukončuji program.")
        break

    else:
        print("Neplatná volba, zkuste to znovu.")