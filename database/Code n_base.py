import sqlite3

"""
Создание базы данных
"""

def connect():
    conn =sqlite3.connect('n_base.db')
    cur =conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS n_base (name TEXT,g INT,kkal INT,p INT,f INT ,c INT)''')
    conn.commit()
    conn.close()
