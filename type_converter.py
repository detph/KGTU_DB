from PyQt5.QtCore import QDateTime

class TypeConverter(object):
    """
    Данный класс позволяет конвертировать
    данные в формат для БД.
    То есть перед занесением данных в БД они
    должны пройти конвертацию !!!
    """
    def __init__(self):

        self.__init_Attributes()
        

    #inits
    def __init_Attributes(self):
        super(TypeConverter, self).__init__()
    





    # конверторы В БД формат
    def QDateTimeToDbDateTime(self, q_datetime):
        """
        Конвертирует Qt дату в дату для БД
        :param q_date: <QDate> : Qt дата
        """
        return str(q_datetime.toPyDateTime())[:23]

    def StrToDbDateTime(self, str_date):
        """
        Конвертирует str дату в дату для БД
        :param str_date: <str> : дата в формате строки
        """
        return str_date[:23]




    # конверторы ИЗ БД формата
    def DbDateTimeToQDateTime(self, db_date):
        """
        Конвертирует дату БД в Qt дату
        :param db_date: <BD_DateType> : дата из БД
        """
        pattern = "yyyy-MM-dd hh:mm:ss"
        return QDateTime().fromString(db_date, pattern)

    def DbDateTimeToStr(self, db_date):
        """
        Конвертирует дату БД в дату-строку
        :param db_date: <BD_DateType> : дата из БД
        """
        return db_date[:23]


# t = TypeConverter()
# d = t.DbDateTimeToQDateTime('2012-07-10 13:45:00')
# print(d)