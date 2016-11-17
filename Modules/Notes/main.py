import sys

from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    from Modules.Notes import appClasses
    app = appClasses.Application()
    app.start()

