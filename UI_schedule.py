# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createSched.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_schedule(object):
    def setupUi(self, schedule):
        schedule.setObjectName("schedule")
        schedule.resize(416, 317)
        schedule.setMaximumSize(QtCore.QSize(416, 317))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        schedule.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(schedule)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.go_to_med = QtWidgets.QPushButton(schedule)
        self.go_to_med.setMinimumSize(QtCore.QSize(150, 50))
        self.go_to_med.setObjectName("go_to_med")
        self.gridLayout_3.addWidget(self.go_to_med, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 1, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.infoText = QtWidgets.QTextBrowser(schedule)
        self.infoText.setMinimumSize(QtCore.QSize(150, 60))
        self.infoText.setObjectName("infoText")
        self.gridLayout_4.addWidget(self.infoText, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 3, 1, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.go_to_rout = QtWidgets.QPushButton(schedule)
        self.go_to_rout.setMinimumSize(QtCore.QSize(150, 50))
        self.go_to_rout.setObjectName("go_to_rout")
        self.gridLayout.addWidget(self.go_to_rout, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.run_sched = QtWidgets.QPushButton(schedule)
        self.run_sched.setMinimumSize(QtCore.QSize(150, 110))
        self.run_sched.setObjectName("run_sched")
        self.gridLayout_5.addWidget(self.run_sched, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addLayout(self.gridLayout_5, 1, 2, 2, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.text = QtWidgets.QTextBrowser(schedule)
        self.text.setMinimumSize(QtCore.QSize(350, 110))
        self.text.setMaximumSize(QtCore.QSize(350, 110))
        self.text.setObjectName("text")
        self.gridLayout_6.addWidget(self.text, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout_2.addLayout(self.gridLayout_6, 0, 1, 1, 2)

        self.retranslateUi(schedule)
        QtCore.QMetaObject.connectSlotsByName(schedule)

    def retranslateUi(self, schedule):
        _translate = QtCore.QCoreApplication.translate
        schedule.setWindowTitle(_translate("schedule", "PillPlanner"))
        self.go_to_med.setText(_translate("schedule", "Enter Medications"))
        self.go_to_rout.setText(_translate("schedule", "Create Personal Routines"))
        self.run_sched.setText(_translate("schedule", "Create Schedule"))
        self.text.setHtml(_translate("schedule", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Create your Schedule</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">First tell us about your daily Routine.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Then tell us what Medication you need.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    schedule = QtWidgets.QWidget()
    ui = Ui_schedule()
    ui.setupUi(schedule)
    schedule.show()
    sys.exit(app.exec_())

