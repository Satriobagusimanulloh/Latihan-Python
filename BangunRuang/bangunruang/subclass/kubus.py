from bangunruang.abstract import BangunRuang

class Kubus(BangunRuang):

    def __init__(self, sisi):
        self.sisi = sisi

    def hitungVolume(self):
        return (self.sisi ** 3)

    def hitungLuasPermukaan(self):
        return (6 * (self.sisi * self.sisi))
    
    def setSisi(self, inputSisi):
        self.sisi = inputSisi

    def getSisi(self):
        return self.sisi