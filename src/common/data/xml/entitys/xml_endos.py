import xml.etree.ElementTree as ET

from src.common.base_classes.base_sections import BaseSections
from src.common.data.xml.sections.section_endos import SectionEndos
from src.common.data.xml.xml_data_provider import XmlDataProvider
from src.dict.endos.model.endo_model import EndoModel


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
                print("xml_endo=", xml_endo)

                endo: EndoModel = self.gen_endo_model_from_xml_element(xml_endo)

                endos.append(endo)

        return endos

    def gen_endo_model_from_xml_element(self, xml_element):
        """ Генерация модели Эндоскопии из xml элемента
        :param xml_element: xml элемент
        :return: Модель Эндоскопия
        """

        print(": XmlEndos.gen_endo_model_from_xml_element()")

        ET.dump(xml_element)

        code = xml_element.find("code").text
        print("code=", code)
        name = xml_element.find("name").text
        print("name=", name)
        uet = xml_element.find("uet").text
        print("uet=", uet)

        return EndoModel(code, name, uet)

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

    def get_endo_model_from_xml_element(self, xml_element):
        """ Генерация модели Эндоскопии из xml элемента
        :param xml_element: xml элемент
        :return: Модель Эндоскопии
        """

        if xml_element.attrib:
            code = xml_element.attrib.get("code")
            name = xml_element.attrib.get("name")
            uet = xml_element.attrib.get("uet")
        else:
            code = xml_element.find("code").text
            name = xml_element.find("name").text
            uet = xml_element.find("uet").text

        return EndoModel(code, name, uet)

    def create_endo(self, endo: EndoModel, is_attribs=False):
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
        name.text = str(endo.name)

        uet = ET.SubElement(xml_element, "uet")
        uet.text = str(endo.uet)

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
        xml_element.set("uet", endo.uet)

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

        try:
            if xml_endo:
                code = xml_endo.find("code")
                code.text = endo.code

                name = xml_endo.find("name")
                name.text = endo.name

                uet = str(xml_endo.find("uet").text)
                uet = endo.uet

                return True
        except Exception as e:
            print("e=", e)
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

            str_search = self.__section.element_name + "[code='" + str(code) + "']"
            element = xml_group.find(str_search)

            if element:
                xml_group.remove(element)
                return True

        except Exception as e:
            print("e=", e)

        return False
