# -*- coding: utf-8 -*-


#PYQT
from PyQt5.QtCore    import Qt
from PyQt5.QtGui     import QPixmap

from Widgets.Dialog import MYDialog
from Widgets.Label  import MYLabel
from icons  import ICON





class DefaultMessages(MYDialog):
    def __init__(
            self,
            name,
            message,
            mssg_type='info',
            btn_Cancel=True
    ):

        super(DefaultMessages, self).__init__(
            layout='H',
            layout_spacing=5,

        )

        self.message_type   = mssg_type
        self.image          = MYLabel(parent=self)
        self.text           = MYLabel(parent=self)

        #PARMS
        self.setFixedSize(400, 180)
        self.setWindowTitle(name)

        self.text.setText(message)
        self.text.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.text.setWordWrap(True)

        if   mssg_type ==    'info': self.image.setPixmap(QPixmap(ICON.DIALOG.info()))
        elif mssg_type ==   'error': self.image.setPixmap(QPixmap(ICON.DIALOG.error()))
        elif mssg_type == 'warning': self.image.setPixmap(QPixmap(ICON.DIALOG.warning()))
        elif mssg_type ==  'accept': self.image.setPixmap(QPixmap(ICON.DIALOG.accept()))


        #LAYOUTING
        if btn_Cancel == False: self.close_btn.hide()

        self.main_layout.addWidget(self.image)
        self.main_layout.addWidget(self.text)





class Message(object):
    def __init__(self):
        super(Message, self).__init__()

    def info(self, title, text):
        dialog = DefaultMessages(
            name=title,
            message=text,
            mssg_type='info',
            btn_Cancel=False
        )
        return dialog.exec_()

    def error(self, title, text):
        dialog = DefaultMessages(
            name=title,
            message=text,
            mssg_type='error',
            btn_Cancel=False
        )
        return dialog.exec_()

    def warning(self, title, text, ):
        dialog = DefaultMessages(
            name=title,
            message=text,
            mssg_type='warning',
            btn_Cancel=False
        )
        return dialog.exec_()

    def accept(self, title, text, ):
        dialog = DefaultMessages(
            name=title,
            message=text,
            mssg_type='accept',
            btn_Cancel=False
        )
        return dialog.exec_()





MESSAGE = Message()





if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    MESSAGE.info('asd', 'asd')
    app.exec_()