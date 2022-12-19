import xml.etree.ElementTree as ET

from ..base_classes.base_sections import BaseSections
from .sections.section_endos import SectionEndos
from .xml_data_provider import XmlDataProvider
from ...dict.endos.model.endo_model import EndoModel


class XmlEndos(BaseSections):
    """ Xml Сруктура для сущностей Эндоскопий """

    __xml_provider = None  # Провайдер данных XML

    def __init__(self):
        """ Конструктор
        :param xml_provider: Xml провайдер
        """

        print(": XmlEndos.__init__()")

        self.__xml_provider: XmlDataProvider = XmlDataProvider()

        self.__section = SectionEndos()

    def select_endos(self):
        """ Получение списка Эндоскопий
        :return: Список моделей Эндоскопий
        """

        print(": XmlEndos.select_endos()")

        if not XmlDataProvider.root:
            return []

        endos = []

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        if xml_group:
            # print("xml_group=", xml_group)
            for xml_endo in xml_group.findall(self.__section.element_name):
                endo: EndoModel = self.gen_endo_model_from_xml_element(xml_endo)

                endos.append(endo)

        return endos

    def gen_endo_model_from_xml_element(self, xml_element):
        """ Генерация модели Эндоскопии из xml элемента
        :param xml_element: xml элемент
        :return: Модель Эндоскопия
        """

        # print(": XmlEndos.gen_endo_model_from_xml_element()")

        if xml_element.attrib:
            code = xml_element.get("code")
            name = xml_element.get("name")
            YET = xml_element.get("YET")
        else:
            code = xml_element.get("code").text
            name = xml_element.get("name").text
            YET = xml_element.get("YET").text

        return EndoModel(code, name, YET)

    def get_endo(self, code):
        """ Получение эндоскопии по коду
        :param xml_element: xml элеммент группы эндоскопий
        :param code: Код докора
        :return: Модель Доктор
        """

        print(": XmlEndos.get_endo()")

        if not self.__xml_provider.root:
            return None

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            endo = self.gen_endo_model_from_xml_element(element)
            return endo
        else:
            str_search = self.__section.element_name + "[@code='" + str(code) + "']"
            element = xml_group.find(str_search)
            if element is not None:
                endo = self.gen_endo_model_from_xml_element(element)
                return endo
        return None

    def create_endo(self, endo: EndoModel, is_attribs = False):
        """ Создание xml элемента для модели Эндоскопии
        :param endo: Модель Врвча
        :return: Результат выполнения
        """

        print(": XmlEndos.create_endo()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)
        xml_endo = ET.SubElement(xml_group, self.__section.element_name)

        if is_attribs:
            if self.create_xml_endo_attributes(xml_endo, endo):
                return True
        else:
            if self.create_xml_endo(xml_endo, endo):
                return True

        return False

    def create_xml_endo(self, xml_element, endo: EndoModel):
        """ Создание xml элемента для модели Эндоскопии
        :param xml_element: корневой xml элемент
        :param endo: Модель Врвча
        """

        print(": XmlEndos.create_xml_endo()")

        code = ET.SubElement(xml_element, "code")
        code.text = str(endo.code)

        name = ET.SubElement(xml_element, "name")
        name.text = endo.name

        YET = ET.SubElement(xml_element, "YET")
        YET.text = endo.YET


        # ET.dump(xml_element)

        return True

    def create_xml_endo_attributes(self, xml_element, endo: EndoModel):
        """ Создание xml элемента для модели Эндоскопии
        :param xml_element: xml элемент
        :param endo: Модель Эндоскопия
        :return: xml элемент для сущности Эндоскопия
        """

        print(": XmlEndos.create_attribs()")

        xml_element.set("code", str(endo.code))
        xml_element.set("name", endo.name)
        xml_element.set("YET", endo.YET)

        # ET.dump(xml_element)

        return True

    def update_endo(self, endo: EndoModel):
        """ Обновление xml элемента для сущности Эндоскопия
        :param xml_element: xml элеммент группы эндоскопий
        :param endo: Модель Эндоскопия
        :return: xml
        """

        print(": XmlEndos.update_endo()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(endo.code) + "']"
        xml_endo = xml_group.find(str_search)

        if xml_endo:
            name = xml_endo.find("name")
            name.text = endo.name

            YET = xml_endo.find("YET")
            YET.text = endo.YET

            return True

        return False

    def delete_endo(self, code):
        """ Удуление xml элемента по коду
        :param xml_element: xml элеммент группы эндоскопий
        :param code: Код докора
        :return:
        """

        print(": XmlEndos.delete_endo()")

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