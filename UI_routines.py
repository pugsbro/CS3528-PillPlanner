# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'routines.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_routines(object):
    def setupUi(self, routines):
        routines.setObjectName("routines")
        routines.resize(508, 469)
        routines.setMaximumSize(QtCore.QSize(600, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        routines.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(routines)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.infoText = QtWidgets.QTextBrowser(routines)
        self.infoText.setMinimumSize(QtCore.QSize(150, 60))
        self.infoText.setMaximumSize(QtCore.QSize(16777215, 30))
        self.infoText.setObjectName("infoText")
        self.gridLayout_10.addWidget(self.infoText, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout_2.addLayout(self.gridLayout_10, 3, 1, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.timeStart = QtWidgets.QTimeEdit(routines)
        self.timeStart.setMinimumSize(QtCore.QSize(150, 30))
        self.timeStart.setTime(QtCore.QTime(6, 0, 0))
        self.timeStart.setObjectName("timeStart")
        self.gridLayout_7.addWidget(self.timeStart, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addLayout(self.gridLayout_7, 1, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.routTypeChoice = QtWidgets.QComboBox(routines)
        self.routTypeChoice.setMinimumSize(QtCore.QSize(150, 30))
        self.routTypeChoice.setObjectName("routTypeChoice")
        self.routTypeChoice.addItem("")
        self.routTypeChoice.addItem("")
        self.routTypeChoice.addItem("")
        self.routTypeChoice.addItem("")
        self.gridLayout_8.addWidget(self.routTypeChoice, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addLayout(self.gridLayout_8, 1, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.routListDisplay = QtWidgets.QComboBox(routines)
        self.routListDisplay.setMinimumSize(QtCore.QSize(150, 30))
        self.routListDisplay.setObjectName("routListDisplay")
        self.gridLayout_3.addWidget(self.routListDisplay, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addLayout(self.gridLayout_3, 6, 0, 1, 2)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.text = QtWidgets.QTextBrowser(routines)
        self.text.setMinimumSize(QtCore.QSize(350, 110))
        self.text.setMaximumSize(QtCore.QSize(600, 600))
        self.text.setObjectName("text")
        self.gridLayout_6.addWidget(self.text, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout_2.addLayout(self.gridLayout_6, 0, 0, 1, 2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.back_to_sched = QtWidgets.QPushButton(routines)
        self.back_to_sched.setMinimumSize(QtCore.QSize(0, 50))
        self.back_to_sched.setObjectName("back_to_sched")
        self.gridLayout_4.addWidget(self.back_to_sched, 1, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addLayout(self.gridLayout_4, 8, 0, 1, 2)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.removeRout = QtWidgets.QPushButton(routines)
        self.removeRout.setMinimumSize(QtCore.QSize(150, 30))
        self.removeRout.setObjectName("removeRout")
        self.gridLayout_9.addWidget(self.removeRout, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout_2.addLayout(self.gridLayout_9, 7, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.addRout = QtWidgets.QPushButton(routines)
        self.addRout.setMinimumSize(QtCore.QSize(150, 30))
        self.addRout.setObjectName("addRout")
        self.gridLayout.addWidget(self.addRout, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.timeEnd = QtWidgets.QTimeEdit(routines)
        self.timeEnd.setMinimumSize(QtCore.QSize(150, 30))
        self.timeEnd.setTime(QtCore.QTime(7, 0, 0))
        self.timeEnd.setObjectName("timeEnd")
        self.gridLayout_11.addWidget(self.timeEnd, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addLayout(self.gridLayout_11, 2, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.customRout = QtWidgets.QPlainTextEdit(routines)
        self.customRout.setMinimumSize(QtCore.QSize(150, 30))
        self.customRout.setMaximumSize(QtCore.QSize(16777215, 30))
        self.customRout.setObjectName("customRout")
        self.gridLayout_12.addWidget(self.customRout, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addLayout(self.gridLayout_12, 2, 1, 1, 1)

        self.retranslateUi(routines)
        QtCore.QMetaObject.connectSlotsByName(routines)

    def retranslateUi(self, routines):
        _translate = QtCore.QCoreApplication.translate
        routines.setWindowTitle(_translate("routines", "PillPlanner"))
        self.routTypeChoice.setItemText(0, _translate("routines", "sleep"))
        self.routTypeChoice.setItemText(1, _translate("routines", "eat"))
        self.routTypeChoice.setItemText(2, _translate("routines", "work"))
        self.routTypeChoice.setItemText(3, _translate("routines", "custom routine"))
        self.text.setHtml(_translate("routines", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Personal Routines</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Here you tell us about your day.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Some of your routines could interfere with your Medication.<br />You may be required to take Antibiotics on an empty stomach for example. Your prescription will have information about this. <br />If in doubt you should consult your Medication instructions, a Pharmacist or your Doctor.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.back_to_sched.setText(_translate("routines", "Back"))
        self.removeRout.setText(_translate("routines", "Remove Routine"))
        self.addRout.setText(_translate("routines", "Add Routine"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    routines = QtWidgets.QWidget()
    ui = Ui_routines()
    ui.setupUi(routines)
    routines.show()
    sys.exit(app.exec_())

