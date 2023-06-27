# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_in_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_LogInWindow(object):
    def setupUi(self, LogInWindow):
        if not LogInWindow.objectName():
            LogInWindow.setObjectName(u"LogInWindow")
        LogInWindow.resize(600, 400)
        LogInWindow.setStyleSheet(u"#LogInWindow {\n"
"	background: #f6f6e9;\n"
"}")
        self.centralwidget = QWidget(LogInWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo_obj = QLabel(self.centralwidget)
        self.logo_obj.setObjectName(u"logo_obj")
        self.logo_obj.setGeometry(QRect(10, 10, 120, 120))
        self.logo_obj.setPixmap(QPixmap(u":/logos/euler_database_manager.png"))
        self.logo_obj.setScaledContents(True)
        self.welcome_header = QLabel(self.centralwidget)
        self.welcome_header.setObjectName(u"welcome_header")
        self.welcome_header.setGeometry(QRect(150, 50, 300, 20))
        self.welcome_header.setAlignment(Qt.AlignCenter)
        self.hostname_label = QLabel(self.centralwidget)
        self.hostname_label.setObjectName(u"hostname_label")
        self.hostname_label.setGeometry(QRect(120, 130, 150, 30))
        self.database_name_label = QLabel(self.centralwidget)
        self.database_name_label.setObjectName(u"database_name_label")
        self.database_name_label.setGeometry(QRect(120, 170, 150, 30))
        self.username_label = QLabel(self.centralwidget)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(120, 210, 150, 30))
        self.password_label = QLabel(self.centralwidget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(120, 250, 150, 30))
        self.hostname_line_edit = QLineEdit(self.centralwidget)
        self.hostname_line_edit.setObjectName(u"hostname_line_edit")
        self.hostname_line_edit.setGeometry(QRect(310, 130, 150, 30))
        self.database_line_edit = QLineEdit(self.centralwidget)
        self.database_line_edit.setObjectName(u"database_line_edit")
        self.database_line_edit.setGeometry(QRect(310, 170, 150, 30))
        self.username_line_edit = QLineEdit(self.centralwidget)
        self.username_line_edit.setObjectName(u"username_line_edit")
        self.username_line_edit.setGeometry(QRect(310, 210, 150, 30))
        self.password_line_edit = QLineEdit(self.centralwidget)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setGeometry(QRect(310, 250, 150, 30))
        self.password_line_edit.setEchoMode(QLineEdit.Password)
        self.connection_status_label = QLabel(self.centralwidget)
        self.connection_status_label.setObjectName(u"connection_status_label")
        self.connection_status_label.setGeometry(QRect(110, 290, 380, 35))
        self.connection_status_label.setStyleSheet(u"#connection_status_label {\n"
"	color: red;\n"
"}")
        self.connection_status_label.setWordWrap(True)
        self.log_in_button = QPushButton(self.centralwidget)
        self.log_in_button.setObjectName(u"log_in_button")
        self.log_in_button.setGeometry(QRect(255, 330, 90, 35))
        self.log_in_button.setStyleSheet(u"#log_in_button {\n"
"	background: green;\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	border-radius: 4px;\n"
"}")
        LogInWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogInWindow)

        QMetaObject.connectSlotsByName(LogInWindow)
    # setupUi

    def retranslateUi(self, LogInWindow):
        LogInWindow.setWindowTitle(QCoreApplication.translate("LogInWindow", u"Euler Database Manager", None))
        self.logo_obj.setText("")
        self.welcome_header.setText(QCoreApplication.translate("LogInWindow", u"Welcome To The Euler Database Manager", None))
        self.hostname_label.setText(QCoreApplication.translate("LogInWindow", u"Host Name:", None))
        self.database_name_label.setText(QCoreApplication.translate("LogInWindow", u"Database Name:", None))
        self.username_label.setText(QCoreApplication.translate("LogInWindow", u"Username:", None))
        self.password_label.setText(QCoreApplication.translate("LogInWindow", u"Password:", None))
        self.connection_status_label.setText("")
        self.log_in_button.setText(QCoreApplication.translate("LogInWindow", u"Log in", None))
    # retranslateUi

