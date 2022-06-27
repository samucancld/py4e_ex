import psycopg2
import psycopg2.extras
#importando las credentiales
from PG_credentials import sql1cred

conn = None
cur = None


try:
    #estableciendo la conexión
    conn = psycopg2.connect(
    host = sql1cred.hostname,
    dbname = sql1cred.database,
    user = sql1cred.username,
    password = sql1cred.pwd,
    port = sql1cred.port_id
    )
    #estableciendo un cursor que retorne diccionarios
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    print('===connection open===')

    #SCRIPT PARA CREAR TABLAS
    c_script = ''' CREATE TABLE IF NOT EXISTS py_tab (
                    id int PRIMARY KEY,
                    name varchar(40) NOT NULL,
                    salary int,
                    dept_id varchar(30)) '''
    #SCRIPT PARA INGRESAR DATOS A UNA TABLA, con placeholders para evitar sql injection
    insert_s = 'INSERT INTO py_tab (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
    #VALORES EN TUPLAS PARA QUE SEAN INMUTABLES
    insert_v = [(1, 'samuca', 1201, 'D1'), (2, 'chuck', 1301, 'D2'), (3, 'emi', 8201, 'sales')]
    #SCRIPT PARA BORRAR TABLAS
    drop_s = 'DROP TABLE IF EXISTS "py_tab";'
    #SCRIPT PARA MOSTRAR TABLAS
    select_s = "SELECT * FROM py_tab;"
    #SCRIPT PARA ACTUALIZAR TABLAS
    update_s = 'UPDATE py_tab SET salary = salary + (salary*0.5)'
    #SCRIPT PARA BORRAR DATOS DE UNA TABLA
    delete_s = 'DELETE FROM py_tab WHERE name = %s'
    delete_v = [('samuca',)]
    
    #CORRIENDO:

    #BORRA LA TABLA SI YA EXISTE
    cur.execute(drop_s)
    #CREA LA TABLA
    cur.execute(c_script)
    #CORRE LOS INSERTS
    for each_value in insert_v:
        cur.execute(insert_s, each_value)
    cur.execute(update_s)
    #CORRE LOS DELETES
    for each_name in delete_v:
        cur.execute(delete_s, each_name)
    #CORRE EL SELECT
    cur.execute(select_s)
    #GUARDA LA SALIDA EN UNA VARIABLE EN FORMA DE DICCIONARIO
    records = cur.fetchall()
    #FORMATEA Y PRESENTA LA DATA
    for each_record in records:
        print(f"{each_record['name']} cobra ${each_record['salary']} working at the {each_record['dept_id']} department")
    #COMMITEA EL CÓDIGO
    conn.commit()
   
except:
    print('===bad connection===')
finally:
    #CIERRA LA CONEXIÓN
    if cur is not None: cur.close()
    if conn is not None: conn.close(), print('===connection closed===')
    

