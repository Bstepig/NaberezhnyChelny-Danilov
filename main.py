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
        self.pushButton.clicked.connect(self.change)
        self.pushButton_2.clicked.connect(self.add)

    def add(self):
        self.open_form()

    def change(self):
        if self.table.selectedItems():
            old_data = self.data[self.table.selectedItems()[0].row()]
            self.open_form(old_data)

    def open_form(self, data=None):
        self.form = ChangeForm()
        if data:
            self.form.pushButton.setText("Изменить")
            self.form.lineEdit.setText(data[1])
            self.form.lineEdit_2.setText(data[2])
            self.form.lineEdit_4.setText(data[3])
            self.form.textEdit.setText(data[4])
            self.form.doubleSpinBox.setValue(data[5])
            self.form.spinBox.setValue(data[6])
            self.form.pushButton.clicked.connect(lambda: self.close_form(data))
        else:
            self.form.pushButton.setText("Добавить")
            self.form.lineEdit.setText('')
            self.form.lineEdit_2.setText('')
            self.form.lineEdit_4.setText('')
            self.form.textEdit.setText('')
            self.form.doubleSpinBox.setValue(0)
            self.form.spinBox.setValue(0)
            self.form.pushButton.clicked.connect(self.close_form)

    def close_form(self, data=None):
        title = self.form.lineEdit.text()
        roast = self.form.lineEdit_2.text()
        status = self.form.lineEdit_4.text()
        desc = self.form.textEdit.toPlainText()
        price = self.form.doubleSpinBox.value()
        amount = self.form.spinBox.value()
        n_data = title, roast, status, desc, price, amount
        cur = self.con.cursor()
        if not data:
            cur.execute(
                """
INSERT INTO coffee (title, roast, status, description, price, amount) 
VALUES (?, ?, ?, ?, ?, ?)""", n_data)
        else:
            cur.execute(f"""
UPDATE coffee 
SET title = ?, roast = ?, status = ?, description = ?, price = ?, amount = ? 
WHERE ID = {data[0]}""", n_data)
        self.con.commit()
        self.form.close()
        self.load_table()


class ChangeForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
