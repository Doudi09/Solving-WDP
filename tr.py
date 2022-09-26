# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'try.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1054, 741)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(220, 250, 481, 351))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 80, 451, 131))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser.setText("fjhsgfjhsgdhjsdjsjdg\nqhgdjhgqsdjsd\njhgqdjhgqsjdshgqd")

        self.pushButton.clicked.connect(self.click)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def click(self):
        self.textBrowser.append('\n\n\n\n\n\n\n\n\n\n \n\n\n\n\n')
        self.textBrowser.append('\n\n\n\n\n\n\n\n\n\n \n\n\n\n\n')
        self.textBrowser.append('\n\n\n\n\n\n\n\n\n\n \n\n\n\n\n')
        self.textBrowser.append('\n\n\n\n\n\n\n\n\n\n \n\n\n\n\n')
        self.textBrowser.append('\n\n\n\n\n\n\n\n\n\n \n\n\n\n\n')
        self.textBrowser.append('\n\n\n\n\n\n\n\n\n\n \n\n\n\n\n')
        self.textBrowser.append('new linen')

    def addText(self,st):
        self.textBrowser.append(st)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))

from PyQt5.Qt import PYQT_VERSION_STR

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    print("PyQt version:", PYQT_VERSION_STR)

    ui.setupUi(Form)
    ui.addText("text added")
    Form.show()
    sys.exit(app.exec_())



