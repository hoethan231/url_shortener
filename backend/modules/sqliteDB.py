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
    except Exception as e:
        return print(e)
             
def add_url(db_file, url, alias):     
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        with connection:
            cursor.execute("INSERT INTO urls (url, alias) VALUES (?,?);", (url, alias))
            if alias == "":
                cursor.execute("UPDATE urls SET alias = ? WHERE alias = ''", 
                                (generateHash(url,cursor.execute("SELECT timestamp FROM urls WHERE alias = ''").fetchall()[0][0]),))
    except Exception as e:
        return print(e)
        
def delete_url(db_file, alias):
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        with connection:
            cursor.execute("DELETE FROM urls WHERE alias = ?;", (alias, ))
    except Exception as e:
        return print(e)
        
        
def get_url(db_file, alias):
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        with connection:
            return cursor.execute("SELECT * FROM urls WHERE alias = ?;", (alias, )).fetchall() 
    except Exception as e:
        return print(e)
        
def get_all_urls(db_file):
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        with connection:
            urls = cursor.execute("SELECT * FROM urls;").fetchall()
            output = [{"id": row[0], "url": row[1], "alias": row[2], "timestamp": row[3]} for row in urls]       
            return output 
    except Exception as e:
        return print(e)
        
def already_exist(db_file, alias):
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        with connection:
            return (len(cursor.execute("SELECT * FROM urls WHERE alias = ?", (alias,)).fetchall()) != 0)
    except Exception as e:
        return print(e)
        
def generateHash(url, timestamp):
    
    combined_string = url + timestamp
    return hashlib.sha256(combined_string.encode()).hexdigest()[0:5]


