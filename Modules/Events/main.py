
from Widgets.MainWindow import MYMainWindow

from Modules.Events.form_add import FormAdd
from Modules.Events.form_edit import FormEdit
from Modules.Events.form_view import FormView
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from Widgets.PushButton import MYPushButton
from Modules.Events.BaseClases.base_ui_list import BaseUIList
from Modules.Events.BaseClases.model import Model
from PyQt5.QtGui import QIcon
from icons import ICON







class Events(MYMainWindow):

    def __init__(self, DB):
        super(Events, self).__init__(
            window_size=(720, 480),
            title='Дела',
            layout='H',
            layout_margins=[10, 10, 10, 10],
            toolbar=True,
            toolbar_section='Top'
        )

        self.__init_Attributes(DB)
        self.__init_Parameters()
        self.__init_Layouting()
        self.__init_Connects()
        self.__init_ToolbarActions()

    # inits
    def __init_Attributes(self, DB):
        self.__list_btn_layout = QHBoxLayout()
        self.__btn_toogle = MYPushButton(parent=self)
        self.__btn_remove_all = MYPushButton(parent=self)
        self.__list_layout = QVBoxLayout()
        self.__model = Model(DB)
        self.__list = BaseUIList(parent=self)
        self.__form_view = FormView(DB, self)
        self.__form_add  = FormAdd(DB, self)
        self.__form_edit = FormEdit(DB, self)

    def __init_Parameters(self):
        self.__btn_toogle.setCheckable(True)
        self.__list_layout.setSpacing(10)
        self.__btn_toogle.setText('Невыполненные дела')
        self.__btn_remove_all.setText('Удалить все')
        self.__btn_remove_all.setIcon(QIcon(ICON.DEFAULT.remove()))
        self.__btn_remove_all.hide()
        self.__list.setModel(self.__model)
        self.__list.initColumnsParms()

    def __init_Layouting(self):
        self.__list_layout.addWidget(self.__list)
        self.__list_btn_layout.addWidget(self.__btn_toogle)
        self.__list_btn_layout.addWidget(self.__btn_remove_all)
        self.__list_layout.addLayout(self.__list_btn_layout)
        self.cwidget.main_layout.addLayout(self.__list_layout)
        self.cwidget.main_layout.addWidget(self.__form_view)

    def __init_Connects(self):
        self.__btn_toogle.clicked.connect(self.__tool_DoFilter)
        self.__btn_remove_all.clicked.connect(self.__tool_RemoveOutstandingEvent)
        self.__form_view.btn_edit.clicked.connect(self.__tool_OpenEditForm)
        self.__form_edit.accepted.connect(self.__tool_EditEvent)
        self.__form_view.btn_remove.clicked.connect(self.__tool_RemoveCurrentEvent)
        self.__form_add.accepted.connect(self.__tool_AddNewEvent)
        self.__list.clicked.connect(self.__tool_LoadAttribsToViewForm)

    def __init_ToolbarActions(self):
        self.toolbar.addAction(
            QIcon(ICON.DEFAULT.add()),
            'Добавить новое дело',
            self.__tool_OpenAddForm
        )




    # class tool
    def __tool_DoFilter(self):
        state = self.__btn_toogle.isChecked()
        if state:
            self.__btn_remove_all.show()
            self.__btn_toogle.setText('Все  дела')
            self.__model.setDateTimeFilter(compare_sign='<')
        else:
            self.__btn_remove_all.hide()
            self.__model.setFilter('')

    def __tool_LoadAttribsToViewForm(self, index):
        # try:
        row = index.row()
        structure = self.__model.getStructure(row)
        # print(structure.asFieldsForRecord)
        self.__form_view.setDataStructure(structure)
        # # except:
        # #     pass

    def __tool_EditEvent(self):
        index = self.__list.selectedIndexes()
        if index:
            index = index[0]
            row = index.row()
        new_structure = self.__form_edit.attribs.dataStructure
        # print(new_structure.asFieldsForRecord)
        self.__model.editRecord(row=row, data_structure=new_structure)
        self.__tool_LoadAttribsToViewForm(index)

    def __tool_AddNewEvent(self):
        struct = self.__form_add.attribs.dataStructure
        # print(struct.asFieldsForRecord)
        self.__model.addRecord(data_structure=struct)

    def __tool_OpenEditForm(self):
        data_structure = self.__form_view.dataStructure
        self.__form_edit.attribs.setDataStructure(data_structure)
        self.__form_edit.exec_()

    def __tool_OpenAddForm(self):
        self.__form_add.exec_()

    def __tool_RemoveOutstandingEvent(self):
        for row in range(self.__model.rowCount()):
            self.__model.removeRecord(row)

    def __tool_RemoveCurrentEvent(self):
        try:
            index = self.__list.selectedIndexes()
            if index:
                index = index[0]
                row = index.row()
                self.__model.removeRecord(row)
        except:
            pass







if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = Events()
    win.show()
    app.exec_()