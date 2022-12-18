import xml.etree.ElementTree as ET

from ..base_classes.base_sections import BaseSections
from .sections.section_hospaitals import SectionHospitals
from .xml_data_provider import XmlDataProvider
from ...dict.hospital.model.hospital_model import HospitalModel


class XmlHospitals(BaseSections):
    """ Xml Сруктура для сущностей Больниц """

    def __init__(self):
        """ Конструктор """

        self.__xml_provider: XmlDataProvider = XmlDataProvider()

        self.__section = SectionHospitals()

    def get_hospital_model_from_xml_element(self, xml_element):
        """ Генерация модели Больницы из xml элемента
        :param xml_element: xml элемент
        :return: Модель Больницы
        """

        if xml_element.attrib:
            code = xml_element.attrib.get("code")
            name = xml_element.attrib.get("name")
        else:
            code = xml_element.find("code").text
            name = xml_element.find("name").text

        return HospitalModel(code, name)

    def get_hospital(self, code):
        """ Получение прибора по коду
        :param xml_element: xml элемент группы приборов
        :param code: Код прибора
        :return: Модель Больница
        """

        print(": XmlHospitals.get_hospital()")

        print("self.__xml_provider.root=", self.__xml_provider.root)
        if not self.__xml_provider.root:
            return None

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            hospital = self.get_hospital_model_from_xml_element(element)
            return hospital
        else:
            str_search = self.__section.element_name + "[@code='" + str(code) + "']"
            element = xml_group.find(str_search)
            if element is not None:
                hospital = self.get_hospital_model_from_xml_element(element)
                return hospital
        return None

    def update_hospital(self, hospital: HospitalModel):
        """ Обновление xml элемента для Больницы
        :param xml_element: xml элеммент группы приборов
        :param hospital: Модель Больница
        :return: xml
        """
        print(": XmlHospitals.update_hospital()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(hospital.code) + "']"
        xml_hospital = xml_group.find(str_search)

        print("xml_hospitals=", xml_hospital)

        if xml_hospital:
            name = xml_hospital.find("name")
            name.text = hospital.name
            return True
    def select_hospitals(self):
        """ Получение списка Больниц
        :return: Список моделей Больниц
        """

        print(": select_hospital")

        if not self.__xml_provider.root:
            return []

        hospitals = []

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        if xml_group:
            print("xml_group=", xml_group)
            for xml_hospitals in xml_group.findall(self.__section.element_name):
                hospital: HospitalModel = self.get_hospital_model_from_xml_element(xml_hospitals)

                hospitals.append(hospital)

        return hospitals

    def creat_xml_hospital(self, xml_element, hospital: HospitalModel):
        """ Создание xml элемента для модели Больницы
        :param xml_element: корневой xml элемент
        :param hospital: Модель Больницы
        """
        print(": create_xml_hospital")
        print("xml_element=",xml_element)
        print("hospital=",hospital)

        code = ET.SubElement(xml_element, "code")
        code.text = str(hospital.code)

        name = ET.SubElement(xml_element, "name")
        name.text = str(hospital.name)

        return True

    def creat_hospital(self, hospital: HospitalModel):
        """ Создание xml элемента для модели Больницы
        :param hospital: Модель Больницы
        :return: Результат выполнения
        """
        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        print("xml_group=", xml_group)

        xml_hospital = ET.SubElement(xml_group, self.__section.element_name)

        print("xml_hospital=", xml_hospital)

        if self.creat_xml_hospital(xml_hospital, hospital):
            return True

        return False

    def delete_hospital(self, code):
        """ Удаление xml элемента по коду
        :param xml_element: xml элеммент группы приборов
        :param code: Код прибора
        :return: Результат выполнения
        """
        print(": hospital.delete")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.__section.group_name)

        str_search = self.__section.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            xml_group.remove(element)
            return True

        return False