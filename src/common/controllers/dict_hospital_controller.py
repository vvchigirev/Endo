from ..Exceptions.business_exception import BusinеssException
from ...dict.hospital.model.hospital_model import HospitalModel
from ..data.xml_hospitals import XmlHospitals


class ControllerDictHospital:
    """ Контроллер Справочник больниц """

    __xml_hospitals: XmlHospitals = None  # Xml структур для Приборов

    def __init__(self):
        """ Конструктор """

        print(": ControllerDictHospital.__init__()")

        self.__xml_hospitals = XmlHospitals()

    def select_hospitals(self):
        """Получение списка больниц
        :return список больниц
        """

        print(": ControllerDictHospitals.select_hospitals()")

        hospitals = []

        try:
            return self.__xml_hospitals.select_hospitals()
        except Exception as e:
            message = "Ошибка получения списка больниц!"
            print(message, e)
            raise BusinеssException(message)

        return hospitals

    def get_hospital(self, code):
        """ Получение Прибора по коду
        :param code: Код больницы
        :return: Модель. Прибор
        """

        try:
            if code != "" or code is not None:
                hospital = self.__xml_hospitals.get_hospital(code)
                return hospital

            return None
        except Exception as e:
            message = "Ошибка получения больницы!"
            print(message, e)
            raise BusinеssException(message)

    def create_hospital(self, hospital: HospitalModel):
        """ Добавление сущности Прибор
        :param hospital: Модель - Прибор
        :return: Результат выполнения
        """

        print(": ControllerDictHospital.create_hospital()")

        print(f"Добавления больницы f{hospital}")

        try:
            if self.__xml_hospitals.get_hospital(hospital.code):
                print(f"Прибор с кодом f{hospital.code} уже существует")
                return False

            if not self.__xml_hospitals.creat_hospital(hospital):
                print("Больница не добавлена")
                return False

            return True
        except Exception as e:
            message = "Ошибка ошибка добавления больницы!"
            print(message, e)
            raise BusinеssException(message)

    def update_hospital(self, hospital: HospitalModel):
        """ Обновление сущности Прибор
        :param hospital: Модель - Прибор
        :return: Результат выполнения
        """

        print(": ControllerDictHospital.update_hospital()")
        try:
            if not self.get_hospital(hospital.code):
                print(f"Прибора с кодом f{hospital.code} не существует")
                return False

            if not self.__xml_hospitals.update_hospital(hospital):
                print("больница не изменена")
                return False

            return True
        except Exception as e:
            message = "Ошибка изменения больницы!"
            print(message, e)
            raise BusinеssException(message)

    def delete_hospital(self, code):
        """ Удаление сущности Прибор
        :param code: Код больницы
        :return: Результат выполнения
        """
        print(": ControllerDictDoctor.delete_doctor()")

        try:
            hospital = self.get_hospital(code)
            if not hospital:
                print(f"Прибора с кодом f{hospital} не найдено")

            try:
                if hospital and self.__xml_hospitals.delete_hospital(code):
                    return True
                return False

            except Exception as e:
                message = "Ошибка удаления больницы"
                print(message + ": ", e)
                raise BusinеssException(message)

        except Exception as e:
            message = "Ошибка удаления больницы!"
            print(message, e)
            raise BusinеssException(message)
