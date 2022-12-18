import xml.etree.ElementTree as ET

from .sections.section_doctors import SectionDoctors
from .sections.section_organs import SectionOrgans
from .sections.section_devices import SectionDevices
from .sections.section_endos import SectionEndos
from .sections.section_hospaitals import SectionHospitals


FILE = ".\data\data.xml"


class XmlDataProvider:
    """ Провайдер данных XML """

    __tree = None
    __root = None
    # __sections = None      # Спислк обязательных секций d xml документе
    __sections = [
        SectionDoctors(),
        SectionOrgans(),
        SectionDevices(),
        SectionEndos(),
        SectionHospitals()
    ]

    def __new__(cls):
        print(": XmlDataProvider.__new__()")

        if not hasattr(cls, 'instance'):
            cls.instance = super(XmlDataProvider, cls).__new__(cls)

        print("cls.__sections=", cls.__sections)

        print("cls.instance=", cls.instance)
        return cls.instance

    def __init__(self):
        """ Конструктор """

        print(": XmlDataProvider.__init__()")

    # region Свойства

    @property
    def root(self):
        """ Свойство. Корневой элемент """

        return self.__root

    @root.setter
    def root(self, value):
        """ Свойство(сетер). Корневой элемент """
        self.__root = value

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