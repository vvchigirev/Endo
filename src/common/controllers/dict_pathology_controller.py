from ..Exceptions.business_exception import BusinеssException
from ...dict.pathology.model.pathology_model import PathologyModel
from src.common.data.xml.entitys.xml_pathologys import XmlPathologys


class ControllerDictPathology:
    """ Контроллер Справочник патологий """

    __xml_pathologys: XmlPathologys = None  # Xml структур для Патологий

    def __init__(self):
        """ Конструктор """

        print(": ControllerDictPathology.__init__()")

        self.__xml_pathologys = XmlPathologys()

    def select_pathologys(self):
        """Получение списка патологий
        :return список патологий
        """

        print(": ControllerDictPathologys.select_pathologys()")

        pathologys = []

        try:
            return self.__xml_pathologys.select_pathologys()
        except Exception as e:
            message = "Ошибка получения списка патологий!"
            print(message, e)
            raise BusinеssException(message)

        return pathologys

    def get_pathology(self, code):
        """ Получение Патологии по коду
        :param code: Код патологии
        :return: Модель. Патология
        """

        try:
            if code != "" or code is not None:
                pathology = self.__xml_pathologys.get_pathology(code)
                return pathology

            return None
        except Exception as e:
            message = "Ошибка получения патологии!"
            print(message, e)
            raise BusinеssException(message)

    def create_pathology(self, pathology: PathologyModel):
        """ Добавление сущности Патология
        :param pathology: Модель - Патология
        :return: Результат выполнения
        """

        print(": ControllerDictPathology.create_pathology()")

        print(f"Добавления патологии f{pathology}")

        try:
            if self.__xml_pathologys.get_pathology(pathology.code):
                print(f"Патология с кодом f{pathology.code} уже существует")
                return False

            if not self.__xml_pathologys.creat_pathology(pathology):
                print("Патология не добавлен")
                return False

            return True
        except Exception as e:
            message = "Ошибка ошибка добавления патологии!"
            print(message, e)
            raise BusinеssException(message)

    def update_pathology(self, pathology: PathologyModel):
        """ Обновление сущности Патология
        :param pathology: Модель - Патология
        :return: Результат выполнения
        """

        print(": ControllerDictPathology.update_pathology()")
        try:
            if not self.get_pathology(pathology.code):
                print(f"Патологии с кодом f{pathology.code} не существует")
                return False

            if not self.__xml_pathologys.update_pathology(pathology):
                print("патология не изменен")
                return False

            return True
        except Exception as e:
            message = "Ошибка изменения патологии!"
            print(message, e)
            raise BusinеssException(message)

    def delete_pathology(self, code):
        """ Удаление сущности Патология
        :param code: Код патологии
        :return: Результат выполнения
        """
        print(": ControllerDictDoctor.delete_doctor()")

        try:
            pathology = self.get_pathology(code)
            if not pathology:
                print(f"Патологии с кодом f{pathology} не найдено")

            try:
                if pathology and self.__xml_pathologys.delete_pathology(code):
                    return True
                return False

            except Exception as e:
                message = "Ошибка удаления патологии"
                print(message + ": ", e)
                raise BusinеssException(message)

        except Exception as e:
            message = "Ошибка удаления патологии!"
            print(message, e)
            raise BusinеssException(message)
