from ...base_classes.base_sections import BaseSections
from ...consts.Keys import Keys


class SectionDevices(BaseSections):
    """ Наименовая блоков элементов для справочника Приборов """

    def __init__(self):
        """ Конструктор """

        self.group_name = Keys.DEVICES
        self.element_name = Keys.DEVICE
