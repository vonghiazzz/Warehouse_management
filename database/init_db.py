import sqlite3
from database.database import get_connection

def init_db():
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        with open("database/schema.sql", "r", encoding="utf-8") as f:
            schema = f.read()

        cursor.executescript(schema)
        conn.commit()
        print("✅ Database initialized successfully.")

    except sqlite3.Error as e:
        print("❌ Lỗi khi tạo bảng:", e)

    finally:
        if conn:
            conn.close()
