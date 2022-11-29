import xml.etree.ElementTree as ET

from ..base_classes.base_xml_element import BaseXmlElement
from ...common.consts.Keys import Keys
from ...dict.doctors.model.doctor_model import DoctorModel


class XmlDoctors(BaseXmlElement):
    """ Xml Сруктура для сущностей Врачей """

    def __init__(self):
        """ Конструктор """

        self.group_name = Keys.DOCTORS
        self.element_name = Keys.DOCTOR

    def select_doctors(self, xml_element):
        """ Получение списка Врачей
        :param xml_element: xml элеммент группы врачей
        :return: Список моделей Врачей
        """

        print(": XmlDoctors.select_doctors()")

        # doctors = [DoctorModel]
        doctors = []

        for xml_doctor in xml_element:
            # print("xml_doctor=", xml_doctor)
            # print(xml_doctor.tag)

            doctor:DoctorModel = self.gen_doctor_model_from_xml_element(xml_doctor)
            # print(doctor)

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
        :param code: Код докора
        :return: Модель Доктор
        """

        pass

    def create_xml_doctor(self, xml_element, doctor: DoctorModel):
        """ Создание xml элемента для модели Врача
        :param xml_element: корневой xml элемент
        :param doctor: Модель Врвча
        """

        print(": XmlDoctors.create()")

        print("xml_element=", xml_element)
        print("doctor=", doctor)

        code = ET.SubElement(xml_element, "code")
        code.text = str(doctor.code)

        last_name = ET.SubElement(xml_element, "last_name")
        last_name.text = doctor.last_name

        first_name = ET.SubElement(xml_element, "first_name")
        first_name.text = doctor.first_name

        middle_name = ET.SubElement(xml_element, "middle_name")
        middle_name.text = doctor.middle_name

        ET.dump(xml_element)

    def create_xml_doctor_attributes(self, xml_element, doctor: DoctorModel):
        """ Создание xml элемента для модели Врача
        :param xml_element: xml элемент
        :param doctor: Модель Доктор
        :return: xml элемент для сущности Врач
        """

        print(": XmlDoctors.create_attribs()")

        print("xml_element=", xml_element)
        print("doctor=", doctor)

        xml_element.set("code", str(doctor.code))
        xml_element.set("last_name", doctor.last_name)
        xml_element.set("first_name", doctor.first_name)
        xml_element.set("middle_name", doctor.middle_name)

        ET.dump(xml_element)

    def update(self, doctor: DoctorModel):
        """ Обновление xml элемента для сущности Доктор
        :param doctor: Модель Доктор
        :return: xml
        """
        pass

    def delete(self, code):
        """ Удуление xml элемента по коду
        :param code: Код доктора
        :return:
        """
        pass
