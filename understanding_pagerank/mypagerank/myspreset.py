from Sqlconnector import SQLiteConnector

my_sql_connector = SQLiteConnector()
my_connection = my_sql_connector.connect('oospider')
my_cursor = my_connection.cursor()


my_cursor.execute('''UPDATE Pages SET new_rank=1.0, old_rank=0.0''')
my_connection.commit()

my_cursor.close()

print("All pages set to a rank of 1.0")
