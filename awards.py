# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'awards.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Awards(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 511, 541))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["ФИО", "Группа", "Премия"])
        self.tableWidget.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignHCenter)
        self.tableWidget.horizontalHeaderItem(1).setTextAlignment(QtCore.Qt.AlignHCenter)
        self.tableWidget.horizontalHeaderItem(2).setTextAlignment(QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 531, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuImport = QtWidgets.QMenu(self.menuBar)
        self.menuImport.setObjectName("menuImport")
        self.menuExport = QtWidgets.QMenu(self.menuImport)
        self.menuExport.setObjectName("menuExport")
        MainWindow.setMenuBar(self.menuBar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionas_xlcs = QtWidgets.QAction(MainWindow)
        self.actionas_xlcs.setObjectName("actionas_xlcs")
        self.actionto_Google_Sheet = QtWidgets.QAction(MainWindow)
        self.actionto_Google_Sheet.setObjectName("actionto_Google_Sheet")
        self.menuExport.addAction(self.actionas_xlcs)
        self.menuExport.addAction(self.actionto_Google_Sheet)
        self.menuImport.addAction(self.actionImport)
        self.menuImport.addAction(self.menuExport.menuAction())
        self.menuBar.addAction(self.menuImport.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuImport.setTitle(_translate("MainWindow", "Menu"))
        self.menuExport.setTitle(_translate("MainWindow", "Save as..."))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionas_xlcs.setText(_translate("MainWindow", "*.xlcs"))
        self.actionto_Google_Sheet.setText(_translate("MainWindow", "as Google Sheet"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
