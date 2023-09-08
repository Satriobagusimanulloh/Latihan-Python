from bangunruang.abstract import BangunRuang

class Balok(BangunRuang):
    
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        
    def hitungVolume(self):
        return (self.panjang * self.lebar * self.tinggi)

    def hitungLuasPermukaan(self):
        return (2 * (self.panjang * self.lebar + self.lebar * self.tinggi + self.panjang * self.tinggi))
    
    def setPanjang(self, inputPanjang):
        self.panjang = inputPanjang
    
    def setLebar(self, inputLebar):
        self.lebar = inputLebar

    def setTinggi(self, inputTinggi):
        self.tinggi = inputTinggi

    def getPanjang(self):
        return self.panjang
    
    def getLebar(self):
        return self.lebar

    def getTinggi(self):
        return self.tinggi