import json

# one list = one class where the instances are the objects represented as dicts


input = '''[
    { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },
    { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
    }
]'''

info = json.loads(input)
print('User count:', len(info))

for each_freaking_object in info:
    print(f'name is {each_freaking_object["name"]} id is {each_freaking_object["id"]} and x equals {each_freaking_object["x"]}')

