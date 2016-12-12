from PyQt5.QtWidgets import QDateEdit
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout

from Modules.Tasks.employees.form_add import FormAdd
from Modules.Tasks.employees.form_edit import FormEdit
from Modules.Tasks.employees.model import ModelEmpTask
from Widgets.ComboBox import MYComboBox
from Widgets.DateEdit import MYDateEdit
from Widgets.PushButton import MYPushButton
from Widgets.TableView import MYTableView
from Widgets.Widget import MYWidget
from Modules.Tasks.employees.form_view import FormView


class EmployeeTask(MYWidget):

    #inits
    def __init__(self, DB):
        super(EmployeeTask, self).__init__(
            layout='H'
        )

        self.__init_Attributes(DB)
        self.__init_Parameters()
        self.__init_Layouting()
        self.__init_Connects()

    def __init_Attributes(self, DB):
        self.__layout_filters = QHBoxLayout()
        self.__layout_list = QVBoxLayout()
        self.__btn_filter_all = MYPushButton(parent=self, text='Все')
        self.__btn_filter_today = MYPushButton(parent=self, text='На сегодня')
        self.__btn_filter_day = MYDateEdit(parent=self)

        self.__form_view = FormView(DB, self)
        self.__form_add = FormAdd(DB, self)
        self.__form_edit = FormEdit(DB, self)

        self.__model = ModelEmpTask(data_base=DB)
        self.__list = MYTableView()

    def __init_Parameters(self):
        self.__list.setModel(self.__model)
        # self.__list.hideColumn(1)
        self.__list.hideColumn(2)
        self.__list.hideColumn(3)
        self.__list.setColumnWidth(0, 250)

    def __init_Layouting(self):
        self.__layout_filters.addWidget(self.__btn_filter_all)
        self.__layout_filters.addWidget(self.__btn_filter_today)
        self.__layout_filters.addWidget(self.__btn_filter_day)
        self.__layout_list.addLayout(self.__layout_filters)
        self.__layout_list.addWidget(self.__list)
        self.main_layout.addLayout(self.__layout_list)
        self.main_layout.addWidget(self.__form_view)

    def __init_Connects(self):
        self.__list.clicked.connect(self.__load_attribs)
        self.__list.doubleClicked.connect(self.__open_FormEdit)
        self.__form_view.btn_add.clicked.connect(self.__open_FormAdd)
        self.__form_view.btn_remove.clicked.connect(self.__remove)
        self.__form_edit.accepted.connect(self.__edit)
        self.__form_add.accepted.connect(self.__add)
        self.__btn_filter_all.clicked.connect(self.__filter_All)
        self.__btn_filter_today.clicked.connect(self.__filter_ToDay)
        self.__btn_filter_day.dateChanged.connect(self.__filter_SpecDate)

    def __load_attribs(self, index):
        row = index.row()
        data = self.__model.getStructure(row)
        self.__form_view.setDataStructure(data)



    def __open_FormEdit(self, index):
        row = index.row()
        data = self.__model.getStructure(row)
        self.__form_edit.attribs.setDataStructure(data)
        self.__form_edit.exec_()

    def __open_FormAdd(self):
        self.__form_add.updatesEnabled()
        self.__form_add.exec_()

    def __edit(self):
        selected = self.__list.selectedIndexes()
        if selected:
            index = selected[0]
            data = self.__form_edit.attribs.dataStructure
            row = index.row()
            self.__model.editRecord(data, row)
            self.__load_attribs(index)

    def __add(self):
        data = self.__form_add.attribs.dataStructure
        self.__model.addRecord(data)

    def __remove(self):
        selected = self.__list.selectedIndexes()
        if selected:
            index = selected[0]
            self.__model.removeRecord(index.row())

    def __filter_All(self):
        self.__model.setFilter('')
        self.__model.select()

    def __filter_ToDay(self):
        d = self.__btn_filter_day.date().currentDate()
        self.__btn_filter_day.setDate(d)
        self.__model.setDateTimeFilter('==')
        self.__model.select()

    def __filter_SpecDate(self):
        dt = self.__btn_filter_day.dateTime()
        self.__model.setDateTimeFilter(
            compare_sign='==',
            field='datetime_start',
            type='d',
            date=dt
        )
        self.__model.select()

    #SLOT
    def createEmployeeTask(self, name):
        self.__form_add.setFIO(name)
        self.__form_add.show()


















if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtSql import QSqlDatabase
    from paths import DB_FILE_PATH

    app = QApplication([])
    DATABASE = QSqlDatabase('QSQLITE')
    DATABASE.setDatabaseName(DB_FILE_PATH)
    DATABASE.open()
    win = EmployeeTask(DATABASE)
    win.show()
    sys.exit(app.exec_())