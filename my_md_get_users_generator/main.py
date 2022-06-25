from hidden import bearer_token
from url_creator import create_url
from bearer_authenticator import bearer_oauth
from connection_establisher import connect_to_endpoint

import os, unidecode
'''samucaa'''
def main():
    url = create_url()
    json_response = connect_to_endpoint(url)
    #print(json.dumps(json_response, indent=4, sort_keys=True))
    try:
        print('========= TU CONSULTA FUE ALMACENADA EN <twitter.md> ! ==========')
        tabla = '| Nombre | @ | Descripción | En Twitter desde |\n|--------|---|-------------|------------------\n'

        for each_user in json_response['data']:
            nameotuser = each_user['name']
            arroba = each_user['username']
            description = each_user['description'].replace('\n', ' ').replace('\r', '').rstrip()
            desde = each_user['created_at'][0:4]
            tabla = tabla + f'|{nameotuser}|{arroba}|{description}|{desde}|\n'
            
        tabla = unidecode.unidecode(tabla)
        file_handler = open('twitter.md','w')
        file_handler.write(tabla)
    except:
        print('==== ERROR ====')

if __name__ == "__main__":
    main()
