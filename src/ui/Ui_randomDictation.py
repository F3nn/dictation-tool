# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'randomDictation_beta.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(900, 250))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 1280))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_4.addWidget(self.plainTextEdit)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_4.addWidget(self.listWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setMinimumSize(QtCore.QSize(0, 22))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setMinimumSize(QtCore.QSize(0, 22))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setMinimumSize(QtCore.QSize(0, 22))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(82, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(10)
        self.spinBox.setProperty("value", 5)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 34))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 34))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGithub = QtWidgets.QAction(MainWindow)
        self.actionGithub.setObjectName("actionGithub")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setEnabled(False)
        self.actionVersion.setObjectName("actionVersion")
        self.actionThanks = QtWidgets.QAction(MainWindow)
        self.actionThanks.setObjectName("actionThanks")
        self.actionLog = QtWidgets.QAction(MainWindow)
        self.actionLog.setObjectName("actionLog")
        self.actionFileOpen = QtWidgets.QAction(MainWindow)
        self.actionFileOpen.setObjectName("actionFileOpen")
        self.actionFileSave = QtWidgets.QAction(MainWindow)
        self.actionFileSave.setObjectName("actionFileSave")
        self.actionFileSavedAs = QtWidgets.QAction(MainWindow)
        self.actionFileSavedAs.setObjectName("actionFileSavedAs")
        self.actionExpert = QtWidgets.QAction(MainWindow)
        self.actionExpert.setVisible(False)
        self.actionExpert.setObjectName("actionExpert")
        self.actionExpertAll = QtWidgets.QAction(MainWindow)
        self.actionExpertAll.setVisible(False)
        self.actionExpertAll.setObjectName("actionExpertAll")
        self.menu.addAction(self.actionGithub)
        self.menu.addSeparator()
        self.menu.addAction(self.actionThanks)
        self.menu.addAction(self.actionLog)
        self.menu.addAction(self.actionVersion)
        self.menu_2.addAction(self.actionFileOpen)
        self.menu_2.addAction(self.actionFileSave)
        self.menu_2.addAction(self.actionFileSavedAs)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionExpert)
        self.menu_2.addAction(self.actionExpertAll)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DictationNow! v1.1.0a"))
        self.radioButton.setText(_translate("MainWindow", "英音"))
        self.radioButton_2.setText(_translate("MainWindow", "美音"))
        self.checkBox.setText(_translate("MainWindow", "乱序"))
        self.label.setText(_translate("MainWindow", "间隔时间"))
        self.pushButton.setText(_translate("MainWindow", "开始听写"))
        self.pushButton_2.setText(_translate("MainWindow", "清除文本"))
        self.menu.setTitle(_translate("MainWindow", "关于"))
        self.menu_2.setTitle(_translate("MainWindow", "文件"))
        self.actionGithub.setText(_translate("MainWindow", "Github"))
        self.actionVersion.setText(_translate("MainWindow", "版本: 1.1.0a"))
        self.actionThanks.setText(_translate("MainWindow", "鸣谢"))
        self.actionLog.setText(_translate("MainWindow", "更新日志"))
        self.actionFileOpen.setText(_translate("MainWindow", "打开"))
        self.actionFileSave.setText(_translate("MainWindow", "保存"))
        self.actionFileSavedAs.setText(_translate("MainWindow", "另存为"))
        self.actionExpert.setText(_translate("MainWindow", "导出听力音频 (beta)"))
        self.actionExpertAll.setText(_translate("MainWindow", "导出并整合 (beta)"))

import ui.icon_rc
