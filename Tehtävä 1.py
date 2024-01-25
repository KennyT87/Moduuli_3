"""
Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.
"""

pituus = float(input("Anna kuhan pituus senttimetreinä:\n"))
alamitta = 37

if pituus < alamitta:
    print(f"Kuha on alamittainen, laske se takaisin järveen. Kuha on {(alamitta - pituus):.1f} senttiä liian pieni")
else:
    print("Kuha on tarpeeksi iso että voit pitää sen!")