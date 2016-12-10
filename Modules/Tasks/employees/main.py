from Modules.Tasks.employees.form_add import FormAdd
from Modules.Tasks.employees.form_edit import FormEdit
from Modules.Tasks.employees.model import ModelEmpTask
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

    def __init_Layouting(self):
        self.main_layout.addWidget(self.__list)
        self.main_layout.addWidget(self.__form_view)

    def __init_Connects(self):
        self.__list.clicked.connect(self.__load_attribs)
        self.__list.doubleClicked.connect(self.__open_FormEdit)
        self.__form_view.btn_add.clicked.connect(self.__open_FormAdd)
        self.__form_view.btn_remove.clicked.connect(self.__remove)
        self.__form_edit.accepted.connect(self.__edit)
        self.__form_add.accepted.connect(self.__add)

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