from ..Exceptions.bsiness_exception import BusinеssException
from ...dict.pathalogy.model.pathalogy_model import PathalogyModel
from ..data.xml_pathalogys import XmlPathalogys


class ControllerDictPathalogy:
    """ Контроллер Справочник патологий """

    __xml_pathalogys: XmlPathalogys = None  # Xml структур для Патологий

    def __init__(self):
        """ Конструктор """

        print(": ControllerDictPathalogy.__init__()")

        self.__xml_pathalogys = XmlPathalogys()

    def select_pathalogys(self):
        """Получение списка патологий
        :return список патологий
        """

        print(": ControllerDictPathalogys.select_pathalogys()")

        pathalogys = []

        try:
            return self.__xml_pathalogys.select_pathalogys()
        except Exception as e:
            message = "Ошибка получения списка патологий!"
            print(message, e)
            raise BusinеssException(message)

        return pathalogys

    def get_pathalogy(self, code):
        """ Получение Патологии по коду
        :param code: Код патологии
        :return: Модель. Патология
        """

        try:
            if code != "" or code is not None:
                pathalogy = self.__xml_pathalogys.get_pathalogy(code)
                return pathalogy

            return None
        except Exception as e:
            message = "Ошибка получения патологии!"
            print(message, e)
            raise BusinеssException(message)

    def create_pathalogy(self, pathalogy: PathalogyModel):
        """ Добавление сущности Патология
        :param pathalogy: Модель - Патология
        :return: Результат выполнения
        """

        print(": ControllerDictPathalogy.create_pathalogy()")

        print(f"Добавления патологии f{pathalogy}")

        try:
            if self.__xml_pathalogys.get_pathalogy(pathalogy.code):
                print(f"Патология с кодом f{pathalogy.code} уже существует")
                return False

            if not self.__xml_pathalogys.creat_pathalogy(pathalogy):
                print("Патология не добавлен")
                return False

            return True
        except Exception as e:
            message = "Ошибка ошибка добавления патологии!"
            print(message, e)
            raise BusinеssException(message)

    def update_pathalogy(self, pathalogy: PathalogyModel):
        """ Обновление сущности Патология
        :param pathalogy: Модель - Патология
        :return: Результат выполнения
        """

        print(": ControllerDictPathalogy.update_pathalogy()")
        try:
            if not self.get_pathalogy(pathalogy.code):
                print(f"Патологии с кодом f{pathalogy.code} не существует")
                return False

            if not self.__xml_pathalogys.update_pathalogy(pathalogy):
                print("патология не изменен")
                return False

            return True
        except Exception as e:
            message = "Ошибка изменения патологии!"
            print(message, e)
            raise BusinеssException(message)

    def delete_pathalogy(self, code):
        """ Удаление сущности Патология
        :param code: Код патологии
        :return: Результат выполнения
        """
        print(": ControllerDictDoctor.delete_doctor()")

        try:
            pathalogy = self.get_pathalogy(code)
            if not pathalogy:
                print(f"Патологии с кодом f{pathalogy} не найдено")

            try:
                if pathalogy and self.__xml_pathalogys.delete_pathalogy(code):
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
