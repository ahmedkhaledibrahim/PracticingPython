from collections import Counter, defaultdict

import intersection

my_artists = {"Sarah Brightman", "Guns N' Roses",
"Opeth", "Vixy and Tony"}
auburns_artists = {"Nickelback", "Guns N' Roses",
"Savage Garden"}

new_set = my_artists.symmetric_difference(auburns_artists)


dict1 = {
    "city":"cairo",
    "name":"ahmed",
    "age":21,
    "job":"SD",
    "nationality":"German"
}
my_name = ["ahmed","khaled","ibrahim","khaled","ahmed"]

frq = dict1.setdefault("city","cairo2")

frequencies = defaultdict(int)

frequencies["one"] = 1

user_nationality = dict1.__setitem__("nationality","Egyptian")
print(dict1.items())
def checkforvalue(val:str,dic:dict):
    if val in dic.values():
        return True
    return False

if type(dict1) is dict:
    print("trues")