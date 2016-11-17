



from Modules.Contacts.BaseClases.base_ui_attribs import BaseUIAttribs
from Widgets.Dialog import MYDialog




class FormEdit(MYDialog):

    def __init__(self, parent=None):
        super(FormEdit, self).__init__(
            parent=parent,
            title='Редактирование контакта'
        )
        self.attribs = BaseUIAttribs('editable')
        self.main_layout.addWidget(self.attribs)
        self.setFixedSize(330, 120)


    def accept(self):
        name = self.attribs.fio.text()
        phone = self.attribs.phone.text()
        self.attribs.dataStructure.setFIO(name)
        self.attribs.dataStructure.setPhone(phone)
        super(FormEdit, self).accept()







if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = FormEdit()
    win.show()
    app.exec_()

