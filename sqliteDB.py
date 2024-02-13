import sqlite3
import hashlib

def create_table(db_file: str):
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        with connection:
            cursor.execute("""CREATE TABLE IF NOT EXISTS urls (
                _id INTEGER PRIMARY KEY,
                url TEXT,
                alias TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP);""")
    except:
        print("some err")
             
def add_url(db_file, url, alias):     
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        with connection:
            cursor.execute("INSERT INTO urls (url, alias) VALUES (?,?);", (url, alias))
    except:
        print("some err")
        
def delete_url(db_file, alias):
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        with connection:
            cursor.execute("DELETE FROM urls WHERE alias = ?;", (alias, ))
    except:
        print("some err")
        
        
def get_url(db_file, alias):
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        with connection:
            return cursor.execute("SELECT * FROM urls WHERE alias = ?;", (alias, )).fetchall() 
    except:
        return print("some err")
        
def get_all_urls(db_file):
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        with connection:
            urls = cursor.execute("SELECT * FROM urls;").fetchall()
            output = [{"id": row[0], "url": row[1], "alias": row[2]} for row in urls]       
            return output 
    except:
        return print("some err")
        
def already_exist(db_file, alias):
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        with connection:
            return (len(cursor.execute("SELECT * FROM urls WHERE alias = ?", (alias,)).fetchall()) != 0)
    except:
        return print("some err:")
        
def generateHash(url, timestamp):
    
    combined_string = url + timestamp
    return hashlib.sha256(combined_string.encode()).hexdigest()[0:5]


