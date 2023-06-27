import sqlite3
import argparse

# Crear o conectar a la base de datos
db = "../insta_database.db"

parser = argparse.ArgumentParser(description='Configura la base de datos.')
parser.add_argument('-s', '--start', action='store_true', help='Inicia la base de datos')
parser.add_argument('-t', '--test', action='store_true', help='Agrega datos para prueba')
parser.add_argument('-x', '--txt', action='store_true', help='Llena base de datos desde un .txt')
args = parser.parse_args()

if args.txt:
    fichero = open(input("Cual es el nombre del archivo: "))
    

if args.start:
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    # Eliminar las tablas si ya existen
    cursor.execute('DROP TABLE IF EXISTS Users')
    cursor.execute('DROP TABLE IF EXISTS PersonalUsers')
    cursor.execute('DROP TABLE IF EXISTS Photos')

    # Crear la tabla de Users
    cursor.execute('''
    CREATE TABLE Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT
    );
    ''')

    # Crear la tabla de PersonalUsers
    cursor.execute('''
    CREATE TABLE PersonalUsers (
        id INTEGER PRIMARY KEY,
        password TEXT NOT NULL,
        cookie TEXT,
        FOREIGN KEY(id) REFERENCES Users(id)
    );
    ''')

    # Crear la tabla de Photos
    cursor.execute('''
    CREATE TABLE Photos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        history INTEGER ,
        hastags TEXT,
        url TEXT
    );
    ''')
    cursor.execute("INSERT INTO Users (username) VALUES (?)", ("keytr",))

    conn.commit()
    conn.close()

