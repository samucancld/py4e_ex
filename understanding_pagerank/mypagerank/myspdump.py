from Sqlconnector import SQLiteConnector

my_sql_connector = SQLiteConnector()
my_connection = my_sql_connector.connect('oospider')
my_cursor = my_connection.cursor()

my_cursor.execute('''SELECT COUNT(from_id) AS inbound, old_rank, new_rank, id, url 
     FROM Pages JOIN Links ON Pages.id = Links.to_id
     WHERE html IS NOT NULL
     GROUP BY id ORDER BY inbound DESC''')

count = 0
for row in my_cursor :
    if count < 50 : print(row)
    count = count + 1
print(count, 'rows.')
my_cursor.close()
