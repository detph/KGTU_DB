
from Widgets.Widget import MYWidget

from Modules.Events.form_add import FormAdd
from Modules.Events.form_edit import FormEdit
from Modules.Events.form_view import FormView
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from Widgets.PushButton import MYPushButton
from Modules.Events.BaseClases.base_ui_list import BaseUIList
from Modules.Events.BaseClases.model import Model
from PyQt5.QtGui import QIcon
from icons import ICON
from PyQt5.QtCore import QDateTime






class Events(MYWidget):



    def __init__(self, DB):
        super(Events, self).__init__(
            layout='H',
            layout_margins=[10, 10, 10, 10]
        )

        self.__init_Attributes(DB)
        self.__init_Parameters()
        self.__init_Layouting()
        self.__init_Connects()





    # inits
    def __init_Attributes(self, DB):
        self.__filters_layout = QHBoxLayout()
        self.__filter_uspeshnie = MYPushButton(parent=self, text='Успешные')
        self.__filter_future = MYPushButton(parent=self, text='Будущие')
        self.__filter_bad = MYPushButton(parent=self, text='Неудавшиеся')
        self.__filter_all = MYPushButton(parent=self, text='Все')
        self.__list_layout = QVBoxLayout()
        self.__model = Model(DB)
        self.__list = BaseUIList(parent=self)
        self.__form_view = FormView(DB, self)
        self.__form_add  = FormAdd(DB, self)
        self.__form_edit = FormEdit(DB, self)

    def __init_Parameters(self):
        self.__list_layout.setSpacing(10)
        self.__list.setModel(self.__model)
        self.__list.initColumnsParms()

    def __init_Layouting(self):
        self.__list_layout.addWidget(self.__list)
        self.__filters_layout.addWidget(self.__filter_all)
        self.__filters_layout.addWidget(self.__filter_bad)
        self.__filters_layout.addWidget(self.__filter_uspeshnie)
        self.__filters_layout.addWidget(self.__filter_future)
        self.__list_layout.addLayout(self.__filters_layout)
        self.main_layout.addLayout(self.__list_layout)
        self.main_layout.addWidget(self.__form_view)

    def __init_Connects(self):
        self.__filter_uspeshnie.clicked.connect(self.__filter_GoodMiting)
        self.__filter_bad.clicked.connect(self.__filter_BadMiting)
        self.__filter_all.clicked.connect(self.__filter_AllRecords)
        self.__form_edit.accepted.connect(self.__tool_EditEvent)
        self.__form_view.btn_remove.clicked.connect(self.__tool_RemoveCurrentEvent)
        self.__form_add.accepted.connect(self.__tool_AddNewEvent)
        self.__list.clicked.connect(self.__tool_LoadAttribsToViewForm)
        self.__list.doubleClicked.connect(self.__tool_OpenEditForm)
        self.__form_view.btn_add.clicked.connect(self.__tool_OpenAddForm)






    # filters
    def __filter_AllRecords(self):
        self.__model.setFilter('')

    def __filter_DateLessThenCurrent(self):
        self.__model.setDateTimeFilter(compare_sign='<')

    def __filter_GoodMiting(self):
        self.__model.setFilter('state > 0')

    def __filter_BadMiting(self):
        current_date = str(QDateTime().currentDateTime().toPyDateTime())
        self.__model.setFilter('state < 1 and datetime < datetime(' + current_date +')')





    # class tool
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
