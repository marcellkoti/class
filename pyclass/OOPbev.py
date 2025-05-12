class Diak:
    def __init__(self,_nev,_ota):
        self._nev = _nev
        self._ota = _ota

   

    def getNev(self):
        return self.nev    


    def getOta(self):
        return self.okatzon
    
    def setOta(self,_ota):
        self.oktazon=_ota

    

    def Kiir(self):
        print("A nevem",self.nev)
        print("Oktatási azonosítóm",self.oktazon)
        




""""
Gz = Diak()
Gz.nev = "Tóth Géza"
Gz.oktazon = "123456789"
print(Gz.nev)
"""

Gz = Diak("Tóth Géza","123456789")
Bl = Diak("kiss Béla","987654321")
Mt = Diak("Cserepes Márta", "564312789")
Mcs = Diak("Elek Marcsi","")
print(Gz.getNev())
Gz.Kiir()
Gz.setOta("123456789")
Gz.Kiir()
Bl.Kiir()
Mt.Kiir()
Mcs.Kiir()
