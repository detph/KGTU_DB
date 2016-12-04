from Modules.Tasks.employees.form_add import FormAdd
from Modules.Tasks.employees.form_edit import FormEdit
from Modules.Tasks.employees.model import ModelEmp
from Widgets.TableView import MYTableView
from Widgets.Widget import MYWidget
from Modules.Tasks.employees.form_view import FormView


class Employee(MYWidget):

    #inits
    def __init__(self, DB):
        super(Employee, self).__init__(
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

        self.__model = ModelEmp(data_base=DB)
        self.__list = MYTableView()

    def __init_Parameters(self):
        self.__list.setModel(self.__model)
        self.__list.hideColumn(1)
        self.__list.hideColumn(2)
        self.__list.hideColumn(3)

    def __init_Layouting(self):
        self.main_layout.addWidget(self.__list)
        self.main_layout.addWidget(self.__form_view)

    def __init_Connects(self):
        self.__list.clicked.connect(self.__load_attribs)
        self.__list.doubleClicked.connect(self.__open_FormEdit)


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
        self.__form_add.exec_()























if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtSql import QSqlDatabase
    from paths import DB_FILE_PATH

    app = QApplication([])
    DATABASE = QSqlDatabase('QSQLITE')
    DATABASE.setDatabaseName(DB_FILE_PATH)
    DATABASE.open()
    win = Employee(DATABASE)
    win.show()
    sys.exit(app.exec_())