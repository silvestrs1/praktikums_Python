"""
    Funkcija Bilde akceptē divus argumentus - skaiļus a un b,
    aprēķina to kubu summu un atgriež to.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem, 
    nosakot trīs simbolus aiz komata.

    Argumenti:
        a {int vai float} -- pirmais skaitlis
        b {int vai float} -- otrais skaitlis
    Atgriež:
        int vai float -- argumentu summa
    
    """
    def bilde (a,b):
        summa=a**3+b**3
        return summa


pirmais=int(input("Ievadi pirmo skaitli: "))
otrais=int(input("Ievadi otri skaitli: "))

aka=bilde(pirmais,otrais)

print("{0:.3f}",format(aka))