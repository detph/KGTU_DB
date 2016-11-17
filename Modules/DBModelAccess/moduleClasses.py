from collections import OrderedDict

from PyQt5.QtCore import QSortFilterProxyModel
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
from PyQt5.QtWidgets import QApplication

from paths import DB_FILE_PATH


# print(DB_FILE_PATH)


class QBestSqlTableModel(QSqlTableModel):

    # filters type
    EmptyFilter = 0
    CurrentFilter = 1
    ChangeFilter = 2

    # record type
    SqlRecord = 0
    DictRecord = 1




    def __init__(self, table, databaseName=DB_FILE_PATH, driver="QSQLITE"):
        """
        Добавление модели
        :param databaseName: <str> : путь до файла с базой
        :param driver: <str> : тип драйвера
        """

        self.db = QSqlDatabase.addDatabase(driver)
        self.db.setDatabaseName(databaseName)
        if self.db.open():
            print("База данных подключена!")
            super(QSqlTableModel, self).__init__(db=self.db)
            self.setEditStrategy(self.OnRowChange)
            if not self.selectTable(table=table):
                print('Таблица "' + table + '" не существует')



    # METHODS
    def addRecord(self, fields, row=0):
        """
        Добавление записи в таблицу
        :param row: место вставки; по умолчанию вставляет в начало
        :param fields: массив значений атрибутов записи
        """

        record = self.record(0)
        record.clearValues()
        i = 0
        for item in fields:
            record.setValue(i, str(item))
            i += 1


    def removeRecord(self, row=-1):
        """
        Удаление записи под номером "row";
        по умолчанию удаляет последнюю запись
        :param row: номер записи
        """

        if row < 0:
            row = self.rowCount() - 1
        self.removeRow(row)


    def getRecord(self, row=0, record_type=DictRecord):
        """
        Получение записи
        :param row:
        :param table:
        :param gettingSetting:
            SqlRecord  - получение QSqlRecord
            DictRecord - получение упорядоченного словаря
        """
        self.selectTable(filter_type=self.EmptyFilter)
        record = self.record(row)

        if record_type == self.SqlRecord:
            return record
        elif record_type == self.DictRecord:
            cols = record.count()

            dict = OrderedDict()
            for i in range(0, cols):
                dict[record.field(i).name()] = record.value(i)
            return dict


    def editRecord(self, row=0, fields = []):
        record = self.record(row)
        i = 0
        for item in fields:
            record.setValue(i, str(item))
            i += 1
        self.setRecord(row, record)
        return record


    def selectTable(self, table, filter_type=CurrentFilter, filter=""):
        """
        Выборка из таблицы "table"
        QBestSqlTableModel.emptyFilter - стереть фильтр
        QBestSqlTableModel.currentFilter - не изменять фильтр
        QBestSqlTableModel.changeFilter - изменение фильтра
        :param filter_type: указыват на то, как надо использовать фильтр
        :param filter: строка с фильтром
        """

        if table == None: return None
        self.setTable(table)
        if filter_type == self.EmptyFilter:
            self.setFilter("")
        elif filter_type == self.CurrentFilter:
            pass
        elif filter_type == self.ChangeFilter:
            self.setFilter(filter)

        self.select()
        return self.db.tables()


    def setHeaders(self, headers=[]):
        for i in range(0, len(headers)):
            self.setHeaderData(i, 1, str(headers[i]))







if __name__ == "__main__":
    app = QApplication([])
    model = QBestSqlTableModel(table='appointments')
    # model.selectTable("notes")
    # model.addNewRecord(fields=("2016-11-06 22:12", 3))
    # model.removeRecord(0)
    app.exit()