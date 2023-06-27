# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'credits_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CreditsDialog(object):
    def setupUi(self, CreditsDialog):
        if not CreditsDialog.objectName():
            CreditsDialog.setObjectName(u"CreditsDialog")
        CreditsDialog.resize(400, 208)
        CreditsDialog.setStyleSheet(u"#centralwidget {\n"
"}")
        self.actionUser_Name_Generator = QAction(CreditsDialog)
        self.actionUser_Name_Generator.setObjectName(u"actionUser_Name_Generator")
        self.actionPassword_Generator = QAction(CreditsDialog)
        self.actionPassword_Generator.setObjectName(u"actionPassword_Generator")
        self.actionPassword_Manager = QAction(CreditsDialog)
        self.actionPassword_Manager.setObjectName(u"actionPassword_Manager")
        self.centralWidget = QWidget(CreditsDialog)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setGeometry(QRect(0, 0, 401, 211))
        self.label = QLabel(self.centralWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 70, 201, 41))
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(CreditsDialog)

        QMetaObject.connectSlotsByName(CreditsDialog)
    # setupUi

    def retranslateUi(self, CreditsDialog):
        CreditsDialog.setWindowTitle(QCoreApplication.translate("CreditsDialog", u"Euler Database Manager", None))
        self.actionUser_Name_Generator.setText(QCoreApplication.translate("CreditsDialog", u"User Name Generator", None))
        self.actionPassword_Generator.setText(QCoreApplication.translate("CreditsDialog", u"Password Generator", None))
        self.actionPassword_Manager.setText(QCoreApplication.translate("CreditsDialog", u"Password Manager", None))
        self.label.setText(QCoreApplication.translate("CreditsDialog", u"Developed by Tamrinotte Inc.", None))
    # retranslateUi

