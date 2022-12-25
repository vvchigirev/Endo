import xml.etree.ElementTree as ET

from ..base_classes.base_sections import BaseSections
from .sections.section_iendo import SectionIEndos
from .xml_data_provider import XmlDataProvider
from ...dict.iendo.model.iendo_model import IEndoModel


class XmlIEndos(BaseSections):
    """ Xml Сруктура для сущностей Приборов """

    def __init__(self):
        """ Конструктор """

        self.__xml_provider: XmlDataProvider = XmlDataProvider()

        self.__section = SectionIEndos()

    def get_iendo_model_from_xml_element(self, xml_element):
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

        return IEndoModel(code, name)

    def get_iendo(self, code):
        """ Получение прибора по коду
        :param xml_element: xml элемент группы приборов
        :param code: Код прибора
        :return: Модель Прибор
        """

        print(": XmlIEndos.get_iendo()")

        print("self.__xml_provider.root=", self.__xml_provider.root)
        if not self.__xml_provider.root:
            return None

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            iendo = self.get_iendo_model_from_xml_element(element)
            return iendo
        else:
            str_search = self.__section.element_name + "[@code='" + str(code) + "']"
            element = xml_group.find(str_search)
            if element is not None:
                iendo = self.get_iendo_model_from_xml_element(element)
                return iendo
        return None

    def update_iendo(self, iendo: IEndoModel):
        """ Обновление xml элемента для Прибора
        :param xml_element: xml элеммент группы приборов
        :param iendo: Модель Прибор
        :return: xml
        """
        print(": XmlIEndos.update_iendo()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(iendo.code) + "']"
        xml_iendo = xml_group.find(str_search)

        print("xml_iendos=", xml_iendo)

        if xml_iendo:
            name = xml_iendo.find("name")
            name.text = iendo.name
            return True
    def select_iendos(self):
        """ Получение списка Приборов
        :return: Список моделей Приборов
        """

        print(": select_iendo")

        if not self.__xml_provider.root:
            return []

        iendos = []

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        if xml_group:
            print("xml_group=", xml_group)
            for xml_iendos in xml_group.findall(self.__section.element_name):
                iendo: IEndoModel = self.get_iendo_model_from_xml_element(xml_iendos)

                iendos.append(iendo)

        return iendos

    def creat_xml_iendo(self, xml_element, iendo: IEndoModel):
        """ Создание xml элемента для модели Прибора
        :param xml_element: корневой xml элемент
        :param iendo: Модель Прибора
        """
        print(": create_xml_iendo")
        print("xml_element=",xml_element)
        print("iendo=",iendo)

        code = ET.SubElement(xml_element, "code")
        code.text = str(iendo.code)

        name = ET.SubElement(xml_element, "name")
        name.text = str(iendo.name)

        return True

    def creat_iendo(self, iendo: IEndoModel):
        """ Создание xml элемента для модели Прибора
        :param iendo: Модель Прибора
        :return: Результат выполнения
        """
        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        xml_iendo = ET.SubElement(xml_group, self.__section.element_name)

        print("xml_iendo=", xml_iendo)

        if self.creat_xml_iendo(xml_iendo, iendo):
            return True

        return False

    def delete_iendo(self, code):
        """ Удаление xml элемента по коду
        :param xml_element: xml элеммент группы приборов
        :param code: Код прибора
        :return: Результат выполнения
        """
        print(": iendo.delete")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            xml_group.remove(element)
            return True

        return False