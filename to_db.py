import mysql.connector
import csv
from datetime import datetime

def import_csv_to_mysql():
    config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'web_2',
    }

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        with open('users.csv', 'r', encoding='utf-8') as users_file:
            users_reader = csv.DictReader(users_file)
            users_data = []
            
            for row in users_reader:
                users_data.append((
                    row['username'],
                    datetime.strptime(row['created_at'], '%Y-%m-%d %H:%M:%S') if 'created_at' in row else None
                ))
            
            cursor.executemany(
                "INSERT INTO users (username, created_at) VALUES ( %s, %s)",
                users_data
            )
            print(f"Добавлено {cursor.rowcount} пользователей")

        with open('logs.csv', 'r', encoding='utf-8') as logs_file:
            logs_reader = csv.DictReader(logs_file)
            logs_data = []
            
            for row in logs_reader:
                logs_data.append((
                    int(row['user_id']) if row['user_id'] else None,
                    row['action_type'],
                    int(row['action_id']) if row['action_id'] else None,
                    row['server_response'],
                    datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')
                ))
            
            cursor.executemany(
                """INSERT INTO logs 
                   (user_id, action_type, action_id, server_response, timestamp) 
                   VALUES (%s, %s, %s, %s, %s)""",
                logs_data
            )
            print(f"Добавлено {cursor.rowcount} записей в лог")

        conn.commit()

    except mysql.connector.Error as err:
        print(f"Ошибка MySQL: {err}")
        conn.rollback()
    except Exception as e:
        print(f"Общая ошибка: {e}")
        conn.rollback()
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

import_csv_to_mysql()