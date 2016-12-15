from PyQt5.QtWidgets import QTabWidget

from Modules.Tasks.main import Tasks
from Widgets.MainWindow import MYMainWindow
from Modules.Events.main import Events
from Modules.Notes.main import Notes
from Modules.Contacts.main import Contacts
from Modules.Emloyees.main import Employees


class AppMainWindow(MYMainWindow):
    def __init__(self, DB):
        super(AppMainWindow, self).__init__(
            window_size=(1000, 600),
            title='Записная книжка',
            layout_margins=[10, 10, 10, 10]
        )

        self.__init_Attributes(DB)
        self.__init_Parameters()
        self.__init_Layouting()
        self.__init_Connects()


    #inits
    def __init_Attributes(self, DB):
        self.tabs = QTabWidget(self)
        self.events = Events(DB=DB)
        self.contacts = Contacts(DB=DB)
        self.notes = Notes(DB=DB)
        self.employees = Employees(DB=DB)
        self.tasks = Tasks(DB=DB)

    def __init_Parameters(self):
        self.tabs.addTab(self.events, 'Дела')
        self.tabs.addTab(self.contacts, 'Контакты')
        self.tabs.addTab(self.notes, 'Заметки')
        self.tabs.addTab(self.employees, 'Сотрудники')
        self.tabs.addTab(self.tasks, 'Поручения')

    def __init_Connects(self):
        self.employees.pushedCreateTask.connect(self.__openTasksCreate)

    def __init_Layouting(self):
        self.cwidget.main_layout.addWidget(self.tabs)

    def __openTasksCreate(self, name):
        self.tabs.setCurrentIndex(4)
        self.tasks.createEmployeeTask(name)