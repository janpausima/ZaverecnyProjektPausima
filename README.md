# ZaverecnyProjektPausima
Základní verze samostatného projektu "Evidence pojištěnců" v Pythonu.

# Evidence pojištěnců
Jednoduchá konzolová aplikace v Pythonu pro evidenci pojištěných osob.
Tato základní verze projektu byla vytvořena pro dokázání nutného minima znalostí a schopnosti samostatné práce během rekvalifikačního kurzu *Programátor webových aplikací v Pythonu*.

## Popis projektu
Aplikace umožňuje správu seznamu pojištěných osob. Uživatel může přidávat nové pojištěné, vypisovat všechny evidované osoby a vyhledávat konkrétní pojištěné podle jména a příjmení.  
Data jsou uchovávána pouze v paměti po dobu běhu aplikace.

## Funkce
- Přidání nového pojištěného (jméno, příjmení, věk, telefonní číslo)
- Výpis všech pojištěných osob
- Vyhledání pojištěného podle jména a příjmení
- Validace vstupů (např. zákaz prázdných hodnot a číslic ve jméně)
- Upozornění a výzvy uživateli k pokračování

## Struktura projektu
EvidencePojistencu/


main.py/    #spouštěcí soubor aplikace

pojistenec.py/  #třída pro pojištěnou osobu

evidence_pojistenych.py/    #správa kolekce pojištěných

uzivatelske_rozhrani.py/    #uživatelské rozhraní (komunikace s uživatelem)

validace_vstupu.py/ #validace vstupních dat

README.md/  #dokumentace k projektu

## Instalace a spuštění
1. Stáhněte si či naklonujte repozitář:
   git clone https://github.com/janpausima/ZaverecnyProjektPausima
2. Přesuňte se do adresáře projektu:
   cd ZaverecnyProjektPausima
3. Spusťte aplikaci:
   python main.py

## Použité technologie
- Python 3.13
- Standardní knihovny jazyka Python

## Autor
Jan Paušíma (pro *ITnetwork.cz*, 2025)
