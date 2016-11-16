



from Modules.Contacts.BaseClases.base_ui_attribs import BaseUIAttribs
from Widgets.Dialog import MYDialog




class FormEdit(MYDialog):

    def __init__(self, parent=None):
        super(FormEdit, self).__init__(
            parent=parent,
            title='Edit Contact'
        )
        self.attribs = BaseUIAttribs('editable')
        self.main_layout.addWidget(self.attribs)
        self.setFixedSize(330, 120)





if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = FormEdit()
    win.show()
    app.exec_()

