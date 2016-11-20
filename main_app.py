import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase
from paths import DB_FILE_PATH

# МОДУЛИ
from Modules.Contacts.main import Contacts
from Modules.Events.main import Events







APP = QApplication([])
DATABASE = QSqlDatabase('QSQLITE')
DATABASE.setDatabaseName(DB_FILE_PATH)





if DATABASE.open():

    # mdl_Contacts = Contacts(DB=DATABASE)
    mdl_Events = Events(DATABASE)

    mdl_Events.show()
    # mdl_Contacts.show()



    sys.exit(APP.exec_())
else:
    print("Не удалось подключить БД !!!")
















