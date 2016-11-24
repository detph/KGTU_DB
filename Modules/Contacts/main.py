

from Widgets.MainWindow import MYMainWindow

from Modules.Contacts.form_add import FormAdd
from Modules.Contacts.form_edit import FormEdit
from Modules.Contacts.form_view import FormView
from Modules.Contacts.BaseClases.model import Model
from Modules.Contacts.BaseClases.base_ui_list import BaseUIList
from PyQt5.QtGui import QIcon
from icons import ICON







class Contacts(MYMainWindow):


    def __init__(self, DB):
        super(Contacts, self).__init__(
            window_size=(720, 480),
            title='Контакты',
            layout='V',
            layout_margins=[10, 10, 10, 10]
        )

        self.__init_Attributes(DB)
        self.__init_Parameters()
        self.__init_Layouting()
        self.__init_Connects()
        # self.fill()


    #inits
    def __init_Attributes(self, DB):
        self.__model = Model(DB)
        self.__list = BaseUIList(parent=self, model=self.__model)
        self.__form_view = FormView(self)
        self.__form_add  = FormAdd(self)
        self.__form_edit = FormEdit(self)

    def __init_Parameters(self):
        self.resize(300, 620)
        self.__model.setHeaders(["ФИО"])
        self.__list.setModel(self.__model)

    def __init_Layouting(self):
        self.cwidget.main_layout.addWidget(self.__form_view)
        self.cwidget.main_layout.addWidget(self.__list)
    
    def __init_Connects(self):
        self.__form_view.btn_edit.clicked.connect(self.__tool_OpenEditForm)
        self.__form_edit.accepted.connect(self.__tool_EditContact)
        self.__form_view.btn_remove.clicked.connect(self.__tool_RemoveCurrentContact)
        self.__form_add.accepted.connect(self.__tool_AddNewContact)
        self.__list.clicked.connect(self.__tool_LoadAttribsToViewForm)
        self.__form_view.btn_add.clicked.connect(self.__tool_OpenAddForm)




    # class tool
    def __tool_LoadAttribsToViewForm(self, index):
        row = index.row()
        structure = self.__model.getStructure(row)
        self.__form_view.setDataStructure(structure)

    def __tool_EditContact(self):
        index = self.__list.selectedIndexes()
        if index:
            index = index[0]
            row = index.row()
        new_structure = self.__form_edit.attribs.dataStructure
        self.__model.editRecord(data_structure=new_structure, row=row)
        self.__tool_LoadAttribsToViewForm(index)

    def __tool_AddNewContact(self):
        structure = self.__form_add.attribs.dataStructure
        self.__model.addRecord(data_structure=structure)

    def __tool_OpenEditForm(self):
        data_structure = self.__form_view.dataStructure
        # print(data_structure.asFieldsForRecord)
        self.__form_edit.attribs.setDataStructure(data_structure)
        self.__form_edit.exec_()
    
    def __tool_OpenAddForm(self):
        self.__form_add.exec_()

    def __tool_RemoveCurrentContact(self):
        index = self.__list.selectedIndexes()
        if index:
            index = index[0]
            row = index.row()
            self.__model.removeRecord(row)



    def fill(self):
        names = [
            'Селиверстов Степан Куприянович',
            'Лазарев Григорий Германович',
            'Иван Григорьевна',
            'Аксёнова Евдокия Якововна',
            'Фролов Егор Святославович',
            'Сафонова Лора Руслановна',
            'Дорофеев Мстислав Яковович',
            'Дорофеева Евпраксия Анатольевна',
            'Кудрявцева Евдокия Серапионовна',
            'Лаврентьева Алла Митрофановна',
            'Дмитриева Мария Куприяновна',
            'Гордеева Кира Валерьяновна',
            'Цветков Филат Мстиславович',
            'Костина Регина Семёновна',
            'Логинов Всеволод Ильяович',
            'Маслова Ираида Пётровна',
            'Рябов Альберт Лаврентьевич',
            'Григорьев Константин Онисимович',
            'Калинин Семён Улебович',
            'Ильин Егор Фролович',
            'Шаров Ярослав Эдуардович',
            'Громов Парфений Артёмович',
            'Кириллова Валентина Андреевна',
            'Егоров Еремей Егорович',
            'Белова Наина Альбертовна',
            'Исаев Еремей Владиславович',
            'Афанасьев Улеб Пётрович',
            'Лыткина Виктория Игоревна',
            'Кулакова Феврония Данииловна',
            'Кириллов Вадим Андреевич',
            'Лобанова Ольга Андреевна',
            'Мухин Еремей Юрьевич',
            'Калашникова Нинель Агафоновна',
            'Кононов Владимир Парфеньевич',
            'Данилов Евсей Агафонович',
            'Никифорова Октябрина Пётровна',
            'Кириллов Илья Мэлорович',
            'Денисов Ефим Святославович',
            'Уварова Юлия Валерьевна',
            'Калинина Алевтина Протасьевна'
        ]
        phones = [
            80012208,
            82004235,
            89809584,
            89737860,
            87405098,
            80790108,
            83513276,
            87274083,
            88478272,
            89688682,
            86759116,
            88412388,
            87788263,
            82347197,
            81954939,
            81873562,
            81931832,
            88630865,
            84827825,
            86697799,
            83944395,
            82363782,
            87962015,
            85028190,
            85472089,
            85120317,
            83505489,
            85295349,
            86988174,
            88996340,
            84596977,
            86605651,
            84849238,
            83586671,
            88668978,
            81829247,
            83421867,
            83571970,
            89094362,
            89335215
        ]

        for i in range(40):
            self.__model.addRecord([names[i], '', phones[i]])
