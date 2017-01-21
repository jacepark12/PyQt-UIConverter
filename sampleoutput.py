# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/parkjaesung/QtWorkspace/UIConverter/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 412)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 471, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.uifiledirText = QtWidgets.QTextBrowser(self.frame)
        self.uifiledirText.setGeometry(QtCore.QRect(10, 40, 451, 31))
        self.uifiledirText.setObjectName("uifiledirText")
        self.uifilebutton = QtWidgets.QPushButton(self.frame)
        self.uifilebutton.setGeometry(QtCore.QRect(10, 0, 151, 32))
        self.uifilebutton.setObjectName("uifilebutton")
        self.frame_2 = QtWidgets.QFrame(self.centralWidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 190, 471, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.outputdirText = QtWidgets.QTextBrowser(self.frame_2)
        self.outputdirText.setGeometry(QtCore.QRect(10, 40, 451, 31))
        self.outputdirText.setObjectName("outputdirText")
        self.outputbutton = QtWidgets.QPushButton(self.frame_2)
        self.outputbutton.setGeometry(QtCore.QRect(10, 0, 151, 32))
        self.outputbutton.setObjectName("outputbutton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 290, 171, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(80, 20, 381, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 528, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.uifilebutton.setText(_translate("MainWindow", "QtDesigner UI file"))
        self.outputbutton.setText(_translate("MainWindow", "Output directory"))
        self.pushButton_3.setText(_translate("MainWindow", "Convert Right Away!"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">QtDesigner To Python file. Just press a button!</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

