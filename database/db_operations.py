import sqlite3

def create_connection():
    conn = sqlite3.connect("data.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            email TEXT,
            plz TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_person(data):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO persons (first_name, email, plz)
        VALUES (?, ?, ?)
    """, (
        data.get("first_name"),
        data.get("email"),
        data.get("plz")
    ))

    conn.commit()
    conn.close()
def get_all_persons():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM persons")
    rows = cursor.fetchall()

    conn.close()
    return rows
