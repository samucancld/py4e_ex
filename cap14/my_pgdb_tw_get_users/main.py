from csv import excel_tab
from logging import exception
from pydoc import replace
from venv import CORE_VENV_DEPS
from hidden import bearer_token
from url_creator import create_url
from bearer_authenticator import bearer_oauth
from connection_establisher import connect_to_endpoint
import os, unidecode

def main():
    url = create_url()
    json_response = connect_to_endpoint(url)

    import psycopg2
    import psycopg2.extras

    from pgconnector import sql1cred

    conn = None
    cur = None

    conn = psycopg2.connect(
    host = sql1cred.hostname,
    dbname = sql1cred.database,
    user = sql1cred.username,
    password = sql1cred.pwd,
    port = sql1cred.port_id
    )

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    print('===connection open===')
    try:
        cur.execute('CREATE TABLE IF NOT EXISTS twitter_acc (arroba VARCHAR(255), name TEXT, descr TEXT, desde int, visitas INTEGER)')
                    
        for each_user in json_response['data']:
            nameotuser = each_user['name']
            arroba = each_user['username']
            description = each_user['description'].replace('\n', ' ').replace('\r', '').rstrip()
            desde = each_user['created_at'][0:4]
            print(f'user: {nameotuser} arroba {arroba} description {description} desde {desde}')
            try:
                cur.execute('SELECT visitas FROM twitter_acc WHERE arroba = %s',(arroba,))
                cvs = cur.fetchone()
                if cvs is None: 
                    cvs = 1
                    insert_s=('INSERT INTO twitter_acc (arroba, name, descr, desde, visitas) values(%s, %s, %s, %s, %s)')
                    insert_v=(arroba, nameotuser, description, desde, cvs)
                    cur.execute(insert_s, insert_v)
                    print('New user:',nameotuser,'count:', cvs)
                else:
                    update_s = ('UPDATE twitter_acc SET visitas = %s WHERE arroba = %s')
                    cvs = int(cvs[0])
                    cvs = cvs + 1
                    print('Updated user',nameotuser, cvs)
                    update_v = (cvs, arroba)
                    cur.execute(update_s, update_v)
                

                conn.commit ()
            except: continue
        print('datos guardados en la base de datos')
        if cur is not None: cur.close()
        if conn is not None: conn.close(), print('===connection closed===')
    except:
        print('==== ERROR ====')

if __name__ == "__main__":
    main()
