
from Widgets.MainWindow import MYMainWindow

from Modules.Appointments.form_add import FormAdd
from Modules.Appointments.form_edit import FormEdit
from Modules.Appointments.form_view import FormView
from Widgets.GroupBox import MYGroupBox, QVBoxLayout
from Modules.Appointments.BaseClases.base_ui_list import BaseUIList
from Modules.DBModelAccess.moduleClasses import QBestSqlTableModel
from PyQt5.QtGui import QIcon
from icons import ICON







class Appointments(MYMainWindow):

    def __init__(self):
        super(Appointments, self).__init__(
            window_size=(720, 480),
            title='Дела',
            layout='H',
            layout_margins=[10, 10, 10, 10],
            toolbar=True,
            toolbar_section='Top'
        )

        self.__init_Attributes()
        self.__init_Parameters()
        self.__init_Layouting()
        self.__init_Connects()
        self.__init_ToolbarActions()

    # inits
    def __init_Attributes(self):
        self.__grp_notdone = MYGroupBox(
            parent=self,
            title='Не выполненные',
            layout='V',
            layout_margins=[10, 10, 10, 10]
        )

        self.__list_layout = QVBoxLayout()
        self.__model = QBestSqlTableModel('appointments')
        self.__list = BaseUIList(self)
        self.__list_notdone = BaseUIList(self)
        self.__form_view = FormView(self)
        self.__form_add  = FormAdd(self)
        self.__form_edit = FormEdit(self)

    def __init_Parameters(self):
        self.__list.setModel(self.__model)

    def __init_Layouting(self):
        self.__list_layout.addWidget(self.__list)
        self.__grp_notdone.main_layout.addWidget(self.__list_notdone)
        self.__list_layout.addWidget(self.__grp_notdone)
        self.cwidget.main_layout.addLayout(self.__list_layout)
        self.cwidget.main_layout.addWidget(self.__form_view)

    def __init_Connects(self):
        self.__form_view.btn_edit.clicked.connect(self.__tool_OpenEditForm)
        self.__form_edit.accepted.connect(self.__tool_EditAppointment)
        self.__form_view.btn_remove.clicked.connect(self.__tool_RemoveCurrentAppointment)
        self.__form_add.accepted.connect(self.__tool_AddNewAppointment)
        self.__list.clicked.connect(self.__tool_LoadAttribsToViewForm)

    def __init_ToolbarActions(self):
        self.toolbar.addAction(
            QIcon(ICON.DEFAULT.add()),
            'Добавить новое дело',
            self.__tool_OpenAddForm
        )




    # class tool
    def __tool_LoadAttribsToViewForm(self, index):
        row = index.row()
        record = self.__model.record(row)
        app_name = record.value(0)
        dbdatetime = record.value(1)
        text = record.value(2)
        contac_name = record.value(3)
        self.__form_view.setFIO(contac_name)
        self.__form_view.setDBDateTime(dbdatetime)
        self.__form_view.setRole(app_name)
        self.__form_view.setDescription(text)

    def __tool_EditAppointment(self):
        print('Appointments edited')

    def __tool_AddNewAppointment(self):
        print('New Appointments added')

    def __tool_OpenEditForm(self):
        print('Opened edit form')
        self.__form_edit.exec_()

    def __tool_OpenAddForm(self):
        print('Opened add form')
        self.__form_add.exec_()

    def __tool_RemoveSelectedAppointment(self):
        print('Selected Appointments removed')

    def __tool_RemoveCurrentAppointment(self):
        print('Current appointments removed')







if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = Appointments()
    win.show()
    app.exec_()