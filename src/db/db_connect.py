from ..
from ..common.utils.config import Config


class DbConnect:

    @staticmethod
    def db_connect():
        """ Подключение к БД
        :return: БД
        """

        config = Config.config["SETTINGS"]

        DB_NAME = config["DB_NAME"]
        DB_HOST = config["DB_HOST"]
        DB_USERNAME = config["DB_USERNAME"]
        DB_PASSWORD = config["DB_PASSWORD"]

        print("DB_HOST=", DB_HOST)
        print("DB_NAME=", DB_NAME)

        db = None
        # db  = PostgresqlDatabase(
        #     DB_NAME,
        #     DB_HOST,
        #     DB_USERNAME,
        #     DB_PASSWORD
        # )

        return db

