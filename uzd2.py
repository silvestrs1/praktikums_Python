""" 
Uzrakstiet programmu, kas ielasa vienu vārdu 
un izvada uz ekrāna sveicienu sekojošā formātā:
"Labdien, vards, pimrdienā!"
Ja ievadīts nav jūsu vards, tiek izdrukāts teksts - Uzredzēšanos!
Pārbaudiet programmas darbību ar dažādiem ievaddatiem.
"""
vards=input("Ievadi vārdu:  ")
if vards=="Silvestrs":
    print("Labdien,"+vards+", pirmdienā!")
else:
    print("Uzredzēšanos")
        