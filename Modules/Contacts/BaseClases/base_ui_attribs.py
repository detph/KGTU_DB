# Qt Types

from Modules.Contacts.BaseClases.data_structure import ContactsStructure

# WIDGETS
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QHBoxLayout
from Widgets.LineEdit import MYLineEdit
from Widgets.Label import MYLabel
from Widgets.Widget import MYWidget

from PyQt5.QtGui     import QDoubleValidator








class BaseUIAttribs(MYWidget):
    """
    Базовый класс, обеспичивающий GUI.
    """

    def __init__(self, type='editable', parent=None):
        super(BaseUIAttribs, self).__init__(
            parent=parent,
            layout='V',
            layout_margins=[10, 10, 10, 10],
            layout_spacing=10
        )

        self.__init_Attributes(type)
        self.__init_Parameters()
        self.__init_Layouting()




    # inits
    def __init_Attributes(self, type):
        self.__structure = ContactsStructure()

        self.__uitype = type

        self.btns_layout = QHBoxLayout()
        self.__form_layout = QFormLayout()

        self.__lbl_fio   = MYLabel(parent=self, bold=True, text='ФИО:')
        self.__lbl_phone  = MYLabel(parent=self, bold=True, text='Телефон:')


        if self.__uitype == 'editable':
            self.__fio   = MYLineEdit(parent=self)
            self.__phone = MYLineEdit(self)

        else:
            self.__fio   = MYLabel(parent=self)
            self.__phone = MYLabel(parent=self)

    def __init_Parameters(self):
        self.__form_layout.setContentsMargins(0, 0, 0, 0)
        self.__form_layout.setSpacing(5)

        if self.__uitype == 'editable':
            validator = QDoubleValidator(0, 15, 2, self)
            self.__phone.setValidator(validator)

    def __init_Layouting(self):

        AS_FIELD = self.__form_layout.FieldRole
        AS_LABEL = self.__form_layout.LabelRole

        self.main_layout.addLayout(self.__form_layout)
        self.main_layout.addLayout(self.btns_layout)

        self.__form_layout.setWidget(0, AS_LABEL, self.__lbl_fio)
        self.__form_layout.setWidget(1, AS_LABEL, self.__lbl_phone)

        self.__form_layout.setWidget(0, AS_FIELD, self.__fio)
        self.__form_layout.setWidget(1, AS_FIELD, self.__phone)




    # PROPERTY
    @property
    def dataStructure(self):
        return self.__structure




    # METHODS
    def setDataStructure(self, struct):
        self.setFIO(struct.FIO)
        self.setPhone(struct.phone)

    def setFIO(self, FIO):
        FIO = str(FIO)
        self.__structure.setFIO(FIO)
        self.__fio.setText(FIO)

    def setPhone(self, phone):
        """
        :param phone: <int>
        """

        self.__structure.setPhone(phone)
        self.__phone.setText(str(phone))








if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])

    struct = ContactsStructure(
        fio='Григорян Олегсей Костикович',
        phone=891148897
    )

    win = BaseUIAttribs('')
    win.setDataStructure(struct)

    win.show()
    app.exec_()

