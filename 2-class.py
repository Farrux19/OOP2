import os ; os.system("cls")

class Hayvon:
    def __init__(self, ism, turi, ovoz):
        self.ism = ism
        self.turi = turi
        self.ovoz = ovoz

    def it(self):
        print(f"Hayvon: {self.turi} 🐶")
        print(f"ismi: {self.ism}")
        print(f"Ovoz: {self.ovoz} 🔊")

hayvon2 = Hayvon("reks", "it", "vov")
hayvon2.it()