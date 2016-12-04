

from Widgets.Widget import MYWidget

from Modules.Emloyees.form_add import FormAdd
from Modules.Emloyees.form_edit import FormEdit
from Modules.Emloyees.form_view import FormView
from Modules.Emloyees.BaseClases.model import Model
from Modules.Emloyees.BaseClases.base_ui_list import BaseUIList








class Employees(MYWidget):

    def __init__(self, DB):
        super(Employees, self).__init__(
            layout='V',
            layout_margins=[10, 10, 10, 10]
        )

        self.__init_Attributes(DB)
        self.__init_Parameters()
        self.__init_Layouting()
        self.__init_Connects()



    #inits
    def __init_Attributes(self, DB):
        self.__model = Model(DB)
        self.__list = BaseUIList(parent=self, model=self.__model)
        self.__form_view = FormView(DB=DB, parent=self)
        self.__form_add  = FormAdd(DB=DB, parent=self)
        self.__form_edit = FormEdit(DB=DB, parent=self)

    def __init_Parameters(self):
        self.resize(500, 620)
        self.__list.setModel(self.__model)
        self.__list.setColumnWidth(0, 250)
        self.__list.setColumnWidth(1, 150)

    def __init_Layouting(self):
        self.main_layout.addWidget(self.__form_view)
        self.main_layout.addWidget(self.__list)

    def __init_Connects(self):
        self.__list.doubleClicked.connect(self.__tool_OpenEditForm)
        self.__form_edit.accepted.connect(self.__tool_EditEmployee)
        self.__form_view.btn_remove.clicked.connect(self.__tool_RemoveCurrentEmployee)
        self.__form_add.accepted.connect(self.__tool_AddNewEmployee)
        self.__list.clicked.connect(self.__tool_LoadAttribsToViewForm)
        self.__form_view.btn_add.clicked.connect(self.__tool_OpenAddForm)



    # class tool
    def __tool_LoadAttribsToViewForm(self, index):
        row = index.row()
        structure = self.__model.getStructure(row)
        # print(structure.asFieldsForRecord)
        self.__form_view.setDataStructure(structure)

    def __tool_EditEmployee(self):
        index = self.__list.selectedIndexes()
        if index:
            index = index[0]
            row = index.row()
        new_structure = self.__form_edit.attribs.dataStructure
        self.__model.editRecord(data_structure=new_structure, row=row)
        self.__tool_LoadAttribsToViewForm(index)

    def __tool_AddNewEmployee(self):
        structure = self.__form_add.attribs.dataStructure
        self.__model.addRecord(data_structure=structure)

    def __tool_OpenEditForm(self):
        data_structure = self.__form_view.dataStructure
        self.__form_edit.attribs.setDataStructure(data_structure)
        self.__form_edit.exec_()
    
    def __tool_OpenAddForm(self):
        self.__form_add.exec_()

    def __tool_RemoveCurrentEmployee(self):
        index = self.__list.selectedIndexes()
        if index:
            index = index[0]
            row = index.row()
            self.__model.removeRecord(row)
