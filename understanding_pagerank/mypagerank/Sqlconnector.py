import sqlite3

class SQLiteConnector:
    def __init__(self) -> None:
        pass

    def connect(self, dbname):
        conn = sqlite3.connect(f'{dbname}.sqlite')
        return conn
