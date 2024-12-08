import sqlite3
import pandas as pd

# Пути к данным
db_path = "output_data/books_database.db"
books_path = "data/Books_df.csv"
genres_path = "data/Genre_df.csv"
subgenres_path = "data/Sub_Genre_df.csv"

# Чтение файлов
books_df = pd.read_csv(books_path)
genres_df = pd.read_csv(genres_path)
subgenres_df = pd.read_csv(subgenres_path)

# Подключение к БД
conn = sqlite3.connect(db_path)

# Загрузка данных
books_df.to_sql("Books", conn, if_exists="replace", index=False)
genres_df.to_sql("Genres", conn, if_exists="replace", index=False)
subgenres_df.to_sql("SubGenres", conn, if_exists="replace", index=False)

print("Данные успешно загружены.")
