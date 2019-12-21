# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(314, 458)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(30, 30, 256, 393))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.splitter)
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(self.splitter)
        self.label_6.setObjectName("label_6")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.splitter)
        self.doubleSpinBox.setMaximum(5000.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_5 = QtWidgets.QLabel(self.splitter)
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(self.splitter)
        self.spinBox.setMaximum(5000)
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Название"))
        self.label_2.setText(_translate("Form", "Степень обжарки"))
        self.label_3.setText(_translate("Form", "Статус (молотый / в зернах)"))
        self.label_4.setText(_translate("Form", "Описание вкуса"))
        self.label_6.setText(_translate("Form", "Цена"))
        self.label_5.setText(_translate("Form", "Объем"))
        self.pushButton.setText(_translate("Form", "Добавить"))
