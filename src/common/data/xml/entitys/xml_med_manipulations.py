import xml.etree.ElementTree as ET

from src.common.base_classes.base_sections import BaseSections
from src.common.data.xml.sections.section_med_manipulations import SectionMedManipulations
from src.common.data.xml.xml_data_provider import XmlDataProvider
from src.dict.med_manipulation.model.med_manipulation_model import MedManipulationModel


class XmlMedManipulations(BaseSections):
    """ Xml Сруктура для сущностей лечебная манипуляцияов """

    def __init__(self):
        """ Конструктор """

        self.__xml_provider: XmlDataProvider = XmlDataProvider()

        self.__section = SectionMedManipulations()

    def get_med_manipulation_model_from_xml_element(self, xml_element):
        """ Генерация модели лечебная манипуляцияа из xml элемента
        :param xml_element: xml элемент
        :return: Модель лечебная манипуляция
        """

        if xml_element.attrib:
            code = xml_element.attrib.get("code")
            name = xml_element.attrib.get("name")
        else:
            code = xml_element.find("code").text
            name = xml_element.find("name").text

        return MedManipulationModel(code, name)

    def get_med_manipulation(self, code):
        """ Получение прибора по коду
        :param xml_element: xml элемент группы приборов
        :param code: Код прибора
        :return: Модель лечебная манипуляция
        """

        print(": XmlMedManipulations.get_med_manipulation()")

        print("self.__xml_provider.root=", self.__xml_provider.root)
        if not self.__xml_provider.root:
            return None

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            med_manipulation = self.get_med_manipulation_model_from_xml_element(element)
            return med_manipulation
        else:
            str_search = self.__section.element_name + "[@code='" + str(code) + "']"
            element = xml_group.find(str_search)
            if element is not None:
                med_manipulation = self.get_med_manipulation_model_from_xml_element(element)
                return med_manipulation
        return None

    def update_med_manipulation(self, med_manipulation: MedManipulationModel):
        """ Обновление xml элемента для лечебная манипуляцияа
        :param xml_element: xml элеммент группы приборов
        :param med_manipulation: Модель лечебная манипуляция
        :return: xml
        """
        print(": XmlMedManipulations.update_med_manipulation()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(med_manipulation.code) + "']"
        xml_med_manipulation = xml_group.find(str_search)

        print("xml_med_manipulations=", xml_med_manipulation)

        if xml_med_manipulation:
            name = xml_med_manipulation.find("name")
            name.text = med_manipulation.name
            return True
    def select_med_manipulations(self):
        """ Получение списка лечебная манипуляцияов
        :return: Список моделей лечебная манипуляцияов
        """

        print(": select_med_manipulation")

        if not self.__xml_provider.root:
            return []

        med_manipulations = []

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        if xml_group:
            print("xml_group=", xml_group)
            for xml_med_manipulations in xml_group.findall(self.__section.element_name):
                med_manipulation: MedManipulationModel = self.get_med_manipulation_model_from_xml_element(xml_med_manipulations)

                med_manipulations.append(med_manipulation)

        return med_manipulations

    def creat_xml_med_manipulation(self, xml_element, med_manipulation: MedManipulationModel):
        """ Создание xml элемента для модели лечебная манипуляцияа
        :param xml_element: корневой xml элемент
        :param med_manipulation: Модель лечебная манипуляцияа
        """
        print(": create_xml_med_manipulation")
        print("xml_element=",xml_element)
        print("med_manipulation=",med_manipulation)

        code = ET.SubElement(xml_element, "code")
        code.text = str(med_manipulation.code)

        name = ET.SubElement(xml_element, "name")
        name.text = str(med_manipulation.name)

        return True

    def creat_med_manipulation(self, med_manipulation: MedManipulationModel):
        """ Создание xml элемента для модели лечебная манипуляция
        :param med_manipulation: Модель лечебная манипуляцияа
        :return: Результат выполнения
        """
        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        xml_med_manipulation = ET.SubElement(xml_group, self.__section.element_name)

        print("xml_med_manipulation=", xml_med_manipulation)

        if self.creat_xml_med_manipulation(xml_med_manipulation, med_manipulation):
            return True

        return False

    def delete_med_manipulation(self, code):
        """ Удаление xml элемента по коду
        :param xml_element: xml элеммент группы приборов
        :param code: Код прибора
        :return: Результат выполнения
        """
        print(": med_manipulation.delete")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            xml_group.remove(element)
            return True

        return False