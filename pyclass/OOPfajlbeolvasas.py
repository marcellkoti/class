class Szavazatok:
    def __init__(self,korzet,szavazat,jeloltek,part):
        self.korzet = int(korzet)
        self.szavazat = int(szavazat)
        self.jeloltek = (jeloltek)
        self.part = part
        
    def __str__(self):
        return f"{self.korzet}, {self.szavazat}, {self.jeloltek}, {self.part}"

def Beolvasas(fajlnev):
    szavazas = []
    try:
        with open(fajlnev,"rt",encoding="utf-8") as file:
            next(file)
            for sor in file:
                if sor.strip():
                    adat = sor.strip().split(" ")
                    print(f"Beolvasott adatok: {adat}")
                    if len(adat) == 4:
                        try:
                            korzet,szavazat,jeloltek,part = adat
                            szavazas.append(Szavazatok(korzet,szavazat,jeloltek,part))
                        except ValueError:
                            print("Hibás adatsor")
                    else:
                        print("Hibás adatsor")
    except FileNotFoundError:
        print("A fájl nem lett megadva")
        return []
    return szavazas

szavazas = Beolvasas("szavazatok.txt")
for szavazat in szavazas:
    print(f"Körzet :{szavazat.korzet}, Szavazat: {szavazat.szavazat}, Jelöltek: {szavazat.jeloltek}, Párt: {szavazat.part}")



