import xml.etree.ElementTree as ET

from ..base_classes.base_sections import BaseSections
from .sections.section_nurses import SectionNurses
from .xml.xml_data_provider import XmlDataProvider
from ...dict.nurse.model.nurse_model import NurseModel


class XmlNurses(BaseSections):
    """ Xml Сруктура для сущностей Мед сестраей """

    __xml_provider = None  # Провайдер данных XML

    def __init__(self):
        """ Конструктор
        :param xml_provider: Xml провайдер
        """

        print(": XmlNurses.__init__()")

        self.__xml_provider: XmlDataProvider = XmlDataProvider()

        self.__section = SectionNurses()

    def select_nurses(self):
        """ Получение списка Мед сестраей
        :return: Список моделей Мед сестраей
        """

        print(": XmlNurses.select_nurses()")

        if not XmlDataProvider.root:
            return []

        nurses = []

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        if xml_group:
            # print("xml_group=", xml_group)
            for xml_nurse in xml_group.findall(self.__section.element_name):
                nurse: NurseModel = self.gen_nurse_model_from_xml_element(xml_nurse)

                nurses.append(nurse)

        return nurses

    def gen_nurse_model_from_xml_element(self, xml_element):
        """ Генерация модели Мед сестраа из xml элемента
        :param xml_element: xml элемент
        :return: Модель Мед сестра
        """

        # print(": XmlNurses.gen_nurse_model_from_xml_element()")

        if xml_element.attrib:
            code = xml_element.get("code")
            l_name = xml_element.get("last_name")
            f_name = xml_element.get("first_name")
            m_name = xml_element.get("middle_name")
        else:
            code = xml_element.find("code").text
            l_name = xml_element.find("last_name").text
            f_name = xml_element.find("first_name").text
            m_name = xml_element.find("middle_name").text

        return NurseModel(code, l_name, f_name, m_name)

    def get_nurse(self, code):
        """ Получение доктора по коду
        :param xml_element: xml элеммент группы мед сестраей
        :param code: Код докора
        :return: Модель Доктор
        """

        print(": XmlNurses.get_nurse()")

        if not self.__xml_provider.root:
            return None

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            nurse = self.gen_nurse_model_from_xml_element(element)
            return nurse
        else:
            str_search = self.__section.element_name + "[@code='" + str(code) + "']"
            element = xml_group.find(str_search)
            if element is not None:
                nurse = self.gen_nurse_model_from_xml_element(element)
                return nurse
        return None

    def create_nurse(self, nurse: NurseModel, is_attribs = False):
        """ Создание xml элемента для модели Мед сестраа
        :param nurse: Модель Врвча
        :return: Результат выполнения
        """

        print(": XmlNurses.create_nurse()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)
        xml_nurse = ET.SubElement(xml_group, self.__section.element_name)

        if is_attribs:
            if self.create_xml_nurse_attributes(xml_nurse, nurse):
                return True
        else:
            if self.create_xml_nurse(xml_nurse, nurse):
                return True

        return False

    def create_xml_nurse(self, xml_element, nurse: NurseModel):
        """ Создание xml элемента для модели Мед сестраа
        :param xml_element: корневой xml элемент
        :param nurse: Модель Врвча
        """

        print(": XmlNurses.create_xml_nurse()")

        code = ET.SubElement(xml_element, "code")
        code.text = str(nurse.code)

        last_name = ET.SubElement(xml_element, "last_name")
        last_name.text = nurse.last_name

        first_name = ET.SubElement(xml_element, "first_name")
        first_name.text = nurse.first_name

        middle_name = ET.SubElement(xml_element, "middle_name")
        middle_name.text = nurse.middle_name

        # ET.dump(xml_element)

        return True

    def create_xml_nurse_attributes(self, xml_element, nurse: NurseModel):
        """ Создание xml элемента для модели Мед сестраа
        :param xml_element: xml элемент
        :param nurse: Модель Доктор
        :return: xml элемент для сущности Мед сестра
        """

        print(": XmlNurses.create_attribs()")

        xml_element.set("code", str(nurse.code))
        xml_element.set("last_name", nurse.last_name)
        xml_element.set("first_name", nurse.first_name)
        xml_element.set("middle_name", nurse.middle_name)

        # ET.dump(xml_element)

        return True

    def update_nurse(self, nurse: NurseModel):
        """ Обновление xml элемента для сущности Доктор
        :param xml_element: xml элеммент группы мед сестраей
        :param nurse: Модель Доктор
        :return: xml
        """

        print(": XmlNurses.update_nurse()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(nurse.code) + "']"
        xml_nurse = xml_group.find(str_search)

        if xml_nurse:
            last_name = xml_nurse.find("last_name")
            last_name.text = nurse.last_name

            first_name = xml_nurse.find("first_name")
            first_name.text = nurse.first_name

            middle_name = xml_nurse.find("middle_name")
            middle_name.text = nurse.middle_name

            return True

        return False

    def delete_nurse(self, code):
        """ Удуление xml элемента по коду
        :param xml_element: xml элеммент группы мед сестраей
        :param code: Код докора
        :return:
        """

        print(": XmlNurses.delete_nurse()")

        try:
            if not self.__xml_provider.root:
                return False

            xml_group = self.__xml_provider.root.find(self.__section.group_name)
            print("xml_group=", xml_group)

            str_search = self.__section.element_name + "[code='" + str(code) + "']"
            print("str=", str_search)
            element = xml_group.find(str_search)

            print("element=", element)
            if element:
                xml_group.remove(element)
                return True
        except Exception as e:
            print("e=", e)

        return False