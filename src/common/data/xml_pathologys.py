import xml.etree.ElementTree as ET

from ..base_classes.base_sections import BaseSections
from .sections.section_pathologys import SectionPathologys
from .xml_data_provider import XmlDataProvider
from ...dict.pathology.model.pathology_model import PathologyModel


class XmlPathologys(BaseSections):
    """ Xml Сруктура для сущностей Патологий """

    def __init__(self):
        """ Конструктор """

        self.__xml_provider: XmlDataProvider = XmlDataProvider()

        self.__section = SectionPathologys()

    def get_pathology_model_from_xml_element(self, xml_element):
        """ Генерация модели Патологии из xml элемента
        :param xml_element: xml элемент
        :return: Модель Патологии
        """

        if xml_element.attrib:
            code = xml_element.attrib.get("code")
            name = xml_element.attrib.get("name")
        else:
            code = xml_element.find("code").text
            name = xml_element.find("name").text

        return PathologyModel(code, name)

    def get_pathology(self, code):
        """ Получение патологии по коду
        :param xml_element: xml элемент группы патологий
        :param code: Код патологии
        :return: Модель Патология
        """

        print(": XmlPathologys.get_pathology()")

        print("self.__xml_provider.root=", self.__xml_provider.root)
        if not self.__xml_provider.root:
            return None

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            pathology = self.get_pathology_model_from_xml_element(element)
            return pathology
        else:
            str_search = self.__section.element_name + "[@code='" + str(code) + "']"
            element = xml_group.find(str_search)
            if element is not None:
                pathology = self.get_pathology_model_from_xml_element(element)
                return pathology
        return None

    def update_pathology(self, pathology: PathologyModel):
        """ Обновление xml элемента для Патологии
        :param xml_element: xml элеммент группы патологий
        :param pathology: Модель Патология
        :return: xml
        """
        print(": XmlPathologys.update_pathology()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(pathology.code) + "']"
        xml_pathology = xml_group.find(str_search)

        print("xml_pathologys=", xml_pathology)

        if xml_pathology:
            name = xml_pathology.find("name")
            name.text = pathology.name
            return True
    def select_pathologys(self):
        """ Получение списка Патологий
        :return: Список моделей Патологий
        """

        print(": select_pathology")

        if not self.__xml_provider.root:
            return []

        pathologys = []

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        if xml_group:
            print("xml_group=", xml_group)
            for xml_pathologys in xml_group.findall(self.__section.element_name):
                pathology: PathologyModel = self.get_pathology_model_from_xml_element(xml_pathologys)

                pathologys.append(pathology)

        return pathologys

    def creat_xml_pathology(self, xml_element, pathology: PathologyModel):
        """ Создание xml элемента для модели Патологии
        :param xml_element: корневой xml элемент
        :param pathology: Модель Патологии
        """
        print(": create_xml_pathology")
        print("xml_element=",xml_element)
        print("pathology=",pathology)

        code = ET.SubElement(xml_element, "code")
        code.text = str(pathology.code)

        name = ET.SubElement(xml_element, "name")
        name.text = str(pathology.name)

        return True

    def creat_pathology(self, pathology: PathologyModel):
        """ Создание xml элемента для модели Патологии
        :param pathology: Модель Патологии
        :return: Результат выполнения
        """
        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        xml_pathology = ET.SubElement(xml_group, self.__section.element_name)

        print("xml_pathology=", xml_pathology)

        if self.creat_xml_pathology(xml_pathology, pathology):
            return True

        return False

    def delete_pathology(self, code):
        """ Удаление xml элемента по коду
        :param xml_element: xml элеммент группы патологий
        :param code: Код патологии
        :return: Результат выполнения
        """
        print(": pathology.delete")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            xml_group.remove(element)
            return True

        return False