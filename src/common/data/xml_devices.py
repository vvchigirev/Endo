import xml.etree.ElementTree as ET

from ..base_classes.base_sections import BaseSections
from ...common.consts.Keys import Keys
from .xml_data_provider import XmlDataProvider
from ...dict.device.model.device_model import DeviceModel


class XmlDevices(BaseSections):
    """ Xml Сруктура для сущностей Приборов """

    def __init__(self, xml_provider: XmlDataProvider = None):
        """ Конструктор
        :param xml_provider: Xml провайдер
        """

        self.__xml_provider: XmlDataProvider = xml_provider

        self.group_name = Keys.ORGANS
        self.element_name = Keys.ORGAN

    def get_device_model_from_xml_element(self, xml_element):
        """ Генерация модели Прибора из xml элемента
        :param xml_element: xml элемент
        :return: Модель Прибора
        """

        if xml_element.attrib:
            code = xml_element.attrib.get("code")
            name = xml_element.attrib.get("name")
        else:
            code = xml_element.find("code").text
            name = xml_element.find("name").text

        return DeviceModel(code, name)

    def get_device(self, code):
        """ Получение прибора по коду
        :param xml_element: xml элеммент группы приборов
        :param code: Код прибора
        :return: Модель Прибор
        """
        print(": device.get_device()")

        if not self.__xml_provider.root:
            return None

        xml_group = self.__xml_provider.root.find(self.group_name)

        str_search = self.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            device = self.get_device_model_from_xml_element(element)
            return device
        else:
            str_search = self.element_name + "[@code='" + str(code) + "']"
            element = xml_group.find(str_search)
            if element is not None:
                device = self.get_device_model_from_xml_element(element)
                return device
        return None

    def update_device(self, device: DeviceModel):
        """ Обновление xml элемента для Прибора
        :param xml_element: xml элеммент группы приборов
        :param device: Модель Прибор
        :return: xml
        """
        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.group_name)

        str_search = self.element_name + "code=['" + str(device.code) + "']"
        xml_device = xml_group.find(str_search)

        if xml_device:
            name = xml_device.find("name")
            name.text = device.name

    def select_devices(self):
        """ Получение списка Приборов
        :return: Список моделей Приборов
        """

        print(": select_device")

        if not self.__xml_provider.root:
            return []

        devices = []

        xml_group = self.__xml_provider.root.find(self.group_name)

        if xml_group:
            print("xml_group=", xml_group)
            for xml_devices in xml_group.findall(self.element_name):
                device: DeviceModel = self.get_device_model_from_xml_element(xml_devices)

                devices.append(device)

        return devices

    def creat_xml_device(self, xml_element, device: DeviceModel):
        """ Создание xml элемента для модели Прибора
        :param xml_element: корневой xml элемент
        :param device: Модель Прибора
        """
        print(": create_xml_device")
        print("xml_element=",xml_element)
        print("device=",device)

        code = ET.SubElement(xml_element, "code")
        code.text = str(device.code)

        name = ET.SubElement(xml_element, "name")
        name.text = str(device.name)

        return True

    def creat_device(self, device: DeviceModel):
        """ Создание xml элемента для модели Прибора
        :param device: Модель Прибора
        :return: Результат выполнения
        """
        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.group_name)

        print("xml_group=", xml_group)

        xml_device = ET.SubElement(xml_group, self.element_name)

        print("xml_device=", xml_device)

        if self.creat_xml_device(xml_device, device):
            return True

        return False

    def delete_device(self, code):
        """ Удаление xml элемента по коду
        :param xml_element: xml элеммент группы приборов
        :param code: Код прибора
        :return: Результат выполнения
        """
        print(": device.delete")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.group_name)

        str_search = self.element_name + "code=['" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            xml_group.remove(element)
            return True

        return False