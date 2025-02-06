import unittest
from PyQt5 import QtWidgets
from bmi import Ui_Dialog  

class TestBMIApp(unittest.TestCase):
    def setUp(self):
        self.app = QtWidgets.QApplication([])
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)

    def test_valid_input(self):
        self.ui.lineEdit.setText("John Doe")
        self.ui.lineEdit_2.setText("25")
        self.ui.lineEdit_3.setText("1.75")
        self.ui.lineEdit_4.setText("70")
        self.ui.pushButton.click()
        self.assertIn("optimal", self.ui.label_3.text())

    def test_invalid_name(self):
        self.ui.lineEdit.setText("John123")
        self.ui.lineEdit_2.setText("25")
        self.ui.lineEdit_3.setText("1.75")
        self.ui.lineEdit_4.setText("70")
        self.ui.pushButton.click()
        self.assertEqual("The name is invalid.Please use letters.", self.ui.label_3.text())

    def test_invalid_age(self):
        self.ui.lineEdit.setText("John Doe")
        self.ui.lineEdit_2.setText("twenty-five")
        self.ui.lineEdit_3.setText("1.75")
        self.ui.lineEdit_4.setText("70")
        self.ui.pushButton.click()
        self.assertEqual("Age is invalid.Please use numbers.", self.ui.label_3.text())

    def test_invalid_height(self):
        self.ui.lineEdit.setText("John Doe")
        self.ui.lineEdit_2.setText("25")
        self.ui.lineEdit_3.setText("height")
        self.ui.lineEdit_4.setText("70")
        self.ui.pushButton.click()
        self.assertEqual("The Height is invalid.Please use numbers.", self.ui.label_3.text())

    def test_invalid_weight(self):
        self.ui.lineEdit.setText("John Doe")
        self.ui.lineEdit_2.setText("25")
        self.ui.lineEdit_3.setText("1.75")
        self.ui.lineEdit_4.setText("weight")
        self.ui.pushButton.click()
        self.assertEqual("The weight is invalid.Please use numbers.", self.ui.label_3.text())

if __name__ == "__main__":
    unittest.main()