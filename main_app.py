import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase
from paths import DB_FILE_PATH

# МОДУЛИ
from Modules.Contacts.main import Contacts
from Modules.Emloyees.main import Employees
from Modules.Notes.main import Notes
from Modules.Main_Window.Window.main import AppMainWindow





APP = QApplication([])
DATABASE = QSqlDatabase('QSQLITE')
DATABASE.setDatabaseName(DB_FILE_PATH)





if DATABASE.open():


    window = AppMainWindow(DATABASE)

    window.show()

    sys.exit(APP.exec_())
else:
    print("Не удалось подключить БД !!!")
















