import json

#just one dict -- just one "object"

data = '''{
    "name" : "Chuck",
    "phone" : {
        "type": "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    },
    "perros" : {
        "raza" : "cuzco",
        "cantidad" : 45
    }
}'''

info = json.loads(data)
print(info)
print(type(info))
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
print(f'Perros: {info["perros"]["cantidad"]} {info["perros"]["raza"]}s')