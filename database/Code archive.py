import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

"""
Создание архива
"""

def connect():
    conn =sqlite3.connect('archive.db')
    cur =conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS archive (meal TEXT, date TEXT,name TEXT,g INT,kkal INT,p INT,f INT ,c INT)''')
    conn.commit()
    conn.close()
