import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from sqlite3 import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.printer)

    def printer(self):
        conn = connect("coffee.sqlite")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM coffee")
        k = cursor.fetchall()
        for i in k:
            self.listWidget.addItem(
                f'ID: {i[0]}, сорт: {i[1]}, обжарка: {i[2]},'
                f'помол: {i[3]}, вкус: {i[4]}, цена: {i[5]} руб, объем упаковки: {i[6]} гр \n')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
