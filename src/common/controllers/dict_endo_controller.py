from ..Exceptions.business_exception import BusinеssException
from ...dict.endos.model.endo_model import EndoModel
from ..data.xml_endos import XmlEndos


class ControllerDictEndo:
    """ Контроллерю Справочник эндоскопий """

    __xml_endos: XmlEndos = None            # Xml структур для эндоскопий

    def __init__(self):
        """ Конструктор
        :param xml_provider: Xml провайдер
        """

        print(": ControllerDictEndo.__init__()")

        self.__xml_endos = XmlEndos()

    def select_endos(self):
        """ Получение списка эндоскопий
        :return: Список моделей эндоскопий
        """

        print(": ControllerDictEndo.select_endos()")

        endos = [EndoModel]

        try:
            return self.__xml_endos.select_endos()
        except Exception as e:
            message = "Ошибка получения списка эндоскопий!"
            print(message, e)
            raise BusinеssException(message, e)

        return endos

    def get_endo(self, code):
        """ Получение эндоскопий по коду
        :param code: Код эндоскопий
        :return: Модель. эндоскопия
        """

        try:
            if code != "" or code is not None:
                endo = self.__xml_endos.get_endo(code)
                return endo

            return None

        except Exception as e:
            message = "Ошибка получения эндоскопий"
            print(message, e)
            raise BusinеssException(message)

    def create_endo(self, endo: EndoModel):
        """ Добавление сущности эндоскопия
        :param endo: Модель - эндоскопия
        :return: Результат выполнения
        """

        print(": ControllerDictEndo.create_endo()")

        print(f"Добавление эндоскопий: f{endo}")

        try:
            if self.__xml_endos.get_endo(endo.code):
                print(f"эндоскопия с кодом {endo.code} уже существует!")
                return False

            if not self.__xml_endos.create_endo(endo):
                print("эндоскопия не добавлен !!!")
                return False

            return True
        except Exception as e:
            message = "Ошибка добавления эндоскопий"
            print(message + ": ", e)
            raise BusinеssException(message)

    def update_endo(self, endo: EndoModel):
        """ Обновление сущности эндоскопия
        :param endo: Модель - эндоскопия
        :return: Результат выполнения
        """

        print(": ControllerDictEndo.update_endo()")

        try:
            if not self.get_endo(endo.code):
                print(f"эндоскопия с кодом {endo.code} не существует!")
                return False

            if not self.__xml_endos.update_endo(endo):
                print("эндоскопия НЕ изменен !!!")
                return False

            return True
        except Exception as e:
            message = "Ошибка изменения эндоскопий"
            print(message, e)
            raise BusinеssException(message)

    def delete_endo(self, code):
        """ Удаление сущности эндоскопия
        :param code: Код эндоскопий
        :return: Результат выполнения
        """
        print(": ControllerDictEndo.delete_endo()")

        try:
            endo = self.get_endo(code)
            if not endo:
                print(f"эндоскопия с кодом {code} не найден!")

            try:
                if endo and self.__xml_endos.delete_endo(code):
                    print(f"Удалим эндоскопий с кодом: {code}")
                    return True
                return False

            except Exception as e:
                message = "Ошибка удаления эндоскопий"
                print(message + ": ", e)
                raise BusinеssException(message)

            return True
        except Exception as e:
            message = "Ошибка удаления эндоскопий"
            print(message, e)
            raise BusinеssException(message, e)
