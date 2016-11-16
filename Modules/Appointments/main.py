

from Widgets.MainWindow import MYMainWindow

from Modules.Appointments.form_add import FormAdd
from Modules.Appointments.form_edit import FormEdit
from Modules.Appointments.form_view import FormView





class Appointments(MYMainWindow):

    def __init__(self):
        super(Appointments, self).__init__(
            window_size=(720, 480),
            title='Appointments',
            layout='H',
            layout_margins=[10, 10, 10, 10]
        )

        self.__init_Attributes()
        self.__init_Parameters()
        self.__init_Layouting()




    #inits
    def __init_Attributes(self):
        self.__list = None
        self.__form_view = FormView(self)
        self.__form_add  = FormAdd(self)
        self.__form_edit = FormEdit(self)

    def __init_Parameters(self):
        pass

    def __init_Layouting(self):
        self.cwidget.main_layout.addWidget(self.__form_view)



    # EVENTS

    
    # PROPERTY
    

    # METHODS
    
    
    



if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = Appointments()
    win.show()
    app.exec_()