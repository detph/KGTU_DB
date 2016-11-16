

from Widgets.MainWindow import MYMainWindow

from Modules.Contacts.form_add import FormAdd
from Modules.Contacts.form_edit import FormEdit
from Modules.Contacts.form_view import FormView
from Modules.Contacts.BaseClases.base_ui_list import BaseUIList
from PyQt5.QtGui import QIcon
from icons import ICON




class Contacts(MYMainWindow):

    def __init__(self):
        super(Contacts, self).__init__(
            window_size=(720, 480),
            title='Contacts',
            layout='V',
            layout_margins=[10, 10, 10, 10],
            toolbar=True,
            toolbar_section='Top'
        )

        self.__init_Attributes()
        self.__init_Parameters()
        self.__init_Layouting()
        self.__init_Connects()
        self.__init_ToolbarActions()



    #inits
    def __init_Attributes(self):
        self.__list = BaseUIList(self)
        self.__form_view = FormView(self)
        self.__form_add  = FormAdd(self)
        self.__form_edit = FormEdit(self)

    def __init_Parameters(self):
        pass

    def __init_Layouting(self):
        self.cwidget.main_layout.addWidget(self.__form_view)
        self.cwidget.main_layout.addWidget(self.__list)
    
    def __init_Connects(self):
        self.__form_view.btn_edit.clicked.connect(self.__tool_OpenEditForm)
        self.__form_edit.accepted.connect(self.__tool_EditContact)
        self.__form_view.btn_remove.clicked.connect(self.__tool_RemoveCurrentContact)
        self.__form_add.accepted.connect(self.__tool_AddNewContact)

    def __init_ToolbarActions(self):
        self.toolbar.addAction(
            QIcon(ICON.DEFAULT.add()),
            'Добавить новый контакт',
            self.__tool_OpenAddForm
        )
        self.toolbar.addAction(
            QIcon(ICON.DEFAULT.remove()),
            'Удалить выделенные контакты',
            self.__tool_RemoveSelectedContacts
        )



    # class tool
    def __tool_EditContact(self):
        print('Contact edited')

    def __tool_AddNewContact(self):
        print('New contact added')

    def __tool_OpenEditForm(self):
        print('Opened edit form')
        self.__form_edit.exec_()
    
    def __tool_OpenAddForm(self):
        print('Opened add form')
        self.__form_add.exec_()
        
    def __tool_RemoveSelectedContacts(self):
        print('Selected contacs removed')

    def __tool_RemoveCurrentContact(self):
        print('Current contact removed')

    


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = Contacts()
    win.show()
    app.exec_()