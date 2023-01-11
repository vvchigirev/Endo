import xml.etree.ElementTree as ET

from ..base_classes.base_sections import BaseSections
from .sections.section_biopsys import SectionBiopsys
from .xml.xml_data_provider import XmlDataProvider
from ...dict.biopsy.model.biopsy_moidel import BiopsyModel


class XmlBiopsys(BaseSections):
    """ Xml Сруктура для сущностей Биопсий """

    def __init__(self):
        """ Конструктор """

        self.__xml_provider: XmlDataProvider = XmlDataProvider()

        self.__section = SectionBiopsys()

    def get_biopsy_model_from_xml_element(self, xml_element):
        """ Генерация модели Биопсии из xml элемента
        :param xml_element: xml элемент
        :return: Модель Биопсии
        """

        if xml_element.attrib:
            code = xml_element.attrib.get("code")
            name = xml_element.attrib.get("name")
        else:
            code = xml_element.find("code").text
            name = xml_element.find("name").text

        return BiopsyModel(code, name)

    def get_biopsy(self, code):
        """ Получение биопсии по коду
        :param xml_element: xml элемент группы биопсий
        :param code: Код биопсии
        :return: Модель Прибор
        """

        print(": XmlBiopsys.get_biopsy()")

        print("self.__xml_provider.root=", self.__xml_provider.root)
        if not self.__xml_provider.root:
            return None

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            biopsy = self.get_biopsy_model_from_xml_element(element)
            return biopsy
        else:
            str_search = self.__section.element_name + "[@code='" + str(code) + "']"
            element = xml_group.find(str_search)
            if element is not None:
                biopsy = self.get_biopsy_model_from_xml_element(element)
                return biopsy
        return None

    def update_biopsy(self, biopsy: BiopsyModel):
        """ Обновление xml элемента для Биопсии
        :param xml_element: xml элеммент группы биопсий
        :param biopsy: Модель Прибор
        :return: xml
        """
        print(": XmlBiopsys.update_biopsy()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(biopsy.code) + "']"
        xml_biopsy = xml_group.find(str_search)

        print("xml_biopsys=", xml_biopsy)

        if xml_biopsy:
            name = xml_biopsy.find("name")
            name.text = biopsy.name
            return True
    def select_biopsys(self):
        """ Получение списка Биопсий
        :return: Список моделей Биопсий
        """

        print(": select_biopsy")

        if not self.__xml_provider.root:
            return []

        biopsys = []

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        if xml_group:
            print("xml_group=", xml_group)
            for xml_biopsys in xml_group.findall(self.__section.element_name):
                biopsy: BiopsyModel = self.get_biopsy_model_from_xml_element(xml_biopsys)

                biopsys.append(biopsy)

        return biopsys

    def creat_xml_biopsy(self, xml_element, biopsy: BiopsyModel):
        """ Создание xml элемента для модели Биопсии
        :param xml_element: корневой xml элемент
        :param biopsy: Модель Биопсии
        """
        print(": create_xml_biopsy")
        print("xml_element=",xml_element)
        print("biopsy=",biopsy)

        code = ET.SubElement(xml_element, "code")
        code.text = str(biopsy.code)

        name = ET.SubElement(xml_element, "name")
        name.text = str(biopsy.name)

        return True

    def creat_biopsy(self, biopsy: BiopsyModel):
        """ Создание xml элемента для модели Биопсии
        :param biopsy: Модель Биопсии
        :return: Результат выполнения
        """
        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        xml_biopsy = ET.SubElement(xml_group, self.__section.element_name)

        print("xml_biopsy=", xml_biopsy)

        if self.creat_xml_biopsy(xml_biopsy, biopsy):
            return True

        return False

    def delete_biopsy(self, code):
        """ Удаление xml элемента по коду
        :param xml_element: xml элеммент группы биопсий
        :param code: Код биопсии
        :return: Результат выполнения
        """
        print(": biopsy.delete")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            xml_group.remove(element)
            return True

        return False