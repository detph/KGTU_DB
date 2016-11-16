from Widgets.ListView import MYListView


class BaseUIList(MYListView):
    # SIGNALS



    def __init__(self, parent=None):
        super(BaseUIList, self).__init__(parent=parent)

        self.__init_Attributes()
        self.__init_Parameters()


    # inits
    def __init_Attributes(self):
        pass

    def __init_Parameters(self):
        pass




if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    from Modules.DBModelAccess.moduleClasses import QBestSqlTableModel
    win = BaseUIList()
    model = QBestSqlTableModel(table='contacts')
    print(model.record(0).field(0).name())
    model.selectTable(table='contacts')
    win.setModel(model)
    win.show()
    sys.exit(app.exec_())