Brus = 24.90
Smørbrød = 45
Banan = 8.50

totalsum = Brus + Smørbrød + Banan
print("Totalsum:", totalsum)

mva = totalsum * 1.25
print("Totalsum med 25% mva:", mva)

per_person = totalsum / 4
print("Totalsum pris per person:", per_person)

prisforskjell = max(Brus, Smørbrød, Banan) - min(Brus, Smørbrød, Banan)
print("Prisforskjell:", prisforskjell)


# --- Refleksjon ---
# Vi fikk ikke i oppgave å legge sammen variablene smørbrød og brus.
# Da jeg delte totalsum på fire, fikk jeg datatypen float. Men svaret kunne like gjerne 
# vært et heltall, altså datatype integer.
# Det er enklere å bytte prisene på produktene. I tillegg er det enklere å huske
# variabelen enn desimaltallene.

