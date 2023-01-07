import xml.etree.ElementTree as ET

from ..base_classes.base_sections import BaseSections
from .sections.section_complications import SectionComplications
from .xml_data_provider import XmlDataProvider
from ...dict.complication.model.complication_model import ComplicationModel


class XmlComplications(BaseSections):
    """ Xml Сруктура для сущностей Осложнений """

    def __init__(self):
        """ Конструктор """

        self.__xml_provider: XmlDataProvider = XmlDataProvider()

        self.__section = SectionComplications()

    def get_complication_model_from_xml_element(self, xml_element):
        """ Генерация модели Осложнения из xml элемента
        :param xml_element: xml элемент
        :return: Модель Осложнения
        """

        if xml_element.attrib:
            code = xml_element.attrib.get("code")
            name = xml_element.attrib.get("name")
        else:
            code = xml_element.find("code").text
            name = xml_element.find("name").text

        return ComplicationModel(code, name)

    def get_complication(self, code):
        """ Получение осложнения по коду
        :param xml_element: xml элемент группы осложнений
        :param code: Код осложнения
        :return: Модель Осложнение
        """

        print(": XmlComplications.get_complication()")

        print("self.__xml_provider.root=", self.__xml_provider.root)
        if not self.__xml_provider.root:
            return None

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            complication = self.get_complication_model_from_xml_element(element)
            return complication
        else:
            str_search = self.__section.element_name + "[@code='" + str(code) + "']"
            element = xml_group.find(str_search)
            if element is not None:
                complication = self.get_complication_model_from_xml_element(element)
                return complication
        return None

    def update_complication(self, complication: ComplicationModel):
        """ Обновление xml элемента для Осложнения
        :param xml_element: xml элеммент группы осложнений
        :param complication: Модель Осложнение
        :return: xml
        """
        print(": XmlComplications.update_complication()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(complication.code) + "']"
        xml_complication = xml_group.find(str_search)

        print("xml_complications=", xml_complication)

        if xml_complication:
            name = xml_complication.find("name")
            name.text = complication.name
            return True
    def select_complications(self):
        """ Получение списка Осложнений
        :return: Список моделей Осложнений
        """

        print(": select_complication")

        if not self.__xml_provider.root:
            return []

        complications = []

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        if xml_group:
            print("xml_group=", xml_group)
            for xml_complications in xml_group.findall(self.__section.element_name):
                complication: ComplicationModel = self.get_complication_model_from_xml_element(xml_complications)

                complications.append(complication)

        return complications

    def creat_xml_complication(self, xml_element, complication: ComplicationModel):
        """ Создание xml элемента для модели Осложнения
        :param xml_element: корневой xml элемент
        :param complication: Модель Осложнения
        """
        print(": create_xml_complication")
        print("xml_element=",xml_element)
        print("complication=",complication)

        code = ET.SubElement(xml_element, "code")
        code.text = str(complication.code)

        name = ET.SubElement(xml_element, "name")
        name.text = str(complication.name)

        return True

    def creat_complication(self, complication: ComplicationModel):
        """ Создание xml элемента для модели Осложнения
        :param complication: Модель Осложнения
        :return: Результат выполнения
        """
        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        xml_complication = ET.SubElement(xml_group, self.__section.element_name)

        print("xml_complication=", xml_complication)

        if self.creat_xml_complication(xml_complication, complication):
            return True

        return False

    def delete_complication(self, code):
        """ Удаление xml элемента по коду
        :param xml_element: xml элеммент группы осложнений
        :param code: Код осложнения
        :return: Результат выполнения
        """
        print(": complication.delete")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            xml_group.remove(element)
            return True

        return False