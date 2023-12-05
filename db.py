import sqlite3
from icecream import ic

DB_NAME = "server_inventory.db"

def db_connect():
    return sqlite3.connect(DB_NAME)

def create_db():
    conn = db_connect()
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS servers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        ip_address TEXT NOT NULL,
        os TEXT NOT NULL,
        status TEXT NOT NULL
    )
    '''

    cursor.execute(create_table_query)
    conn.commit()
    conn.close()
    

def insert_server(name, ip_address, os, status):
    conn = db_connect()
    cursor = conn.cursor()
    
    insert_query = "INSERT INTO servers (name, ip_address, os, status) VALUES (?,?,?,?)"
    cursor.execute(insert_query, (name, ip_address, os, status))
    
    conn.commit()
    conn.close()
    

def get_all_servers():
    conn = db_connect()
    cursor = conn.cursor()
    
    query = "SELECT * FROM servers"
    cursor.execute(query)
    servers = cursor.fetchall()
    
    conn.close()
    return servers


def update_server_status(server_id, new_status):
    conn = db_connect()
    cursor = conn.cursor()
    
    query = "UPDATE servers SET status = ? WHERE id = ?"
    cursor.execute(query, (new_status, server_id))
    
    conn.commit()
    conn.close()
    

def delete_server(server_id):
    conn = db_connect()
    cursor = conn.cursor()
    
    query = "DELETE FROM servers WHERE id = ?"
    cursor.execute(query, (server_id,))
    
    conn.commit()
    conn.close()
    
    
create_db()

insert_server("Web Server", "162.168.1.100", "Ubuntu", "active")
insert_server("DB Server", "162.168.1.101", "Debian", "active")

servers = get_all_servers()
for server in servers:
    ic("Server: ", server)
    
update_server_status(1, "offline")

delete_server(2)

servers = get_all_servers()
for server in servers:
    ic("Server: ", server)