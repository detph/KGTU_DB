from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout

from DataBase.access_model import DBAccessModel
from Modules.Tasks.global_task.form import Form
from Widgets.PushButton import MYPushButton
from Widgets.TableView import MYTableView
from Widgets.Widget import MYWidget
from icons import ICON
from Modules.Tasks.BaseClases.model import ModelTask





class GlobalTasks(MYWidget):

    #inits
    def __init__(self, DB):
        super(GlobalTasks, self).__init__(layout_margins=[10, 10, 10, 10])

        self.__model = ModelTask(DB=DB)
        self.__form_add = Form()
        self.__form_edit = Form()

        self.__view = MYTableView(parent=self)
        self.__view.setModel(self.__model)

        self.__btn_layout = QHBoxLayout()
        self.__btn_add = MYPushButton(parent=self)
        self.__btn_remove = MYPushButton(parent=self)
        self.__btn_add.setIcon(QIcon(ICON.DEFAULT.add()))
        self.__btn_remove.setIcon(QIcon(ICON.DEFAULT.remove()))

        self.__btn_layout.addWidget(self.__btn_add)
        self.__btn_layout.addWidget(self.__btn_remove)
        self.main_layout.addLayout(self.__btn_layout)
        self.main_layout.addWidget(self.__view)

        self.__view.doubleClicked.connect(self.__open_EditForm)
        self.__btn_add.clicked.connect(self.__open_AddForm)
        self.__btn_remove.clicked.connect(self.__remove)
        self.__form_add.accepted.connect(self.__add)
        self.__form_edit.accepted.connect(self.__edit)


    def __open_AddForm(self):
        self.__form_add.setText('')
        self.__form_add.exec_()

    def __open_EditForm(self):
        index = self.__view.selectedIndexes()[0]
        row = index.row()
        text = self.__model.getRecord(row, self.__model.PyDictRecord)
        text = text['name']
        self.__form_edit.setText(text)
        self.__form_edit.exec_()

    def __add(self):
        text = self.__form_add.text()
        self.__model.addRecord([text])

    def __edit(self):
        index = self.__view.selectedIndexes()[0]
        row = index.row()
        text = [self.__form_edit.text()]
        self.__model.editRecord(row=row, fields=text)

    def __remove(self):
        selected = self.__view.selectedIndexes()
        if selected:
            index = selected[0]
            row = index.row()
            self.__model.removeRecord(row)

