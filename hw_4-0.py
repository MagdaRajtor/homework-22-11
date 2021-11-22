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

def szyfruj(tekst):
    s = input("Chcesz użyć szyfru (G)a-de-ry-po-lu-ki, czy (P)o-li-ty-ka-re-nu? ").upper()
    if s == "G":
        szyfr = gadery
    elif s == "P":
        szyfr = ren
    return zamień(tekst, szyfr)

#testy
t1 = "Ala ma kota"
print(szyfruj(t1))
print(szyfruj(szyfruj(t1)))