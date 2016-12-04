from DataBase.access_model import DBAccessModel
from Modules.Tasks.BaseClases.data_structure import Structure








class ModelEmp(DBAccessModel):
    def __init__(self, data_base):
        super(ModelEmp, self).__init__(
            table=DBAccessModel.TableEmployeesTask,
            app_db=data_base
        )
        self.setHeaders(
            ['ФИО', 'Поручение', 'Дата начала', 'Дата отчета']
        )


    # METHODS
    def getStructure(self, row):
        attrs = self.getRecord(row=row, record_type=self.PyDictRecord)
        data = Structure()
        data.setName(attrs['fio'])
        data.setTask(attrs['task'])
        data.setDBDateTimeStart(attrs['datetime_start'])
        data.setDBDateTimeFinish(attrs['datetime_finish'])
        return data

    def addRecord(self, data_structure, row=0):
        values = data_structure.asFieldsForRecord
        super(ModelEmp, self).addRecord(fields=values, row=row)

    def editRecord(self, data_structure, row=0):
        values = data_structure.asFieldsForRecord
        super(ModelEmp, self).editRecord(fields=values, row=row)