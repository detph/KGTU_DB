# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:



from PyQt5.QtWidgets import QTableView

from parameters      import ENABLE_STYLES
from style import STYLE


class MYTableView(QTableView):
    #INIT
    def __init__(self, parent=None):
        super(MYTableView, self).__init__()

        #PARMS
        if parent: self.setParent(parent)

        self.setAlternatingRowColors(True)
        self.horizontalHeader().setStretchLastSection(True)

        if ENABLE_STYLES: self.setStyleSheet(STYLE.ListWidget)
