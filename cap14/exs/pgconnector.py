from dataclasses import dataclass
import json

@dataclass
class Credentials:
    hostname: str
    database: str
    username: str
    pwd: str
    port_id: str

fhandler = open('pgcredentials.json')
jsonstr = fhandler.read()
parsedjson = json.loads(jsonstr)
# print(json.dumps(parsedjson, indent=4))

sql1cred = Credentials(
    hostname = parsedjson['results'][0]['credentials'][0]['hostname'],
    database = parsedjson['results'][0]['credentials'][0]['database'],
    username = parsedjson['results'][0]['credentials'][0]['username'],
    pwd = parsedjson['results'][0]['credentials'][0]['pwd'],
    port_id = parsedjson['results'][0]['credentials'][0]['port_id']
    )
