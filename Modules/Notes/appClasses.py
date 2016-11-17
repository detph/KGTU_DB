import sys

from PyQt5.QtCore import QDate
from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlRecord
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QItemDelegate
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton

from Modules.DBModelAccess.moduleClasses import QBestSqlTableModel
from paths import DB_FILE_PATH

class Record():

    def __init__(self, theme, text, datetime, isactive):

        self.theme = theme
        self.text = text
        self.datetime = datetime
        self.isActive = isactive
        self.shownTimes = 0

class Application(QApplication):

    currentIndex = -1
    currentRecord = None

    def __init__(self, args = []):
        super(QApplication, self).__init__(args)
        import Widgets.notes
        self.window = Widgets.notes.getForm()
        self.timer = QTimer()
        self.line = []

    def setDataView(self):

        self.currentDateTime = QDateTime()

        self.model = QBestSqlTableModel(DB_FILE_PATH)
        # self.model.setProxy(self.model)
        self.model.selectTable("notes")
        # print(self.model.rowCount())



        # self.model.setHeaderData(0, 0, "Hello")
        self.model.setHeaders(["Время", "Тема", "Выполнение"])
        self.window.noteList.setModel(self.model)
        self.window.noteList.setColumnWidth(0, 70)
        self.window.noteList.hideColumn(3)
        self.window.noteList.setItemDelegate(noteListDelegate(self.window.noteList))

        self.window.calendar.clicked.connect(self.selectCalendarDate)
        self.window.noteList.clicked.connect(self.selectNote)

        self.window.addNoteButton.clicked.connect(self.addNote)
        self.window.remNoteButton.clicked.connect(self.remNote)
        self.window.saveButton.clicked.connect(self.saveNote)

        self.window.calendar.setSelectedDate(QDate())
        self.selectCalendarDate()

        self.timer.timeout.connect(self.timerNoteEvent)

        self.dialog = QMessageBox(self.window)
        self.dialog.addButton(QPushButton("Отложить"), QMessageBox.RejectRole)
        self.dialog.addButton(QPushButton("Выполнено"), QMessageBox.AcceptRole)

        self.putDateTimeToLineFromTable()


    def selectCalendarDate(self):
        date = self.window.calendar.selectedDate()
        self.currentDateTime.setDate(date)
        self.window.dateTimeEdit.setDateTime(self.currentDateTime)
        self.model.setFilter("date(datetime) == date('" + str(date.toPyDate()) + "')")

        # print(self.model.getRecord(table="employees", gettingSetting=1))

    def selectNote(self, row = None):
        index = self.model.rowCount() - 1
        if row:
            index = row.row()
        self.currentIndex = index
        self.currentRecord = self.model.record(index)
        self.window.noteList.selectRow(index)
        print(index)
        self.currentDateTime = QDateTime.fromString(
            self.currentRecord.value(0)[0:16],
            "yyyy-MM-dd hh:mm"
        )
        self.window.dateTimeEdit.setDateTime(self.currentDateTime)
        self.showNoteItems(
            self.model.record(index).value(1),
            self.model.record(index).value(2),
            self.model.record(index).value(3)
        )
        self.window.themeEdit.setFocus()
        self.getDateTimeFromStr(self.currentRecord.value(0)[:])

    def addNote(self):
        self.currentIndex = 0
        self.currentDateTime.setTime(QTime.currentTime())
        datetime = str(self.currentDateTime.toPyDateTime())[0:23]
        self.showNoteItems("", 0,  "")
        self.model.addRecord(fields=[datetime, " ", 0, " "])
        self.selectCalendarDate()
        self.selectNote()

    def remNote(self):
        self.currentIndex = -1
        rows = self.window.noteList.selectedIndexes()
        if rows:
            for item in rows:
                self.model.removeRow(item.row())
            self.selectCalendarDate()
        self.putDateTimeToLineFromTable()

    def saveNote(self):
        if self.currentIndex >= 0:
            rowNumb = self.currentIndex
            row = self.currentRecord
            dateEnd = row.value(0)[19:]
            row.clearValues()
            row.setValue(0, str(self.window.dateTimeEdit.dateTime().toPyDateTime()) + dateEnd)
            row.setValue(1, self.window.themeEdit.text())
            row.setValue(2, self.window.completionEdit.currentIndex())
            row.setValue(3, self.window.textEdit.toPlainText())
            self.model.setRecord(rowNumb, row)
            self.showNoteItems("", 0, "")
            self.currentIndex -1
            self.timer.start(1000)
            self.putDateTimeToLineFromTable()

    @staticmethod
    def getDateTimeFromStr(string):
        pattern = "yyyy-MM-dd HH:mm"
        return QDateTime.fromString(string[0:16], pattern)

    @staticmethod
    def isDateTimeEquales(date2):
        date1 = QDateTime.currentDateTime()
        # print(str(date2.toPyDateTime())[0:16], str(date1.toPyDateTime())[0:16])
        # if str(date2.toPyDateTime())[0:16] == str(date1.toPyDateTime())[0:16]: return True
        if date2.toPyDateTime() <= date1.toPyDateTime(): return True
        return False

    def timerNoteEvent(self):
        # print(QDateTime.currentDateTime().toString())
        # dt = self.getNearestDateTime()
        if len(self.line) > 0:
            record = self.getNearestActiveRecordFromLine()
            # print(record.datetime.toString())
            if self.isDateTimeEquales(record.datetime):
                self.dialog.setText(record.text)
                self.dialog.setWindowTitle(record.theme)
                self.window.showNormal()
                if self.dialog.exec() == 1:
                    print("Задача выполенна")
                    self.model.setFilter("completion < 2")
                    record = self.model.record(0)
                    record.setValue(2, 2)
                    self.model.setRecord(0, record)
                    self.putDateTimeToLineFromTable()
                    self.selectCalendarDate()
                else:
                    self.model.setFilter("completion < 2")
                    record = self.model.record(0)
                    self.selectNote(0)
                    # datetime = str(self.getDateTimeFromStr(
                    #     record.value(0)
                    # ))
                    # print(datetime)
                    # record.setValue(0, datetime)
                    # self.model.setRecord(0, record)

                    self.timer.stop()
                    # self.putDateTimeToLineFromTable()

    def putDateTimeToLineFromTable(self):
        self.model.setFilter("completion < 2")
        self.model.sort(0, Qt.AscendingOrder)
        self.line = []

        if self.model.rowCount():
            record = self.model.record(0)
            self.line.append(
                Record(
                    theme=record.value(1),
                    datetime=self.getDateTimeFromStr(record.value(0)),
                    text=record.value(3),
                    isactive=record.value(2)
                )
            )
        self.selectCalendarDate()
        self.timer.start(1000)

    def getNearestActiveRecordFromLine(self):
        # self.sortDateTimeLine()
        for item in self.line:
            if item.isActive < 2:
                return item

    def clickEnterEditingNote(self, event):
        print(event.key())
        # super(self.window.noteEditFrame, self).keyPressEvent()

    def showNoteItems(self, theme, comp, text):

        self.window.themeEdit.setText(theme)
        self.window.completionEdit.setCurrentIndex(comp)
        self.window.textEdit.setText(text)

    def start(self):

        self.setDataView()
        self.window.show()
        self.timer.start(1000)

        sys.exit(self.exec_())

class noteListDelegate(QItemDelegate ):

    def __init__(self, ListView):
        super(QItemDelegate, self).__init__()
        self.ListView = ListView

    def paint(self, Painter, StyleOptionViewItem, ModelIndex):
        try:
            if self.ListView.selecterIndexes()[0].row() == ModelIndex.row():
                Painter.setColor(Qt.red)
                Painter.drawRect(StyleOptionViewItem.rect)
        except: pass
        text = ""
        col = ModelIndex.column()
        str = ModelIndex.data(Qt.DisplayRole)
        if col == 2:
            if str == 0:
                text = "Не выполено"
            elif str == 1:
                text = "В процессе"
            elif str == 2:
                text = "Выполнено"
        elif col == 0:
            datetimeText = ""
            if len(str) > 0:
                datetimeText = QDateTime.fromString(
                    str[0:16],
                    "yyyy-MM-dd HH:mm"
                ).time().toString()[0:5]

            text = datetimeText
        elif col == 1:
            if str.isspace():
                text = "Пусто"
            else:
                text = str
        Painter.drawText(StyleOptionViewItem.rect, Qt.AlignCenter, text)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        pass













