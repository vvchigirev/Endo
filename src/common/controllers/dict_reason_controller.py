from ..Exceptions.business_exception import BusinеssException
from ...dict.reason.model.reason_model import ReasonModel
from ..data.xml_reasons import XmlReasons


class ControllerDictReason:
    """ Контроллер Справочник причин обращения """

    __xml_reasons: XmlReasons = None  # Xml структур для Причин обращения

    def __init__(self):
        """ Конструктор """

        print(": ControllerDictReason.__init__()")

        self.__xml_reasons = XmlReasons()

    def select_reasons(self):
        """Получение списка причин обращения
        :return список причин обращения
        """

        print(": ControllerDictReasons.select_reasons()")

        reasons = []

        try:
            return self.__xml_reasons.select_reasons()
        except Exception as e:
            message = "Ошибка получения списка причин обращения!"
            print(message, e)
            raise BusinеssException(message)

        return reasons

    def get_reason(self, code):
        """ Получение Причины обращения по коду
        :param code: Код причины обращения
        :return: Модель. Причина обращения
        """

        try:
            if code != "" or code is not None:
                reason = self.__xml_reasons.get_reason(code)
                return reason

            return None
        except Exception as e:
            message = "Ошибка получения причины обращения!"
            print(message, e)
            raise BusinеssException(message)

    def create_reason(self, reason: ReasonModel):
        """ Добавление сущности Причина обращения
        :param reason: Модель - Причина обращения
        :return: Результат выполнения
        """

        print(": ControllerDictReason.create_reason()")

        print(f"Добавления причины обращения f{reason}")

        try:
            if self.__xml_reasons.get_reason(reason.code):
                print(f"Причина обращения с кодом f{reason.code} уже существует")
                return False

            if not self.__xml_reasons.creat_reason(reason):
                print("Причина обращения не добавлен")
                return False

            return True
        except Exception as e:
            message = "Ошибка ошибка добавления причины обращения!"
            print(message, e)
            raise BusinеssException(message)

    def update_reason(self, reason: ReasonModel):
        """ Обновление сущности Причина обращения
        :param reason: Модель - Причина обращения
        :return: Результат выполнения
        """

        print(": ControllerDictReason.update_reason()")
        try:
            if not self.get_reason(reason.code):
                print(f"Причины обращения с кодом f{reason.code} не существует")
                return False

            if not self.__xml_reasons.update_reason(reason):
                print("причина обращения не изменен")
                return False

            return True
        except Exception as e:
            message = "Ошибка изменения причины обращения!"
            print(message, e)
            raise BusinеssException(message)

    def delete_reason(self, code):
        """ Удаление сущности Причина обращения
        :param code: Код причины обращения
        :return: Результат выполнения
        """
        print(": ControllerDictDoctor.delete_doctor()")

        try:
            reason = self.get_reason(code)
            if not reason:
                print(f"Причины обращения с кодом f{reason} не найдено")

            try:
                if reason and self.__xml_reasons.delete_reason(code):
                    return True
                return False

            except Exception as e:
                message = "Ошибка удаления причины обращения"
                print(message + ": ", e)
                raise BusinеssException(message)

        except Exception as e:
            message = "Ошибка удаления причины обращения!"
            print(message, e)
            raise BusinеssException(message)
