import xml.etree.ElementTree as ET

from ..base_classes.base_sections import BaseSections
from .sections.section_reasons import SectionReasons
from .xml.xml_data_provider import XmlDataProvider
from ...dict.reason.model.reason_model import ReasonModel


class XmlReasons(BaseSections):
    """ Xml Сруктура для сущностей причин обращения """

    def __init__(self):
        """ Конструктор """

        self.__xml_provider: XmlDataProvider = XmlDataProvider()

        self.__section = SectionReasons()

    def get_reason_model_from_xml_element(self, xml_element):
        """ Генерация модели Причины обращения из xml элемента
        :param xml_element: xml элемент
        :return: Модель Причины обращения
        """

        if xml_element.attrib:
            code = xml_element.attrib.get("code")
            name = xml_element.attrib.get("name")
        else:
            code = xml_element.find("code").text
            name = xml_element.find("name").text

        return ReasonModel(code, name)

    def get_reason(self, code):
        """ Получение причины обращения по коду
        :param xml_element: xml элемент группы причин обращения
        :param code: Код причины обращения
        :return: Модель Причина обращения
        """

        print(": XmlReasons.get_reason()")

        print("self.__xml_provider.root=", self.__xml_provider.root)
        if not self.__xml_provider.root:
            return None

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            reason = self.get_reason_model_from_xml_element(element)
            return reason
        else:
            str_search = self.__section.element_name + "[@code='" + str(code) + "']"
            element = xml_group.find(str_search)
            if element is not None:
                reason = self.get_reason_model_from_xml_element(element)
                return reason
        return None

    def update_reason(self, reason: ReasonModel):
        """ Обновление xml элемента для Причины обращения
        :param xml_element: xml элеммент группы причин обращения
        :param reason: Модель Причина обращения
        :return: xml
        """
        print(": XmlReasons.update_reason()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(reason.code) + "']"
        xml_reason = xml_group.find(str_search)

        print("xml_reasons=", xml_reason)

        if xml_reason:
            name = xml_reason.find("name")
            name.text = reason.name
            return True
    def select_reasons(self):
        """ Получение списка причин обращения
        :return: Список моделей причин обращения
        """

        print(": select_reason")

        if not self.__xml_provider.root:
            return []

        reasons = []

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        if xml_group:
            print("xml_group=", xml_group)
            for xml_reasons in xml_group.findall(self.__section.element_name):
                reason: ReasonModel = self.get_reason_model_from_xml_element(xml_reasons)

                reasons.append(reason)

        return reasons

    def creat_xml_reason(self, xml_element, reason: ReasonModel):
        """ Создание xml элемента для модели Причины обращения
        :param xml_element: корневой xml элемент
        :param reason: Модель Причины обращения
        """
        print(": create_xml_reason")
        print("xml_element=",xml_element)
        print("reason=",reason)

        code = ET.SubElement(xml_element, "code")
        code.text = str(reason.code)

        name = ET.SubElement(xml_element, "name")
        name.text = str(reason.name)

        return True

    def creat_reason(self, reason: ReasonModel):
        """ Создание xml элемента для модели Причины обращения
        :param reason: Модель Причины обращения
        :return: Результат выполнения
        """
        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        xml_reason = ET.SubElement(xml_group, self.__section.element_name)

        print("xml_reason=", xml_reason)

        if self.creat_xml_reason(xml_reason, reason):
            return True

        return False

    def delete_reason(self, code):
        """ Удаление xml элемента по коду
        :param xml_element: xml элеммент группы причин обращения
        :param code: Код причины обращения
        :return: Результат выполнения
        """
        print(": reason.delete")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            xml_group.remove(element)
            return True

        return False