from ..Exceptions.business_exception import BusinеssException
from ...dict.nurse.model.nurse_model import NurseModel
from ..data.xml_nurses import XmlNurses


class ControllerDictNurse:
    """ Контроллер Справочник докторов """

    __xml_nurses: XmlNurses = None            # Xml структур для Врачей

    def __init__(self):
        """ Конструктор
        :param xml_provider: Xml провайдер
        """

        print(": ControllerDictNurse.__init__()")

        self.__xml_nurses = XmlNurses()

    def select_nurses(self):
        """ Получение списка вречей
        :return: Список моделей врачей
        """

        print(": ControllerDictNurse.select_nurses()")

        nurses = [NurseModel]

        try:
            return self.__xml_nurses.select_nurses()
        except Exception as e:
            message = "Ошибка получения списка врачей!"
            print(message, e)
            raise BusinеssException(message, e)

        return nurses

    def get_nurse(self, code):
        """ Получение Врача по коду
        :param code: Код врача
        :return: Модель. Врач
        """

        try:
            if code != "" or code is not None:
                nurse = self.__xml_nurses.get_nurse(code)
                return nurse

            return None

        except Exception as e:
            message = "Ошибка получения врача"
            print(message, e)
            raise BusinеssException(message)

    def create_nurse(self, nurse: NurseModel):
        """ Добавление сущности Врач
        :param nurse: Модель - Врач
        :return: Результат выполнения
        """

        print(": ControllerDictNurse.create_nurse()")

        print(f"Добавление врача: f{nurse}")

        try:
            if self.__xml_nurses.get_nurse(nurse.code):
                print(f"Врач с кодом {nurse.code} уже существует!")
                return False

            if not self.__xml_nurses.create_nurse(nurse):
                print("Врач не добавлен !!!")
                return False

            return True
        except Exception as e:
            message = "Ошибка добавления врача"
            print(message + ": ", e)
            raise BusinеssException(message)

    def update_nurse(self, nurse: NurseModel):
        """ Обновление сущности Врач
        :param nurse: Модель - Врач
        :return: Результат выполнения
        """

        print(": ControllerDictNurse.update_nurse()")

        try:
            if not self.get_nurse(nurse.code):
                print(f"Врачь с кодом {nurse.code} не существует!")
                return False

            if not self.__xml_nurses.update_nurse(nurse):
                print("Врач НЕ изменен !!!")
                return False

            return True
        except Exception as e:
            message = "Ошибка изменения врача"
            print(message, e)
            raise BusinеssException(message)

    def delete_nurse(self, code):
        """ Удаление сущности Врач
        :param code: Код Врача
        :return: Результат выполнения
        """
        print(": ControllerDictNurse.delete_nurse()")

        try:
            nurse = self.get_nurse(code)
            if not nurse:
                print(f"Врач с кодом {code} не найден!")
                return False

            try:
                if nurse:
                    print(f"Удалим врача с кодом: {code}")

                    result = self.__xml_nurses.delete_nurse(code)
                    print("result=", result)
                    if result:
                        print("Врач удален!")
                        return True
                    else:
                        print("Врач не удален!")

                return False
            except Exception as e:
                message = "Ошибка удаления врача"
                print(message + ": ", e)
                raise BusinеssException(message)

            return True
        except Exception as e:
            message = "Ошибка удаления врача"
            print(message, e)
            raise BusinеssException(message, e)
