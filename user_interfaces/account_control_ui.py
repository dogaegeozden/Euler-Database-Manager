# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account_control.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_AccountControlDialog(object):
    def setupUi(self, AccountControlDialog):
        if not AccountControlDialog.objectName():
            AccountControlDialog.setObjectName(u"AccountControlDialog")
        AccountControlDialog.resize(820, 680)
        self.list_of_accounts_header_label = QLabel(AccountControlDialog)
        self.list_of_accounts_header_label.setObjectName(u"list_of_accounts_header_label")
        self.list_of_accounts_header_label.setGeometry(QRect(10, 5, 110, 30))
        self.list_of_accounts_list_view = QListView(AccountControlDialog)
        self.list_of_accounts_list_view.setObjectName(u"list_of_accounts_list_view")
        self.list_of_accounts_list_view.setGeometry(QRect(10, 40, 370, 290))
        self.delete_the_account_button = QPushButton(AccountControlDialog)
        self.delete_the_account_button.setObjectName(u"delete_the_account_button")
        self.delete_the_account_button.setGeometry(QRect(400, 240, 90, 25))
        self.add_an_account_button = QPushButton(AccountControlDialog)
        self.add_an_account_button.setObjectName(u"add_an_account_button")
        self.add_an_account_button.setGeometry(QRect(400, 110, 90, 25))
        self.username_line_edit = QLineEdit(AccountControlDialog)
        self.username_line_edit.setObjectName(u"username_line_edit")
        self.username_line_edit.setGeometry(QRect(400, 70, 180, 25))
        self.password_line_edit = QLineEdit(AccountControlDialog)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setGeometry(QRect(620, 70, 180, 25))
        self.username_label = QLabel(AccountControlDialog)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(400, 40, 110, 20))
        self.password_label = QLabel(AccountControlDialog)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(620, 40, 110, 20))
        self.create_delete_update_an_account_label = QLabel(AccountControlDialog)
        self.create_delete_update_an_account_label.setObjectName(u"create_delete_update_an_account_label")
        self.create_delete_update_an_account_label.setGeometry(QRect(400, 5, 381, 30))
        self.selected_account_label = QLabel(AccountControlDialog)
        self.selected_account_label.setObjectName(u"selected_account_label")
        self.selected_account_label.setGeometry(QRect(400, 200, 140, 30))
        self.selected_account_label.setStyleSheet(u"#selected_account_label {\n"
"	font-weight: bold;\n"
"}")
        self.list_of_the_users_permissions_list_view = QListView(AccountControlDialog)
        self.list_of_the_users_permissions_list_view.setObjectName(u"list_of_the_users_permissions_list_view")
        self.list_of_the_users_permissions_list_view.setGeometry(QRect(10, 380, 370, 290))
        self.list_of_the_users_permissions_label = QLabel(AccountControlDialog)
        self.list_of_the_users_permissions_label.setObjectName(u"list_of_the_users_permissions_label")
        self.list_of_the_users_permissions_label.setGeometry(QRect(10, 350, 200, 30))
        self.grant_revoke_permissions_label = QLabel(AccountControlDialog)
        self.grant_revoke_permissions_label.setObjectName(u"grant_revoke_permissions_label")
        self.grant_revoke_permissions_label.setGeometry(QRect(400, 350, 380, 30))
        self.table_name_line_edit = QLineEdit(AccountControlDialog)
        self.table_name_line_edit.setObjectName(u"table_name_line_edit")
        self.table_name_line_edit.setGeometry(QRect(400, 410, 250, 25))
        self.table_name_label = QLabel(AccountControlDialog)
        self.table_name_label.setObjectName(u"table_name_label")
        self.table_name_label.setGeometry(QRect(400, 380, 115, 20))
        self.permission_names = QLabel(AccountControlDialog)
        self.permission_names.setObjectName(u"permission_names")
        self.permission_names.setGeometry(QRect(400, 440, 230, 20))
        self.revoke_permissions_button = QPushButton(AccountControlDialog)
        self.revoke_permissions_button.setObjectName(u"revoke_permissions_button")
        self.revoke_permissions_button.setGeometry(QRect(500, 590, 90, 25))
        self.create_an_account_info_label = QLabel(AccountControlDialog)
        self.create_an_account_info_label.setObjectName(u"create_an_account_info_label")
        self.create_an_account_info_label.setGeometry(QRect(400, 140, 410, 55))
        self.create_an_account_info_label.setStyleSheet(u"#create_an_account_info_label {\n"
"	color: red;\n"
"}")
        self.create_an_account_info_label.setWordWrap(True)
        self.grant_permissions_button = QPushButton(AccountControlDialog)
        self.grant_permissions_button.setObjectName(u"grant_permissions_button")
        self.grant_permissions_button.setGeometry(QRect(400, 590, 90, 25))
        self.permissions_line_edit = QTextEdit(AccountControlDialog)
        self.permissions_line_edit.setObjectName(u"permissions_line_edit")
        self.permissions_line_edit.setGeometry(QRect(400, 470, 340, 70))
        self.permissions_hint_label = QLabel(AccountControlDialog)
        self.permissions_hint_label.setObjectName(u"permissions_hint_label")
        self.permissions_hint_label.setGeometry(QRect(400, 550, 371, 30))
        self.delete_the_account_info_label = QLabel(AccountControlDialog)
        self.delete_the_account_info_label.setObjectName(u"delete_the_account_info_label")
        self.delete_the_account_info_label.setGeometry(QRect(400, 270, 411, 55))
        self.delete_the_account_info_label.setStyleSheet(u"#delete_the_account_info_label {\n"
"	color: red;\n"
"}")
        self.delete_the_account_info_label.setWordWrap(True)
        self.selected_account_name_label = QLabel(AccountControlDialog)
        self.selected_account_name_label.setObjectName(u"selected_account_name_label")
        self.selected_account_name_label.setGeometry(QRect(540, 200, 200, 30))
        self.permissions_info_label = QLabel(AccountControlDialog)
        self.permissions_info_label.setObjectName(u"permissions_info_label")
        self.permissions_info_label.setGeometry(QRect(400, 610, 410, 55))
        self.permissions_info_label.setStyleSheet(u"#permissions_info_label {\n"
"	color: red;\n"
"}")
        self.magnifier_button = QPushButton(AccountControlDialog)
        self.magnifier_button.setObjectName(u"magnifier_button")
        self.magnifier_button.setGeometry(QRect(780, 550, 30, 30))
        self.magnifier_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/magnifier.png", QSize(), QIcon.Normal, QIcon.Off)
        self.magnifier_button.setIcon(icon)

        self.retranslateUi(AccountControlDialog)

        QMetaObject.connectSlotsByName(AccountControlDialog)
    # setupUi

    def retranslateUi(self, AccountControlDialog):
        AccountControlDialog.setWindowTitle(QCoreApplication.translate("AccountControlDialog", u"Account Control Dialog", None))
