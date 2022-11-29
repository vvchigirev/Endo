from ..Exceptions.business_exception import BusinеssException
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

    def select_doctors(self):
        """ Получение списка вречей
        :return: Список моделей врачей
        """

        print(": ControllerDictDoctor.select_doctors()")

        doctors = []

        # doctor1 = DoctorModel(50, "Ivanov", "Ivan", "Ivanovich")
        # doctors.append(doctor1)
        # doctor2 = DoctorModel(51, "Petrov", "Petr", "Petrovich")
        # doctors.append(doctor2)

        # print("doctors=", doctors)

        xml_element = self.__data_provider.select_elements(self.__xml_doctors.group_name)
        if xml_element is not None:
            doctors = self.__xml_doctors.select_doctors(xml_element)

        return doctors

    def get_doctor(self, сode):
        """ Получение Врача по коду
        :param сode: Код врача
        :return: Модель. Врач
        """

        try:
            return True
        except Exception as e:
            message = "Ошибка добавления врача"
            print(message, e)
            raise BusinеssException(message)

        return doc

    def create_doctor(self, doctor: DoctorModel):
        """ Добавление сущности Врач
        :param doctor: Модель - Врач
        :return: Результат выполнения
        """

        print(": ControllerDictDoctor.create_doctor()")

        try:
            print(f"Добавление врача: f{doctor}")

            xml_element = self.__data_provider.create_element(
                self.__xml_doctors.group_name,
                self.__xml_doctors.element_name)

            if xml_element is not None:
                # self.__xml_doctors.create(xml_element, doctor)
                self.__xml_doctors.create_attribs(xml_element, doctor)

            return True
        except Exception as e:
            message = "Ошибка добавления врача"
            print(message + ": ", e)
            raise BusinеssException(message)

    def update_doctor(self, doctor: DoctorModel):
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
            raise BusinеssException(message)

    def delete_doctor(self, doctor: DoctorModel):
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
            raise BusinеssException(message)
