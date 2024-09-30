import json
import os
os.system("cls")

ls = {
    "ism": "ali",
    "yosh": 24,
    "adres": "mars"
}
d = json.dumps(ls)
print(d)