from PyQt5.QtWidgets import QTextEdit

from Widgets.Dialog import MYDialog






class Form(MYDialog):

    #inits
    def __init__(self):
        super(Form, self).__init__()
        self.__edit = QTextEdit(self)
        self.main_layout.addWidget(self.__edit)

    def setText(self, text):
        self.__edit.setText(text)

    def text(self):
        return self.__edit.toPlainText()

    
    
    
    
    
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = Form()
    win.show()
    sys.exit(app.exec_())