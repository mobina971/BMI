# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BMI.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets 
import sqlite3
import os
import re

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(512, 609)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 200, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 260, 71, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(190, 80, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 140, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 360, 401, 101))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 320, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 200, 131, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 260, 131, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(140, 140, 31, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(140, 80, 51, 31))
        self.label_5.setObjectName("label_5")

        self.pushButton.clicked.connect(self.onclick)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def onclick(self):
        Name = self.lineEdit.text()
        Age = self.lineEdit_2.text()
        Height = self.lineEdit_3.text()
        Weight = self.lineEdit_4.text()
        
        if not re.match("^[a-zA-Z ]+$", Name):
            self.label_3.setText("The name is invalid.Please use letters.")
            return
        if not re.match("^\d+$", Age):
            self.label_3.setText("Age is invalid.Please use numbers.")
            return
        if not re.match("^\d+(\.\d+)?$", Height):
            self.label_3.setText("The Height is invalid.Please use numbers.")
            return
        if not re.match("^\d+(\.\d+)?$", Weight):
            self.label_3.setText("The weight is invalid.Please use numbers.")
            return

        bmi_value = float(Weight) / (float(Height) **2)
        if bmi_value < 18.5 :
            self.label_3.setText('  Your BMI value is : ' + str(bmi_value) + "   underweight")
        elif 18.5 < bmi_value < 24.9 :
            self.label_3.setText('  Your BMI value is : ' + str(bmi_value) + "   optimal")
        elif 25 < bmi_value < 29.9 :
            self.label_3.setText('  Your BMI value is : ' + str(bmi_value) + "   overweight")
        elif 30 < bmi_value < 34.9 :
            self.label_3.setText('  Your BMI value is : ' + str(bmi_value) + "   type 1 obesity")
        elif 35 < bmi_value < 39.9 :
            self.label_3.setText('  Your BMI value is : ' + str(bmi_value) + "   type 2 obesity")
        elif bmi_value > 40 :
            self.label_3.setText('  Your BMI value is : ' + str(bmi_value) + "   type 3 obesity")


        conn = sqlite3.connect(self.database_path)
        c = conn.cursor()
        c.execute(''' 
                INSERT INTO bmi_data(Name, Age, Height, Weight, bmi )
                VALUES (?, ?, ?, ?, ?)
                ''' , (Name, Age, Height, Weight, bmi_value))
        conn.commit()

        c.execute('SELECT * FROM bmi_data WHERE Name=? AND Age=? AND Height=? AND Weight=? AND bmi=?',
                 (Name, Age, Height, Weight, bmi_value))
        result = c.fetchone()
        if result :
            print(" information saved successfully.")
            print(result)
        else :
            print("Failed to save data.")
        conn.close()

        os.chdir('bmiproj')
        with open('bmi_data.txt','a') as file :
            file.write(f'Name : {Name}, Age : {Age}, Height : {Height}, Weight : {Height}, BMI : {bmi_value:.2f}\n')


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Height(m)  :"))
        self.label_2.setText(_translate("Dialog", "Weight(kg) :"))
        self.pushButton.setText(_translate("Dialog", "submit"))
        self.label_4.setText(_translate("Dialog", "Age  :"))
        self.label_5.setText(_translate("Dialog", "Name :"))

        self.database_path = os.path.join(os.path.expanduser("~"),"bmi_database.db")
        conn = sqlite3.connect(self.database_path )
        c = conn.cursor()
        c.execute('''
                  CREATE TABLE IF NOT EXISTS bmi_data
                  (Name TEXT NOT NULL, 
                  Age INTEGER NOT NULL, 
                  Height REAL NOT NULL, 
                  Weight REAL NOT NULL, 
                  bmi REAL)
                  ''')
        
        conn.commit()
        conn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())