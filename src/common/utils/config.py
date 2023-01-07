import os
import configparser


class Config:
    __instance = None
    __config = None

    def __new__(cls):
        print(": Config.__new__()")

        # if not hasattr(cls, 'instance'):
        #     cls.instance = super(Config, cls).__new__(cls)

        if Config.__instance is None:
            print("__file__=", __file__)

            project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

            print("project_root=", project_root)

            config_file = os.path.join(project_root, "config.ini")

            print("config_file=", config_file)

            Config.__instance = object.__new__(cls)
            Config.__instance.load_config(config_file)

        return Config.__instance

    # region Свойства

    @property
    def config(self):
        """Свойство. Настройки"""

        return self.__config

    # endregion

    def load_config(self, file_path):
        """ Загрузка настроек
        :param file_path: Путь к файлу настроек
        :return:
        """

        print(": Config.load_config()")

        if os.path.exists(file_path):
            self.__config = configparser.ConfigParser()
            self.__config.read(file_path)
        else:
            message = "Файл настроек config.ini не найден"
            print(message)
            raise ValueError(message)