#if QT_CONFIG(tooltip)
        AccountControlDialog.setToolTip(QCoreApplication.translate("AccountControlDialog", u"https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        AccountControlDialog.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.list_of_accounts_header_label.setText(QCoreApplication.translate("AccountControlDialog", u"List of Accounts", None))
        self.delete_the_account_button.setText(QCoreApplication.translate("AccountControlDialog", u"Delete", None))
#if QT_CONFIG(statustip)
        self.add_an_account_button.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.add_an_account_button.setText(QCoreApplication.translate("AccountControlDialog", u"Create", None))
#if QT_CONFIG(tooltip)
        self.username_line_edit.setToolTip(QCoreApplication.translate("AccountControlDialog", u"Hint: Enter a username that is already exist to change the account's password.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.username_line_edit.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.username_label.setText(QCoreApplication.translate("AccountControlDialog", u"Username", None))
        self.password_label.setText(QCoreApplication.translate("AccountControlDialog", u"Password", None))
        self.create_delete_update_an_account_label.setText(QCoreApplication.translate("AccountControlDialog", u"Create/Delete/Update An Account", None))
        self.selected_account_label.setText(QCoreApplication.translate("AccountControlDialog", u"Selected Account: ", None))
        self.list_of_the_users_permissions_label.setText(QCoreApplication.translate("AccountControlDialog", u"List of The User's Permissions", None))
        self.grant_revoke_permissions_label.setText(QCoreApplication.translate("AccountControlDialog", u"Grant/Revoke Permissions", None))
        self.table_name_label.setText(QCoreApplication.translate("AccountControlDialog", u"Table Name", None))
        self.permission_names.setText(QCoreApplication.translate("AccountControlDialog", u"Permission Name/s", None))
        self.revoke_permissions_button.setText(QCoreApplication.translate("AccountControlDialog", u"Revoke", None))
        self.create_an_account_info_label.setText("")
        self.grant_permissions_button.setText(QCoreApplication.translate("AccountControlDialog", u"Grant", None))
        self.permissions_hint_label.setText(QCoreApplication.translate("AccountControlDialog", u"Separate the permissions with ','. Ex: SELECT, CREATE", None))
        self.delete_the_account_info_label.setText("")
        self.selected_account_name_label.setText("")
        self.permissions_info_label.setText("")
#if QT_CONFIG(tooltip)
        self.magnifier_button.setToolTip(QCoreApplication.translate("AccountControlDialog", u"https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html", None))
#endif // QT_CONFIG(tooltip)
        self.magnifier_button.setText("")
    # retranslateUi

