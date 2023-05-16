# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'siralamaGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import random
from PyQt5 import QtCore, QtGui, QtWidgets
import sortAlgorithms


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        #Global variables
        self._prefferedSort = "No Selection"
        self._arr = list()
        self._algorithms = sortAlgorithms.Algorithms()
        self._sizeOfList = 10
        self._speed=0
        #end

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 453)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.sizeSlider = QtWidgets.QSlider(self.centralwidget)
        self.sizeSlider.setGeometry(QtCore.QRect(20, 50, 160, 22))
        self.sizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.sizeSlider.setObjectName("sizeSlider")
        self.sizeSlider.valueChanged.connect(self.sizeSlideChange)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 100, 13))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.speedSlider = QtWidgets.QSlider(self.centralwidget)
        self.speedSlider.setGeometry(QtCore.QRect(20, 110, 160, 22))
        self.speedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider.setObjectName("speedSlider")
        self.speedSlider.valueChanged.connect(self.speedSlideChange)
        

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 100, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.radioButtonBubble = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonBubble.setGeometry(QtCore.QRect(20, 200, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.radioButtonBubble.setFont(font)
        self.radioButtonBubble.setObjectName("radioButtonBubble")
        self.radioButtonBubble.toggled.connect(lambda: self.radioButtonClicked(self.radioButtonBubble))

        self.radioButtonInsertion = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonInsertion.setGeometry(QtCore.QRect(20, 230, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.radioButtonInsertion.setFont(font)
        self.radioButtonInsertion.setObjectName("radioButtonInsertion")
        self.radioButtonInsertion.toggled.connect(lambda: self.radioButtonClicked(self.radioButtonInsertion))


        self.radioButtonMerge = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonMerge.setGeometry(QtCore.QRect(20, 290, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.radioButtonMerge.setFont(font)
        self.radioButtonMerge.setObjectName("radioButtonMerge")
        self.radioButtonMerge.toggled.connect(lambda: self.radioButtonClicked(self.radioButtonMerge))


        self.radioButtonSelection = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonSelection.setGeometry(QtCore.QRect(20, 260, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.radioButtonSelection.setFont(font)
        self.radioButtonSelection.setObjectName("radioButtonSelection")
        self.radioButtonSelection.toggled.connect(lambda: self.radioButtonClicked(self.radioButtonSelection))

        #Quick Button
        self.radioButtonQuick = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonQuick.setGeometry(QtCore.QRect(20, 350, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.radioButtonQuick.setFont(font)
        self.radioButtonQuick.setObjectName("radioButtonQuick")
        self.radioButtonQuick.toggled.connect(lambda: self.radioButtonClicked(self.radioButtonQuick))

        #Heap Button
        self.radioButtonHeap = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonHeap.setGeometry(QtCore.QRect(20, 320, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.radioButtonHeap.setFont(font)
        self.radioButtonHeap.setObjectName("radioButtonHeap")
        self.radioButtonHeap.toggled.connect(lambda: self.radioButtonClicked(self.radioButtonHeap))

        #Sort Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 390, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sortButtonClickEvent)
        #end sort button

        #visualize chart
        self.chartwidget = QtWidgets.QWidget(self.centralwidget)
        self.chartwidget.setGeometry(QtCore.QRect(250, 20, 521, 401))
        self.chartwidget.setObjectName("chartwidget")
        #end visalize chart

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Size:"))
        self.label_2.setText(_translate("MainWindow", "Speed:"))
        self.label_3.setText(_translate("MainWindow", "Sorting:"))
        self.radioButtonBubble.setText(_translate("MainWindow", "Bubble Sort"))
        self.radioButtonInsertion.setText(_translate("MainWindow", "Insertion Sort"))
        self.radioButtonMerge.setText(_translate("MainWindow", "Merge Sort"))
        self.radioButtonSelection.setText(_translate("MainWindow", "Selection Sort"))
        self.radioButtonQuick.setText(_translate("MainWindow", "Quick Sort"))
        self.radioButtonHeap.setText(_translate("MainWindow", "Heap Sort"))
        self.pushButton.setText(_translate("MainWindow", "Sort"))
    
    
    def sortButtonClickEvent(self):
        if self._prefferedSort == "Bubble Sort":
            print("Your Choose: "+ self._prefferedSort)
            result = self._algorithms.bubble_sort(self._arr)
            print(result)

        elif self._prefferedSort == "Insertion Sort":
            print("Your Choose: "+ self._prefferedSort)
            result = self._algorithms.insertion_sort(self._arr)
            print(result)
        elif self._prefferedSort == "Merge Sort":
            print("Your Choose: "+ self._prefferedSort)
            result = self._algorithms.merge_sort(self._arr)
            print(result)
        elif self._prefferedSort == "Selection Sort":
            print("Your Choose: "+ self._prefferedSort)
            result = self._algorithms.selection_sort(self._arr)
            print(result)
        elif self._prefferedSort == "Heap Sort":
            print("Your Choose: "+ self._prefferedSort)
            result = self._algorithms.bubble_sort(self._arr)
            print(result)
        elif self._prefferedSort == "Quick Sort":
            print("Your Choose: "+ self._prefferedSort)
            result = self._algorithms.quick_sort(self._arr,0, len(self._arr) - 1)
            print(result)
        else:
            print("seçim yapılmadı")
            self.createListOfRandomNumber(self._sizeOfList)
            print(self._arr)
    
    def radioButtonClicked(self,b):
        if b.isChecked():
            self._prefferedSort = b.text()

    def createListOfRandomNumber(self,size):
        Random_ListOfIntegers = random.sample(range(0, 1000), size)
        self._arr = Random_ListOfIntegers

    def sizeSlideChange(self,value):
        self._sizeOfList = value
        self.label.setText("Size: "+str(self._sizeOfList))
    
    def speedSlideChange(self,value):
        self._speed = value
        self.label_2.setText("Speed: "+str(self._speed))

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
