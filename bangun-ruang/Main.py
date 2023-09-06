from abc import ABC, abstractclassmethod
import math

class BangunRuang(ABC):

    def __init__(self,inputRusuk, inputPanjang, inputLebar, inputTinggi, inputJari):
        self.rusuk = inputRusuk
        self.panjang = inputPanjang
        self.lebar = inputLebar
        self.tinggi = inputTinggi
        self.jari = inputJari


    @abstractclassmethod
    def hitungVolume(self):
        pass

    @property
    @abstractclassmethod
    def rusuk(self):
        pass

    @property
    @abstractclassmethod
    def panjang(self):
        pass

    @property
    @abstractclassmethod
    def lebar(self):
        pass

    @property
    @abstractclassmethod
    def tinggi(self):
        pass

    @property
    @abstractclassmethod
    def jari(self):
        pass


class Kubus(BangunRuang):

    def __init__(self, inputRusuk):
        super().__init__(inputRusuk, 0, 0, 0, 0)
    
    def hitungVolume(self):
        return (self.rusuk**3)

    @BangunRuang.rusuk.setter
    def rusuk(self, inputRusuk):
        self.__rusuk = inputRusuk

    @rusuk.getter
    def rusuk(self):
        return self.__rusuk
    
    @BangunRuang.panjang.setter
    def panjang(self, inputPanjang):
        self.__panjang = inputPanjang

    @panjang.getter
    def panjang(self):
        return self.__panjang
    
    @BangunRuang.lebar.setter
    def lebar(self, inputLebar):
        self.__lebar = inputLebar

    @lebar.getter
    def lebar(self):
        return self.__lebar
    
    @BangunRuang.tinggi.setter
    def tinggi(self, inputTinggi):
        self.__tinggi = inputTinggi

    @tinggi.getter
    def tinggi(self):
        return self.__tinggi
    
    @BangunRuang.jari.setter
    def jari(self, inputJari):
        self.__jari = inputJari

    @jari.getter
    def jari(self):
        return self.__jari
    

class Balok(BangunRuang):

    def __init__(self, inputPanjang, inputLebar, inputTinggi):
        super().__init__(0, inputPanjang, inputLebar, inputTinggi, 0)

    def hitungVolume(self):
        return (self.panjang * self.lebar * self.tinggi)

    @BangunRuang.rusuk.setter
    def rusuk(self, inputRusuk):
        self.__rusuk = inputRusuk

    @rusuk.getter
    def rusuk(self):
        return self.__rusuk
    
    @BangunRuang.panjang.setter
    def panjang(self, inputPanjang):
        self.__panjang = inputPanjang

    @panjang.getter
    def panjang(self):
        return self.__panjang
    
    @BangunRuang.lebar.setter
    def lebar(self, inputLebar):
        self.__lebar = inputLebar

    @lebar.getter
    def lebar(self):
        return self.__lebar
    
    @BangunRuang.tinggi.setter
    def tinggi(self, inputTinggi):
        self.__tinggi = inputTinggi

    @tinggi.getter
    def tinggi(self):
        return self.__tinggi
    
    @BangunRuang.jari.setter
    def jari(self, inputJari):
        self.__jari = inputJari

    @jari.getter
    def jari(self):
        return self.__jari
    

class Bola(BangunRuang):

    def __init__(self, inputJari):
        super().__init__(0, 0, 0, 0, inputJari)

    def hitungVolume(self):
        return (4/3 * math.pi * self.jari**3)

    @BangunRuang.rusuk.setter
    def rusuk(self, inputRusuk):
        self.__rusuk = inputRusuk

    @rusuk.getter
    def rusuk(self):
        return self.__rusuk
    
    @BangunRuang.panjang.setter
    def panjang(self, inputPanjang):
        self.__panjang = inputPanjang

    @panjang.getter
    def panjang(self):
        return self.__panjang
    
    @BangunRuang.lebar.setter
    def lebar(self, inputLebar):
        self.__lebar = inputLebar

    @lebar.getter
    def lebar(self):
        return self.__lebar
    
    @BangunRuang.tinggi.setter
    def tinggi(self, inputTinggi):
        self.__tinggi = inputTinggi

    @tinggi.getter
    def tinggi(self):
        return self.__tinggi
    
    @BangunRuang.jari.setter
    def jari(self, inputJari):
        self.__jari = inputJari

    @jari.getter
    def jari(self):
        return self.__jari
    

