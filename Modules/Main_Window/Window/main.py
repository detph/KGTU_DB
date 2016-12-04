from PyQt5.QtWidgets import QTabWidget

from Widgets.MainWindow import MYMainWindow
from Modules.Events.main import Events
from Modules.Notes.main import Notes
from Modules.Contacts.main import Contacts
from Modules.Emloyees.main import Employees


class AppMainWindow(MYMainWindow):

    #SIGNALS



    def __init__(self, DB):
        super(AppMainWindow, self).__init__(
            window_size=(720, 480),
            title='Записная книжка',
            layout_margins=[0, 0, 0, 0]
        )

        self.__init_Attributes(DB)
        self.__init_Parameters()
        self.__init_Layouting()



    #inits
    def __init_Attributes(self, DB):
        self.tabs = QTabWidget(self)
        self.events = Events(DB=DB)
        self.contacts = Contacts(DB=DB)
        self.notes = Notes(DB=DB)
        self.employees = Employees(DB=DB)

    def __init_Parameters(self):
        self.tabs.addTab(self.events, 'Дела')
        self.tabs.addTab(self.contacts, 'Контакты')
        self.tabs.addTab(self.notes, 'Заметки')
        self.tabs.addTab(self.employees, 'Сотрудники')

    def __init_Layouting(self):
        self.cwidget.main_layout.addWidget(self.tabs)