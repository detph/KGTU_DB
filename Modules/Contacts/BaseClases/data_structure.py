


class ContactsStructure(object):
    """
    Данный класс хранит структуру данных
    для работы с "Контактами" (Contacts).

    Property:
      FIO(): <str> : возвращает ФИО
    phone(): <int> : возвращает номер телефона
    """


    def __init__(
            self,
            fio=None,
            phone=None,
    ):
        """
        :param fio: <str> : ФИО
        :param phone: <int> : номер телефона
        """

        self.__init_Attributes()
        self.__init_Parameters(fio=fio, phone=phone)




    # inits
    def __init_Attributes(self):
        super(ContactsStructure, self).__init__()

        self.__fio = ''
        self.__phone = 0

    def __init_Parameters(self, fio, phone):
        if fio: self.setFIO(fio)
        if phone: self.setPhone(phone)



    

    # PROPERTY
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





    # METHODS
    def setFIO(self, FIO='Фамилия Имя Отчество'):
        FIO = str(FIO)
        self.__fio = FIO

    def setPhone(self, phone):
        """
        :param phone: <int> : назначение дела
        """
        self.__phone = int(phone)








if __name__ == '__main__':

    struct = ContactsStructure(
        fio='Григорян Олегсей Костикович',
        phone=891148897
    )


