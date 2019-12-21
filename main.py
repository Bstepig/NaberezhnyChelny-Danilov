#!/usr/bin/python3

# -*- coding: utf-8 -*-
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.initUI()
        self.show()

    def initUI(self):
        self.con = sqlite3.connect('coffee.sqlite')
        self.load_table()

    def load_table(self):
        cur = self.con.cursor()
        self.data = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.table.setRowCount(len(self.data))
        self.table.setColumnCount(len(self.data[0]))
        self.titles = [description[0] for description in cur.description]
        self.table.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(self.data):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
