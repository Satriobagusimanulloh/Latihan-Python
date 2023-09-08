from abc import ABC, abstractmethod
import math

class BangunRuang(ABC):

    @abstractmethod
    def hitungVolume(self):
        pass

    @abstractmethod
    def hitungLuasPermukaan(self):
        pass