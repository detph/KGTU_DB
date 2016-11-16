from Modules.DBModelAccess.moduleClasses import QBestSqlTableModel



class Model(QBestSqlTableModel):
    def __init__(self):
        super(Model, self).__init__()

        self.__init_Parameters()


    def __init_Parameters(self):
        self.setTable('appointments')
    

    # METHODS

    def addRecord(self, record_values):
        """
        :param record_values: <list> : список значений
        """
        self.addRecord(fields=record_values)

    def removeRecord(self, row):
        self.removeRecord(row)

    def editRecord(self, row, record_values):
        QBestSqlTableModel.editRecord(self, row=row, fields=record_values)