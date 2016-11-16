


from PyQt5.QtGui import QIcon
from Widgets.PushButton import MYPushButton
from icons import ICON
from Modules.Appointments.BaseClases.base_ui_attribs import BaseUIAttribs
from PyQt5.QtCore import Qt




class FormEdit(BaseUIAttribs):

    def __init__(self, parent=None):
        super(FormEdit, self).__init__(type='editable')
        if parent: self.setParent(parent, Qt.Window)
        self.__btn_ok = MYPushButton(parent=self)
        self.__btn_cancel = MYPushButton(parent=self)

        self.__btn_ok.setIcon(QIcon(ICON.DEFAULT.OK()))
        self.__btn_cancel.setIcon(QIcon(ICON.DEFAULT.cancel()))

        self.btns_layout.addWidget(self.__btn_ok)
        self.btns_layout.addWidget(self.__btn_cancel)




if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = FormEdit()
    win.show()
    app.exec_()

