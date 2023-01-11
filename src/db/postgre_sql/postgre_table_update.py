import psycopg2
from psycopg2 import Error
from src.common.utils.config import Config

try:
    config = Config().config["SETTINGS"]

    DB_HOST = config["DB_HOST"]
    DB_NAME = config["DB_NAME"]
    DB_USER = config["DB_USERNAME"]
    DB_PASSWORD = config["DB_PASSWORD"]
    DB_PORT = config["DB_PORT"]

    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

    cursor = connection.cursor()

    # Выполнение SQL-запроса для обновления таблицы
    update_query = """  UPDATE dict_doctors 
                        SET 
                            Middle_name = 'П' 
                        WHERE id = 3"""
    cursor.execute(update_query)
    connection.commit()

    count = cursor.rowcount
    print(count, "Запись успешно изменена")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")