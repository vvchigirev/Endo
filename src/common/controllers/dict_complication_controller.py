from ..Exceptions.business_exception import BusinеssException
from ...dict.complication.model.complication_model import ComplicationModel
from ..data.xml_complications import XmlComplications


class ControllerDictComplication:
    """ Контроллер Справочник осложнений """

    __xml_complications: XmlComplications = None  # Xml структур для Осложнений

    def __init__(self):
        """ Конструктор """

        print(": ControllerDictComplication.__init__()")

        self.__xml_complications = XmlComplications()

    def select_complications(self):
        """Получение списка осложнений
        :return список осложнений
        """

        print(": ControllerDictComplications.select_complications()")

        complications = []

        try:
            return self.__xml_complications.select_complications()
        except Exception as e:
            message = "Ошибка получения списка осложнений!"
            print(message, e)
            raise BusinеssException(message)

        return complications

    def get_complication(self, code):
        """ Получение Осложнения по коду
        :param code: Код осложнения
        :return: Модель. Осложнение
        """

        try:
            if code != "" or code is not None:
                complication = self.__xml_complications.get_complication(code)
                return complication

            return None
        except Exception as e:
            message = "Ошибка получения осложнения!"
            print(message, e)
            raise BusinеssException(message)

    def create_complication(self, complication: ComplicationModel):
        """ Добавление сущности Осложнение
        :param complication: Модель - Осложнение
        :return: Результат выполнения
        """

        print(": ControllerDictComplication.create_complication()")

        print(f"Добавления осложнения f{complication}")

        try:
            if self.__xml_complications.get_complication(complication.code):
                print(f"Осложнение с кодом f{complication.code} уже существует")
                return False

            if not self.__xml_complications.creat_complication(complication):
                print("Осложнение не добавлен")
                return False

            return True
        except Exception as e:
            message = "Ошибка ошибка добавления осложнения!"
            print(message, e)
            raise BusinеssException(message)

    def update_complication(self, complication: ComplicationModel):
        """ Обновление сущности Осложнение
        :param complication: Модель - Осложнение
        :return: Результат выполнения
        """

        print(": ControllerDictComplication.update_complication()")
        try:
            if not self.get_complication(complication.code):
                print(f"Осложнения с кодом f{complication.code} не существует")
                return False

            if not self.__xml_complications.update_complication(complication):
                print("осложнение не изменен")
                return False

            return True
        except Exception as e:
            message = "Ошибка изменения осложнения!"
            print(message, e)
            raise BusinеssException(message)

    def delete_complication(self, code):
        """ Удаление сущности Осложнение
        :param code: Код осложнения
        :return: Результат выполнения
        """
        print(": ControllerDictDoctor.delete_doctor()")

        try:
            complication = self.get_complication(code)
            if not complication:
                print(f"Осложнения с кодом f{complication} не найдено")

            try:
                if complication and self.__xml_complications.delete_complication(code):
                    return True
                return False

            except Exception as e:
                message = "Ошибка удаления осложнения"
                print(message + ": ", e)
                raise BusinеssException(message)

        except Exception as e:
            message = "Ошибка удаления осложнения!"
            print(message, e)
            raise BusinеssException(message)
