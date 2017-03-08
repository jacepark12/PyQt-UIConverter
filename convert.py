# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import configparser


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.uifile = ''
        self.outputdir = ''
        self.tempdir = ''
        self.bundle_dir = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 412)
        self.mainwindow = MainWindow
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
        self.log = QtWidgets.QTextBrowser(self.centralWidget)
        self.log.setGeometry(QtCore.QRect(520, 20, 256, 301))
        self.log.setObjectName("log")
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

        # Set Event handling
        self.uifilebutton.clicked.connect(self.getUIFile)
        self.outputbutton.clicked.connect(self.getOutputDirectory)
        self.pushButton_3.clicked.connect(self.convert)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.uifilebutton.setText(_translate("MainWindow", "QtDesigner UI file"))
        self.outputbutton.setText(_translate("MainWindow", "Output directory"))
        self.pushButton_3.setText(_translate("MainWindow", "Convert Right Away!"))
        self.textBrowser_3.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">QtDesigner To Python file. Just press a button!</p></body></html>"))

    # PyQt event handling code
    # TODO extract as a module

    def getUIFile(self):
        self.uifile, _ = QtWidgets.QFileDialog.getOpenFileName(self.mainwindow, 'Open UI File', './', filter='*.ui')
        # set dir to textbox
        self.uifiledirText.setText(self.uifile)

        # save to config file
        self.setconfig('Dir', 'Input', self.uifile)

    def getOutputDirectory(self):
        self.outputdir = QtWidgets.QFileDialog.getExistingDirectory(self.mainwindow, 'Output Directory', './')
        # set dir to textbox
        self.outputdirText.setText(self.outputdir)

        # save to config file
        self.setconfig('Dir', 'Output', self.outputdir)

    def convert(self):
        # if output file name is not set
        if '.py' not in self.outputfile.split('/')[-1]:
            # converted file name is equivalent to input ui file
            self.outputfile += '/' + self.uifile.split('/')[-1].replace('.ui', '.py')

        print('outputdir : ', self.outputfile)
        cmd = 'pyuic5 -x %s -o %s' % (self.uifile, self.outputfile) #여기서 실제로 ui파일을 py로 바꿈

        try:
            result = os.popen(cmd).read()
        except:
            result = 'Error Catched'

        #이제 병합하는 로직을 짜야함!!!!!!!!!!!!!

        self.setLog('Converted %s' % self.uifile)

    def setconfig(self, section, key, value):

        config_reader = configparser.ConfigParser()
        config_writer = config_reader
        config_reader.read(self.bundle_dir + '/config/resource.config')

        # check existing sections
        if section not in config_reader.sections():
            config_writer.add_section(section)

        # Add key & values to section
        config_writer.set(section, key, value)

        # write to file
        with open(self.bundle_dir + '/config/resource.config', 'w') as configfile:
            config_writer.write(configfile)

    def getConfig(self, section, key):
        print('getConfig method : ', self.bundle_dir)
        config = configparser.ConfigParser()
        config.read(self.bundle_dir + '/config/resource.config')
        print(config.sections())
        return config.get(section, key)

    def initDir(self):
        self.uifile = self.getConfig('Dir', 'Input')
        self.outputfile = self.getConfig('Dir', 'Output')

        # dislplay
        self.uifiledirText.setText(self.uifile)
        self.outputdirText.setText(self.outputfile)

    def setLog(self, input):
        self.log.setText(input)


if __name__ == "__main__":
    import sys, os

    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
        print(bundle_dir)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.bundle_dir = bundle_dir
    ui.initDir()
    MainWindow.show()
    sys.exit(app.exec_())
