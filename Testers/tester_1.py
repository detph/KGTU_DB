from PyQt5.QtCore import QDate, QDateTime, QTime



t1 = QTime(20, 0)
t2 = QTime(21, 0)
d1 = QDate(2012, 10, 10)
d2 = QDate(2012, 10, 11)

dt1 = QDateTime()
dt2 = QDateTime()

dt1.setDate(d1)
dt1.setTime(t1)

dt2.setDate(d2)
dt2.setTime(t2)

print('date 1 = ', d1.toString())
print('date 2 = ', d2.toString())
print(dt2 < dt1)