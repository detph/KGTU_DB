# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:




from PyQt5.QtWidgets import QPushButton

from parameters      import ENABLE_STYLES
from style import STYLE


class MYPushButton(QPushButton):
    def __init__(self,
                 parent=None,
                 text=''):
        super(MYPushButton, self).__init__()
        if parent: self.setParent(parent)
        if text: self.setText(text)
        self.setFixedHeight(30)
        if ENABLE_STYLES: self.setStyleSheet(STYLE.PushButton)
