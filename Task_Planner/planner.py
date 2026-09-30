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