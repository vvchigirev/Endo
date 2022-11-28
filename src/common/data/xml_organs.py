from ...common.consts.Keys import Keys
from ..base_classes.base_xml_element import BaseXmlElement


class XmlOrgans(BaseXmlElement):
    """ Xml Сруктура для сущностей Органов """

    def __init__(self):
        """ Конструктор """

        self.group_name = Keys.ORGANS
        self.element_name = Keys.ORGAN
