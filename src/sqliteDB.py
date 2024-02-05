import sqlite3

def connect():
    return sqlite3.connect("../database.db")

def create_table():
    connection = connect()
    with connection:
        connection.execute("""CREATE TABLE IF NOT EXISTS urls (
            _id INTEGER PRIMARY KEY,
            url TEXT,
            alias TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);""")
        
        
def add_url(url, alias):
    connection = connect()
    with connection:
        connection.execute("INSERT INTO urls (url, alias) VALUES (?,?);", (url, alias))
        
def delete_url(alias):
    connection = connect()
    with connection:
        connection.execute("DELETE FROM urls WHERE alias = ?;", (alias, ))
        
def get_url(alias):
    connection = connect()
    with connection:
        return connection.execute("SELECT * FROM urls WHERE alias = ?;", (alias, )).fetchall()   
        
def get_all_urls():
    connection = connect()
    with connection:
        urls = connection.execute("SELECT * FROM urls;").fetchall()
        output = [{"id": row[0], "url": row[1], "alias": row[2]} for row in urls]       
        return output
    
