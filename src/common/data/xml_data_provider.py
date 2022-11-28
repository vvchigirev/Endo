import xml.etree.ElementTree as ET

from xml.etree.ElementTree import ElementTree

from ...common.consts.Keys import Keys
from ..data.xml_doctors import XmlDoctors
from ..data.xml_organs import XmlOrgans
from ...dict.doctors.models.doctor_model import DoctorModel

FILE = ".\data\data.xml"


class XmlDataProvider:
    """ Провайдер данных XML """

    __tree = None
    __root = None

    __parent_elements = [
        XmlDoctors(),
        XmlOrgans(),
    ]

    def __init__(self):
        """ Конструктор """

        self.__tree = None
        self.__root = None

    # region Свойства

    def read(self):
        """ Чтение xml файла """

        print(": XmlDataProvider.read()")

        try:
            self.__tree = ET.parse(FILE)
        except Exception as e:
            print("e=", e)

        if self.__tree is not None:
            self.__root = self.__tree.getroot()
        else:
            self.__root = ET.Element("Endo")
            self.__tree = ET.ElementTree(self.__root)

        for element in XmlDataProvider.__parent_elements:
            find = self.__root.find(element.group_name)
            if find is None:
                ET.SubElement(self.__root, element.group_name)

        ET.dump(self.__tree)

    def write(self):
        """ Запись данных в xml файл """

        print(": XmlDataProvider.write()")

        ET.dump(self.__tree)

        self.__tree.write(FILE, encoding="utf-8", method="xml")

    def select_elements(self):
        """ Получение списка элементов указанной группы
        :return:
        """

        print(": XmlDataProvider.select_elements()")

    def create_element(self, group_name=None, element_name=None):
        """ Добавление элемента в xml документ
        :param group_name: Наименование группы куда добавить элемент
        :param element_name: Наименование добавляемый элемент
        """

        print(": XmlDataProvider.create_element()")

        if not group_name:
            return None

        if self.__root:
            find_element = self.__root.find(group_name)

            ET.dump(find_element)

            if find_element is not None:
                element = ET.SubElement(find_element, element_name)

                return element
        return None
