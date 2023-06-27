import sqlite3

db = "../insta_database.db"

def newuser(username):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    # Verificar si el usuario ya existe
    cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("El usuario ya existe.")
        return

    # Insertar el nuevo usuario en la base de datos
    cursor.execute("INSERT INTO Users (username) VALUES (?)", (username,))
    conn.commit()

    print("Usuario agregado correctamente.")

    conn.close()


def seeusers():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()

    conn.close()

    return users


def newPersonalUser(username, password, cookie):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    # Verificar si el usuario ya existe
    cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("El usuario ya existe.")
        user_id = existing_user[0]
    else:
        newuser(username)
        cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
        existing_user = cursor.fetchone()
        user_id = existing_user[0]

    # Insertar el nuevo usuario personal en la base de datos
    cursor.execute("INSERT INTO PersonalUsers (id, password, cookie) VALUES (?,?,?)", (user_id, password, cookie))
    conn.commit()

    print("Usuario personal agregado correctamente.")

    conn.close()


def seepersonalusers():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM PersonalUsers")
    personal_users = cursor.fetchall()

    conn.close()

    return personal_users


def newphoto(description, history, hashtags, url):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    # Insertar la nueva foto en la base de datos
    cursor.execute("INSERT INTO Photos (description, history, hastags, url) VALUES (?,?,?,?)",
                   (description, history, hashtags, url))
    conn.commit()

    print("Foto agregada correctamente.")

    conn.close()


def seephotos():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Photos")
    photos = cursor.fetchall()
    conn.close()
    return photos

   
