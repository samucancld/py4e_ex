import psycopg2
import psycopg2.extras
#importando las credentiales
from pgconnector import sql1cred

conn = None
cur = None


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

    

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = %s ', (email,))
    row = cur.fetchone()
    #print(row)
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (%s, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = %s',
                    (email,))
    conn.commit()


# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC'

cur.execute(sqlstr)
records = cur.fetchall()
#print(records)

for row in records:
    print(str(row[0]), row[1])

if cur is not None: cur.close()
if conn is not None: conn.close(), print('===connection closed===')
    











