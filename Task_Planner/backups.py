# Database

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

# Planner

from database import connect_db

conn, cursor = connect_db()

def task_add_db(
        task_name,
        priority,
        due_date,
        due_time
):

    cursor.execute(
        """
        INSERT INTO tasks (
            task_name,
            priority,
            due_date,
            due_time,
            status
        )
        VALUES (
            ?,?,?,?,?
        )
    """,
        (
            task_name,
            priority,
            due_date,
            due_time,
            "pending"
        )
    )

    conn.commit()

#task_add_db(
#    task_name="Finish MSC",
#    priority="High",
#    due_date="2026-10-01",
#    due_time="14:00"
#)

def load_tasks():
    cursor.execute("""
    SELECT * FROM tasks
    """)
    rows = cursor.fetchall()

    return rows

rows = load_tasks()
for row in rows:
    print(row)