from PyQt5.QtWidgets import QTabWidget

from Widgets.Widget import MYWidget







class Tasks(MYWidget):



    def __init__(self, DB):
        super(Tasks, self).__init__(
            layout='H',
            layout_margins=[10, 10, 10, 10]
        )

        self.__init_Attributes(DB)
        self.__init_Parameters()
        self.__init_Layouting()
        self.__init_Connects()





    # inits
    def __init_Attributes(self, DB):
        self.__tabs = QTabWidget(parent=self)
        self.__employee = Employee(DB)

    def __init_Parameters(self):
        pass

    def __init_Layouting(self):
        pass

    def __init_Connects(self):
        pass






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
