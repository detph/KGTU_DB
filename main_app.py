import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase
from paths import DB_FILE_PATH
from Utility.messages import MESSAGE

# МОДУЛИ
from Modules.Main_Window.Window.main import AppMainWindow





APP = QApplication([])
DATABASE = QSqlDatabase('QSQLITE')
DATABASE.setDatabaseName(DB_FILE_PATH)





if DATABASE.open():

    window = AppMainWindow(DATABASE)
    window.show()
    sys.exit(APP.exec_())

else:
    MESSAGE.error(
        title='Ошибка базыд данных',
        text='Не удалось подключить базу данных < ' + DB_FILE_PATH + '> '
    )
















