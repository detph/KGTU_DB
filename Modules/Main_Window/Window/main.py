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
            layout_margins=[0, 0, 0, 0],
            toolbar=True,
            toolbar_section='Left'
        )

        self.__init_Attributes(DB)
        self.__init_Parameters()
        self.__init_Layouting()
        self.__init_ToolbarActions()



    #inits
    def __init_Attributes(self, DB):
        self.events = Events(DB=DB)
        self.contacts = Contacts(DB=DB)
        self.notes = Notes(DB=DB)
        self.employees = Employees(DB=DB)

    def __init_Parameters(self):
        pass

    def __init_Layouting(self):
        self.cwidget.main_layout.addWidget(self.events)


    def __init_ToolbarActions(self):
        self.toolbar.addAction(
            'Заметки',
            self.notes.show
        )
        self.toolbar.addAction(
            'Сотрудники',
            self.employees.show
        )
        self.toolbar.addAction(
            'Контакты',
            self.contacts.show
        )

    # TOOLS

    # EVENTS


    # PROPERTY


    # METHODS