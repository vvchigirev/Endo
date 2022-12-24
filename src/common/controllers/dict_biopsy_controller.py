from ..Exceptions.business_exception import BusinеssException
from ...dict.biopsy.model.biopsy_moidel import BiopsyModel
from ..data.xml_biopsys import XmlBiopsys


class ControllerDictBiopsy:
    """ Контроллер Справочник биопсий"""

    __xml_biopsys: XmlBiopsys = None  # Xml структур для Биопсий

    def __init__(self):
        """ Конструктор """

        print(": ControllerDictBiopsy.__init__()")

        self.__xml_biopsys = XmlBiopsys()

    def select_biopsys(self):
        """Получение списка биопсий
        :return список биопсий
        """

        print(": ControllerDictBiopsys.select_biopsys()")

        biopsys = []

        try:
            return self.__xml_biopsys.select_biopsys()
        except Exception as e:
            message = "Ошибка получения списка биопсий!"
            print(message, e)
            raise BusinеssException(message)

        return biopsys

    def get_biopsy(self, code):
        """ Получение Биопсии по коду
        :param code: Код биопсии
        :return: Модель. Биопсия
        """

        try:
            if code != "" or code is not None:
                biopsy = self.__xml_biopsys.get_biopsy(code)
                return biopsy

            return None
        except Exception as e:
            message = "Ошибка получения биопсии!"
            print(message, e)
            raise BusinеssException(message)

    def create_biopsy(self, biopsy: BiopsyModel):
        """ Добавление сущности Биопсия
        :param biopsy: Модель - Биопсия
        :return: Результат выполнения
        """

        print(": ControllerDictBiopsy.create_biopsy()")

        print(f"Добавления биопсиии f{biopsy}")

        try:
            if self.__xml_biopsys.get_biopsy(biopsy.code):
                print(f"Биопсия с кодом f{biopsy.code} уже существует")
                return False

            if not self.__xml_biopsys.creat_biopsy(biopsy):
                print("Биопсия не добавлен")
                return False

            return True
        except Exception as e:
            message = "Ошибка ошибка добавления биопсия!"
            print(message, e)
            raise BusinеssException(message)

    def update_biopsy(self, biopsy: BiopsyModel):
        """ Обновление сущности Биопсия
        :param biopsy: Модель - Биопсия
        :return: Результат выполнения
        """

        print(": ControllerDictBiopsy.update_biopsy()")
        try:
            if not self.get_biopsy(biopsy.code):
                print(f"Биопсии с кодом f{biopsy.code} не существует")
                return False

            if not self.__xml_biopsys.update_biopsy(biopsy):
                print("биопсия не изменен")
                return False

            return True
        except Exception as e:
            message = "Ошибка изменения биопсия!"
            print(message, e)
            raise BusinеssException(message)

    def delete_biopsy(self, code):
        """ Удаление сущности Биопсия
        :param code: Код биопсия
        :return: Результат выполнения
        """
        print(": ControllerDictDoctor.delete_doctor()")

        try:
            biopsy = self.get_biopsy(code)
            if not biopsy:
                print(f"Биопсии с кодом f{biopsy} не найдено")

            try:
                if biopsy and self.__xml_biopsys.delete_biopsy(code):
                    return True
                return False

            except Exception as e:
                message = "Ошибка удаления биопсии"
                print(message + ": ", e)
                raise BusinеssException(message)

        except Exception as e:
            message = "Ошибка удаления биопсии!"
            print(message, e)
            raise BusinеssException(message)
