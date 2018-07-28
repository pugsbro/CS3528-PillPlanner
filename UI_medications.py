# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medications.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_medications(object):
    def setupUi(self, medications):
        medications.setObjectName("medications")
        medications.resize(504, 404)
        medications.setMaximumSize(QtCore.QSize(600, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        medications.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(medications)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.instructionDisplayDose = QtWidgets.QTextBrowser(medications)
        self.instructionDisplayDose.setMinimumSize(QtCore.QSize(160, 30))
        self.instructionDisplayDose.setMaximumSize(QtCore.QSize(160, 30))
        self.instructionDisplayDose.setObjectName("instructionDisplayDose")
        self.gridLayout_5.addWidget(self.instructionDisplayDose, 0, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.instructionDisplayMult = QtWidgets.QTextBrowser(medications)
        self.instructionDisplayMult.setMinimumSize(QtCore.QSize(160, 30))
        self.instructionDisplayMult.setMaximumSize(QtCore.QSize(160, 30))
        self.instructionDisplayMult.setObjectName("instructionDisplayMult")
        self.gridLayout_5.addWidget(self.instructionDisplayMult, 1, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.instructionDisplayJump = QtWidgets.QTextBrowser(medications)
        self.instructionDisplayJump.setMinimumSize(QtCore.QSize(160, 30))
        self.instructionDisplayJump.setMaximumSize(QtCore.QSize(160, 30))
        self.instructionDisplayJump.setObjectName("instructionDisplayJump")
        self.gridLayout_5.addWidget(self.instructionDisplayJump, 2, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addLayout(self.gridLayout_5, 1, 1, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.nameOfMed = QtWidgets.QPlainTextEdit(medications)
        self.nameOfMed.setMinimumSize(QtCore.QSize(150, 30))
        self.nameOfMed.setMaximumSize(QtCore.QSize(150, 30))
        self.nameOfMed.setObjectName("nameOfMed")
        self.gridLayout_7.addWidget(self.nameOfMed, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.searchMed = QtWidgets.QPushButton(medications)
        self.searchMed.setMinimumSize(QtCore.QSize(150, 30))
        self.searchMed.setObjectName("searchMed")
        self.gridLayout_7.addWidget(self.searchMed, 1, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.addMed = QtWidgets.QPushButton(medications)
        self.addMed.setMinimumSize(QtCore.QSize(150, 30))
        self.addMed.setMaximumSize(QtCore.QSize(150, 16777215))
        self.addMed.setObjectName("addMed")
        self.gridLayout_7.addWidget(self.addMed, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_7, 1, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.removeMed = QtWidgets.QPushButton(medications)
        self.removeMed.setMinimumSize(QtCore.QSize(150, 30))
        self.removeMed.setObjectName("removeMed")
        self.gridLayout_9.addWidget(self.removeMed, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout_2.addLayout(self.gridLayout_9, 3, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.multiplicityChoice = QtWidgets.QComboBox(medications)
        self.multiplicityChoice.setMinimumSize(QtCore.QSize(150, 30))
        self.multiplicityChoice.setObjectName("multiplicityChoice")
        self.gridLayout_8.addWidget(self.multiplicityChoice, 1, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.dosageChoice = QtWidgets.QComboBox(medications)
        self.dosageChoice.setMinimumSize(QtCore.QSize(150, 30))
        self.dosageChoice.setObjectName("dosageChoice")
        self.gridLayout_8.addWidget(self.dosageChoice, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.jumpChoice = QtWidgets.QComboBox(medications)
        self.jumpChoice.setMinimumSize(QtCore.QSize(150, 30))
        self.jumpChoice.setObjectName("jumpChoice")
        self.gridLayout_8.addWidget(self.jumpChoice, 2, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addLayout(self.gridLayout_8, 1, 2, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.text = QtWidgets.QTextBrowser(medications)
        self.text.setMinimumSize(QtCore.QSize(350, 110))
        self.text.setMaximumSize(QtCore.QSize(600, 600))
        self.text.setObjectName("text")
        self.gridLayout_6.addWidget(self.text, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout_2.addLayout(self.gridLayout_6, 0, 0, 1, 3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.back_to_sched = QtWidgets.QPushButton(medications)
        self.back_to_sched.setMinimumSize(QtCore.QSize(0, 50))
        self.back_to_sched.setObjectName("back_to_sched")
        self.gridLayout_4.addWidget(self.back_to_sched, 1, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addLayout(self.gridLayout_4, 4, 0, 1, 3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.medicationListDisplay = QtWidgets.QComboBox(medications)
        self.medicationListDisplay.setMinimumSize(QtCore.QSize(150, 30))
        self.medicationListDisplay.setObjectName("medicationListDisplay")
        self.gridLayout_3.addWidget(self.medicationListDisplay, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 0, 1, 3)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.infoText = QtWidgets.QTextBrowser(medications)
        self.infoText.setMinimumSize(QtCore.QSize(326, 60))
        self.infoText.setMaximumSize(QtCore.QSize(384, 30))
        self.infoText.setObjectName("infoText")
        self.gridLayout_10.addWidget(self.infoText, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addLayout(self.gridLayout_10, 3, 1, 1, 2)

        self.retranslateUi(medications)
        QtCore.QMetaObject.connectSlotsByName(medications)

    def retranslateUi(self, medications):
        _translate = QtCore.QCoreApplication.translate
        medications.setWindowTitle(_translate("medications", "PillPlanner"))
        self.instructionDisplayDose.setHtml(_translate("medications", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Dose of your Medication:</span></p></body></html>"))
        self.instructionDisplayMult.setHtml(_translate("medications", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Number of Doses per Day:</p></body></html>"))
        self.instructionDisplayJump.setHtml(_translate("medications", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Time between Doses:</span></p></body></html>"))
        self.nameOfMed.setPlainText(_translate("medications", "Medication Name"))
        self.searchMed.setText(_translate("medications", "Search..."))
        self.addMed.setText(_translate("medications", "Add Medication"))
        self.removeMed.setText(_translate("medications", "Remove Medication"))
        self.text.setHtml(_translate("medications", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Medications</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">What Medications are you taking?</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">We need first their names and of course the dosage and the number of times you should take them every day.</span></p></body></html>"))
        self.back_to_sched.setText(_translate("medications", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    medications = QtWidgets.QWidget()
    ui = Ui_medications()
    ui.setupUi(medications)
    medications.show()
    sys.exit(app.exec_())

