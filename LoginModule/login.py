# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 440)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 440))
        MainWindow.setMaximumSize(QtCore.QSize(600, 440))
        MainWindow.setStyleSheet("")
        self.bgApp = QtWidgets.QWidget(MainWindow)
        self.bgApp.setStyleSheet("font: 10pt \"HarmonyOS Sans SC\";")
        self.bgApp.setObjectName("bgApp")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.bgApp)
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.container = QtWidgets.QFrame(self.bgApp)
        self.container.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.container)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.contentTopBg = QtWidgets.QFrame(self.container)
        self.contentTopBg.setMinimumSize(QtCore.QSize(0, 50))
        self.contentTopBg.setMaximumSize(QtCore.QSize(16777215, 50))
        self.contentTopBg.setStyleSheet("background-color: rgb(33, 37, 43);\n"
"")
        self.contentTopBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentTopBg.setObjectName("contentTopBg")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftBox = QtWidgets.QFrame(self.contentTopBg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy)
        self.leftBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.leftBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftBox.setObjectName("leftBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.topLogo = QtWidgets.QFrame(self.leftBox)
        self.topLogo.setMinimumSize(QtCore.QSize(42, 42))
        self.topLogo.setMaximumSize(QtCore.QSize(60, 42))
        self.topLogo.setAutoFillBackground(False)
        self.topLogo.setStyleSheet("#topLogo {\n"
"    background-color: rgb(33, 37, 43);\n"
"    background-image: url(:/images/images/images/cloud_blue.png);\n"
"    background-position: centered;\n"
"    background-repeat: no-repeat;\n"
"}")
        self.topLogo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.topLogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topLogo.setObjectName("topLogo")
        self.horizontalLayout_3.addWidget(self.topLogo)
        self.titleRightInfo = QtWidgets.QLabel(self.leftBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy)
        self.titleRightInfo.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("HarmonyOS Sans SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setStyleSheet("#titleRightInfo { padding-left: 10px; }")
        self.titleRightInfo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.titleRightInfo.setObjectName("titleRightInfo")
        self.horizontalLayout_3.addWidget(self.titleRightInfo)
        self.horizontalLayout.addWidget(self.leftBox)
        self.rightButtons = QtWidgets.QFrame(self.contentTopBg)
        self.rightButtons.setMinimumSize(QtCore.QSize(0, 28))
        self.rightButtons.setStyleSheet("#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: #bd93f9; border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: #ff79c6; border-style: solid; border-radius: 4px; }")
        self.rightButtons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightButtons.setObjectName("rightButtons")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minimizeAppBtn = QtWidgets.QPushButton(self.rightButtons)
        self.minimizeAppBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QtCore.QSize(28, 28))
        self.minimizeAppBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimizeAppBtn.setToolTip("")
        self.minimizeAppBtn.setStyleSheet("#minimizeAppBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#minimizeAppBtn:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#minimizeAppBtn:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        self.minimizeAppBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/icons/icon_minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QtCore.QSize(20, 20))
        self.minimizeAppBtn.setObjectName("minimizeAppBtn")
        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)
        self.closeAppBtn = QtWidgets.QPushButton(self.rightButtons)
        self.closeAppBtn.setMinimumSize(QtCore.QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QtCore.QSize(28, 28))
        self.closeAppBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeAppBtn.setToolTip("")
        self.closeAppBtn.setStyleSheet("#closeAppBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#closeAppBtn:hover { background-color: rgb(253, 84, 63); border-style: solid; border-radius: 4px; }\n"
"#closeAppBtn:pressed { background-color: rgb(196, 58, 43); border-style: solid; border-radius: 4px; }")
        self.closeAppBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/icons/icon_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeAppBtn.setIcon(icon1)
        self.closeAppBtn.setIconSize(QtCore.QSize(20, 20))
        self.closeAppBtn.setObjectName("closeAppBtn")
        self.horizontalLayout_2.addWidget(self.closeAppBtn)
        self.horizontalLayout.addWidget(self.rightButtons, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_5.addWidget(self.contentTopBg)
        self.pagesContainer = QtWidgets.QFrame(self.container)
        self.pagesContainer.setStyleSheet("/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(33, 37, 43);\n"
"    color: rgb(255,255,255);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding-left: 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(111, 168, 220);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"")
        self.pagesContainer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pagesContainer.setObjectName("pagesContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pagesContainer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.pagesContainer)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setObjectName("loginPage")
        self.user = QtWidgets.QLabel(self.loginPage)
        self.user.setGeometry(QtCore.QRect(261, 20, 60, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user.sizePolicy().hasHeightForWidth())
        self.user.setSizePolicy(sizePolicy)
        self.user.setText("")
        self.user.setPixmap(QtGui.QPixmap(":/images/images/images/user.png"))
        self.user.setScaledContents(True)
        self.user.setObjectName("user")
        self.info = QtWidgets.QFrame(self.loginPage)
        self.info.setGeometry(QtCore.QRect(141, 120, 291, 121))
        self.info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info.setObjectName("info")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.info)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.login_layout = QtWidgets.QVBoxLayout()
        self.login_layout.setSpacing(15)
        self.login_layout.setObjectName("login_layout")
        self.horizontalLayout_4.addLayout(self.login_layout)
        self.login_button = QtWidgets.QPushButton(self.loginPage)
        self.login_button.setGeometry(QtCore.QRect(241, 280, 100, 35))
        font = QtGui.QFont()
        font.setFamily("HarmonyOS Sans SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("/*Button */\n"
"QPushButton {\n"
"    border: 2px solid rgb(109, 158, 235);\n"
"    border-radius: 5px;    \n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(109, 158, 235);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(109, 158, 235);\n"
"    color: rgb(255,255,255);\n"
"    border: 2px solid rgb(129, 178, 255);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(89, 138, 215);\n"
"    color: rgb(255,255,255);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.login_button.setFlat(False)
        self.login_button.setObjectName("login_button")
        self.register_lable = QtWidgets.QLabel(self.loginPage)
        self.register_lable.setGeometry(QtCore.QRect(10, 320, 55, 18))
        font = QtGui.QFont()
        font.setFamily("HarmonyOS Sans SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.register_lable.setFont(font)
        self.register_lable.setStyleSheet(" color: rgb(113, 126, 149);")
        self.register_lable.setObjectName("register_lable")
        self.stackedWidget.addWidget(self.loginPage)
        self.registerPage = QtWidgets.QWidget()
        self.registerPage.setObjectName("registerPage")
        self.register_info = QtWidgets.QFrame(self.registerPage)
        self.register_info.setGeometry(QtCore.QRect(141, 55, 300, 205))
        self.register_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.register_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.register_info.setObjectName("register_info")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.register_info)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.register_layout = QtWidgets.QVBoxLayout()
        self.register_layout.setSpacing(15)
        self.register_layout.setObjectName("register_layout")
        self.horizontalLayout_9.addLayout(self.register_layout)
        self.register_button = QtWidgets.QPushButton(self.registerPage)
        self.register_button.setGeometry(QtCore.QRect(241, 280, 100, 35))
        font = QtGui.QFont()
        font.setFamily("HarmonyOS Sans SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.register_button.setFont(font)
        self.register_button.setStyleSheet("/*Button */\n"
"QPushButton {\n"
"    border: 2px solid rgb(109, 158, 235);\n"
"    border-radius: 5px;    \n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(109, 158, 235);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(109, 158, 235);\n"
"    color: rgb(255,255,255);\n"
"    border: 2px solid rgb(129, 178, 255);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(89, 138, 215);\n"
"    color: rgb(255,255,255);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.register_button.setFlat(False)
        self.register_button.setObjectName("register_button")
        self.login_lable = QtWidgets.QLabel(self.registerPage)
        self.login_lable.setGeometry(QtCore.QRect(10, 320, 55, 18))
        font = QtGui.QFont()
        font.setFamily("HarmonyOS Sans SC")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.login_lable.setFont(font)
        self.login_lable.setStyleSheet(" color: rgb(113, 126, 149);")
        self.login_lable.setObjectName("login_lable")
        self.label = QtWidgets.QLabel(self.registerPage)
        self.label.setGeometry(QtCore.QRect(141, 25, 55, 18))
        self.label.setStyleSheet(" color: rgb(113, 126, 149);")
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.registerPage)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout_5.addWidget(self.pagesContainer)
        self.bottomBar = QtWidgets.QFrame(self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomBar.sizePolicy().hasHeightForWidth())
        self.bottomBar.setSizePolicy(sizePolicy)
        self.bottomBar.setMinimumSize(QtCore.QSize(0, 22))
        self.bottomBar.setMaximumSize(QtCore.QSize(16777215, 22))
        self.bottomBar.setStyleSheet("background-color: rgb(44, 49, 58);")
        self.bottomBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomBar.setObjectName("bottomBar")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.creditsLabel = QtWidgets.QLabel(self.bottomBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.creditsLabel.sizePolicy().hasHeightForWidth())
        self.creditsLabel.setSizePolicy(sizePolicy)
        self.creditsLabel.setMinimumSize(QtCore.QSize(0, 16))
        self.creditsLabel.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setFamily("HarmonyOS Sans SC")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.creditsLabel.setFont(font)
        self.creditsLabel.setStyleSheet("QLabel {\n"
"    font: 8pt \"HarmonyOS Sans SC\";\n"
"    color: rgb(113, 126, 149); \n"
"    padding-left: 10px; \n"
"    padding-right: 10px;\n"
"    padding-bottom: 2px;\n"
" }")
        self.creditsLabel.setLineWidth(1)
        self.creditsLabel.setTextFormat(QtCore.Qt.AutoText)
        self.creditsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.creditsLabel.setIndent(0)
        self.creditsLabel.setObjectName("creditsLabel")
        self.horizontalLayout_5.addWidget(self.creditsLabel)
        self.version = QtWidgets.QLabel(self.bottomBar)
        self.version.setMaximumSize(QtCore.QSize(16777215, 16))
        self.version.setStyleSheet("QLabel {\n"
"     font-size: 11px; \n"
"    color: rgb(113, 126, 149); \n"
"    padding-left: 10px; \n"
"    padding-right: 10px;\n"
"    padding-bottom: 2px;\n"
" }")
        self.version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version.setIndent(0)
        self.version.setObjectName("version")
        self.horizontalLayout_5.addWidget(self.version)
        self.verticalLayout_5.addWidget(self.bottomBar)
        self.horizontalLayout_6.addWidget(self.container)
        MainWindow.setCentralWidget(self.bgApp)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleRightInfo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">OCR&amp;RPA自动化执行软件</span></p></body></html>"))
        self.login_button.setText(_translate("MainWindow", "登 录"))
        self.register_lable.setText(_translate("MainWindow", "注册账号"))
        self.register_button.setText(_translate("MainWindow", "注 册"))
        self.login_lable.setText(_translate("MainWindow", "登录账号"))
        self.label.setText(_translate("MainWindow", "注册账号"))
        self.creditsLabel.setText(_translate("MainWindow", "By：HUST-ISE"))
        self.version.setText(_translate("MainWindow", "v0.0.1"))
import lib.resources_rc