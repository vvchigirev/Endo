from .....common.base_classes.base_sections import BaseSections
from .....common.consts.Keys import Keys


class SectionDevices(BaseSections):
    """ Наименовая блоков элементов для справочника Приборов """

    def __init__(self):
        """ Конструктор """

        super(SectionDevices, self).__init__(Keys.DEVICES, Keys.DEVICE)
