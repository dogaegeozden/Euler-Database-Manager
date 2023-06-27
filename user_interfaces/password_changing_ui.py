# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'password_changing.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ChangePasswordDialog(object):
    def setupUi(self, ChangePasswordDialog):
        if not ChangePasswordDialog.objectName():
            ChangePasswordDialog.setObjectName(u"ChangePasswordDialog")
        ChangePasswordDialog.resize(400, 300)
        self.password_changing_line_edit = QLineEdit(ChangePasswordDialog)
        self.password_changing_line_edit.setObjectName(u"password_changing_line_edit")
        self.password_changing_line_edit.setGeometry(QRect(100, 100, 200, 25))
        self.submit_button = QPushButton(ChangePasswordDialog)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(155, 210, 90, 25))
        self.header1 = QLabel(ChangePasswordDialog)
        self.header1.setObjectName(u"header1")
        self.header1.setGeometry(QRect(100, 60, 200, 25))
        self.header1.setAlignment(Qt.AlignCenter)
        self.info_label = QLabel(ChangePasswordDialog)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(50, 130, 300, 60))
        self.info_label.setStyleSheet(u"#warningLabel {\n"
"	color: red;\n"
"}")
        self.info_label.setWordWrap(True)

        self.retranslateUi(ChangePasswordDialog)

        QMetaObject.connectSlotsByName(ChangePasswordDialog)
    # setupUi

    def retranslateUi(self, ChangePasswordDialog):
        ChangePasswordDialog.setWindowTitle(QCoreApplication.translate("ChangePasswordDialog", u"Password Changing", None))
        self.submit_button.setText(QCoreApplication.translate("ChangePasswordDialog", u"Submit", None))
        self.header1.setText(QCoreApplication.translate("ChangePasswordDialog", u"Enter the new password", None))
        self.info_label.setText("")
    # retranslateUi

