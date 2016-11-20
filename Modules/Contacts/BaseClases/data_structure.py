


class Structure(object):
    """
    Данный класс хранит структуру данных
    для работы с "Контактами" (Contacts).

    Property:
      FIO(): <str> : возвращает ФИО
    phone(): <str> : возвращает номер телефона
    group(): <str> : возвращает группу
    """


    def __init__(
            self,
            fio=None,
            phone=None,
            group=None
    ):
        """
        :param fio: <str> : ФИО
        :param phone: <str> : номер телефона
        :param group: <str> : группа контакта
        """

        self.__init_Attributes()
        self.__init_Parameters(fio=fio, phone=phone, group=group)




    # inits
    def __init_Attributes(self):
        super(Structure, self).__init__()
        self.__fio = ''
        self.__phone = ''
        self.__group = ''

    def __init_Parameters(self, fio, phone, group):
        if fio: self.setFIO(fio)
        if phone: self.setPhone(phone)
        if group: self.setGroup(group)


    

    @property
    def asFieldsForRecord(self):
        return [
            self.__fio,
            self.__phone,
            self.__group
        ]
    
    @property
    def FIO(self):
        try:
            return self.__fio
        except:
            return None

    @property
    def phone(self):
        try:
            return self.__phone
        except:
            return None

    @property
    def group(self):
        try:
            return self.__group
        except:
            return None




    # METHODS
    def setFIO(self, FIO='Фамилия Имя Отчество'):
        FIO = str(FIO)
        self.__fio = FIO

    def setGroup(self, group='Личные'):
        """
        :param group: <str> : группа
        """
        self.__group = str(group)

    def setPhone(self, phone='89114889773'):
        """
        :param phone: <str> : номер телефона
        """
        self.__phone = str(phone)








if __name__ == '__main__':

    struct = Structure(
        fio='Григорян Олегсей Костикович',
        phone='891148897',
        group='Работа'
    )

    print(struct.FIO)
    print(struct.phone)
    print(struct.group)