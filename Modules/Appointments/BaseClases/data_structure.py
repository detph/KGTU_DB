
#Qt Types
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QDateTime

# DB type convertor
from type_converter import TypeConverter






class AppointmentStructure(object):
    """
    Данный класс хранит структуру данных
    для работы с "Делом" (Appointment).

    Property:
            FIO(): <str> : возвращает ФИО
           role(): <str> : возвращает тип встречи
          qDate(): <QDate> : возвращает Qt дату
          qTime(): <QTime> : возвращает Qt время
        strTime(): <str>: возвращает строку времени
        strDate(): <str>: возвращает строку даты
      qDateTime(): <QDateTime>: возвращает Qt времядату
     dbDateTime(): <DBDateTime>: возвращает БД времядату
    description(): <str> : возвращает описание встречи
    """


    def __init__(
            self,
            fio=None,
            phone=None,
            descript=None,
            qdate_qtime=None,
            q_time=None,
            q_datetime=None,
            db_datetime=None
    ):
        """
        Для определения даты и времени возможно
        указать один из следущих параметров:
            - qdate_qtime
            - q_datetime
            - db_datetime
        Параметры написаны в приорететном порядке
        (т.е. после qdate_qtime параметры q_datetime
        и db_datetime использоваться не будут).


        :param fio: <str> : ФИО
        :param phone: <str, int> : номер телефона
        :param descript: <str> : описание дела
        :param qdate_qtime: <tuple(QDate, QTime)> : Qt дата и Qt время
        :param q_datetime: <QDateTime> : Qt время и дата
        :param db_datetime: <DBDateTime> : БД время и дата
        """

        self.__init_Attributes()
        self.__init_Parameters(
            fio=fio ,
            phone=phone,
            descript=descript,
            qdate_qtime=qdate_qtime,
            q_time=q_time,
            q_datetime=q_datetime,
            db_datetime=db_datetime
        )




    # inits
    def __init_Attributes(self):
        super(AppointmentStructure, self).__init__()

        self.__fio = ''
        self.__role = ''
        self.__descript = ''
        self.__datetime = QDateTime()
        self.__db_datetime = ''

    def __init_Parameters(self, fio, phone, descript, qdate_qtime, q_time, q_datetime, db_datetime):
        if fio: self.setFIO(fio)
        if phone: self.setRole(phone)
        if descript: self.setDescription(descript)
        if qdate_qtime:
            self.setDate(qdate_qtime[0], qdate_qtime[1])
        else:
            if q_datetime:
                self.setQDateTime(q_datetime)
            else:
                if db_datetime:
                    self.setDBDateTime(db_datetime)


    

    # PROPERTY
    @property
    def FIO(self):
        try:
            return self.__fio
        except:
            return None

    @property
    def role(self):
        try:
            return self.__role
        except:
            return None

    @property
    def description(self):
        try:
            return self.__descript
        except:
            return None

    @property
    def qDate(self):
        try:
            return self.__datetime.date()
        except:
            return None

    @property
    def qTime(self):
        try:
            return self.__datetime.time()
        except:
            return None

    @property
    def strDate(self):
        try:
            return self.__datetime.date().toString()
        except:
            return None

    @property
    def strTime(self):
        try:
            return self.__datetime.time().toString()[0:5]
        except:
            return None

    @property
    def qDateTime(self):
        try:
            return self.__datetime
        except:
            return None

    @property
    def dbDateTime(self):
        try:
            return self.__db_datetime
        except:
            return None





    # METHODS
    def setFIO(self, FIO='Фамилия Имя Отчество'):
        FIO = str(FIO)
        self.__fio = FIO

    def setRole(self, role):
        """
        :param role: <str> : назначение дела
        """

        role = str(role)
        self.__role = role

    def setDescription(self, text=''):
        text = str(text)
        self.__descript = text

    def setDate(self, qdate, qtime):
        """
        :param qdate: <QDate>
        :param qtime: <QTime>
        """

        self.__datetime.setDate(qdate)
        self.__datetime.setTime(qtime)
        self.__db_datetime = TypeConverter.QDateTimeToDbDateTime(self, self.__datetime)

    def setQDateTime(self, qdatetime):
        self.__datetime = qdatetime
        self.__db_datetime = TypeConverter.QDateTimeToDbDateTime(self, self.__datetime)

    def setDBDateTime(self, db_datetime):
        self.__db_datetime = db_datetime
        self.__datetime = TypeConverter.DbDateTimeToQDateTime(self, self.__db_datetime)







if __name__ == '__main__':
    date = QDate()
    time = QTime()

    date.setDate(2012, 7, 10)
    time.setHMS(13, 45, 0)

    fio = 'Курлыкин Иван Иваныч'
    role = 'Собеседование'
    descript = 'Встреча в метрополисе'

    struct = AppointmentStructure(
        fio=fio,
        phone=role,
        descript=descript,
        qdate_qtime=(date, time)
    )


    print(struct.dbDateTime)
