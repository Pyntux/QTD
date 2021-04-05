# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTD3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 440)
        MainWindow.setMinimumSize(QtCore.QSize(340, 440))
        MainWindow.setMaximumSize(QtCore.QSize(400, 520))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/shutdown.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 125))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 125))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.spinBox_hour = QtWidgets.QSpinBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_hour.setFont(font)
        self.spinBox_hour.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_hour.setMaximum(23)
        self.spinBox_hour.setObjectName("spinBox_hour")
        self.gridLayout_7.addWidget(self.spinBox_hour, 3, 0, 1, 1)
        self.spinBox_min = QtWidgets.QSpinBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_min.setFont(font)
        self.spinBox_min.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_min.setMaximum(59)
        self.spinBox_min.setObjectName("spinBox_min")
        self.gridLayout_7.addWidget(self.spinBox_min, 3, 1, 1, 1)
        self.spinBox_single = QtWidgets.QSpinBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_single.setFont(font)
        self.spinBox_single.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_single.setMinimum(1)
        self.spinBox_single.setMaximum(1000)
        self.spinBox_single.setProperty("value", 15)
        self.spinBox_single.setObjectName("spinBox_single")
        self.gridLayout_7.addWidget(self.spinBox_single, 2, 0, 1, 2)
        self.comboBox_make_in = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_make_in.setObjectName("comboBox_make_in")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/hourglass.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_make_in.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/timer.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_make_in.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/clock.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_make_in.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/now2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_make_in.addItem(icon4, "")
        self.gridLayout_7.addWidget(self.comboBox_make_in, 1, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_icon = QtWidgets.QLabel(self.frame_2)
        self.label_icon.setMinimumSize(QtCore.QSize(42, 42))
        self.label_icon.setMaximumSize(QtCore.QSize(42, 42))
        self.label_icon.setText("")
        self.label_icon.setPixmap(QtGui.QPixmap("icons/now2.ico"))
        self.label_icon.setScaledContents(True)
        self.label_icon.setObjectName("label_icon")
        self.gridLayout_7.addWidget(self.label_icon, 4, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lcd_clock = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_clock.setMinimumSize(QtCore.QSize(0, 60))
        self.lcd_clock.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcd_clock.setDigitCount(8)
        self.lcd_clock.setObjectName("lcd_clock")
        self.gridLayout_5.addWidget(self.lcd_clock, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.apply_button = QtWidgets.QPushButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/apply.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.apply_button.setIcon(icon5)
        self.apply_button.setIconSize(QtCore.QSize(20, 20))
        self.apply_button.setObjectName("apply_button")
        self.gridLayout_3.addWidget(self.apply_button, 0, 0, 1, 1)
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/reset.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_button.setIcon(icon6)
        self.reset_button.setIconSize(QtCore.QSize(20, 20))
        self.reset_button.setObjectName("reset_button")
        self.gridLayout_3.addWidget(self.reset_button, 0, 1, 1, 1)
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/exit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button.setIcon(icon7)
        self.exit_button.setIconSize(QtCore.QSize(20, 20))
        self.exit_button.setObjectName("exit_button")
        self.gridLayout_3.addWidget(self.exit_button, 1, 0, 1, 1)
        self.tray_button = QtWidgets.QPushButton(self.centralwidget)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/go_to_tray.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tray_button.setIcon(icon8)
        self.tray_button.setIconSize(QtCore.QSize(20, 20))
        self.tray_button.setObjectName("tray_button")
        self.gridLayout_3.addWidget(self.tray_button, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.choose_label = QtWidgets.QLabel(self.frame)
        self.choose_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.choose_label.setFont(font)
        self.choose_label.setObjectName("choose_label")
        self.gridLayout_6.addWidget(self.choose_label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.comboBox_action = QtWidgets.QComboBox(self.frame)
        self.comboBox_action.setObjectName("comboBox_action")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/shutdown.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_action.addItem(icon9, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/reboot.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_action.addItem(icon10, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/hibernate.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_action.addItem(icon11, "")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/sleep.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox_action.addItem(icon12, "")
        self.gridLayout_6.addWidget(self.comboBox_action, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_info = QtWidgets.QFrame(self.centralwidget)
        self.frame_info.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_info.setStyleSheet("color: rgb(0, 170, 255);\n"
                                      "background-color: rgb(255, 255, 255);")
        self.frame_info.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_info.setLineWidth(2)
        self.frame_info.setObjectName("frame_info")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_info)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_info = QtWidgets.QLabel(self.frame_info)
        self.label_info.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_info.setStyleSheet("color: rgb(40, 135, 220);")
        self.label_info.setFrameShape(QtWidgets.QFrame.Box)
        self.label_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_info.setLineWidth(0)
        self.label_info.setObjectName("label_info")
        self.gridLayout_9.addWidget(self.label_info, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label_info_icon = QtWidgets.QLabel(self.frame_info)
        self.label_info_icon.setMaximumSize(QtCore.QSize(25, 30))
        self.label_info_icon.setText("")
        self.label_info_icon.setPixmap(QtGui.QPixmap(
            "../Proba sa timer u jednoj funkciji/icons/info.ico"))
        self.label_info_icon.setScaledContents(True)
        self.label_info_icon.setObjectName("label_info_icon")
        self.gridLayout_9.addWidget(self.label_info_icon, 0, 0, 1, 1)
        self.label_info_icon.raise_()
        self.label_info.raise_()
        self.gridLayout_8.addWidget(self.frame_info, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_8, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QTD"))
        self.comboBox_make_in.setItemText(0, _translate("MainWindow", "Minutes from now"))
        self.comboBox_make_in.setItemText(1, _translate("MainWindow", "Hours from now"))
        self.comboBox_make_in.setItemText(2, _translate("MainWindow", "At selected time"))
        self.comboBox_make_in.setItemText(3, _translate("MainWindow", "Now"))
        self.label_2.setText(_translate("MainWindow", "Make action in:"))
        self.apply_button.setText(_translate("MainWindow", "Apply"))
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.tray_button.setText(_translate("MainWindow", "Tray"))
        self.choose_label.setText(_translate("MainWindow", "Choose your action:"))
        self.comboBox_action.setItemText(0, _translate("MainWindow", "Shutdown"))
        self.comboBox_action.setItemText(1, _translate("MainWindow", "Reboot"))
        self.comboBox_action.setItemText(2, _translate("MainWindow", "Hibernate"))
        self.comboBox_action.setItemText(3, _translate("MainWindow", "Sleep"))
        self.label_info.setText(_translate("MainWindow", "Welcome to QTD!"))