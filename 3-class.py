import os ; os.system("cls")

class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
        self.baholar = []

    def baho(self, baho):
        self.baholar.append(baho)

    def malumotlar(self):
        print(f"ismi: {self.ism}")
        print(f"yoshi: {self.yosh}")
        print(f"bahosi: {self.baholar}")

talaba1 = Talaba("Olim", 23)
talaba1.baho(3)
talaba1.baho(2)
talaba1.malumotlar()
print()
talaba2 = Talaba("qochqarbek", 21)
talaba2.baho(5)
talaba2.baho(4)
talaba2.malumotlar()