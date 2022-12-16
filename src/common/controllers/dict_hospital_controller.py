from ..Exceptions.business_exception import BusinеssException
from ...dict.hospital.model.hospital_model import HospitalModel
from ..data.xml_data_provider import XmlDataProvider
from ..data.xml_hospitals import XmlHospitals


class ControllerDictHospital:
    """ Контроллер Справочник больниц """

    __data_provider: XmlDataProvider = None  # Провайдер данных XML
    __xml_hospitals: XmlHospitals = None  # Xml структур для Органов

    def __init__(self, xml_provider: XmlDataProvider = None):
        """ Конструктор
        :param xml_provider: Xml провайдер
        """

        print(": ControllerDictHospital.__init__()")

        self.__data_provider = xml_provider
        self.__xml_hospitals = XmlHospitals(self.__data_provider)

    def select_hospitals(self):
        """Получение списка больниц
        :return список больниц
        """

        print(": ControllerDictHospitals.select_hospitals()")

        hospitals = []

        try:
            return self.__xml_hospitals.select_hospitals()
        except Exception as e:
            message = "Ошибка получения списка врачей!"
            print(message, e)
            raise BusinеssException(message)

        return hospitals

    def get_hospital(self, code):
        """ Получение Органа по коду
        :param code: Код больницы
        :return: Модель. Орган
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

    def creat_hospital(self, hospital: HospitalModel):
        """ Добавление сущности Орган
        :param hospital: Модель - Орган
        :return: Результат выполнения
        """

        print(": ControllerDictHospital.create_hospital()")

        print(f"Добавления больницы f{hospital}")

        try:
            if self.__xml_hospitals.get_hospital(hospital.code):
                print(f"Орган с кодом f{hospital.code} уже существует")
                return False

            if not self.__xml_hospitals.creat_hospital(hospital):
                print("Орган не добавлен")
                return False

            return True
        except Exception as e:
            message = "Ошибка ошибка добавления больницы!"
            print(message, e)
            raise BusinеssException(message)

    def update_hospital(self, hospital: HospitalModel):
        """ Обновление сущности Орган
        :param hospital: Модель - Орган
        :return: Результат выполнения
        """

        print(": ControllerDictHospital.update_hospital()")
        try:
            if not self.get_hospital(hospital.code):
                print(f"Органа с кодом f{hospital.code} не существует")
                return False

            if not self.__xml_hospitals.update_hospital(hospital):
                print("доктор не изменен")
                return False

            return True
        except Exception as e:
            message = "Ошибка изменения больницы!"
            print(message, e)
            raise BusinеssException(message)

    def delet_hospital(self, code):
        """ Удаление сущности Орган
        :param code: Код больницы
        :return: Результат выполнения
        """
        print(": ControllerDictDoctor.delete_doctor()")

        try:
            hospital = self.get_hospital(code)
            print("hospital", hospital)
            if not hospital:
                print(f"Органа с кодом {hospital} не найдено")

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
