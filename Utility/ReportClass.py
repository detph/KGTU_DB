from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QTextDocument
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrinter, QPrintDialog
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QApplication


class Report():

    printer = None
    previewDialog = None
    document = None
    Html = ''

    def __init__(self, name = 'Отчет', date = QDate.currentDate()):
        self.__initObjects()

        self.name = name
        self.date = date

        self.__setHeader()

    def showPreview(self):
        self.previewDialog.exec()

    def __initObjects(self):
        self.printer = QPrinter(QPrinter.HighResolution)
        #self.printer.setOutputFormat(QPrinter.PdfFormat)
        self.printer.setPageSize(QPrinter.A4)

        self.previewDialog = QPrintPreviewDialog()
        #self.previewDialog.paintRequested.connect()

        self.document = QTextDocument()
        self.document.setDefaultFont(QFont("Times",14))

    def __setHeader(self):
        self.Html += "\
        <div>\
            <h3 align='center'>" + self.name + "</h3>\
            <h4 align='right'>" + self.date.toString() + "</h4>\
        </div>\
        "

    def addString(self, string):
        self.Html += string

    def addTable(self,fields, rows):
        self.Html += "<table  width='100%'>"

        self.Html += "<tr  border='1'>"
        self.Html += "<th><strong>№</strong></th>"
        for item in fields:
            self.Html += "<th><strong>"+str(item)+"</strong></th>"

        self.Html += "</tr>"
        N = 0
        for row in rows:
            N += 1
            self.Html += "<tr>"
            self.Html += "<td align='center'>"+str(N)+"</td>"
            for item in row:
                self.Html += "<td align='center'>"+str(item)+"</td>"
            self.Html += "</tr>"


        self.Html += "</table>"

    def addTableFromModel(self, model, fieldsIndexes = None, fieldsNames = None, fieldsConstraint = None):
        fields = []
        fieldsNames.reverse()
        for i in range(0, model.columnCount()):
            if fieldsIndexes != None:
                if i in fieldsIndexes:
                    if fieldsConstraint != None:
                        fields.append(fieldsConstraint(fieldsNames.pop()))
                    else:
                        fields.append(fieldsNames.pop())
            else:
                fields.append(model.record(0).fieldName(i))

        rows = []
        for i in range(0, model.rowCount()):
            row = []
            for j in range(0, model.columnCount()):
                if j in fieldsIndexes:
                    row.append(model.record(i).value(j))
            rows.append(row)

        self.addTable( fields, rows)

    def Print(self):
        dialog = QPrintDialog(self.printer)

        if dialog.exec():
            self.printer.setFullPage(True)
            self.document.setHtml(self.Html)
            self.document.print(self.printer)

