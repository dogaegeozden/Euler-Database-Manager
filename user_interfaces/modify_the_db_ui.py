# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modify_the_db.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_ModifyTheTableDialog(object):
    def setupUi(self, ModifyTheTableDialog):
        if not ModifyTheTableDialog.objectName():
            ModifyTheTableDialog.setObjectName(u"ModifyTheTableDialog")
        ModifyTheTableDialog.resize(220, 510)
        self.select_an_operation_combo_box = QComboBox(ModifyTheTableDialog)
        self.select_an_operation_combo_box.addItem("")
        self.select_an_operation_combo_box.addItem("")
        self.select_an_operation_combo_box.addItem("")
        self.select_an_operation_combo_box.addItem("")
        self.select_an_operation_combo_box.addItem("")
        self.select_an_operation_combo_box.setObjectName(u"select_an_operation_combo_box")
        self.select_an_operation_combo_box.setGeometry(QRect(10, 60, 200, 25))
        self.select_an_operation_label = QLabel(ModifyTheTableDialog)
        self.select_an_operation_label.setObjectName(u"select_an_operation_label")
        self.select_an_operation_label.setGeometry(QRect(10, 20, 200, 30))
        self.magnifier_button = QPushButton(ModifyTheTableDialog)
        self.magnifier_button.setObjectName(u"magnifier_button")
        self.magnifier_button.setGeometry(QRect(180, 470, 30, 30))
        self.magnifier_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/magnifier.png", QSize(), QIcon.Normal, QIcon.Off)
        self.magnifier_button.setIcon(icon)
        self.text_edit1 = QTextEdit(ModifyTheTableDialog)
        self.text_edit1.setObjectName(u"text_edit1")
        self.text_edit1.setGeometry(QRect(20, 175, 180, 210))
        self.line_edit1 = QLineEdit(ModifyTheTableDialog)
        self.line_edit1.setObjectName(u"line_edit1")
        self.line_edit1.setGeometry(QRect(20, 120, 180, 25))
        self.label2 = QLabel(ModifyTheTableDialog)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(20, 145, 180, 30))
        self.label1 = QLabel(ModifyTheTableDialog)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(20, 90, 180, 30))
        self.info_label = QLabel(ModifyTheTableDialog)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(20, 385, 180, 75))
        self.info_label.setStyleSheet(u"#info_label {\n"
"	color: red;\n"
"}")
        self.info_label.setWordWrap(True)
        self.commit_button = QPushButton(ModifyTheTableDialog)
        self.commit_button.setObjectName(u"commit_button")
        self.commit_button.setGeometry(QRect(65, 470, 90, 30))

        self.retranslateUi(ModifyTheTableDialog)

        QMetaObject.connectSlotsByName(ModifyTheTableDialog)
    # setupUi

    def retranslateUi(self, ModifyTheTableDialog):
        ModifyTheTableDialog.setWindowTitle(QCoreApplication.translate("ModifyTheTableDialog", u"Modify The Database", None))
        self.select_an_operation_combo_box.setItemText(0, QCoreApplication.translate("ModifyTheTableDialog", u"Create Table", None))
        self.select_an_operation_combo_box.setItemText(1, QCoreApplication.translate("ModifyTheTableDialog", u"Drop Table", None))
        self.select_an_operation_combo_box.setItemText(2, QCoreApplication.translate("ModifyTheTableDialog", u"Add Column", None))
        self.select_an_operation_combo_box.setItemText(3, QCoreApplication.translate("ModifyTheTableDialog", u"Drop Column", None))
        self.select_an_operation_combo_box.setItemText(4, QCoreApplication.translate("ModifyTheTableDialog", u"Modify Column", None))

        self.select_an_operation_label.setText(QCoreApplication.translate("ModifyTheTableDialog", u"Select An Operatation", None))
#if QT_CONFIG(tooltip)
        self.magnifier_button.setToolTip(QCoreApplication.translate("ModifyTheTableDialog", u"https://dev.mysql.com/doc/refman/8.0/en/creating-tables.html", None))
#endif // QT_CONFIG(tooltip)
        self.magnifier_button.setText("")
        self.label2.setText(QCoreApplication.translate("ModifyTheTableDialog", u"Columns' Specifications:", None))
        self.label1.setText(QCoreApplication.translate("ModifyTheTableDialog", u"Table Name:", None))
        self.info_label.setText("")
        self.commit_button.setText(QCoreApplication.translate("ModifyTheTableDialog", u"Create", None))
    # retranslateUi

