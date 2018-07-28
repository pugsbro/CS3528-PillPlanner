# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewSched.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_viewSched(object):
    def setupUi(self, viewSched):
        viewSched.setObjectName("viewSched")
        viewSched.resize(370, 388)
        viewSched.setMinimumSize(QtCore.QSize(0, 0))
        viewSched.setMaximumSize(QtCore.QSize(370, 513))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        viewSched.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(viewSched)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.text = QtWidgets.QTextBrowser(viewSched)
        self.text.setEnabled(True)
        self.text.setMinimumSize(QtCore.QSize(350, 100))
        self.text.setMaximumSize(QtCore.QSize(350, 110))
        self.text.setObjectName("text")
        self.gridLayout.addWidget(self.text, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.back_to_sched = QtWidgets.QPushButton(viewSched)
        self.back_to_sched.setMinimumSize(QtCore.QSize(0, 50))
        self.back_to_sched.setObjectName("back_to_sched")
        self.gridLayout_3.addWidget(self.back_to_sched, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_2.addLayout(self.gridLayout_3, 3, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.createTXT = QtWidgets.QPushButton(viewSched)
        self.createTXT.setMinimumSize(QtCore.QSize(0, 50))
        self.createTXT.setObjectName("createTXT")
        self.gridLayout_4.addWidget(self.createTXT, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ScheduleDisplay = QtWidgets.QTextBrowser(viewSched)
        self.ScheduleDisplay.setMinimumSize(QtCore.QSize(150, 100))
        self.ScheduleDisplay.setObjectName("ScheduleDisplay")
        self.verticalLayout.addWidget(self.ScheduleDisplay)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.retranslateUi(viewSched)
        QtCore.QMetaObject.connectSlotsByName(viewSched)

    def retranslateUi(self, viewSched):
        _translate = QtCore.QCoreApplication.translate
        viewSched.setWindowTitle(_translate("viewSched", "PillPlanner"))
        self.text.setHtml(_translate("viewSched", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">This is your Schedule</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">If there is something wrong please go Back to change it or ask your Doctor or Pharmacist for help.</span></p></body></html>"))
        self.back_to_sched.setText(_translate("viewSched", "Back"))
        self.createTXT.setText(_translate("viewSched", "Create Text File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewSched = QtWidgets.QWidget()
    ui = Ui_viewSched()
    ui.setupUi(viewSched)
    viewSched.show()
    sys.exit(app.exec_())

