import mysql.connector
import time
from datetime import datetime
import clickhouse_connect

# Настройки подключения к базе данных
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'mydatabase',
}

chouse_config = clickhouse_connect.get_client(
    host= 'localhost',
    user='default',
    password= '',
    database= 'default',
    port= 8123,
)

def fetch_data():
    # Подключение к базе данных
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Выполнение запроса
    cursor.execute("SELECT * FROM messages")  # Замените на ваш запрос
    data = cursor.fetchall()

    # Закрытие соединения
    cursor.close()
    conn.close()

    return data


def to_clickhouse(data):

    if not data:
        print("Нет данных")
        return

    new_data_ch = []
    for row in data:
        uid, timestamp, message = row
        new_data_ch.append((uid, timestamp, message))

    chouse_config.insert("messages", new_data_ch, column_names=["id", "export_timestamp", "message"])

    print("Перенесено", len(new_data_ch), "строк")


if __name__ == "__main__":
    while True:
        data = fetch_data()
        to_clickhouse(data)
        time.sleep(300)  # 5 минут
