import xml.etree.ElementTree as ET

from .sections.section_doctors import SectionDoctors
from .sections.section_organs import SectionOrgans
from .sections.section_devices import SectionDevices
FILE = ".\data\data.xml"


class XmlDataProvider:
    """ Провайдер данных XML """

    __tree = None
    __root = None
    __sections = None      # Спислк обязательных секций d xml документе

    def __init__(self):
        """ Конструктор """

        self.__tree = None
        self.__root = None

        self.__sections = [
            SectionDoctors(),
            SectionOrgans(),
            SectionDevices()
        ]

    # region Свойства

    @property
    def root(self):
        """ Свойство. Корневой элемент """

        return self.__root

    # endregion

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

        for section in self.__sections:
            find = self.__root.find(section.group_name)
            if find is None:
                ET.SubElement(self.__root, section.group_name)

        # ET.dump(self.__tree) # Отображение считанных данных из xml файла

    def write(self):
        """ Запись данных в xml файл """

        print(": XmlDataProvider.write()")

        ET.dump(self.__tree)

        # self.__tree.write(FILE, encoding="utf-8", method="xml")
        self.__tree.write(FILE, encoding="utf-8")