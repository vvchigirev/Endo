import xml.etree.ElementTree as ET

from ..base_classes.base_sections import BaseSections
from .sections.section_devices import SectionDevices
from .xml_data_provider import XmlDataProvider
from ...dict.device.model.device_model import DeviceModel


class XmlDevices(BaseSections):
    """ Xml Сруктура для сущностей Приборов """

    def __init__(self):
        """ Конструктор """

        self.__xml_provider: XmlDataProvider = XmlDataProvider()

        self.__section = SectionDevices()

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
        :param xml_element: xml элемент группы приборов
        :param code: Код прибора
        :return: Модель Прибор
        """

        print(": XmlDevices.get_device()")

        print("self.__xml_provider.root=", self.__xml_provider.root)
        if not self.__xml_provider.root:
            return None

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            device = self.get_device_model_from_xml_element(element)
            return device
        else:
            str_search = self.__section.element_name + "[@code='" + str(code) + "']"
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
        print(": XmlDevices.update_device()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(device.code) + "']"
        xml_device = xml_group.find(str_search)

        print("xml_devices=", xml_device)

        if xml_device:
            name = xml_device.find("name")
            name.text = device.name
            return True
    def select_devices(self):
        """ Получение списка Приборов
        :return: Список моделей Приборов
        """

        print(": select_device")

        if not self.__xml_provider.root:
            return []

        devices = []

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        if xml_group:
            print("xml_group=", xml_group)
            for xml_devices in xml_group.findall(self.__section.element_name):
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

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        xml_device = ET.SubElement(xml_group, self.__section.element_name)

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

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            xml_group.remove(element)
            return True

        return False