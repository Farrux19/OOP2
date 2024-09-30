import json
import os
os.system("cls")

ls = {
    "ism": "ali",
    "yosh": 24,
    "adres": "mars"
}

d = json.loads(ls,indent=4)

print(d)