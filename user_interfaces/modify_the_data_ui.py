# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modify_the_data.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ModifyTheDataDialog(object):
    def setupUi(self, ModifyTheDataDialog):
        if not ModifyTheDataDialog.objectName():
            ModifyTheDataDialog.setObjectName(u"ModifyTheDataDialog")
        ModifyTheDataDialog.resize(441, 482)
        self.formLayoutWidget = QWidget(ModifyTheDataDialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 20, 421, 361))
        self.data_form_layout = QFormLayout(self.formLayoutWidget)
        self.data_form_layout.setObjectName(u"data_form_layout")
        self.data_form_layout.setContentsMargins(0, 0, 0, 0)
        self.delete_button = QPushButton(ModifyTheDataDialog)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(100, 430, 120, 30))
        self.save_changes_button = QPushButton(ModifyTheDataDialog)
        self.save_changes_button.setObjectName(u"save_changes_button")
        self.save_changes_button.setGeometry(QRect(230, 430, 120, 30))
        self.info_label = QLabel(ModifyTheDataDialog)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(10, 390, 420, 30))
        self.info_label.setStyleSheet(u"#info_label {\n"
"	color: red;\n"
"}")
        self.info_label.setWordWrap(True)

        self.retranslateUi(ModifyTheDataDialog)

        QMetaObject.connectSlotsByName(ModifyTheDataDialog)
    # setupUi

    def retranslateUi(self, ModifyTheDataDialog):
        ModifyTheDataDialog.setWindowTitle(QCoreApplication.translate("ModifyTheDataDialog", u"Control The Data", None))
        self.delete_button.setText(QCoreApplication.translate("ModifyTheDataDialog", u"Delete", None))
        self.save_changes_button.setText(QCoreApplication.translate("ModifyTheDataDialog", u"Save Changes", None))
        self.info_label.setText("")
    # retranslateUi

