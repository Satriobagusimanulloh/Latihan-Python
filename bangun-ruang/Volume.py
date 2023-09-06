from Main import BangunRuang, Kubus, Balok, Bola, Tabung, Kerucut, Limas, Prisma

kubus1 = Kubus(10)
print(f"Panjang rusuk kubus\t: {kubus1.rusuk}")
print(f"Volume kubus\t\t: {kubus1.hitungVolume()}")

balok1 = Balok(8, 6, 5)
print(f"Panjang panjang balok\t: {balok1.panjang}")
print(f"Panjang lebar balok\t: {balok1.lebar}")
print(f"Panjang tinggi balok\t: {balok1.tinggi}")
print(f"Volume balok\t\t: {balok1.hitungVolume()}")

bola1 = Bola(20)
print(f"Jari-jari bola\t\t: {bola1.jari}")
print(f"Volume bola\t\t: {bola1.hitungVolume()}")

tabung1 = Tabung(30, 10)
print(f"Tinggi tabung\t\t: {tabung1.tinggi}")
print(f"Jari-jari tabung\t: {tabung1.jari}")
print(f"Volume tabung\t\t: {tabung1.hitungVolume()}")

kerucut1 = Kerucut(30, 10)
print(f"Tinggi kerucut\t\t: {kerucut1.tinggi}")
print(f"Jari-jari kerucut\t: {kerucut1.jari}")
print(f"Volume kerucut\t\t: {kerucut1.hitungVolume()}")

limas1 = Limas(10, 10, 15)
print(f"Panjang limas\t\t: {limas1.panjang}")
print(f"Lebar limas\t\t: {limas1.lebar}")
print(f"Tinggi limas\t\t: {limas1.tinggi}")
print(f"Volume limas\t\t: {limas1.hitungVolume()}")

prisma1 = Prisma(3, 5, 10)
print(f"Panjang prisma\t\t: {prisma1.panjang}")
print(f"Lebar prisma\t\t: {prisma1.lebar}")
print(f"Tinggi prisma\t\t: {prisma1.tinggi}")
print(f"Volume prisma\t\t: {prisma1.hitungVolume()}")