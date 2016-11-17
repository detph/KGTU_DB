


from Modules.Appointments.BaseClases.base_ui_attribs import BaseUIAttribs
from Widgets.Dialog import MYDialog





class FormAdd(MYDialog):

    def __init__(self, parent=None):
        super(FormAdd, self).__init__(
            parent=parent,
            title='Добавление дела'
        )
        self.attribs = BaseUIAttribs('editable')
        self.main_layout.addWidget(self.attribs)










if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = FormAdd()
    win.show()
    app.exec_()

