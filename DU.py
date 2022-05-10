veta = input("Zadej vetu: ")
#veta = "HAODF653"
pocetCisel = 0
pocetPismen = 0
pocetZnaku = 0
pocetMezer = 0
seznamCisel = []
seznamPismen = []
seznamZnaku = []
suma = 0
a = set()


for i in veta:
    if i.isdigit():
        seznamCisel.append(i)
        pocetCisel += 1
        suma += int(i)
    elif i.isalpha():
        pocetPismen += 1
    elif i.isspace():
        pocetMezer += 1
    elif not i.isalpha() or not i.isdigit():
        pocetZnaku += 1
a = set()

for pismo in veta:
    seznamPismen.append(pismo)
    item = seznamPismen
for specZnaky in veta:
    if specZnaky.isalnum():
        seznamZnaku.append(specZnaky)
        item = seznamZnaku
for numbs in veta:
    if numbs.isdigit():
        seznamCisel.append(numbs)
        item = seznamCisel
for item in veta:
    a = item
    print(f"{a} = {str(veta.count(item))}")




print(f"pocet cisel  je: {pocetCisel:>5}")
print(f"soucet cisel je: {suma:>5}")
print(f"prumer cisel je: {suma/pocetCisel:>5}")
print(f"seznam cisel ve vete: {seznamCisel}")
print(f"nejmensi cislo je: {min(seznamCisel):>5}")
print(f"nejvetsi cislo je: {max(seznamCisel):>5}")
print(f"pocet pismen je: {pocetPismen:>5}")
print(f"pocet znaku  je: {pocetZnaku:>5}")
print(f"pocet mezer  je: {pocetMezer:>5}")


prvniZnak = veta[0]
posledniZnak = veta[-1]
print(f"prvni znak je: {prvniZnak}")
print(f"posledni znak je: {posledniZnak} ")

