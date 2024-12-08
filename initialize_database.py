import sqlite3

# Подключение к базе данных
db_path = "output_data/books_database.db"
conn = sqlite3.connect(db_path)

# SQL для создания таблиц
create_tables_sql = """
CREATE TABLE IF NOT EXISTS Books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT,
    Author TEXT,
    Main_Genre TEXT,
    Sub_Genre TEXT,
    Type TEXT,
    Price REAL,
    Rating REAL,
    People_Rated INTEGER,
    URL TEXT
);

CREATE TABLE IF NOT EXISTS Genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT,
    Number_Of_SubGenres INTEGER,
    URL TEXT
);

CREATE TABLE IF NOT EXISTS SubGenres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT,
    Main_Genre TEXT,
    No_Of_Books INTEGER,
    URL TEXT
);
"""

# Выполнение SQL
with conn:
    conn.executescript(create_tables_sql)

print("Таблицы успешно созданы.")
