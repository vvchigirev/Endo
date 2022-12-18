import xml.etree.ElementTree as ET

from ..base_classes.base_sections import BaseSections
from ...common.consts.Keys import Keys
from .xml_data_provider import XmlDataProvider
from ...dict.hospital.model.hospital_model import HospitalModel


class XmlHospitals(BaseSections):
    """ Xml Сруктура для сущностей Больниц """

    def __init__(self, xml_provider: XmlDataProvider = None):
        """ Конструктор
        :param xml_provider: Xml провайдер
        """

        self.__xml_provider: XmlDataProvider = xml_provider

        self.group_name = Keys.HOSPITALS
        self.element_name = Keys.HOSPITAL

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
        """ Получение больницы по коду
        :param xml_element: xml элеммент группы больниц
        :param code: Код больницы
        :return: Модель Больница
        """
        print(": hospital.get_hospital()")

        if not self.__xml_provider.root:
            return None

        xml_group = self.__xml_provider.root.find(self.group_name)

        str_search = self.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            hospital = self.get_hospital_model_from_xml_element(element)
            return hospital
        else:
            str_search = self.element_name + "[@code='" + str(code) + "']"
            element = xml_group.find(str_search)
            if element is not None:
                hospital = self.get_hospital_model_from_xml_element(element)
                return hospital
        return None

    def update_hospital(self, hospital: HospitalModel):
        """ Обновление xml элемента для Больницы
        :param xml_element: xml элеммент группы больниц
        :param hospital: Модель Больница
        :return: xml
        """
        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.group_name)

        str_search = self.element_name + "[code='" + str(hospital.code) + "']"
        xml_hospital = xml_group.find(str_search)

        if xml_hospital:
            name = xml_hospital.find("name")
            name.text = hospital.name

    def select_hospitals(self):
        """ Получение списка Больниц
        :return: Список моделей Больниц
        """

        print(": select_hospital")

        if not self.__xml_provider.root:
            return []

        hospitals = []

        xml_group = self.__xml_provider.root.find(self.group_name)

        if xml_group:
            print("xml_group=", xml_group)
            for xml_hospitals in xml_group.findall(self.element_name):
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

        xml_group = self.__xml_provider.root.find(self.group_name)

        print("xml_group=", xml_group)

        xml_hospital = ET.SubElement(xml_group, self.element_name)

        print("xml_hospital=", xml_hospital)

        if self.creat_xml_hospital(xml_hospital, hospital):
            return True

        return False

    def delete_hospital(self, code):
        """ Удаление xml элемента по коду
        :param xml_element: xml элеммент группы больниц
        :param code: Код больницы
        :return: Результат выполнения
        """
        print(": hospital.delete")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.group_name)

        str_search = self.element_name + "[code='" + str(code) + "']"

        element = xml_group.find(str_search)

        if element:
            xml_group.remove(element)
            return True

        return False