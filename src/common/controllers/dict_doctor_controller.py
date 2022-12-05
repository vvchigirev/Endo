from ..Exceptions.business_exception import BusinеssException
from ...dict.doctors.model.doctor_model import DoctorModel
from ..data.xml_data_provider import XmlDataProvider
from ..data.xml_doctors import XmlDoctors


class ControllerDictDoctor:
    """ Контроллерю Справочник докторов """

    __data_provider: XmlDataProvider = None  # Провайдер данных XML
    __xml_doctors: XmlDoctors = None  # Xml структур для Врачей

    def __init__(self, xml_provider: XmlDataProvider = None):
        """ Конструктор
        :param xml_provider: Xml провайдер
        """

        self.__data_provider = xml_provider
        self.__xml_doctors = XmlDoctors(self.__data_provider)

    def select_doctors(self):
        """ Получение списка вречей
        :return: Список моделей врачей
        """

        print(": ControllerDictDoctor.select_doctors()")

        doctors = [DoctorModel]

        try:
            return self.__xml_doctors.select_doctors()
        except Exception as e:
            message = "Ошибка получения списка врачей!"
            print(message, e)
            raise BusinеssException(message)

        return doctors

    def get_doctor(self, code):
        """ Получение Врача по коду
        :param code: Код врача
        :return: Модель. Врач
        """

        try:
            if code != "" or code is not None:
                doctor = self.__xml_doctors.get_doctor(code)
                return doctor

            return None

        except Exception as e:
            message = "Ошибка получения врача"
            print(message, e)
            raise BusinеssException(message)

    def create_doctor(self, doctor: DoctorModel):
        """ Добавление сущности Врач
        :param doctor: Модель - Врач
        :return: Результат выполнения
        """

        print(": ControllerDictDoctor.create_doctor()")

        print(f"Добавление врача: f{doctor}")

        try:
            if self.__xml_doctors.get_doctor(doctor.code):
                print(f"Врач с кодом {doctor.code} уже существует!")
                return False

            if not self.__xml_doctors.create_doctor(doctor):
                print("Врач не добавлен !!!")
                return False

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

        print(": ControllerDictDoctor.update_doctor()")

        try:
            if not self.get_doctor(doctor.code):
                print(f"Врачь с кодом {doctor.code} не существует!")
                return False

            if not self.__xml_doctors.update_doctor(doctor):
                print("Врач НЕ изменен !!!")
                return False

            return True
        except Exception as e:
            message = "Ошибка изменения врача"
            print(message, e)
            raise BusinеssException(message)

    def delete_doctor(self, code):
        """ Удаление сущности Врач
        :param code: Код Врача
        :return: Результат выполнения
        """
        print(": ControllerDictDoctor.delete_doctor()")

        try:
            doctor = self.get_doctor(code)
            if not doctor:
                print(f"Врач с кодом {code} не найден!")
                return False

            try:
                if doctor:
                    print(f"Удалим врача с кодом: {code}")

                    if self.__xml_doctors.delete_doctor(code):
                        return True

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
