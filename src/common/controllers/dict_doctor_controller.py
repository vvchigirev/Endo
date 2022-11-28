from ...dict.doctors.model.doctor_model import DoctorModel
from ..data.xml_data_provider import XmlDataProvider
from ..data.xml_doctors import XmlDoctors


class ControllerDictDoctor:
    """ Контроллерю Справочник докторов """

    __data_provider: XmlDataProvider = None  # Провайдер данных XML
    __xml_doctors: XmlDoctors = None  # Xml структур для Врачей

    def __init__(self, xml_provider: XmlDataProvider=None):
        """ Конструктор
        :param xml_provider: Xml провайдер
        """

        self.__data_provider = xml_provider
        self.__xml_doctors = XmlDoctors()

    def select_all(self):
        """ Получение списка вречей
        :return: Список моделей врачей
        """

        return None

    def get_el(self, сode):
        """ Получение врача по коду
        :param сode: Код врача
        :return: Модель. Врач
        """

        try:
            print(f"Добавление врача: f{doctor}")
            return True
        except Exception as e:
            message = "Ошибка добавления врача"
            print(message, e)
            raise Exception(message)

        return doc

    def add_el(self, doctor: DoctorModel):
        """ Добавление сущности Врач
        :param doctor: Модель - Врач
        :return: Результат выполнения
        """

        print(": ControllerDictDoctor.add_el()")

        try:
            print(f"Добавление врача: f{doctor}")

            xml_element = self.__data_provider.create_element(
                self.__xml_doctors.group_name,
                self.__xml_doctors.element_name)

            if xml_element is not None:
                self.__xml_doctors.create(xml_element, doctor)

            return True
        except Exception as e:
            message = "Ошибка добавления врача"
            print(message + ": ", e)
            raise Exception(message)

    def update_el(self, doctor: DoctorModel):
        """ Обновление сущности Врач
        :param doctor: Модель - Врач
        :return: Результат выполнения
        """

        try:
            print(f"Изменим врача: f{doctor}")
            return True
        except Exception as e:
            message = "Ошибка изменения врача"
            print(message, e)
            raise Exception(message)

    def delete_el(self, doctor: DoctorModel):
        """ Удаление сущности Врач
        :param doctor: Модель - Врач
        :return: результат выполнения
        """

        try:
            print(f"Удалим врача: f{doctor}")
            return True
        except Exception as e:
            message = "Ошибка удаления врача"
            print(message, e)
            raise Exception(message)
