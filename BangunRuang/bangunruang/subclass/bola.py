from bangunruang.abstract import BangunRuang
import math

class Bola(BangunRuang):

    def __init__(self, jari):
        self.jari = jari

    def hitungVolume(self):
        return (4/3 * math.pi * (self.jari ** 3))

    def hitungLuasPermukaan(self):
        return (4 * math.pi * (self.jari * self.jari))
    
    def setJari(self, inputJari):
        self.jari = inputJari

    def getJari(self):
        return self.jari