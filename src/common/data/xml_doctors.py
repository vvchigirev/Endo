import xml.etree.ElementTree as ET

from ..base_classes.base_sections import BaseSections
from ...common.consts.Keys import Keys
from .xml_data_provider import XmlDataProvider
from ...dict.doctors.model.doctor_model import DoctorModel


class XmlDoctors(BaseSections):
    """ Xml Сруктура для сущностей Врачей """

    __xml_provider = None  # Провайдер данных XML

    def __init__(self, xml_provider: XmlDataProvider = None):
        """ Конструктор
        :param xml_provider: Xml провайдер
        """

        self.__xml_provider: XmlDataProvider = xml_provider

        self.group_name = Keys.DOCTORS
        self.element_name = Keys.DOCTOR

    def select_doctors(self):
        """ Получение списка Врачей
        :return: Список моделей Врачей
        """

        print(": XmlDoctors.select_doctors()")

        if not self.__xml_provider.root:
            return []

        doctors = []

        xml_group = self.__xml_provider.root.find(self.group_name)

        if xml_group:
            print("xml_group=", xml_group)
            for xml_doctor in xml_group.findall(self.element_name):
                doctor: DoctorModel = self.gen_doctor_model_from_xml_element(xml_doctor)

                doctors.append(doctor)

        return doctors

    def gen_doctor_model_from_xml_element(self, xml_element):
        """ Генерация модели Врача из xml элемента
        :param xml_element: xml элемент
        :return: Модель Врач
        """

        # print(": XmlDoctors.gen_doctor_model_from_xml_element()")

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

        return DoctorModel(code, l_name, f_name, m_name)

    def get_doctor(self, code):
        """ Получение доктора по коду
        :param xml_element: xml элеммент группы врачей
        :param code: Код докора
        :return: Модель Доктор
        """

        print(": XmlDoctors.get_doctor()")

        if not self.__xml_provider.root:
            return None

        xml_group = self.__xml_provider.root.find(self.group_name)

        str_search = self.element_name + "[code='" + str(code) + "']"
        element = xml_group.find(str_search)

        if element:
            doctor = self.gen_doctor_model_from_xml_element(element)
            return doctor
        else:
            str_search = self.element_name + "[@code='" + str(code) + "']"
            element = xml_group.find(str_search)
            if element is not None:
                doctor = self.gen_doctor_model_from_xml_element(element)
                return doctor
        return None

    def create_doctor(self, doctor: DoctorModel, is_attribs = False):
        """ Создание xml элемента для модели Врача
        :param doctor: Модель Врвча
        :return: Результат выполнения
        """

        print(": XmlDoctors.create_doctor()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.group_name)
        xml_doctor = ET.SubElement(xml_group, self.element_name)

        if is_attribs:
            if self.create_xml_doctor_attributes(xml_doctor, doctor):
                return True
        else:
            if self.create_xml_doctor(xml_doctor, doctor):
                return True

        return False

    def create_xml_doctor(self, xml_element, doctor: DoctorModel):
        """ Создание xml элемента для модели Врача
        :param xml_element: корневой xml элемент
        :param doctor: Модель Врвча
        """

        print(": XmlDoctors.create_xml_doctor()")

        code = ET.SubElement(xml_element, "code")
        code.text = str(doctor.code)

        last_name = ET.SubElement(xml_element, "last_name")
        last_name.text = doctor.last_name

        first_name = ET.SubElement(xml_element, "first_name")
        first_name.text = doctor.first_name

        middle_name = ET.SubElement(xml_element, "middle_name")
        middle_name.text = doctor.middle_name

        # ET.dump(xml_element)

        return True

    def create_xml_doctor_attributes(self, xml_element, doctor: DoctorModel):
        """ Создание xml элемента для модели Врача
        :param xml_element: xml элемент
        :param doctor: Модель Доктор
        :return: xml элемент для сущности Врач
        """

        print(": XmlDoctors.create_attribs()")

        xml_element.set("code", str(doctor.code))
        xml_element.set("last_name", doctor.last_name)
        xml_element.set("first_name", doctor.first_name)
        xml_element.set("middle_name", doctor.middle_name)

        # ET.dump(xml_element)

        return True

    def update_doctor(self, doctor: DoctorModel):
        """ Обновление xml элемента для сущности Доктор
        :param xml_element: xml элеммент группы врачей
        :param doctor: Модель Доктор
        :return: xml
        """

        print(": XmlDoctors.update_doctor()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.group_name)

        str_search = self.element_name + "[code='" + str(doctor.code) + "']"
        xml_doctor = xml_group.find(str_search)

        if xml_doctor:
            last_name = xml_doctor.find("last_name")
            last_name.text = doctor.last_name

            first_name = xml_doctor.find("first_name")
            first_name.text = doctor.first_name

            middle_name = xml_doctor.find("middle_name")
            middle_name.text = doctor.middle_name

            return True

        return False

    def delete_doctor(self, code):
        """ Удуление xml элемента по коду
        :param xml_element: xml элеммент группы врачей
        :param code: Код докора
        :return:
        """

        print(": XmlDoctors.delete_doctor()")

        if not self.__xml_provider.root:
            return False

        xml_group = self.__xml_provider.root.find(self.group_name)

        str_search = self.element_name + "[code='" + str(code) + "']"
        print("str=", str_search)
        element = xml_group.find(str_search)

        if element:
            xml_group.remove(element)
            return True

        return False