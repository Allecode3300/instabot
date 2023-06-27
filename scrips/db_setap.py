import sqlite3

# Crear o conectar a la base de datos
db = "../insta_database.db"
conn = sqlite3.connect(db)

# Crear el cursor
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

conn.commit()
conn.close()
