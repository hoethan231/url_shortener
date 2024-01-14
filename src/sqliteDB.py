import sqlite3

connection = sqlite3.connect("../database.db")

def create_table():
    with connection:
        connection.execute("""CREATE TABLE urls (
            _id INTEGER PRIMARY KEY,
            url TEXT,
            alias TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);""")
        
def add_url(url, alias):
    with connection:
        connection.execute("INSERT INTO urls (url, alias) VALUES (?,?);", (url, alias))
        
def delete_url(url):
    with connection:
        connection.execute("DELETE FROM urls WHERE url = ?;", (url, ))
        
def get_url(alias):
    with connection:
        return connection.execute("SELECT * FROM urls WHERE alias = ?;", (alias, )).fetchall()
        
def get_all_urls():
    with connection:
        return connection.execute("SELECT * FROM urls;").fetchall()
    
