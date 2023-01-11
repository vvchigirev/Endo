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

    # Создайте курсор для выполнения операций с базой данных
    cursor = connection.cursor()

    # SQL-запрос для создания новой таблицы
    create_table_dostors = '''CREATE TABLE dict_nurse (
                                ID INT PRIMARY KEY     NOT NULL,
                                Last_Name varchar    NOT NULL,
                                First_Name varchar    NOT NULL,
                                Middle_Name varchar    NOT NULL
                              ); '''

    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table_dostors)
    connection.commit()

    print("Таблица успешно создана в PostgreSQL")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")