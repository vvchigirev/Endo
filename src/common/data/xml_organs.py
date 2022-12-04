import xml.etree.ElementTree as ET

from ..base_classes.base_sections import BaseSections
from ...common.consts.Keys import Keys
from .xml_data_provider import XmlDataProvider
from ...dict.organs.model.organ_model import OrganModel


class XmlOrgans(BaseSections):
    """ Xml Сруктура для сущностей Органов """

    def __init__(self, xml_provider: XmlDataProvider = None):
        """ Конструктор
        :param xml_provider: Xml провайдер
        """

        self.__xml_provider: XmlDataProvider = xml_provider

        self.group_name = Keys.ORGANS
        self.element_name = Keys.ORGAN

    def get_organ_model_from_xml_element(self, xml_element):
        """ Генерация модели Органа из xml элемента
        :param xml_element: xml элемент
        :return: Модель Органа
        """

        if xml_element.attrib:
            code = xml_element.attrib.get("code")
            name = xml_element.attrib.get("name")
        else:
            code = xml_element.find("code").text
            name = xml_element.find("name").text

        return OrganModel(code, name)

    def get_organ(self, code):
        """ Получение органа по коду
        :param xml_element: xml элеммент группы органов
        :param code: Код органа
        :return: Модель Орган
        """
        print(": organ.get_organ()")

        if not self.__xml_provider.root:
            return None

        xml_group = self.__xml_provider.root.find(self.group_name)

        str_search = self.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            organ = self.get_organ_model_from_xml_element(element)
            return organ
        else:
            str_search = self.element_name + "[@code='" + str(code) + "']"
            element = xml_group.find(str_search)
            if element is not None:
                organ = self.get_organ_model_from_xml_element(element)
                return organ
        return None

    def update_organ(self, organ: OrganModel):
        """ Обновление xml элемента для Органа
        :param xml_element: xml элеммент группы органов
        :param organ: Модель Орган
        :return: xml
        """
        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.group_name)

        str_search = self.element_name + "[code='" + str(organ.code) + "']"
        xml_organ = xml_group.find(str_search)

        if xml_organ:
            name = xml_organ.find("name")
            name.text = organ.name

    def select_organs(self):
        """ Получение списка Органов
        :return: Список моделей Органов
        """

        print(": select_organ")

        if not self.__xml_provider.root:
            return []

        organs = []

        xml_group = self.__xml_provider.root.find(self.group_name)

        if xml_group:
            print("xml_group=", xml_group)
            for xml_organs in xml_group.findall(self.element_name):
                organ: OrganModel = self.get_organ_model_from_xml_element(xml_organs)

                organs.append(organ)

        return organs

    def creat_xml_organ(self, xml_element, organ: OrganModel):
        """ Создание xml элемента для модели Органа
        :param xml_element: корневой xml элемент
        :param organ: Модель Органа
        """
        print(": create_xml_organ")
        print("xml_element=",xml_element)
        print("organ=",organ)

        code = ET.SubElement(xml_element, "code")
        code.text = str(organ.code)

        name = ET.SubElement(xml_element, "name")
        name.text = str(organ.name)

        return True

    def creat_organ(self, organ: OrganModel):
        """ Создание xml элемента для модели Органа
        :param organ: Модель Органа
        :return: Результат выполнения
        """
        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.group_name)

        print("xml_group=", xml_group)

        xml_organ = ET.SubElement(xml_group, self.element_name)

        print("xml_organ=", xml_organ)

        if self.creat_xml_organ(xml_organ, organ):
            return True

        return False

    def delete_organ(self, code):
        """ Удаление xml элемента по коду
        :param xml_element: xml элеммент группы органов
        :param code: Код органа
        :return: Результат выполнения
        """
        print(": organ.delete")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.group_name)

        str_search = self.element_name + "[code='" + str(code) + "']"

        element = xml_group.find(str_search)

        if element:
            xml_group.remove(element)
            return True

        return False