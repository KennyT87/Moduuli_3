"""
Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
Vuosi on karkausvuosi, jos se on jaollinen neljällä.
Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.
"""
year = int(input("Anna vuosiluku:\n"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year} on karkausvuosi.")
else:
    print(f"{year} ei ole karkausvuosi.")