# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\faulstichf\git\RfemPythonWsClient\Examples\FrameGenerator_2D\MyApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 880)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonCalculate = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCalculate.setGeometry(QtCore.QRect(1130, 810, 75, 23))
        self.buttonCalculate.setObjectName("buttonCalculate")
        self.buttonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCancel.setGeometry(QtCore.QRect(1210, 810, 75, 23))
        self.buttonCancel.setObjectName("buttonCancel")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 791, 731))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Structure = QtWidgets.QWidget()
        self.Structure.setObjectName("Structure")
        self.groupBox = QtWidgets.QGroupBox(self.Structure)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 391, 91))
        self.groupBox.setObjectName("groupBox")
        self.checkBox_loads = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_loads.setGeometry(QtCore.QRect(10, 30, 121, 17))
        self.checkBox_loads.setObjectName("checkBox_loads")
        self.checkBox_steel_design = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_steel_design.setGeometry(QtCore.QRect(10, 50, 121, 17))
        self.checkBox_steel_design.setObjectName("checkBox_steel_design")
        self.groupBox_2 = QtWidgets.QGroupBox(self.Structure)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 391, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_l_1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_l_1.setGeometry(QtCore.QRect(40, 30, 113, 20))
        self.lineEdit_l_1.setObjectName("lineEdit_l_1")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 31, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(160, 30, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(160, 60, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 31, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_l_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_l_2.setGeometry(QtCore.QRect(40, 60, 113, 20))
        self.lineEdit_l_2.setObjectName("lineEdit_l_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(160, 90, 31, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 31, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_l_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_l_3.setGeometry(QtCore.QRect(40, 90, 113, 20))
        self.lineEdit_l_3.setObjectName("lineEdit_l_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(360, 90, 31, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(210, 60, 31, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(210, 90, 31, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(210, 30, 31, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(360, 60, 31, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(360, 30, 31, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_h_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_h_3.setGeometry(QtCore.QRect(240, 90, 113, 20))
        self.lineEdit_h_3.setObjectName("lineEdit_h_3")
        self.lineEdit_h_1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_h_1.setGeometry(QtCore.QRect(240, 30, 113, 20))
        self.lineEdit_h_1.setObjectName("lineEdit_h_1")
        self.lineEdit_h_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_h_2.setGeometry(QtCore.QRect(240, 60, 113, 20))
        self.lineEdit_h_2.setObjectName("lineEdit_h_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.Structure)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 470, 391, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox_CS_s = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_CS_s.setGeometry(QtCore.QRect(210, 120, 141, 22))
        self.comboBox_CS_s.setObjectName("comboBox_CS_s")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(10, 60, 101, 20))
        self.label_17.setObjectName("label_17")
        self.comboBox_CS_i_c = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_CS_i_c.setGeometry(QtCore.QRect(210, 60, 141, 22))
        self.comboBox_CS_i_c.setObjectName("comboBox_CS_i_c")
        self.comboBox_CS_r = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_CS_r.setGeometry(QtCore.QRect(210, 90, 141, 22))
        self.comboBox_CS_r.setObjectName("comboBox_CS_r")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(10, 30, 101, 20))
        self.label_18.setObjectName("label_18")
        self.comboBox_CS_o_c = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_CS_o_c.setGeometry(QtCore.QRect(210, 30, 141, 22))
        self.comboBox_CS_o_c.setObjectName("comboBox_CS_o_c")
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setGeometry(QtCore.QRect(10, 120, 101, 20))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(10, 90, 101, 20))
        self.label_20.setObjectName("label_20")
        self.groupBox_4 = QtWidgets.QGroupBox(self.Structure)
        self.groupBox_4.setGeometry(QtCore.QRect(420, 470, 351, 171))
        self.groupBox_4.setObjectName("groupBox_4")
        self.comboBox_support_4 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_support_4.setGeometry(QtCore.QRect(170, 120, 141, 22))
        self.comboBox_support_4.setObjectName("comboBox_support_4")
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setGeometry(QtCore.QRect(10, 120, 101, 20))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(10, 90, 101, 20))
        self.label_22.setObjectName("label_22")
        self.comboBox_support_1 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_support_1.setGeometry(QtCore.QRect(170, 30, 141, 22))
        self.comboBox_support_1.setObjectName("comboBox_support_1")
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(10, 60, 101, 20))
        self.label_23.setObjectName("label_23")
        self.comboBox_support_3 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_support_3.setGeometry(QtCore.QRect(170, 90, 141, 22))
        self.comboBox_support_3.setObjectName("comboBox_support_3")
        self.comboBox_support_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_support_2.setGeometry(QtCore.QRect(170, 60, 141, 22))
        self.comboBox_support_2.setObjectName("comboBox_support_2")
        self.label_24 = QtWidgets.QLabel(self.groupBox_4)
        self.label_24.setGeometry(QtCore.QRect(10, 30, 101, 20))
        self.label_24.setObjectName("label_24")
        self.groupBox_5 = QtWidgets.QGroupBox(self.Structure)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 280, 391, 181))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setGeometry(QtCore.QRect(10, 40, 101, 20))
        self.label_13.setObjectName("label_13")
        self.comboBox_Material_o_c = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_Material_o_c.setGeometry(QtCore.QRect(210, 40, 141, 22))
        self.comboBox_Material_o_c.setCurrentText("")
        self.comboBox_Material_o_c.setObjectName("comboBox_Material_o_c")
        self.comboBox_Material_i_c = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_Material_i_c.setGeometry(QtCore.QRect(210, 70, 141, 22))
        self.comboBox_Material_i_c.setObjectName("comboBox_Material_i_c")
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setGeometry(QtCore.QRect(10, 70, 101, 20))
        self.label_14.setObjectName("label_14")
        self.comboBox_Material_r = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_Material_r.setGeometry(QtCore.QRect(210, 100, 141, 22))
        self.comboBox_Material_r.setObjectName("comboBox_Material_r")
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(10, 100, 101, 20))
        self.label_15.setObjectName("label_15")
        self.comboBox_Material_s = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_Material_s.setGeometry(QtCore.QRect(210, 130, 141, 22))
        self.comboBox_Material_s.setObjectName("comboBox_Material_s")
        self.label_16 = QtWidgets.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(10, 130, 101, 20))
        self.label_16.setObjectName("label_16")
        self.groupBox_6 = QtWidgets.QGroupBox(self.Structure)
        self.groupBox_6.setGeometry(QtCore.QRect(420, 29, 351, 431))
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.tabWidget.addTab(self.Structure, "")
        self.Loads = QtWidgets.QWidget()
        self.Loads.setObjectName("Loads")
        self.groupBox_7 = QtWidgets.QGroupBox(self.Loads)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 30, 761, 71))
        self.groupBox_7.setObjectName("groupBox_7")
        self.lineEdit_g_r = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_g_r.setGeometry(QtCore.QRect(40, 30, 113, 20))
        self.lineEdit_g_r.setObjectName("lineEdit_g_r")
        self.label_25 = QtWidgets.QLabel(self.groupBox_7)
        self.label_25.setGeometry(QtCore.QRect(10, 30, 31, 21))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_7)
        self.label_26.setGeometry(QtCore.QRect(160, 30, 31, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_7)
        self.label_27.setGeometry(QtCore.QRect(380, 30, 31, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_7)
        self.label_28.setGeometry(QtCore.QRect(230, 30, 31, 21))
        self.label_28.setObjectName("label_28")
        self.lineEdit_g_s = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_g_s.setGeometry(QtCore.QRect(260, 30, 113, 20))
        self.lineEdit_g_s.setObjectName("lineEdit_g_s")
        self.label_29 = QtWidgets.QLabel(self.groupBox_7)
        self.label_29.setGeometry(QtCore.QRect(600, 30, 31, 16))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.groupBox_7)
        self.label_30.setGeometry(QtCore.QRect(450, 30, 31, 21))
        self.label_30.setObjectName("label_30")
        self.lineEdit_g_w = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_g_w.setGeometry(QtCore.QRect(480, 30, 113, 20))
        self.lineEdit_g_w.setObjectName("lineEdit_g_w")
        self.groupBox_9 = QtWidgets.QGroupBox(self.Loads)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 110, 761, 71))
        self.groupBox_9.setObjectName("groupBox_9")
        self.lineEdit_s_r = QtWidgets.QLineEdit(self.groupBox_9)
        self.lineEdit_s_r.setGeometry(QtCore.QRect(40, 30, 113, 20))
        self.lineEdit_s_r.setObjectName("lineEdit_s_r")
        self.label_37 = QtWidgets.QLabel(self.groupBox_9)
        self.label_37.setGeometry(QtCore.QRect(10, 30, 31, 21))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.groupBox_9)
        self.label_38.setGeometry(QtCore.QRect(160, 30, 31, 16))
        self.label_38.setObjectName("label_38")
        self.groupBox_11 = QtWidgets.QGroupBox(self.Loads)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 190, 761, 71))
        self.groupBox_11.setObjectName("groupBox_11")
        self.lineEdit_p_s = QtWidgets.QLineEdit(self.groupBox_11)
        self.lineEdit_p_s.setGeometry(QtCore.QRect(40, 30, 113, 20))
        self.lineEdit_p_s.setObjectName("lineEdit_p_s")
        self.label_39 = QtWidgets.QLabel(self.groupBox_11)
        self.label_39.setGeometry(QtCore.QRect(10, 30, 31, 21))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.groupBox_11)
        self.label_40.setGeometry(QtCore.QRect(160, 30, 31, 16))
        self.label_40.setObjectName("label_40")
        self.tabWidget.addTab(self.Loads, "")
        self.SteelDesign = QtWidgets.QWidget()
        self.SteelDesign.setObjectName("SteelDesign")
        self.tabWidget.addTab(self.SteelDesign, "")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(820, 30, 471, 711))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Frame Generator"))
        self.buttonCalculate.setText(_translate("MainWindow", "Calculate"))
        self.buttonCancel.setText(_translate("MainWindow", "Cancel"))
        self.groupBox.setTitle(_translate("MainWindow", "Options"))
        self.checkBox_loads.setText(_translate("MainWindow", "Loads"))
        self.checkBox_steel_design.setText(_translate("MainWindow", "Steel Design"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Dimensions"))
        self.lineEdit_l_1.setText(_translate("MainWindow", "6"))
        self.label.setText(_translate("MainWindow", "l<sub>1</sub>"))
        self.label_2.setText(_translate("MainWindow", "m"))
        self.label_3.setText(_translate("MainWindow", "m"))
        self.label_4.setText(_translate("MainWindow", "l<sub>2</sub>"))
        self.lineEdit_l_2.setText(_translate("MainWindow", "6"))
        self.label_5.setText(_translate("MainWindow", "m"))
        self.label_6.setText(_translate("MainWindow", "l<sub>3</sub>"))
        self.lineEdit_l_3.setText(_translate("MainWindow", "6"))
        self.label_7.setText(_translate("MainWindow", "m"))
        self.label_8.setText(_translate("MainWindow", "h<sub>2</sub>"))
        self.label_9.setText(_translate("MainWindow", "h<sub>3</sub>"))
        self.label_10.setText(_translate("MainWindow", "h<sub>1</sub>"))
        self.label_11.setText(_translate("MainWindow", "m"))
        self.label_12.setText(_translate("MainWindow", "m"))
        self.lineEdit_h_3.setText(_translate("MainWindow", "1"))
        self.lineEdit_h_1.setText(_translate("MainWindow", "3"))
        self.lineEdit_h_2.setText(_translate("MainWindow", "3"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Cross Sections"))
        self.label_17.setText(_translate("MainWindow", "Inside Columns"))
        self.label_18.setText(_translate("MainWindow", "Outside Columns"))
        self.label_19.setText(_translate("MainWindow", "Slab"))
        self.label_20.setText(_translate("MainWindow", "Roof"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Supports"))
        self.label_21.setText(_translate("MainWindow", "Support 4"))
        self.label_22.setText(_translate("MainWindow", "Support 3"))
        self.label_23.setText(_translate("MainWindow", "Support 2"))
        self.label_24.setText(_translate("MainWindow", "Support 1"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Material"))
        self.label_13.setText(_translate("MainWindow", "Outside Columns"))
        self.label_14.setText(_translate("MainWindow", "Inside Columns"))
        self.label_15.setText(_translate("MainWindow", "Roof"))
        self.label_16.setText(_translate("MainWindow", "Slab"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Structure), _translate("MainWindow", "Structure"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Self-weight"))
        self.lineEdit_g_r.setText(_translate("MainWindow", "6"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p>g<span style=\" vertical-align:sub;\">r</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "kN/m"))
        self.label_27.setText(_translate("MainWindow", "kN/m"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p>g<span style=\" vertical-align:sub;\">s</span></p></body></html>"))
        self.lineEdit_g_s.setText(_translate("MainWindow", "6"))
        self.label_29.setText(_translate("MainWindow", "kN/m"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p>g<span style=\" vertical-align:sub;\">w</span></p></body></html>"))
        self.lineEdit_g_w.setText(_translate("MainWindow", "6"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Snow"))
        self.lineEdit_s_r.setText(_translate("MainWindow", "6"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p>s<span style=\" vertical-align:sub;\">r</span></p></body></html>"))
        self.label_38.setText(_translate("MainWindow", "kN/m"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Load on Slab "))
        self.lineEdit_p_s.setText(_translate("MainWindow", "6"))
        self.label_39.setText(_translate("MainWindow", "<html><head/><body><p>p<span style=\" vertical-align:sub;\">s</span></p></body></html>"))
        self.label_40.setText(_translate("MainWindow", "kN/m"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Loads), _translate("MainWindow", "Loads"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SteelDesign), _translate("MainWindow", "Steel Design"))
