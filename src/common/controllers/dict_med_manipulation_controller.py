from ..Exceptions.business_exception import BusinеssException
from ...dict.med_manipulation.model.med_manipulation_model import MedManipulationModel
from ..data.xml_med_manipulations import XmlMedManipulations


class ControllerDictMedManipulation:
    """ Контроллер Справочник лечебных манипуляций """

    __xml_med_manipulations: XmlMedManipulations = None  # Xml структур для Лечебная манипуляци

    def __init__(self):
        """ Конструктор """

        print(": ControllerDictMedManipulation.__init__()")

        self.__xml_med_manipulations = XmlMedManipulations()

    def select_med_manipulations(self):
        """Получение списка лечебных манипуляций
        :return список лечебных манипуляций
        """

        print(": ControllerDictMedManipulations.select_med_manipulations()")

        med_manipulations = []

        try:
            return self.__xml_med_manipulations.select_med_manipulations()
        except Exception as e:
            message = "Ошибка получения списка лечебных манипуляций!"
            print(message, e)
            raise BusinеssException(message)

        return med_manipulations

    def get_med_manipulation(self, code):
        """ Получение Лечебная манипуляция по коду
        :param code: Код лечебная манипуляция
        :return: Модель. Лечебная манипуляция
        """

        try:
            if code != "" or code is not None:
                med_manipulation = self.__xml_med_manipulations.get_med_manipulation(code)
                return med_manipulation

            return None
        except Exception as e:
            message = "Ошибка получения лечебная манипуляция!"
            print(message, e)
            raise BusinеssException(message)

    def create_med_manipulation(self, med_manipulation: MedManipulationModel):
        """ Добавление сущности Лечебная манипуляция
        :param med_manipulation: Модель - Лечебная манипуляция
        :return: Результат выполнения
        """

        print(": ControllerDictMedManipulation.create_med_manipulation()")

        print(f"Добавления лечебная манипуляция f{med_manipulation}")

        try:
            if self.__xml_med_manipulations.get_med_manipulation(med_manipulation.code):
                print(f"Лечебная манипуляция с кодом f{med_manipulation.code} уже существует")
                return False

            if not self.__xml_med_manipulations.creat_med_manipulation(med_manipulation):
                print("Лечебная манипуляция не добавлен")
                return False

            return True
        except Exception as e:
            message = "Ошибка ошибка добавления лечебная манипуляция!"
            print(message, e)
            raise BusinеssException(message)

    def update_med_manipulation(self, med_manipulation: MedManipulationModel):
        """ Обновление сущности Лечебная манипуляция
        :param med_manipulation: Модель - Лечебная манипуляция
        :return: Результат выполнения
        """

        print(": ControllerDictMedManipulation.update_med_manipulation()")
        try:
            if not self.get_med_manipulation(med_manipulation.code):
                print(f"Лечебная манипуляция с кодом f{med_manipulation.code} не существует")
                return False

            if not self.__xml_med_manipulations.update_med_manipulation(med_manipulation):
                print("лечебная манипуляция не изменен")
                return False

            return True
        except Exception as e:
            message = "Ошибка изменения лечебная манипуляция!"
            print(message, e)
            raise BusinеssException(message)

    def delete_med_manipulation(self, code):
        """ Удаление сущности Лечебная манипуляция
        :param code: Код лечебная манипуляция
        :return: Результат выполнения
        """
        print(": ControllerDictDoctor.delete_doctor()")

        try:
            med_manipulation = self.get_med_manipulation(code)
            if not med_manipulation:
                print(f"Лечебная манипуляция с кодом f{med_manipulation} не найдено")

            try:
                if med_manipulation and self.__xml_med_manipulations.delete_med_manipulation(code):
                    return True
                return False

            except Exception as e:
                message = "Ошибка удаления лечебная манипуляция"
                print(message + ": ", e)
                raise BusinеssException(message)

        except Exception as e:
            message = "Ошибка удаления лечебная манипуляция!"
            print(message, e)
            raise BusinеssException(message)
