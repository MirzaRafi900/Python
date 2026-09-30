import sqlite3

def connect_db():
    conn = sqlite3.connect('Planner.db')

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL,
        priority TEXT NOT NULL,
        due_date TEXT,
        due_time TEXT,
        status TEXT
    )
    
    """)

    conn.commit()

    return conn, cursor

# outside Function
conn, cursor = connect_db()
print("Database Connected Successfully")

