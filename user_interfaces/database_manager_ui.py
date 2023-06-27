# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'database_manager.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 680)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(True)
        self.importAB = QAction(MainWindow)
        self.importAB.setObjectName(u"importAB")
        self.exportAB = QAction(MainWindow)
        self.exportAB.setObjectName(u"exportAB")
        self.credits_action_button = QAction(MainWindow)
        self.credits_action_button.setObjectName(u"credits_action_button")
        self.show_permissions_action_button = QAction(MainWindow)
        self.show_permissions_action_button.setObjectName(u"show_permissions_action_button")
        self.change_password_action_button = QAction(MainWindow)
        self.change_password_action_button.setObjectName(u"change_password_action_button")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(1200, 600))
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"	margin: auto;\n"
"}")
        self.selected_table_view = QTableView(self.centralwidget)
        self.selected_table_view.setObjectName(u"selected_table_view")
        self.selected_table_view.setGeometry(QRect(280, 140, 900, 500))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.selected_table_view.sizePolicy().hasHeightForWidth())
        self.selected_table_view.setSizePolicy(sizePolicy2)
        self.list_of_tables_view = QListView(self.centralwidget)
        self.list_of_tables_view.setObjectName(u"list_of_tables_view")
        self.list_of_tables_view.setGeometry(QRect(10, 140, 255, 500))
        sizePolicy2.setHeightForWidth(self.list_of_tables_view.sizePolicy().hasHeightForWidth())
        self.list_of_tables_view.setSizePolicy(sizePolicy2)
        self.list_of_tables_label = QLabel(self.centralwidget)
        self.list_of_tables_label.setObjectName(u"list_of_tables_label")
        self.list_of_tables_label.setGeometry(QRect(10, 70, 255, 30))
        self.selected_table_label = QLabel(self.centralwidget)
        self.selected_table_label.setObjectName(u"selected_table_label")
        self.selected_table_label.setGeometry(QRect(280, 70, 255, 30))
        self.username_label = QLabel(self.centralwidget)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(10, 20, 140, 30))
        self.username_label.setStyleSheet(u"#username_label {\n"
"	font-weight: bold;\n"
"}")
        self.modify_the_database_button = QPushButton(self.centralwidget)
        self.modify_the_database_button.setObjectName(u"modify_the_database_button")
        self.modify_the_database_button.setGeometry(QRect(480, 20, 170, 30))
        self.modify_the_database_button.setStyleSheet(u"")
        self.account_control_button = QPushButton(self.centralwidget)
        self.account_control_button.setObjectName(u"account_control_button")
        self.account_control_button.setGeometry(QRect(280, 20, 170, 30))
        self.account_control_button.setStyleSheet(u"")
        self.modify_the_data_button = QPushButton(self.centralwidget)
        self.modify_the_data_button.setObjectName(u"modify_the_data_button")
        self.modify_the_data_button.setGeometry(QRect(680, 20, 170, 30))
        self.modify_the_data_button.setStyleSheet(u"")
        self.warning_label = QLabel(self.centralwidget)
        self.warning_label.setObjectName(u"warning_label")
        self.warning_label.setGeometry(QRect(690, 100, 480, 30))
        self.warning_label.setStyleSheet(u"#warning_label {\n"
"	color: red;\n"
"}")
        self.warning_label.setWordWrap(True)
        self.selected_table_data_filter = QLineEdit(self.centralwidget)
        self.selected_table_data_filter.setObjectName(u"selected_table_data_filter")
        self.selected_table_data_filter.setGeometry(QRect(279, 100, 400, 30))
        self.list_of_tables_filter = QLineEdit(self.centralwidget)
        self.list_of_tables_filter.setObjectName(u"list_of_tables_filter")
        self.list_of_tables_filter.setGeometry(QRect(9, 100, 255, 30))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 22))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuMyAccount = QMenu(self.menubar)
        self.menuMyAccount.setObjectName(u"menuMyAccount")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMyAccount.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.credits_action_button)
        self.menuMyAccount.addAction(self.show_permissions_action_button)
        self.menuMyAccount.addAction(self.change_password_action_button)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Euler Database Manager", None))
        self.importAB.setText(QCoreApplication.translate("MainWindow", u"Import File", None))
        self.exportAB.setText(QCoreApplication.translate("MainWindow", u"Export File", None))
        self.credits_action_button.setText(QCoreApplication.translate("MainWindow", u"Credits", None))
        self.show_permissions_action_button.setText(QCoreApplication.translate("MainWindow", u"Show Permissions", None))
        self.change_password_action_button.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.list_of_tables_label.setText(QCoreApplication.translate("MainWindow", u"List of Tables", None))
        self.selected_table_label.setText(QCoreApplication.translate("MainWindow", u"Selected Table", None))
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.modify_the_database_button.setText(QCoreApplication.translate("MainWindow", u"Modifty The Database", None))
        self.account_control_button.setText(QCoreApplication.translate("MainWindow", u"Control User Accounts", None))
        self.modify_the_data_button.setText(QCoreApplication.translate("MainWindow", u"Modify The Data", None))
        self.warning_label.setText("")
        self.selected_table_data_filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.list_of_tables_filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuMyAccount.setTitle(QCoreApplication.translate("MainWindow", u"My Account", None))
    # retranslateUi

