import os; os.system("cls")

class Matn:
    a = ""
    def salom(self,ism):
        self.a = ism

class Alik(Matn):
    def show(self):
        print(f"salom ==> {self.a}")

s = Alik()
ism = input("ism:  ")
s.salom(ism)
s.show()