import sqlite3
import json

# Подключение к БД
db_path = "output_data/books_database.db"
conn = sqlite3.connect(db_path)

# Запросы
queries = {
    "top_rated_books": """
        SELECT Title, Author, Rating
        FROM Books
        WHERE Rating > 4.5
        ORDER BY Rating DESC
        LIMIT 5;
    """,
    "average_price_per_genre": """
        SELECT "Main Genre", AVG(Price) AS Average_Price  -- Используем правильное имя с пробелом
        FROM Books
        GROUP BY "Main Genre"
        HAVING COUNT(*) > 2;
    """,
    "book_count_per_subgenre": """
        SELECT "Sub Genre", COUNT(*) AS Book_Count  -- Используем правильное имя с пробелом
        FROM Books
        GROUP BY "Sub Genre";
    """,
    "update_book_price": """
        UPDATE Books
        SET Price = Price * 1.1
        WHERE Rating > 4.6;
    """,
    "expensive_books": """
        SELECT Title, Price
        FROM Books
        WHERE Price > 500
        ORDER BY Price DESC;
    """
}


# Функция для преобразования результатов запроса в список словарей
def query_to_dict(cursor, query):
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]  # Получаем имена столбцов
    results = cursor.fetchall()  # Извлекаем все строки
    return [dict(zip(columns, row)) for row in results]  # Создаем словари для каждой строки

# Выполнение запросов
results = {}
for name, query in queries.items():
    cursor = conn.cursor()  # Создаем курсор для выполнения запросов
    if "UPDATE" in query:
        with conn:
            conn.execute(query)
        results[name] = "Данные обновлены."
    else:
        results[name] = query_to_dict(cursor, query)

# Сохранение в JSON
output_path = "output_data/queries.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)

print("Запросы выполнены и результаты сохранены в json.")
