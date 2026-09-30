from database import connect_db

conn, cursor = connect_db()

def task_add_db(
        task_name,
        priority,
        due_date,
        due_time
):
    cursor.execute("""
        INSERT INTO tasks (
            task_name, 
            priority,
            due_date,
            due_time,
            status
            )
            VALUES (
                ?, ?, ?, ?, ?
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

task_add_db(
    task_name="Finish MSc",
    priority="High",
    due_date="2027/03/01"
)



