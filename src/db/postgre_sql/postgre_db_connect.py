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

    print("DB_HOST=", DB_HOST)
    print("DB_NAME=", DB_NAME)
    print("DB_USER=", DB_USER)
    print("DB_PASSWORD=", DB_PASSWORD)

    # Подключение к существующей базе данных
    # connection = psycopg2.connect(
    #     host=config["DB_HOST"],
    #     database=config["DB_NAME"],
    #     user=config["DB_USERNAME"],
    #     password=config["DB_PASSWORD"],
    #     port=config["DB_PORT"]
    # )
    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()

    # Распечатать сведения о PostgreSQL
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")

    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")

    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")