"""
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
"""

gender = input("Anna sukupuolesi (n tai m):\n")
hgb = float(input("Anna hemoglobiiniarvosi: "))

if ((gender == "n") & (117<hgb<175)) or ((gender == "m") & (134<hgb<195)):
    print("Hemoglobiiniarvosi on normaali.")
elif ((gender == "n") & (hgb<117)) or ((gender == "m") & (hgb<134)):
    print("Hemoglobiiniarvosi on alhainen.")
elif ((gender == "n") & (hgb>175)) or ((gender == "m") & (hgb>195)):
    print("Hemoglobiiniarvosi on korkea.")