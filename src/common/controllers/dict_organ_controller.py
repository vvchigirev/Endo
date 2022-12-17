from ..Exceptions.business_exception import BusinеssException
from ...dict.organs.model.organ_model import OrganModel
from ..data.xml_organs import XmlOrgans


class ControllerDictOrgan:
    """ Контроллер Справочник органов """

    __xml_organs: XmlOrgans = None  # Xml структур для Органов

    def __init__(self):
        """ Конструктор """

        print(": ControllerDictOrgan.__init__()")

        self.__xml_organs = XmlOrgans()

    def select_organs(self):
        """Получение списка органов
        :return список органов
        """

        print(": ControllerDictOrgans.select_organs()")

        organs = []

        try:
            return self.__xml_organs.select_organs()
        except Exception as e:
            message = "Ошибка получения списка врачей!"
            print(message, e)
            raise BusinеssException(message)

        return organs

    def get_organ(self, code):
        """ Получение Органа по коду
        :param code: Код органа
        :return: Модель. Орган
        """

        try:
            if code != "" or code is not None:
                organ = self.__xml_organs.get_organ(code)
                return organ

            return None
        except Exception as e:
            message = "Ошибка получения органа!"
            print(message, e)
            raise BusinеssException(message)

    def create_organ(self, organ: OrganModel):
        """ Добавление сущности Орган
        :param organ: Модель - Орган
        :return: Результат выполнения
        """

        print(": ControllerDictOrgan.create_organ()")

        print(f"Добавления органа f{organ}")

        try:
            if self.__xml_organs.get_organ(organ.code):
                print(f"Орган с кодом f{organ.code} уже существует")
                return False

            if not self.__xml_organs.creat_organ(organ):
                print("Орган не добавлен")
                return False

            return True
        except Exception as e:
            message = "Ошибка ошибка добавления органа!"
            print(message, e)
            raise BusinеssException(message)

    def update_organ(self, organ: OrganModel):
        """ Обновление сущности Орган
        :param organ: Модель - Орган
        :return: Результат выполнения
        """

        print(": ControllerDictOrgan.update_organ()")
        try:
            if not self.get_organ(organ.code):
                print(f"Органа с кодом f{organ.code} не существует")
                return False

            if not self.__xml_organs.update_organ(organ):
                print("доктор не изменен")
                return False

            return True
        except Exception as e:
            message = "Ошибка изменения органа!"
            print(message, e)
            raise BusinеssException(message)

    def delete_organ(self, code):
        """ Удаление сущности Орган
        :param code: Код органа
        :return: Результат выполнения
        """
        print(": ControllerDictDoctor.delete_doctor()")

        try:
            organ = self.get_organ(code)
            print("organ", organ)
            if not organ:
                print(f"Органа с кодом {organ} не найдено")

            try:
                if organ and self.__xml_organs.delete_organ(code):
                    return True
                return False

            except Exception as e:
                message = "Ошибка удаления органа"
                print(message + ": ", e)
                raise BusinеssException(message)

        except Exception as e:
            message = "Ошибка удаления органа!"
            print(message, e)
            raise BusinеssException(message)
