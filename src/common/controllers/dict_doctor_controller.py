from ..Exceptions.business_exception import BusinеssException
from ...dict.doctors.model.doctor_model import DoctorModel
from src.common.data.xml.entitys.xml_doctors import XmlDoctors


class ControllerDictDoctor:
    """ Контроллер Справочник докторов """

    __xml_doctors: XmlDoctors = None            # Xml структур для Мед сестер

    def __init__(self):
        """ Конструктор
        :param xml_provider: Xml провайдер
        """

        print(": ControllerDictDoctor.__init__()")

        self.__xml_doctors = XmlDoctors()

    def select_doctors(self):
        """ Получение списка вречей
        :return: Список моделей мед сестер
        """

        print(": ControllerDictDoctor.select_doctors()")

        doctors = [DoctorModel]

        try:
            return self.__xml_doctors.select_doctors()
        except Exception as e:
            message = "Ошибка получения списка мед сестер!"
            print(message, e)
            raise BusinеssException(message, e)

        return doctors

    def get_doctor(self, code):
        """ Получение Мед сестры по коду
        :param code: Код мед сестры
        :return: Модель. Врач
        """

        try:
            if code != "" or code is not None:
                doctor = self.__xml_doctors.get_doctor(code)
                return doctor

            return None

        except Exception as e:
            message = "Ошибка получения мед сестры"
            print(message, e)
            raise BusinеssException(message)

    def create_doctor(self, doctor: DoctorModel):
        """ Добавление сущности Врач
        :param doctor: Модель - Врач
        :return: Результат выполнения
        """

        print(": ControllerDictDoctor.create_doctor()")

        print(f"Добавление мед сестры: f{doctor}")

        try:
            if self.__xml_doctors.get_doctor(doctor.code):
                print(f"Врач с кодом {doctor.code} уже существует!")
                return False

            if not self.__xml_doctors.create_doctor(doctor):
                print("Врач не добавлен !!!")
                return False

            return True
        except Exception as e:
            message = "Ошибка добавления мед сестры"
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
            message = "Ошибка изменения мед сестры"
            print(message, e)
            raise BusinеssException(message)

    def delete_doctor(self, code):
        """ Удаление сущности Врач
        :param code: Код Мед сестры
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
                    print(f"Удалим мед сестры с кодом: {code}")

                    result = self.__xml_doctors.delete_doctor(code)
                    print("result=", result)
                    if result:
                        print("Врач удален!")
                        return True
                    else:
                        print("Врач не удален!")

                return False
            except Exception as e:
                message = "Ошибка удаления мед сестры"
                print(message + ": ", e)
                raise BusinеssException(message)

            return True
        except Exception as e:
            message = "Ошибка удаления мед сестры"
            print(message, e)
            raise BusinеssException(message, e)
