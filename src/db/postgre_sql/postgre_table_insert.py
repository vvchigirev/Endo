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

    # Выполнение SQL-запроса для вставки данных в таблицу
    # insert_query = """ INSERT INTO dict_doctors (
    #                         ID,
    #                         Last_Name,
    #                         First_Name,
    #                         Middle_name
    #                     )
    #                     VALUES (
    #                         1,
    #                         'Иванов',
    #                         'Иван',
    #                         'Иванович'
    #                     )"""
    # insert_query = """ INSERT INTO dict_doctors (
    #                             ID,
    #                             Last_Name,
    #                             First_Name,
    #                             Middle_name
    #                         )
    #                         VALUES (
    #                             2,
    #                             'Петров',
    #                             'Петр',
    #                             'Петрович'
    #                         )"""
    # insert_query = """ INSERT INTO dict_doctors (
    #                                 ID,
    #                                 Last_Name,
    #                                 First_Name,
    #                                 Middle_name
    #                             )
    #                             VALUES (
    #                                 3,
    #                                 'Сидоров',
    #                                 'Иван',
    #                                 'Петрович'
    #                             )"""
    # insert_query = """ INSERT INTO dict_doctors (
    #                                     ID,
    #                                     Last_Name,
    #                                     First_Name,
    #                                     Middle_name
    #                                 )
    #                                 VALUES (
    #                                     5,
    #                                     '1',
    #                                     '2',
    #                                     '3'
    #                                 )"""

    # cursor.execute(insert_query)

    # insert_query = """ INSERT INTO dict_doctors (
    #                                         ID,
    #                                         Last_Name,
    #                                         First_Name,
    #                                         Middle_name
    #                                     )
    #                                     VALUES (
    #                                         %s,
    #                                         %s,
    #                                         %s,
    #                                         %s
    #                                     )"""
    #
    # doctor_tuple = (10, "Снигирев", "Снигирь", "Снигиричь")
    # cursor.execute(insert_query, doctor_tuple)

    insert_query = """ INSERT INTO dict_doctors (
                                                ID, 
                                                Last_Name, 
                                                First_Name,
                                                Middle_name
                                            ) 
                                            VALUES (
                                                :id, 
                                                :last_name, 
                                                :first_name,
                                                :middle_name
                                            )"""

    doctor_tuple = {
        "id": 11,
        "last_name": '11 Иванов',
        "first_name": '11 Иван',
        "middle_names": '11 Иванович'
    }
    cursor.execute(insert_query, doctor_tuple)

    connection.commit()
    print("1 запись успешно вставлена")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")