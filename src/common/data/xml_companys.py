import xml.etree.ElementTree as ET

from ..base_classes.base_sections import BaseSections
from .sections.section_companys import SectionCompanys
from .xml_data_provider import XmlDataProvider
from ...dict.insuranсe_company.model.company_model import CompanyModel


class XmlCompanys(BaseSections):
    """ Xml Сруктура для сущностей Страховых компаний """

    def __init__(self):
        """ Конструктор """

        self.__xml_provider: XmlDataProvider = XmlDataProvider()

        self.__section = SectionCompanys()

    def get_company_model_from_xml_element(self, xml_element):
        """ Генерация модели Страховой компании из xml элемента
        :param xml_element: xml элемент
        :return: Модель Страховой компании
        """

        if xml_element.attrib:
            code = xml_element.attrib.get("code")
            name = xml_element.attrib.get("name")
        else:
            code = xml_element.find("code").text
            name = xml_element.find("name").text

        return CompanyModel(code, name)

    def get_company(self, code):
        """ Получение страховой компании по коду
        :param xml_element: xml элемент группы страховых компаний
        :param code: Код страховой компании
        :return: Модель Страховая компания
        """

        print(": XmlCompanys.get_company()")

        print("self.__xml_provider.root=", self.__xml_provider.root)
        if not self.__xml_provider.root:
            return None

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            company = self.get_company_model_from_xml_element(element)
            return company
        else:
            str_search = self.__section.element_name + "[@code='" + str(code) + "']"
            element = xml_group.find(str_search)
            if element is not None:
                company = self.get_company_model_from_xml_element(element)
                return company
        return None

    def update_company(self, company: CompanyModel):
        """ Обновление xml элемента для Страховой компании
        :param xml_element: xml элеммент группы страховых компаний
        :param company: Модель Страховая компания
        :return: xml
        """
        print(": XmlCompanys.update_company()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(company.code) + "']"
        xml_company = xml_group.find(str_search)

        print("xml_companys=", xml_company)

        if xml_company:
            name = xml_company.find("name")
            name.text = company.name
            return True
    def select_companys(self):
        """ Получение списка Страховых компаний
        :return: Список моделей Страховых компаний
        """

        print(": select_company")

        if not self.__xml_provider.root:
            return []

        companys = []

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        if xml_group:
            print("xml_group=", xml_group)
            for xml_companys in xml_group.findall(self.__section.element_name):
                company: CompanyModel = self.get_company_model_from_xml_element(xml_companys)

                companys.append(company)

        return companys

    def creat_xml_company(self, xml_element, company: CompanyModel):
        """ Создание xml элемента для модели Страховой компании
        :param xml_element: корневой xml элемент
        :param company: Модель Страховой компании
        """
        print(": create_xml_company")
        print("xml_element=",xml_element)
        print("company=",company)

        code = ET.SubElement(xml_element, "code")
        code.text = str(company.code)

        name = ET.SubElement(xml_element, "name")
        name.text = str(company.name)

        return True

    def creat_company(self, company: CompanyModel):
        """ Создание xml элемента для модели Страховой компании
        :param company: Модель Страховой компании
        :return: Результат выполнения
        """
        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        xml_company = ET.SubElement(xml_group, self.__section.element_name)

        print("xml_company=", xml_company)

        if self.creat_xml_company(xml_company, company):
            return True

        return False

    def delete_company(self, code):
        """ Удаление xml элемента по коду
        :param xml_element: xml элеммент группы страховых компаний
        :param code: Код страховой компании
        :return: Результат выполнения
        """
        print(": company.delete")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            xml_group.remove(element)
            return True

        return False