class Tabung(BangunRuang):

    def __init__(self,inputTinggi, inputJari):
        super().__init__(0, 0, 0, inputTinggi, inputJari)

    def hitungVolume(self):
        return (math.pi * (self.jari**2) * self.tinggi)

    @BangunRuang.rusuk.setter
    def rusuk(self, inputRusuk):
        self.__rusuk = inputRusuk

    @rusuk.getter
    def rusuk(self):
        return self.__rusuk
    
    @BangunRuang.panjang.setter
    def panjang(self, inputPanjang):
        self.__panjang = inputPanjang

    @panjang.getter
    def panjang(self):
        return self.__panjang
    
    @BangunRuang.lebar.setter
    def lebar(self, inputLebar):
        self.__lebar = inputLebar

    @lebar.getter
    def lebar(self):
        return self.__lebar
    
    @BangunRuang.tinggi.setter
    def tinggi(self, inputTinggi):
        self.__tinggi = inputTinggi

    @tinggi.getter
    def tinggi(self):
        return self.__tinggi
    
    @BangunRuang.jari.setter
    def jari(self, inputJari):
        self.__jari = inputJari

    @jari.getter
    def jari(self):
        return self.__jari
    

class Kerucut(BangunRuang):

    def __init__(self,inputTinggi, inputJari):
        super().__init__(0, 0, 0, inputTinggi, inputJari)

    def hitungVolume(self):
        return (1/3 * math.pi * (self.jari**2) * self.tinggi)

    @BangunRuang.rusuk.setter
    def rusuk(self, inputRusuk):
        self.__rusuk = inputRusuk

    @rusuk.getter
    def rusuk(self):
        return self.__rusuk
    
    @BangunRuang.panjang.setter
    def panjang(self, inputPanjang):
        self.__panjang = inputPanjang

    @panjang.getter
    def panjang(self):
        return self.__panjang
    
    @BangunRuang.lebar.setter
    def lebar(self, inputLebar):
        self.__lebar = inputLebar

    @lebar.getter
    def lebar(self):
        return self.__lebar
    
    @BangunRuang.tinggi.setter
    def tinggi(self, inputTinggi):
        self.__tinggi = inputTinggi

    @tinggi.getter
    def tinggi(self):
        return self.__tinggi
    
    @BangunRuang.jari.setter
    def jari(self, inputJari):
        self.__jari = inputJari

    @jari.getter
    def jari(self):
        return self.__jari
    

class Limas(BangunRuang):

    def __init__(self,inputPanjang, inputLebar, inputTinggi):
        super().__init__(0, inputPanjang, inputLebar, inputTinggi, 0)

    def hitungVolume(self):
        return (1/3 * (self.panjang * self.lebar) * self.tinggi)

    @BangunRuang.rusuk.setter
    def rusuk(self, inputRusuk):
        self.__rusuk = inputRusuk

    @rusuk.getter
    def rusuk(self):
        return self.__rusuk
    
    @BangunRuang.panjang.setter
    def panjang(self, inputPanjang):
        self.__panjang = inputPanjang

    @panjang.getter
    def panjang(self):
        return self.__panjang
    
    @BangunRuang.lebar.setter
    def lebar(self, inputLebar):
        self.__lebar = inputLebar

    @lebar.getter
    def lebar(self):
        return self.__lebar
    
    @BangunRuang.tinggi.setter
    def tinggi(self, inputTinggi):
        self.__tinggi = inputTinggi

    @tinggi.getter
    def tinggi(self):
        return self.__tinggi
    
    @BangunRuang.jari.setter
    def jari(self, inputJari):
        self.__jari = inputJari

    @jari.getter
    def jari(self):
        return self.__jari
    

class Prisma(BangunRuang):

    def __init__(self,inputPanjang, inputLebar, inputTinggi):
        super().__init__(0, inputPanjang, inputLebar, inputTinggi, 0)

    def hitungVolume(self):
        return (1/2 * (self.panjang * self.lebar * self.tinggi))

    @BangunRuang.rusuk.setter
    def rusuk(self, inputRusuk):
        self.__rusuk = inputRusuk

    @rusuk.getter
    def rusuk(self):
        return self.__rusuk
    
    @BangunRuang.panjang.setter
    def panjang(self, inputPanjang):
        self.__panjang = inputPanjang

    @panjang.getter
    def panjang(self):
        return self.__panjang
    
    @BangunRuang.lebar.setter
    def lebar(self, inputLebar):
        self.__lebar = inputLebar

    @lebar.getter
    def lebar(self):
        return self.__lebar
    
    @BangunRuang.tinggi.setter
    def tinggi(self, inputTinggi):
        self.__tinggi = inputTinggi

    @tinggi.getter
    def tinggi(self):
        return self.__tinggi
    
    @BangunRuang.jari.setter
    def jari(self, inputJari):
        self.__jari = inputJari

    @jari.getter
    def jari(self):
        return self.__jari