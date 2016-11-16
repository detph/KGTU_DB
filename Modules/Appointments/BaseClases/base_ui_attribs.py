# Qt Types

from Modules.Appointments.BaseClases.data_structure import AppointmentStructure

# WIDGETS
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QTimeEdit
from PyQt5.QtWidgets import QDateEdit
from Widgets.LineEdit import MYLineEdit
from Widgets.Label import MYLabel
from Widgets.Widget import MYWidget




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
        self.__structure = AppointmentStructure()

        self.__uitype = type

        self.btns_layout = QHBoxLayout()
        self.__form_layout = QFormLayout()

        self.__lbl_fio   = MYLabel(parent=self, bold=True, text='ФИО:')
        self.__lbl_time  = MYLabel(parent=self, bold=True, text='Время:')
        self.__lbl_date  = MYLabel(parent=self, bold=True, text='Дата:')
        self.__lbl_role  = MYLabel(parent=self, bold=True, text='Назначение:')

        if self.__uitype == 'editable':
            self.__time  = QTimeEdit(self)
            self.__date  = QDateEdit(self)
            self.__role  = MYLineEdit(parent=self)
            self.__fio   = MYLineEdit(parent=self)
            self.__descript = QTextEdit(self)

        else:
            self.__time = MYLabel(parent=self, italic=True, text='')
            self.__date = MYLabel(parent=self, italic=True, text='')
            self.__role = MYLabel(parent=self, italic=True, text='')
            self.__fio = MYLabel(parent=self, italic=True, text='')
            self.__descript = QTextBrowser(self)

    def __init_Parameters(self):
        self.__form_layout.setContentsMargins(0, 0, 0, 0)
        self.__form_layout.setSpacing(5)

        if self.__uitype == 'editable':
            self.__date.setCalendarPopup(True)

    def __init_Layouting(self):

        AS_FIELD = self.__form_layout.FieldRole
        AS_LABEL = self.__form_layout.LabelRole

        self.main_layout.addLayout(self.__form_layout)
        self.main_layout.addWidget(self.__descript)
        self.main_layout.addLayout(self.btns_layout)

        self.__form_layout.setWidget(0, AS_LABEL, self.__lbl_fio)
        self.__form_layout.setWidget(1, AS_LABEL, self.__lbl_date)
        self.__form_layout.setWidget(2, AS_LABEL, self.__lbl_time)
        self.__form_layout.setWidget(3, AS_LABEL, self.__lbl_role)

        self.__form_layout.setWidget(0, AS_FIELD, self.__fio)
        self.__form_layout.setWidget(1, AS_FIELD, self.__date)
        self.__form_layout.setWidget(2, AS_FIELD, self.__time)
        self.__form_layout.setWidget(3, AS_FIELD, self.__role)




    # PROPERTY
    @property
    def dataStructure(self):
        return self.__structure




    # METHODS
    def setDataStructure(self, struct):
        self.setFIO(struct.FIO)
        self.setRole(struct.role)
        self.setDescription(struct.description)
        self.setDateTime(struct.qDateTime)

    def setFIO(self, FIO):
        FIO = str(FIO)
        self.__structure.setFIO(FIO)
        self.__fio.setText(FIO)

    def setRole(self, role):
        """
        :param role: <str> : назначение дела
        """

        role = str(role)
        self.__structure.setRole(role)
        self.__role.setText(role)

    def setDescription(self, text=''):
        text = str(text)
        self.__structure.setDescription(text)
        self.__descript.setText(text)

    def setDateTime(self, q_datetime):
        self.__structure.setQDateTime(q_datetime)

        if self.__uitype == 'editable':
            self.__date.setDate(self.__structure.qDate)
            self.__time.setTime(self.__structure.qTime)
        else:
            self.__date.setText(self.__structure.strDate)
            self.__time.setText(self.__structure.strTime)






if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    from PyQt5.QtCore import QDate, QTime
    date = QDate()
    time = QTime()

    date.setDate(2012, 7, 10)
    time.setHMS(13, 45, 0)

    fio = 'Курлыкин Иван Иваныч'
    role = '8911488943'
    descript = 'Встреча в метрополисе'


    struct = AppointmentStructure(
        fio=fio,
        role=role,
        descript=descript,
        qdate_qtime=(date, time)
    )

    win = BaseUIAttribs()
    win.setDataStructure(struct)

    win.show()
    app.exec_()

