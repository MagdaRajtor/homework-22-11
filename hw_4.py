gadery = {"g": "a", "d": "e", "r": "y", "p": "o", "l": "u", "k": "i"}
ren = {"p": "o", "l": "i", "t": "y", "k": "a", "r": "e", "n": "u"}

def zamień(tekst, szyfr):
    wyn = ""
    for znak in tekst.lower():
        #jest w kluczach
        if znak in szyfr:
            kod = szyfr[znak]
        else:
            #jest w wartościach
            for l1, l2 in szyfr.items():
                if znak == l2:
                    kod = l1
                    break
                #nie ma w słowniku
                kod = znak
        wyn += kod
    return wyn

def stwórz():
    wyn = {}
    szyfr = input("Podaj swój szyfr (po 2 litery oddzielone myślnikami): ").lower()
    for fragment in szyfr.split("-"):
        if fragment[0] not in wyn and fragment[0] not in wyn.values() and fragment[1] not in wyn.values():
            wyn[fragment[0]] = fragment[1]
        else:
            return "Szyfr nie jest jednoznaczny!"
    return wyn

def szyfruj(tekst):
    s = input("Chcesz użyć szyfru (G)a-de-ry-po-lu-ki, (P)o-li-ty-ka-re-nu?, czy (W)łasnego? ").upper()
    if s == "G":
        szyfr = gadery
    elif s == "P":
        szyfr = ren
    elif s == "W":
        szyfr = stwórz()
    return zamień(tekst, szyfr)

#testy
t1 = "Ala ma kota"
s1 = "MA-LI-NO-WE-BU-TY"
print(szyfruj(t1))
print(szyfruj(szyfruj(t1)))
