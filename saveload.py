import json
dota = {}
def read():
    global dota
    with open('data.json', 'r', encoding='utf-8') as f:
        dota = json.load(f)

def save():
    global dota
    with open('data.json', 'w', ) as f:
        json.dump(dota, f, indent=4)