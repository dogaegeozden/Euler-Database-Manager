# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'permissions_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PermissionsDialog(object):
    def setupUi(self, PermissionsDialog):
        if not PermissionsDialog.objectName():
            PermissionsDialog.setObjectName(u"PermissionsDialog")
        PermissionsDialog.resize(400, 300)
        self.ok_button = QPushButton(PermissionsDialog)
        self.ok_button.setObjectName(u"ok_button")
        self.ok_button.setGeometry(QRect(150, 255, 89, 25))
        self.dialog_header = QLabel(PermissionsDialog)
        self.dialog_header.setObjectName(u"dialog_header")
        self.dialog_header.setGeometry(QRect(50, 15, 290, 30))
        self.dialog_header.setAlignment(Qt.AlignCenter)
        self.list_of_permissions_view = QListView(PermissionsDialog)
        self.list_of_permissions_view.setObjectName(u"list_of_permissions_view")
        self.list_of_permissions_view.setGeometry(QRect(50, 55, 300, 180))

        self.retranslateUi(PermissionsDialog)

        QMetaObject.connectSlotsByName(PermissionsDialog)
    # setupUi

    def retranslateUi(self, PermissionsDialog):
        PermissionsDialog.setWindowTitle(QCoreApplication.translate("PermissionsDialog", u"User Permissions", None))
        self.ok_button.setText(QCoreApplication.translate("PermissionsDialog", u"OK", None))
        self.dialog_header.setText(QCoreApplication.translate("PermissionsDialog", u"User's Permissions", None))
    # retranslateUi

