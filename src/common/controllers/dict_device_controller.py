from ..Exceptions.business_exception import BusinеssException
from ...dict.device.model.device_model import DeviceModel
from ..data.xml_devices import XmlDevices


class ControllerDictDevice:
    """ Контроллер Справочник приборов """

    __xml_devices: XmlDevices = None  # Xml структур для Приборов

    def __init__(self):
        """ Конструктор """

        print(": ControllerDictDevice.__init__()")

        self.__xml_devices = XmlDevices()

    def select_devices(self):
        """Получение списка приборов
        :return список приборов
        """

        print(": ControllerDictDevices.select_devices()")

        devices = []

        try:
            return self.__xml_devices.select_devices()
        except Exception as e:
            message = "Ошибка получения списка приборов!"
            print(message, e)
            raise BusinеssException(message)

        return devices

    def get_device(self, code):
        """ Получение Прибора по коду
        :param code: Код прибора
        :return: Модель. Прибор
        """

        try:
            if code != "" or code is not None:
                device = self.__xml_devices.get_device(code)
                return device

            return None
        except Exception as e:
            message = "Ошибка получения прибора!"
            print(message, e)
            raise BusinеssException(message)

    def creat_device(self, device: DeviceModel):
        """ Добавление сущности Прибор
        :param device: Модель - Прибор
        :return: Результат выполнения
        """

        print(": ControllerDictDevice.create_device()")

        print(f"Добавления прибора f{device}")

        try:
            if self.__xml_devices.get_device(device.code):
                print(f"Прибор с кодом f{device.code} уже существует")
                return False

            if not self.__xml_devices.creat_device(device):
                print("Прибор не добавлен")
                return False

            return True
        except Exception as e:
            message = "Ошибка ошибка добавления прибора!"
            print(message, e)
            raise BusinеssException(message)

    def update_device(self, device: DeviceModel):
        """ Обновление сущности Прибор
        :param device: Модель - Прибор
        :return: Результат выполнения
        """

        print(": ControllerDictDevice.update_device()")
        try:
            if not self.get_device(device.code):
                print(f"Прибора с кодом f{device.code} не существует")
                return False

            if not self.__xml_devices.update_device(device):
                print("прибор не изменен")
                return False

            return True
        except Exception as e:
            message = "Ошибка изменения прибора!"
            print(message, e)
            raise BusinеssException(message)

    def delet_device(self, code):
        """ Удаление сущности Прибор
        :param code: Код прибора
        :return: Результат выполнения
        """
        print(": ControllerDictDoctor.delete_doctor()")

        try:
            device = self.get_device(code)
            if not device:
                print(f"Прибора с кодом f{device} не найдено")

            try:
                if device and self.__xml_devices.delete_device(code):
                    return True
                return False

            except Exception as e:
                message = "Ошибка удаления прибора"
                print(message + ": ", e)
                raise BusinеssException(message)

        except Exception as e:
            message = "Ошибка удаления прибора!"
            print(message, e)
            raise BusinеssException(message)
