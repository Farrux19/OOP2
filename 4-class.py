import os;os.system("cls")

class Kino:
    def __init__(self, kino, muallif, yil):
        self.kino = kino
        self.muallif = muallif
        self.yil = yil

    def malumot(self):
        print(f"kino: {self.kino}")
        print(f"Muallif: {self.muallif}")
        print(f"Yil: {self.yil}")

kino1 = Kino("Qaynona kelin", "Axat Qayum", 2024)
kino2 = Kino("ogay ona", "Axat Qayum", 2023)

kino1.malumot()
print()
kino2.malumot()
