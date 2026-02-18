import sqlite3
from typing import Optional, List, Dict, Any

DB_NAME = "" # Any string


def get_connection_template() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_NAME) # Can create param
    conn.row_factory = sqlite3.Row
    return conn


def init_db_template():
    # create_tables_sql = """
    #   -- Таблица пользователей
    #   CREATE TABLE IF NOT EXISTS users (
    #       id INTEGER PRIMARY KEY AUTOINCREMENT,
    #       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    #   );
    #   """
    # conn = get_connection()
    # try:
    #     cursor = conn.cursor()
    #     cursor.executescript(create_tables_sql)
    #     conn.commit()
    #     print("[SUCCESS] База данных инициализирована. Таблицы созданы.")
    # except sqlite3.Error as e:
    #     print(f"[ERROR] Ошибка при создании таблиц: {e}")
    # finally:
    #     conn.close()
    pass


def insert_method_template():
    # conn = get_connection()
    # try:
    #     cursor = conn.cursor()
    #     cursor.execute(
    #         """
    #         INSERT INTO sessions (user_id, title, parent_session_id)
    #         VALUES (?, ?, ?)
    #         """,
    #         (user_id, title, parent_session_id)
    #     )
    #     session_id = cursor.lastrowid
    #     conn.commit()
    #     print(f"[INFO] Данные внесены")
    #     return session_id
    # except sqlite3.Error as e:
    #     print(f"[ERROR] Ошибка при создании сессии: {e}")
    #     return -1
    # finally:
    #     conn.close()
    pass


def get_last_row_template():
    # conn = get_connection()
    # try:
    #     cursor = conn.cursor()
    #     cursor.execute(
    #         """
    #         SELECT id, title, parent_session_id, created_at, updated_at
    #         FROM sessions
    #         WHERE user_id = ?
    #         ORDER BY created_at DESC
    #         LIMIT 1
    #         """,
    #         (user_id,)
    #     )
    #     row = cursor.fetchone()
    #     return dict(row) if row else None
    # except sqlite3.Error as e:
    #     print(f"[ERROR] Ошибка при получении сессии: {e}")
    #     return None
    # finally:
    #     conn.close()
    pass


if __name__ == "__main__":
    init_db_template()

