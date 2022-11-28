import xml.etree.ElementTree as ET

from ..base_classes.base_xml_element import BaseXmlElement
from ...common.consts.Keys import Keys
from ...dict.doctors.models.doctor_model import DoctorModel


class XmlDoctors(BaseXmlElement):
    """ Xml Сруктура для сущностей Врачей """

    def __init__(self):
        """ Конструктор """

        self.group_name = Keys.DOCTORS
        self.element_name = Keys.DOCTOR

    def select(self):
        """ Получение докторов
        :return: Список моделей Доктор
        """

        pass

    def get(self, code):
        """ Получение доктора по коду
        :param code: Код докора
        :return: Модель Доктор
        """

        pass

    # def create(self, doctor: DoctorModel):
    #     """ Создание xml элемента для модели доктора
    #     :param doctor: Модель Доктор
    #     :return: xml элемент для сущности Доктор
    #     """
    #
    #     print(": XmlDoctors.create()")
    #
    #     print("self.element_name=", self.element_name)
    #
    #     xml_doctor = ET.Element(self.element_name)
    #     print("xml_doctor=", xml_doctor)
    #     ET.dump(xml_doctor)
    #
    #     code = ET.SubElement(xml_doctor, "code")
    #     code.text = str(doctor.kode)
    #
    #     last_name = ET.SubElement(xml_doctor, "last_name")
    #     last_name.text = doctor.last_name
    #
    #     first_name = ET.SubElement(xml_doctor, "f_name")
    #     first_name.text = doctor.first_name
    #
    #     middle_name = ET.SubElement(xml_doctor, "m_name")
    #     middle_name.text = doctor.middle_name
    #
    #     ET.dump(xml_doctor)
    #
    #     # self.__x
    #
    #     return xml_doctor
    def create(self, xml_element, doctor: DoctorModel):
        """ Создание xml элемента для модели доктора
        :param xml_element: корневой xml элемент
        :param doctor: Модель Врвча
        """

        print(": XmlDoctors.create()")

        print("xml_element=", xml_element)
        print("doctor=", doctor)

        code = ET.SubElement(xml_element, "code")
        code.text = str(doctor.kode)

        last_name = ET.SubElement(xml_element, "last_name")
        last_name.text = doctor.last_name

        first_name = ET.SubElement(xml_element, "f_name")
        first_name.text = doctor.first_name

        middle_name = ET.SubElement(xml_element, "m_name")
        middle_name.text = doctor.middle_name

        ET.dump(xml_element)

    def create_attribs(self, xml_element, doctor: DoctorModel):
        """ Создание xml элемента для модели доктора
        :param doctor: Модель Доктор
        :return: xml элемент для сущности Доктор
        """

        print(": XmlDoctors.create()")

        print("xml_element=", xml_element)
        print("doctor=", doctor)

        # print("self.element_name=", self.element_name)

        code = ET.SubElement(xml_element, "code")
        code.text = str(doctor.kode)

        last_name = ET.SubElement(xml_element, "last_name")
        last_name.text = doctor.last_name

        first_name = ET.SubElement(xml_element, "f_name")
        first_name.text = doctor.first_name

        middle_name = ET.SubElement(xml_element, "m_name")
        middle_name.text = doctor.middle_name

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
