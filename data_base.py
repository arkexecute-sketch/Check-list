import psycopg2

conn_params = {
    "host": "localhost",
    "database": "checklist_app",
    "user": "postgres",
    "password": "89644583851",
    "port": "5432"
}

try:
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXIST checklists (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXIST tasks (
            id SERIAL PRIMARY KEY,
            checklist_id INTEGER REFERENCES checklists(id) ON DELETE CASCADE,
            description TEXT NOT NULL,
            is_done BOOLEAN DEFAULT FALSE
        );
    """)

    conn.commit()
    print('Таблицы успешно созданы!')

except Exception as e:
    print(f'Ошибка: {e}')
finally:
    if conn:
        cursor.close()
        conn.close()