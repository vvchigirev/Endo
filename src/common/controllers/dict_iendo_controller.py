from ..Exceptions.business_exception import BusinеssException
from ...dict.iendo.model.iendo_model import IEndoModel
from ..data.xml_iendo import XmlIEndos


class ControllerDictIEndo:
    """ Контроллер Справочник приборов """

    __xml_iendos: XmlIEndos = None  # Xml структур для Приборов

    def __init__(self):
        """ Конструктор """

        print(": ControllerDictIEndo.__init__()")

        self.__xml_iendos = XmlIEndos()

    def select_iendos(self):
        """Получение списка приборов
        :return список приборов
        """

        print(": ControllerDictIEndos.select_iendos()")

        iendos = []

        try:
            return self.__xml_iendos.select_iendos()
        except Exception as e:
            message = "Ошибка получения списка приборов!"
            print(message, e)
            raise BusinеssException(message)

        return iendos

    def get_iendo(self, code):
        """ Получение Прибора по коду
        :param code: Код прибора
        :return: Модель. Прибор
        """

        try:
            if code != "" or code is not None:
                iendo = self.__xml_iendos.get_iendo(code)
                return iendo

            return None
        except Exception as e:
            message = "Ошибка получения прибора!"
            print(message, e)
            raise BusinеssException(message)

    def create_iendo(self, iendo: IEndoModel):
        """ Добавление сущности Прибор
        :param iendo: Модель - Прибор
        :return: Результат выполнения
        """

        print(": ControllerDictIEndo.create_iendo()")

        print(f"Добавления прибора f{iendo}")

        try:
            if self.__xml_iendos.get_iendo(iendo.code):
                print(f"Прибор с кодом f{iendo.code} уже существует")
                return False

            if not self.__xml_iendos.creat_iendo(iendo):
                print("Прибор не добавлен")
                return False

            return True
        except Exception as e:
            message = "Ошибка ошибка добавления прибора!"
            print(message, e)
            raise BusinеssException(message)

    def update_iendo(self, iendo: IEndoModel):
        """ Обновление сущности Прибор
        :param iendo: Модель - Прибор
        :return: Результат выполнения
        """

        print(": ControllerDictIEndo.update_iendo()")
        try:
            if not self.get_iendo(iendo.code):
                print(f"Прибора с кодом f{iendo.code} не существует")
                return False

            if not self.__xml_iendos.update_iendo(iendo):
                print("прибор не изменен")
                return False

            return True
        except Exception as e:
            message = "Ошибка изменения прибора!"
            print(message, e)
            raise BusinеssException(message)

    def delete_iendo(self, code):
        """ Удаление сущности Прибор
        :param code: Код прибора
        :return: Результат выполнения
        """
        print(": ControllerDictDoctor.delete_doctor()")

        try:
            iendo = self.get_iendo(code)
            if not iendo:
                print(f"Прибора с кодом f{iendo} не найдено")

            try:
                if iendo and self.__xml_iendos.delete_iendo(code):
                    return True
                return False

            except Exception as e:
                message = "Ошибка удаления прибора"
                print(message + ": ", e)
                raise BusinеssException(message)

        except Exception as e:
            message = "Ошибка удаления прибора!"
            print(message, e)
            raise BusinеssException(message)
