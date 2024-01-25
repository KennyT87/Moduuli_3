"""
Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
Tehtävässä on käytettävä if/elif/else-toistorakennetta.

LUX on parvekkeellinen hytti yläkannella.
A on ikkunallinen hytti autokannen yläpuolella.
B on ikkunaton hytti autokannen yläpuolella.
C on ikkunaton hytti autokannen alapuolella.
Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.
"""

LUX_dsc = "LUX: Parvekkeellinen hytti yläkannella."
A_dsc = "A: Ikkunallinen hytti autokannen yläpuolella."
B_dsc = "B: Ikkunaton hytti autokannen yläpuolella."
C_dsc = "C: Ikkunaton hytti autokannen alapuolella."

luokka = input("Anna hyttiluokka nähdäksesi kuvauksen (LUX, A, B, C):\n")
if luokka == "LUX":
    print(LUX_dsc)
elif luokka == "A":
    print(A_dsc)
elif luokka == "B":
    print(B_dsc)
elif luokka == "C":
    print(C_dsc)
else:
    print("Virheellinen hyttiluokka.")