# This Python file uses the following encoding: utf-8
# LIBRARIES/MODULES
# Python3 modules
from sys import argv
from os import path
import mysql.connector
import datetime
import pandas as pd
from re import compile
from logging import basicConfig, DEBUG, debug, disable, CRITICAL
from copy import copy
from numpy import array, append as npappend
from webbrowser import open as wbopen
from pathlib import Path

# PySide2 modules
from PySide2.QtCore import QRect, QSortFilterProxyModel, Qt, QAbstractTableModel, QAbstractListModel
from PySide2.QtWidgets import QMessageBox, QAction, QMenu, QSpinBox, QLineEdit, QLabel, QApplication, QMainWindow, QDialog

# GUIs
from user_interfaces.database_manager_ui import Ui_MainWindow
from user_interfaces.log_in_win_ui import Ui_LogInWindow
from user_interfaces.permissions_dialog_ui import Ui_PermissionsDialog
from user_interfaces.account_control_ui import Ui_AccountControlDialog
from user_interfaces.modify_the_data_ui import Ui_ModifyTheDataDialog
from user_interfaces.credits_dialog_ui import Ui_CreditsDialog
from user_interfaces.password_changing_ui import Ui_ChangePasswordDialog
from user_interfaces.modify_the_db_ui import Ui_ModifyTheTableDialog

# RESOURCES
import resources_rc

# Configuring debugging feature code
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Disabling the debugging feature. Hint: Comment out the line to enable debugging.
# disable(CRITICAL)

# GLOBAL VARIABLES
# Creating a variable called base_dir which leads to the current working directory.
base_dir = path.dirname(__file__)

def main():
    """The function which runs the entire program"""
    app = QApplication(argv)
    login_win = LogInWindow()
    login_win.show()
    app.exec_()

# CLASSES
class DataModelFLV(QAbstractListModel):
    def __init__(self, list_of_all_tables=None):
        super().__init__()
        self.list_of_all_tables = list_of_all_tables or []

    def data(self, index, role):
        """A function which specifiys the data object model"""
        if role == Qt.DisplayRole:
            table_name = self.list_of_all_tables[index.row()]
            return table_name

    def rowCount(self, index): # Keep the name as rowCount
        """A function which returns the length of the list_of_all_tables"""
        return len(self.list_of_all_tables)


class SelectedTableDataModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

class PasswordChangingDialog(QDialog, Ui_ChangePasswordDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Load the GUI
        self.setupUi(self)

        # Connecting change_password function with the submit_button as the function will going to trigger with a press signal.
        self.submit_button.pressed.connect(self.change_password)

    def change_password(self):
        """A function which changes the password"""
        # Creating a regular expression to validate the passwords
        password_regex = compile(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{20,40}')

        # Getting the new password from the line edit widget.
        new_password = self.password_changing_line_edit.text()

        # Validating the password with the password regular expression.
        result = password_regex.search(new_password)

        # Checking the result to write conditionals.
        if result.group() == new_password:
            # Printing the new password in debug mode.
            debug(f'New Password = {result}')

            # Creating a cursor to change the password.
            mysql_change_password_cursor = mysql_database_connection.cursor()

            # Executing the show grants instruction to display selected user's permissions
            mysql_change_password_cursor.execute(f'SET PASSWORD FOR \'{user}\'@\'{host}\'=\'{new_password}\'')

            # Seting the style sheet of the info_label
            self.info_label.setStyleSheet(u"#info_label {color: lightgreen;}")
            # Setting the text value of the info_label as it will going to show a warning message.
            self.info_label.setText("Your password has been changed.")

        # Checking if the regular expression match is not equal to the new password. Hint: It means that the password is not vaild.
        else:            
            # Seting the style sheet of the info_label
            self.info_label.setStyleSheet(u"#info_label {color: red;}")
            # Setting the text value of the info_label as it will going to show a warning message.
            self.info_label.setText("Passwords must contain both upper and lower case characters, must has at least one digit and must be 20-40 characters long.")


class CreditsDialog(QDialog, Ui_CreditsDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Load the GUI
        self.setupUi(self)

# Self contained dialog box class.
class PermissionsDialog(QDialog, Ui_PermissionsDialog):
    # Initialize the window to make it self contained.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Load the GUI
        self.setupUi(self)

        # Setting the text of the permission box's header
        self.dialog_header.setText(f'{user}\'s Permissions')

        # Creating the datas model for the list of user permissions
        self.list_of_permissions_data_model = DataModelFLV(list_of_user_permissions)

        # Seting the model for the listOfPermissionsW widget
        self.list_of_permissions_view.setModel(self.list_of_permissions_data_model)

        # Connectiong the okBtn widget with the closePD function with pressed signal
        self.ok_button.pressed.connect(self.close)

# Self contained QDialog class.
class ControlUserAccsDialog(QDialog, Ui_AccountControlDialog):
    # Initialize the window to make it self contained.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Load the GUI
        self.setupUi(self)

        # Loading the list of user accounts
        self.load_the_list_of_accounts()

        # Loading the selected user's list of permissions
        self.load_selected_users_list_of_permissions()

        # Connecting the identify_the_selection with the list_view widget as the function will going to trigger with a click signal.
        self.list_of_accounts_list_view.clicked.connect(self.identify_the_selection)

        # Connecting the delete_the_account function with the delete_the_account button as the function will going to trigger withy a press signal.
        self.delete_the_account_button.pressed.connect(self.delete_the_account)
        
        # Connecting the create_an_account function with the add_an_account_button as the function will going to trigger with a press signal.
        self.add_an_account_button.pressed.connect(self.create_an_account)

        # Connecting the grant button with the grant permission function as the function will going to trigger with a press signal
        self.grant_permissions_button.pressed.connect(self.grant_permissions)

        # Connecting the revoke_permissions button with the revoke_permissions function as the function will going to trigger with a press signal.
        self.revoke_permissions_button.pressed.connect(self.revoke_permissions)

        # Connecting the change_the_button_label function with the username_line_edit widget as the function will going to trigger with a text change signal.
        self.username_line_edit.textChanged.connect(self.change_the_button_label)

        # Connecting the open_the_help_page function with the magnifier_button as the function will going to trigger with a press signal.
        self.magnifier_button.pressed.connect(self.open_the_help_page)

        # Trying to execute the code which is inside the try block.
        try:
            # Setting the text value of the selected_account_name_label
            self.selected_account_name_label.setText(selected_account)
       
        # Instructing the computer about what to do if the application fails to execute the code which is inside the try block.
        except:
            # Setting the selected account name label to empty string
            self.selected_account_name_label.setText("")

    # Creating a contex menu.
    def contextMenuEvent(self, e):
        # Creating the context menu. Hint: This is the menu which opens when the user right clicks to the gui.
        self.context_menu = QMenu()
        # Creating a refresh button to the context menu.
        self.refresh_button = QAction("Refresh")
        # Connecting the refresh_the_views function with the refresh_button as the function will going to trigger with a trigger signal.
        self.refresh_button.triggered.connect(self.refresh_the_views)
        # Adding the refresh button to the context menu.
        self.context_menu.addAction(self.refresh_button)
        # Showing the context_menu.
        self.context_menu.exec_(e.globalPos())

    def refresh_the_views(self):
        """A function which reloads the views in the control user accounts dialog"""
        # Reloading the selected user's list of permissions.
        self.load_selected_users_list_of_permissions()
        # Reloading the list of accounts.
        self.load_the_list_of_accounts()

    def open_the_help_page(self):
        """A function which opens the mysql permissions help page in the browser."""
        # Opening the help page in the default browser.
        wbopen("https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html")

    def change_the_button_label(self):
        """A function which changes the text value of the create button if the username is in the list of users list"""
        # Creating a variable called username_text from the username_line_edit widget's text input.
        username_text = self.username_line_edit.text()
        # Checking if the username_text is in the list_of_user_accounts.
        if username_text in list_of_account_names:
            # If the username is in the list of accounts changing the add_an_account_buttons text value to "Change."
            self.add_an_account_button.setText("Change")
        # Checking if the username is not in the list_of_user_accounts.
        else:
            # Setting the add_an_account_button's text value to "Create".
            self.add_an_account_button.setText("Create")

    def revoke_permissions(self):
        """A function which revoke's permission"""
        # Creating a global variable called account_selection_status to identify if the user selected an account or not.
        global account_selection_status
        # Initializing the account_selection_status variable. Hint: By default it's set to False.
        account_selection_status = False

        # Validating if selected_account variable is defined or not.
        try:
            # Calling the selected account variable.
            selected_account
            # Printing the selected account in debug mode.
            debug(f'Selected Account: {selected_account}')
            # Setting the status to True if the variable is defined.
            account_selection_status = True
            # Creating global variables called regex_username_string, regex_hostname_string and regex_database_string
            global regex_username_string, regex_hostname_string, regex_database_string
            # Initialzing the regular expression specification strings for the host and database variables
            list_of_username_statements = [selected_account, f'\'{selected_account}\'']
            regex_username_string = '|'.join(list_of_username_statements)
            list_of_hostname_statements = [host, f'\'{host}\'']
            regex_hostname_string = '|'.join(list_of_hostname_statements)
            list_of_database_statements = [database, f'\'{database}\'']
            regex_database_string = '|'.join(list_of_database_statements)
        
        # Hanling NameErrors
        except NameError:
            # Printing the what went wrong in debug mode.
            debug("Name Error: \"selected_account\" variable isn't defined.")

        # Handling any other case.
        else:
            # Printing the "Variable is defined." in debug mode.
            debug("Variable is defined.")

        # Creating a global variable called valid_tables
        global valid_tables
        # Initializing the valid_tables with the list_of_table_names's copy. Hint: Using copy function prevents the reflections to the list_of_table_names.
        valid_tables = copy(list_of_table_names)
        # Appending the '*' to the list of valid_tables.
        valid_tables.append('*')

        # Checking if account_selection_status is equal to True.
        if account_selection_status == True:

            # Creating a variable called table_name from the table_name_line_edit widget's input value.
            table_name = self.table_name_line_edit.text()

            # Checking if the table_name value that the user entered is in the valid_tables list.
            if table_name in valid_tables:
                
                # Checking if the table name that the user entered is equal to '*'
                if table_name == '*':
                    # Assigning a new value to the table_name variable.
                    table_name = '\*'

                # Capturing the permissions string from the widget called permissions_line_edit
                permissions_string = self.permissions_line_edit.toPlainText()

                # Creating a mysql command string to revoke permissions.
                mysql_command = f'REVOKE {permissions_string} ON {database}.{table_name} FROM \'{selected_account}\'@\'{host}\';'

                # Printing the mysql command in debug mode.
                debug(f'MySQL Command: {mysql_command}')

                # Creating a regular expression to validate the mysql command.
                revoke_permissions_regex = compile(r'REVOKE ((^{set_of_permissions})?,? ?({set_of_permissions})){{0,14}} ON ({set_of_database_names})\.({table_name}) FROM ({set_of_usernames})@({set_of_hostnames})\;'.format(set_of_permissions=mysql_permissions_keys_string, set_of_database_names=regex_database_string, table_name=table_name, set_of_usernames=regex_username_string, set_of_hostnames=regex_hostname_string))
                
                # Validating the mysql_command with the revoke permission regex.
                result = revoke_permissions_regex.search(mysql_command)
                
                # Printing the results in debug mode.
                debug(f'Regex Search Result: {result}')

                # Checking if the result is equal to mysql_command.
                if result.group() == mysql_command:
                    
                    # Trying to execute the block which is inside the try block.
                    try:
                        # Creating a cursor to revoke permissions
                        mysql_revoke_permissions_cursor = mysql_database_connection.cursor()

                        # Executing the mysql command
                        mysql_revoke_permissions_cursor.execute(mysql_command)

                        # Setting the style sheet of the label.
                        self.permissions_info_label.setStyleSheet(u"#permissions_info_label {color: lightgreen;}")

                        # Setting the text value of the permissions_info_label widget.
                        self.permissions_info_label.setText("Permissions revoked.")

                        # Reloading the selected user's list of permissions.
                        self.load_selected_users_list_of_permissions()

                    # Instructing the computer about what to do if the application fails to execute the code which is inside the try block.
                    except:
                        # Setting the style sheet of permissions_info_label.
                        self.permissions_info_label.setStyleSheet(u"#permissionIL {color: red;}")
                        # Setting the text value of the permissions_info_label widget.
                        self.permissions_info_label.setText("Wrong permission specification!")

            # Checking if the table_name is not in the list of valid_tables
            else:
                # Setting the style sheet of permissions_info_label.
                self.permissions_info_label.setStyleSheet(u"#permissionIL {color: red;}")
                # Setting the text value of the permissions_info_label widget.
                self.permissions_info_label.setText("Table isn't exist!")

        # Checking if the account_selection_status is not equal to False.
        else:
            # Setting the text value of the permissions_info_label widget.
            self.permissions_info_label.setText("You must select a user!")

    def grant_permissions(self):
        """A function which grants permissions"""
        # Creating a global variable called account_selection_status
        global account_selection_status
        # Initializing the account_selection_status 
        account_selection_status = False

        # Trying to execute the code which is inside the try block.
        try:
            # Calling the selected_account variable. Hint: If the variable is not exists, it will give an error and except block will get in action.
            selected_account
            # Printing the selected account variable in debug mode.
            debug(f'Selected Account: {selected_account}')
            # Setting the status to True if the variable is defined.
            account_selection_status = True
            # Creating global variables called regex_username_string, regex_hostname_string and regex_database_string
            global regex_username_string, regex_hostname_string, regex_database_string
            # Initialzing the regular expression specification strings for the host and database variables
            list_of_username_statements = [selected_account, f'\'{selected_account}\'']
            regex_username_string = '|'.join(list_of_username_statements)
            list_of_hostname_statements = [host, f'\'{host}\'']
            regex_hostname_string = '|'.join(list_of_hostname_statements)
            list_of_database_statements = [database, f'\'{database}\'']
            regex_database_string = '|'.join(list_of_database_statements)

        # Hanling NameErrors
        except NameError:
            # Printing the what went wrong in debug mode.
            debug("Name Error: \"selected_account\" variable isn't defined.")

        # Handling any other case.
        else:
            # Printing the "Variable is defined." in debug mode.
            debug("Variable is defined.")

        # Creating a global variable called valid_tables
        global valid_tables
        # Initializing the valid_tables with the list_of_table_names's copy. Hint: Using copy function prevents the reflections to the list_of_table_names.
        valid_tables = copy(list_of_table_names)
        # Appending the '*' to the list of valid_tables.
        valid_tables.append('*')

        # Checking if the account_selection_status is equal to True.
        if account_selection_status == True:
            # Creating a variable called table_name from the table_name_line_edit widget's input.
            table_name = self.table_name_line_edit.text()
            # Checking if the table name is in the valid_tables list.
            if table_name in valid_tables:

                # Checking if the user entered '*' as the table name.
                if table_name == '*':
                    # Assigning a new value to the table_name variable.
                    table_name = '\*'

                # Capturing the permissions string from the widget called permissionsLE
                permissions_string = self.permissions_line_edit.toPlainText()

                # Creating a mysql command string
                mysql_command = f'GRANT {permissions_string} ON {database}.{table_name} TO \'{selected_account}\'@\'{host}\';'
                # Printing the mysql_command in debug mode.
                debug(f'MySQL Command: {mysql_command}')

                # Creating a regular expression to valide the mysql_command.
                grant_permissions_regex = compile(r'GRANT ((^{set_of_permissions})?,? ?({set_of_permissions})){{0,14}} ON ({set_of_database_names})\.({table_name}) TO ({set_of_usernames})@({set_of_hostnames})\;'.format(set_of_permissions=mysql_permissions_keys_string, set_of_database_names=regex_database_string, table_name=table_name, set_of_usernames=regex_username_string, set_of_hostnames=regex_hostname_string))
                
                # Creating a variable called results by searching the mysql_command with the regular expression. Hint: Pattern matching. 
                result = grant_permissions_regex.search(mysql_command)
                # Printing the search results in debug mode.
                debug(f'Regex Search Result: {result.group()}')

                # Checking if the result is equal to the mysql_command
                if result.group() == mysql_command:
                    
                    # Trying to execute the block which is inside the try block.
                    try:
                        # Creating a cursor to grant permissions.
                        mysql_grant_permission_cursor = mysql_database_connection.cursor()

                        # # Executing mysql command.
                        mysql_grant_permission_cursor.execute(mysql_command)

                        # Setting the style sheet of the permissions_info_label.
                        self.permissions_info_label.setStyleSheet(u"#permissions_info_label {color: lightgreen;}")

                        # Setting the text of the permissions_info_label.
                        self.permissions_info_label.setText("Permissions granted.")

                        # Reloading the user's list of permissions
                        self.load_selected_users_list_of_permissions()

                    # Instructing the computer about what to do if the application fails to execute the code which is inside the try block.
                    except:
                        # Setting the style sheet of the permissions_info_label.
                        self.permissions_info_label.setStyleSheet(u"#permissions_info_label {color: red;}")
                        # Setting the text of the permissions_info_label.
                        self.permissions_info_label.setText("You don't have the required permissions!")

                # Checking if the search results are not equal to the mysql_command.
                else:
                    # Setting the style sheet of the permissions_info_label.
                    self.permissions_info_label.setStyleSheet(u"#permissions_info_label {color: red;}")
                    # Setting the text of the permissions_info_label.
                    self.permissions_info_label.setText("Wrong permission specification!")

            # Checking if the table_name is not in the valid_tables list.
            else:
                # Setting the style sheet of the permissions_info_label.
                self.permissions_info_label.setStyleSheet(u"#permissions_info_label {color: red;}")
                # Setting the text of the permissions_info_label.
                self.permissions_info_label.setText("Table isn't exist!")

        # Checking if the account_selection_status is not equal to True.
        else:
            # Setting the style sheet of the permissions_info_label.
            self.permissions_info_label.setStyleSheet(u"#permissions_info_label {color: red;}")
            # Setting the text of the permissions_info_label.
            self.permissions_info_label.setText("You must select an account!")

    def identify_the_selection(self):
        """A function which loads that user's permissions and sets the text value of selected account_name_label based after user selected an item from the list view."""
        # Creating a variable called indexes.
        indexes = self.list_of_accounts_list_view.selectedIndexes()
        # Printing the indexes in debug mode.
        debug(f'Selected Indexes = {indexes}')

        # Checking if indexes variable is exists.
        if indexes:
            # Indexes is a single-item list in single-select mode.
            index = indexes[0]
            # Creating a global variable called selected_account
            global selected_account
            
            selected_account = self.list_of_accounts_data_model.list_of_all_tables[index.row()]

            # Creating the data model for the selected user's permissions
            self.list_of_the_users_permissions_list_view_data_model = DataModelFLV()

            # Loading the selected user's permissions to the datamodel
            self.load_selected_users_list_of_permissions()

            # Setting the data model for the list of user permissions list view
            self.list_of_the_users_permissions_list_view.setModel(self.list_of_the_users_permissions_list_view_data_model)

            # Displaying the selected account with a label
            self.selected_account_name_label.setText(selected_account)

    def load_selected_users_list_of_permissions(self):
        """A function which loads the """
        # Trying to execute the code which is inside the try block.
        try:
            # Creating a cursor to show grants
            mysql_show_grants_cursor = mysql_database_connection.cursor()

            # Creating a string called mysql_command.
            mysql_command = f'SHOW GRANTS FOR \'{selected_account}\'@\'{host}\''

            # Executing the mysql command.
            mysql_show_grants_cursor.execute(mysql_command)

            # Fetching all the data from the mysql command's output
            selected_users_permissions = mysql_show_grants_cursor.fetchall()

            # Creating a global variable called list_of_the_users_permissions
            global list_of_the_users_permissions

            # Initializing the list_of_the_user_permissions 
            list_of_the_users_permissions = [ str(permission_string[0]) for permission_string in selected_users_permissions ]

            # Creating the data model for the selected user's permissions
            self.list_of_the_users_permissions_list_view_data_model = DataModelFLV(list_of_the_users_permissions)

            # Setting the data model for the list of user permissions list view
            self.list_of_the_users_permissions_list_view.setModel(self.list_of_the_users_permissions_list_view_data_model)
        
        # Instructing the computer about what to do if the application fails to execute the code which is inside the try block.
        except:
            debug(f'Couldn\'t load the list_of_the_users_permissions_list_view')

    def load_the_list_of_accounts(self):
        """A function which loads the list_of_accounts_list_view."""
        # Trying to execute the code which is inside the try block.
        try:
            # Checking if the user has the required permissions.
            if mysql_permissions_dictionary['select_user_permission'] == True:
                # Create a cursor for to list user accounts
                mysql_list_accounts_cursor = mysql_database_connection.cursor()

                # Creating a string called mysql_command.
                mysql_command = f'SELECT User FROM mysql.user'

                # Executing the mysql_command.
                mysql_list_accounts_cursor.execute(mysql_command)

                # Creating a global variable called list_of_accounts_names.
                global list_of_account_names

                # Initializing the list_of_accounts_names variable, by creating a list from the mysql_command's out put.
                list_of_account_names = [ str(account_name[0]) for account_name in mysql_list_accounts_cursor.fetchall() ]

                # Creating the data model for the list of user accounts list view
                self.list_of_accounts_data_model = DataModelFLV(list_of_account_names)

                # Setting the data model for the list_of_accounts_list_view widget
                self.list_of_accounts_list_view.setModel(self.list_of_accounts_data_model)

            # Checking if the user doesn't have the required permissions.
            else:
                debug(f'User doesn\'t have the required permissions.')

        # Instructing the computer about what to do if the application fails to execute the code which is inside the try block.
        except:
            # Printing what went wrong in debug mode.
            debug(f'Couldn\'t load the list_of_accounts_list_view.')

    def create_an_account(self):
        """A function which creates an account"""
        # Creating a variable called new_account_username from the username_line_edit widget's text input.
        new_account_username = self.username_line_edit.text()

        # Checking if the new_account_name is not in the list_of_account_names. Hint: Making sure account name is not already exists.
        if new_account_username not in list_of_account_names:
            # Creating a regular expression to validate the username
            username_regex = compile(r'\w{8,24}')
            
            # Validating the new username.
            username_validation_result = username_regex.search(new_account_username)

            # Checking if the user name pattern matching result is not returning None(Null)
            if username_validation_result != None:
                # Checking if username is a valid username with regular expressions and it isn't exists.
                if username_validation_result.group() == new_account_username:
                    # Creating a regular expression to validate the password.
                    password_regex = compile(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{20,40}')

                    # Creating a variable called account_password from the password_line_edit widget's text input.
                    account_password = self.password_line_edit.text()

                    # Validating the password.
                    password_validation_result = password_regex.search(account_password)

                    # Checking if the password pattern searching result doesn't return None(Null)
                    if password_validation_result != None:
                        # Checking if the password is a valid password with regular expressions
                        if password_validation_result.group() == account_password:

                            # Creating a mysql command which creates a user.
                            mysql_command = f'CREATE USER \'{new_account_username}\'@\'{host}\' IDENTIFIED BY \'{account_password}\';'

                            # Printing the mysql commands in debug mode.
                            debug(f'MySQL Command1: {mysql_command}')
                            
                            # Trying to execute the code which is inside the try block.
                            try:
                                # Creating a cursor to delete the selected user account
                                mysql_create_an_account_cursor = mysql_database_connection.cursor()

                                # Executing the mysql command.
                                mysql_create_an_account_cursor.execute(mysql_command)

                                # Loading the list of accounts
                                self.load_the_list_of_accounts()

                                # Setting the style sheet of the create_an_account_info_label
                                self.create_an_account_info_label.setStyleSheet(u"#create_an_account_info_label {color: lightgreen;}")

                                # Setting the text value of the create_an_account_info_label.
                                self.create_an_account_info_label.setText(f'Account {new_account_username} has been created.')

                                # Setting the text of the username_line_edit widget to an empty string.
                                self.username_line_edit.setText("")
                                # Setting the text of the password_line_edit widget to an empty string.
                                self.password_line_edit.setText("")

                            # Instructing computer about what to do if it fails to execute the mysql command.
                            except:
                                # Setting the style sheet of the create_an_account_info_label
                                self.create_an_account_info_label.setStyleSheet(u"#create_an_account_info_label {color: red;}")
                                # Setting the text value of the create_an_account_info_label.
                                self.create_an_account_info_label.setText("You don't have the required permissions!")

                        # Checking if the password is not valid.
                        else:
                            # Setting the style sheet of the create_an_account_info_label
                            self.create_an_account_info_label.setStyleSheet(u"#create_an_account_info_label {color: red;}")
                            # Setting the text of create_an_account_info_label
                            self.create_an_account_info_label.setText("Passwords must be in between 20-40 characters long and must include lower case, capital case letters and numbers!")
                    else:
                        # Setting the style sheet of the create_an_account_info_label
                        self.create_an_account_info_label.setStyleSheet(u"#create_an_account_info_label {color: red;}")
                        # Setting the text of create_an_account_info_label
                        self.create_an_account_info_label.setText("Passwords must be in between 20-40 characters long and must include lower case, capital case letters and numbers!")

                # Checking if the username is not valid.
                else:
                    # Setting the style sheet of the create_an_account_info_label
                    self.create_an_account_info_label.setStyleSheet(u"#create_an_account_info_label {color: red;}")
                    # Setting the text of create_an_account_info_label
                    self.create_an_account_info_label.setText("Username must be 8-24 characters long without any symbols except underscore.")
            else:
                # Setting the style sheet of the create_an_account_info_label
                self.create_an_account_info_label.setStyleSheet(u"#create_an_account_info_label {color: red;}")
                # Setting the text of create_an_account_info_label
                self.create_an_account_info_label.setText("Username must be 8-24 characters long without any symbols except underscore.")


        # Checking if the username that the user entered is already is in use.
        else:
            # Setting the style sheet of the create_an_account_info_label
            self.create_an_account_info_label.setStyleSheet(u"#create_an_account_info_label {color: red;}")
            # Setting the text of create_an_account_info_label
            self.create_an_account_info_label.setText(f'User {accUN} is already exists!')


    def delete_the_account(self):
        """A function which deletes the selected user account."""
        # Creating a variable called account_selection_status. Hint: By default it's set to False.
        account_selection_status = False
        # Trying to execute the block which is inside the try block.
        try:
            # Calling the selected_account.
            selected_account
            # Printing the selected_account in debug mode.
            debug(f'Selected Account: {selected_account}')
            # Setting the account_selection_status to True if the variable is defined.
            account_selection_status = True
        
        # Instructing the computer about what to do if the application faces with a NameError.
        except NameError:
            # Printing what went wrong in debug mode.
            debug("Name Error: \"selectedAcc\" variable isn't defined.")

        # Instructing the computer about what to do if the application fails to execute the block which is inside the try block and, doesn't face with a NameError.
        else:
            # Printing what went wrong in debug mode.
            debug("\"selectedAcc\" variable isn't defined.")

        # Checking if the account_selection_status is equal to True
        if account_selection_status == True:

            # Creating a mysql command
            mysql_command = f'DROP USER {selected_account}@{host};'

            # Printing the mysql command in debug mode.
            debug(f'MySQL Command: {mysql_command}')

            # Trying to execute the code which is inside the try block.
            try:
                # Creating a cursor to delete the selected user account
                mysql_delete_the_account_cursor = mysql_database_connection.cursor()

                # Executing the mysql_command.
                mysql_delete_the_account_cursor.execute(mysql_command)

                # Reloading the list_of_accounts_list_view
                self.load_the_list_of_accounts()

                # Setting the text of the selected_account_name_label to an empty string.
                self.selected_account_name_label.setText("")

            # Instruct the computer about what to do if the code fails to execute the code which is inside the try block.
            except:
                # Setting the style sheet of the delete_the_account_info_label
                self.delete_the_account_info_label.setStyleSheet(u"#delete_the_account_info_label {color: red;}")
                # Setting the text value of the delete_the_account_info_label
                self.delete_the_account_info_label.setText("You don't have the required permissions!")

        # Checking if the user didn't selected an account.
        else:
            # Setting the style sheet of the delete_the_account_info_label
            self.delete_the_account_info_label.setStyleSheet(u"#delete_the_account_info_label {color: red;}")
            # Setting the text value of the delete_the_account_info_label
            self.delete_the_account_info_label.setText(f'User {selected_account} not exists!')


# Self contained QDialog class.
class ModifyTheDBDialog(QDialog, Ui_ModifyTheTableDialog):
    # Initialize the window to make it self contained.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loading the GUI
        self.setupUi(self)

        # Connecting the operation_changed function with the select_an_operation_combo_box as the function will going to change with a currentTextChanged signal
        self.select_an_operation_combo_box.currentTextChanged.connect(self.operation_changed)

        # Connecting the open_the_help_page function with the magnifier_button widget as the function will going to trigger with a press signal.
        self.magnifier_button.pressed.connect(self.open_the_help_page)

        # Connecting the commit_changes function with the commit_button as the function will going to trigger with a press signal.
        self.commit_button.pressed.connect(self.commit_changes)

    def operation_changed(self, op):
        """A function which redesigns the graphical user interface and the way how it behaves."""
        # Printing the selected operation in debug mode.
        debug(f'Selected Operation: {op}')

        # Checking if the selected operation is equal to "Create Table"
        if op == "Create Table":
            # Resizing the ModifyTheDBDialog window.
            self.resize(220, 500)
            # Setting the label1 widget's text.
            self.label1.setText("Table Name:")
            # Setting the text of the label2 widget
            self.label2.setText("Columns' Specifications:")
            # Showing the widget called label2.
            self.label2.show()
            # Showing the widget called textEdit1.
            self.text_edit1.show()
            # Setting the geometry of the widget called textEdit1.
            self.text_edit1.setGeometry(QRect(20, 175, 180, 210))
            # Setting the geomerty of the info_label widget
            self.info_label.setGeometry(QRect(20, 385, 180, 75))
            # Setting the geometry of the widget called magnifier_button
            self.magnifier_button.setGeometry(QRect(20, 460, 25, 25))
            # Seeting the tool tip attribute of the widget called magnifier button.
            self.magnifier_button.setToolTip("https://www.w3schools.com/mySQl/mysql_create_table.asp")
            # Setting the text of the commit button.
            self.commit_button.setText("Create")
            # Setting the geometry of the commit button.
            self.commit_button.setGeometry(QRect(65, 460, 90, 25))

        # Checking if the selected operationg is equal to "Drop Table"
        elif op == "Drop Table":
            # Resizing the ModifyTheDBDialog window.
            self.resize(220, 260)
            # Hiding the widget called label2
            self.label2.hide()
            # Hiding the widget called text_edit1
            self.text_edit1.hide()
            # Setting the geomerty of the info_label.
            self.info_label.setGeometry(QRect(20, 145, 180, 75))
            # Setting the geomerty of the magnifier_button.
            self.magnifier_button.setGeometry(QRect(20, 220, 25, 25))
            # Setting the tool tip attribute of the magnifier_button.
            self.magnifier_button.setToolTip("https://www.w3schools.com/mySQl/mysql_drop_table.asp")
            # Setting the text of the commit_button.
            self.commit_button.setText("Drop")
            # Setting the geomerty of the commit button.
            self.commit_button.setGeometry(QRect(65, 220, 90, 25))

        # Checking if the selected operation is equal to "Add Column"
        elif op == "Add Column":
            # Resizing the ModifyTheDBDialog window.
            self.resize(220, 320)
            # Setting the text of the label1
            self.label1.setText("Table Name:")
            # Showing the label1.
            self.label1.show()
            # Setting the text of the label 2.
            self.label2.setText("Column Name:")
            # Showing the label2.
            self.label2.show()
            # Showing the text_edit1 
            self.text_edit1.show()
            # Setting the geomerty of the text_edit1
            self.text_edit1.setGeometry(QRect(20, 175, 180, 25))
            # Setting the geomerty of the info_label.
            self.info_label.setGeometry(QRect(20, 200, 180, 75))
            # Setting the geomerty of the magnifier_button.
            self.magnifier_button.setGeometry(QRect(20, 275, 25, 25))
            # Setting the tool tip attribute of the magnifier_button.
            self.magnifier_button.setToolTip("https://www.w3schools.com/mySQl/mysql_alter.asp")
            # Setting the text of the commit_button.
            self.commit_button.setText('Add')
            # Setting the geomerty of the commit button.
            self.commit_button.setGeometry(QRect(65, 275, 90, 25))

        # Checking if the selected operation is equal to "Drop Column"
        elif op == "Drop Column":
            # Resizing the ModifyTheDBDialog window.
            self.resize(220, 320)
            # Setting the text of the label1
            self.label1.setText("Table Name:")
            # Showing the label1.
            self.label1.show()
            # Setting the text of the label2
            self.label2.setText("Column Name:")
            # Showing the label2.
            self.label2.show()
            # Showing the text_edit1
            self.text_edit1.show()
            # Setting the geometry of the text_edit1.
            self.text_edit1.setGeometry(QRect(20, 175, 180, 25))
            # Setting the geomerty of the info_label.
            self.info_label.setGeometry(QRect(20, 200, 180, 75))
            # Setting the geomerty of the magnifier_button.
            self.magnifier_button.setGeometry(QRect(20, 275, 25, 25))
            # Setting the tool tip attribute of the magnifier_button.
            self.magnifier_button.setToolTip("https://www.w3schools.com/mySQl/mysql_alter.asp")
            # Setting the text of the commit_button.
            self.commit_button.setText('Drop')
            # Setting the geomerty of the commit button.
            self.commit_button.setGeometry(QRect(65, 275, 90, 25))

        # Checking if the selected operation is equal to "Modify Column"
        elif op == "Modify Column":
            # Resizing the ModifyTheDBDialog window.
            self.resize(220, 500)
            # Setting the text of the label1
            self.label1.setText("Table Name:")
            # Showing the label1.
            self.label1.show()
            # Setting the text of the label2
            self.label2.setText("Modification Statement:")
            # Showing the label2.
            self.label2.show()
            # Showing the text_edit1
            self.text_edit1.show()
            # Setting the geometry of the text_edit1.
            self.text_edit1.setGeometry(QRect(20, 175, 180, 210))
            # Setting the geomerty of the info_label.
            self.info_label.setGeometry(QRect(20, 385, 180, 75))
            # Setting the geomerty of the magnifier_button.
            self.magnifier_button.setGeometry(QRect(20, 460, 25, 25))
            # Setting the tool tip attribute of the magnifier_button.
            self.magnifier_button.setToolTip("https://www.w3schools.com/mySQl/mysql_alter.asp")
            # Setting the text of the commit_button.
            self.commit_button.setText('Modify')
            # Setting the geomerty of the commit button.
            self.commit_button.setGeometry(QRect(65, 460, 90, 25))


    def open_the_help_page(self):
        """A function which opens the help page in the browser depending on the operation of his/her choice."""
        # Creating a variable called op. Hint: Which the selected operation.
        op = self.select_an_operation_combo_box.currentText()
        # Printing the text value of the combo box.
        debug(f'Opening the help page for: {op}')
        # Checking if op(Selected operation variable) is equal to "Create Table"
        if op == "Create Table":
            # Opening the help page in the web browser.
            wbopen("https://www.w3schools.com/mySQl/mysql_create_table.asp")
        # Checking if op(Selected operation variable) is equal to "Drop Table"
        elif op == "Drop Table":
            # Opening the help page in the web browser.
            wbopen("https://www.w3schools.com/mySQl/mysql_drop_table.asp")
        # Checking if op(Selected operation variable) is equal to "Drop Table"
        elif op == "Add Column":
            # Opening the help page in the web browser.
            wbopen("https://www.w3schools.com/mySQl/mysql_alter.asp")
        # Checking if op(Selected operation variable) is equal to "Drop Column"
        elif op == "Drop Column":
            # Opening the help page in the web browser.
            wbopen("https://www.w3schools.com/mySQl/mysql_alter.asp")
        # Checking if op(Selected operation) is not equal to "Create Table", "Drop Table", "Add Column" or "Drop Column"
        else:
            # Opening the help page in the web browser.
            wbopen("https://www.w3schools.com/mySQl/mysql_alter.asp")


    def commit_changes(self):
        """A function which adds column to a specified table."""
        # Creating a variable called function id. Hint: It's value is equal to the name of the selected operation.
        function_id = self.select_an_operation_combo_box.currentText()

        # Checking if the function_id is equal to "Create Table"
        if function_id == "Create Table":

            # Creating a table name variable from the lineEdit1 widget's text value.
            table_name = self.line_edit1.text()

            # Checking if table_name isn't in list_of_table_names.
            if table_name not in list_of_table_names:

                # Creating a regular expression to validate column specifications
                column_specification_regex = compile(r'^(\w{2,100} \w{2,100}).')

                # Creating column specifications variable fro mthe textEdit1 widget's text value.
                column_specifications = self.text_edit1.toPlainText()

                # Creating a result value from by matching column specifications with the regular expression that you just created.
                result = column_specification_regex.search(column_specifications)

                # Creating a string to hold the mysql command.
                mysql_command = f'CREATE TABLE {table_name} ({column_specifications});'

                # Printing out the mysql command in debug mode.
                debug(f'MySQL Command: {mysql_command}')

                # Making sure that regular expression is matching.
                if result != None:
                    # Trying to create cursor and execute the mysql commands.
                    try:
                        # Creating mysql cursor to a create table
                        mysql_create_table_cursor = mysql_database_connection.cursor()

                        # Executing the mysql command.
                        mysql_create_table_cursor.execute(mysql_command)

                        # Clearing the text area of line_edit1 widget
                        self.line_edit1.setText("")

                        # Clearing the text area of text_edit1 widget
                        self.text_edit1.setText("")

                        # Setting the style sheet of the info_label widget
                        self.info_label.setStyleSheet(u"#info_label {color: lightgreen;}")

                        # Setting the text value of the info_label widget.
                        self.info_label.setText(f'Table {table_name} has been created.')

                    # Setting set of instructions for exceptional case where application fails to execute the mysql code.
                    except:
                        # Seting the style sheet of the info_label
                        self.info_label.setStyleSheet(u"#info_label {color: lightgreen;}")
                        # Setting the text value of the info_label as it will going to show a warning message.
                        self.info_label.setText("You don't have the required permissions.")

                # Setting the style sheet and the text value of the info_label widget as it will going to show the warning in red color.
                else:
                    self.info_label.setStyleSheet(u"#info_label {color: red;}")
                    self.info_label.setText("Wrong columns' specifications statement!")

            # Setting the style sheet and the text value of the info_label widget as it will going to show the warning in red color.
            else:
                self.info_label.setStyleSheet(u"#info_label {color: red;}")
                self.info_label.setText(f'Table {table_name} is already exists!')

        # Checking if the function_id is equal to "Drop Table"
        elif function_id == "Drop Table":

            # Creating a variable called table_name from the line_edit1 widgets text input.
            table_name = self.line_edit1.text()

            # Checking if the table_name is in the list_of_table_names.
            if table_name in list_of_table_names:

                # Creating a sql command.
                mysql_command = f'DROP TABLE IF EXISTS {table_name};'

                # Printing out the mysql command in debug mode.
                debug(f'MySQL Command: {mysql_command}')

                # Tring to execute the code which is inside the try block.
                try:
                    # Creating a cursor to drop the table.
                    mysql_drop_table_cursor = mysql_database_connection.cursor()
                    # Executing the mysql command
                    mysql_drop_table_cursor.execute(mysql_command)
                    # Setting the line_edit1 widget's text value to an empty string.
                    self.line_edit1.setText("")
                    # Setting the style sheet of the info_label
                    self.info_label.setStyleSheet(u"#info_label {color: lightgreen;}")
                    # Setting the text value of the info_label.
                    self.info_label.setText(f'Table {table_name} successfully deleted.')

                # Instruction computer about what to do if the application fails to execute the code which is inside the try block.
                except:
                    # Setting the style sheet of the info_label
                    self.info_label.setStyleSheet(u"#info_label {color: red;}")
                    # Setting the text value of the info_label.
                    self.info_label.setText("You don't have the required permissions.")

            # Checking if the table_name is not in the list of table names.
            else:
                self.info_label.setStyleSheet(u"#info_label {color: red;}")
                self.info_label.setText(f'Table {table_name} not found!')

        # Checking the function id is equal to "Add Column"
        elif function_id == "Add Column":
            # Creating a varaible called table name from the line_edit1 widget's text input.
            table_name = self.line_edit1.text()

            # Checking if the table_name is in the list_of_table_names.
            if table_name in list_of_table_names:

                # Creating a simple regular expression to validate the column specification statement.
                column_specification_regex = compile(r'^(\w{2,100} \w{2,100}).')

                # Creating a column specification variable from the text value of the text_edit1 widget
                column_specifications = self.text_edit1.toPlainText()

                # Creating a result variable from the regex's match.
                result = column_specification_regex.search(column_specifications)

                # Creating a mysql command.
                mysql_command = f'ALTER TABLE {table_name} ADD {column_specifications};'

                # Printing the mysql command in debug mode.
                debug(f'MySQL Command: {mysql_command}')

                # Checking if the user entered a valid column_specifications value.
                if result != None:

                    # Tring to execute the code which is inside the try block.
                    try:
                        # Creating a cursor to add a column.
                        mysql_add_column_cursor = mysql_database_connection.cursor()
                        # Executing the mysql_command.
                        mysql_add_column_cursor.execute(mysql_command)
                        # Setting the text_edit1 widget's text value to an empty string.
                        self.text_edit1.setText("")
                        # Setting the style sheet of the info_label
                        self.info_label.setStyleSheet(u"#info_label {color: lightgreen;}")
                        # Setting the text value of the info_label.
                        self.info_label.setText(f'Column has been added to {table_name}.')

                    # Instructing the computer about what to do if the application fails to execute the code which is inside the try block.
                    except:
                        # Setting the style sheet of the info label.
                        self.info_label.setStyleSheet(u"#info_label {color: red;}")
                        # Setting the text of the info_label.
                        self.info_label.setText("You don't have the required permissions!")

                # Checking if the user didn't entered a valid columns_specifications value.
                else:
                    # Setting the style sheet of the info label.
                    self.info_label.setStyleSheet(u"#info_label {color: red;}")
                    # Setting the text of the info_label.
                    self.info_label.setText("Wrong column specification statement!")

            # Checking if the table name is not in the list_of_table_names.
            else:
                # Setting the style sheet of the info label.
                self.info_label.setStyleSheet(u"#info_label {color: red;}")
                # Setting the text of the info_label.
                self.info_label.setText(f'Table {table_name} not found!')

        # Checking if the function_id is equal to "Drop Column".
        elif function_id == "Drop Column":

            # Creating table name variable from the lineEdit1 widget's text value.
            table_name = self.line_edit1.text()

            # Checking if the table_name is in the list_of_table_names.
            if table_name in list_of_table_names:

                return_list_of_column_names(table_name)

                # Creating a variable called the_column_name from the text_edit1 widget's text value
                the_column_name = self.text_edit1.toPlainText()

                # Checing if the column name which the user is entered is in the return_list_of_column_names(table_name)
                if the_column_name in return_list_of_column_names(table_name):
                    
                    # Checking if the table only has 1 column. Hint: You can't drop the column if the table only has 1 column.
                    if len(return_list_of_column_names(table_name)) == 1:
                         # Setting the text of the text_edit1 widget to an empty string.
                        self.text_edit1.setText("")
                        # Setting the style sheet of the info_label.
                        self.info_label.setStyleSheet(u"#info_label {color: lightgreen;}")
                        # Setting the text of the info_label.
                        self.info_label.setText(f'Table only has 1 column. Try to drop the table instead.')

                    # Checking if the column has more than 1 column. Hint: A table cannot be exists with a column.
                    else:
                        # Trying to execute the instructions located inside the try block and handling the errors with the except block.
                        try:
                            # Creating a mysql command to the drop a column
                            mysql_command2 = f'ALTER TABLE {table_name} DROP COLUMN {the_column_name};'
                            # Printing the sql command in debug mode.
                            debug(f'MySQL Command: {mysql_command2}')
                            # Creating a cursor to drop the column
                            mysql_drop_column_cursor = mysql_database_connection.cursor()
                            # Executing the mysql command.
                            mysql_drop_column_cursor.execute(mysql_command2)
                            # Setting the text of the text_edit1 widget to an empty string.
                            self.text_edit1.setText("")
                            # Setting the style sheet of the info_label.
                            self.info_label.setStyleSheet(u"#info_label {color: lightgreen;}")
                            # Setting the text of the info_label.
                            self.info_label.setText(f'Column {the_column_name} has been deleted from {table_name}.')

                        # Instructing the computer about what to do if it fails to execute the code which is inside the try block.
                        except:
                            # Setting the style sheet of the info_label
                            self.info_label.setStyleSheet(u"#info_label {color: red;}")
                            # Setting the text of the info_label.
                            self.info_label.setText("You don't have the required permissions!")

                # Checking if the column_name is in the return_list_of_column_names(table_name)
                else:
                    # Setting the style sheet the info_label widget.
                    self.info_label.setStyleSheet(u"#info_label {color: red;}")
                    # Setting the text of the info_label.
                    self.info_label.setText("Column not found!")

            # Checking if the table_name is not in the list_of_the_table_names.
            else:
                # Setting the style sheet the info_label widget.
                self.info_label.setStyleSheet(u"#info_label {color: red;}")
                # Setting the text of the info_label.
                self.info_label.setText("Table not found!")

        # Checking the function id
        elif function_id == "Modify Column":
            # Creating a variable called table name which is equal to the the line_edit1 widget's text input.
            table_name = self.line_edit1.text()

            # Checking if the table_name is in the list_of_table_names.
            if table_name in list_of_table_names:

                # Creating a variable called column_specifications which is equal to the text input of the text_edit1 widget
                column_specifications = self.text_edit1.toPlainText()

                # Creating a variable called column name variable from the text_edit widget's text value's first part.
                the_column_name = str(column_specifications.split(" ")[0])

                # Checking if the_column_name is in the return_list_of_column_names(table_name).
                if the_column_name in return_list_of_column_names(table_name):

                    # Creating a mysql command to modify the column
                    mysql_command2 = f'ALTER TABLE {table_name} MODIFY COLUMN {column_specifications};'

                    # Printing the mysql command in debug mode.
                    debug(f'MySQL Command: {mysql_command2}')

                    # Trying to execute the which is inside the try block.
                    try:
                        # Creating a cursor to modify the column.
                        mysql_modify_column_cursor = mysql_database_connection.cursor()
                        # Executing the mysql command.
                        mysql_modify_column_cursor.execute(mysql_command2)
                        # Setting text_edit1 widget's text to empty string.
                        self.text_edit1.setText("")
                        # Setting the style s
                        # heet of the info_label.
                        self.info_label.setStyleSheet(u"#info_label {color: lightgreen;}")
                        # Setting the info_label widget's text.
                        self.info_label.setText(f'Column {the_column_name} has been modified.')

                    # Intructing computer about what to do if the code fails to execute the code which is inside the try block.
                    except:
                        # Setting the style sheet of the info_label.
                        self.info_label.setStyleSheet(u"#info_label {color: red;}")
                        # Setting the info_label widget's text.
                        self.info_label.setText("You don't have the required permissions!")

                # Checking if the column_name is not in the return_list_of_column_names(table_name)
                else:
                    # Setting the style sheet of the info_label.
                    self.info_label.setStyleSheet(u"#info_label {color: red;}")
                    # Setting the info_label widget's text.
                    self.info_label.setText("Column not found!")

            # Checking if the table_name is not in the list_of_table_names
            else:
                # Setting the style sheet of the info_label.
                self.info_label.setStyleSheet(u"#info_label {color: red;}")
                # Setting the info_label widget's text.
                self.info_label.setText("Table not found!")

# Self contained QDialog class.
class ModifyTheDataDialog(QDialog, Ui_ModifyTheDataDialog):
    # Initialize the window to make it self contained.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loading the GUI
        self.setupUi(self)

        # Creating a global variable called listOfLineEdit
        global list_of_line_edits

        # Initializing the listOfLineEdit variable with an empty numpy array.
        list_of_line_edits = array([])

        # Creating the label which writes the "Row Index:"
        self.row_label = QLabel('Row Number:')

        # Creating a spin box
        self.row_spin_box = QSpinBox()

        # Setting a range to the spin box widget
        self.row_spin_box.setRange(1, len(list_of_row_indexes)+1)

        # Connecting the spinbox widget with the update_the_form function as the function will going to trigger with a value change signal.
        self.row_spin_box.valueChanged.connect(self.update_the_form)

        # Connecting the save changes button with the change_the_data function as the function will going to trigger with a pressed signal.
        self.save_changes_button.pressed.connect(self.change_the_data)

        # Adding the first row to the form layout
        self.data_form_layout.addRow(self.row_label, self.row_spin_box)

        # Connecting the deleteRow function with the deleteBtn as the function will going to trigger with a press signal.
        self.delete_button.pressed.connect(self.delete_row)

        # Looping through each in column in list of columns creating a label and a line edit widget inside a row.
        for c in list_of_columns:
            self.data_line_edit_widget = QLineEdit()
            self.data_line_edit_widget.setObjectName(u"{col}_line_edit_widget".format(col=c))
            self.data_label = QLabel(f'{c}:')
            list_of_line_edits = npappend(list_of_line_edits, self.data_line_edit_widget)
            self.data_form_layout.addRow(self.data_label, self.data_line_edit_widget)

        global row_index
        row_index = 0
        global temporary_var
        temporary_var = array([])

        # Setting the form widgets' text for initial display.
        try:
            for n in range(len(list_of_line_edits)):
                list_of_line_edits[n].setText(str(list_of_selected_table_data[row_index][n]))
                temporary_var = npappend(temporary_var, list_of_line_edits[n].text())
                debug(f'{list_of_line_edits[n]}')

        except:
            self.save_changes_button.setText("Create")

    def update_the_form(self, i):
        """A function which updates the form fields' values every time the id lineEdit field's values changes"""
        # Creating a globaL row index variable
        global row_index
        # Initializing the row_index variable 
        row_index = i - 1

        # Printing the row index in debug mode.
        debug(f'Row Index = {row_index}')
        # Creating a global temporary_var
        global temporary_var
        # Initializing the temporary_var
        temporary_var = array([])

        # Iterating in range of the total number of line edit widgets
        for n in range(len(list_of_line_edits)):
            # Trying of setting every single line edit widget's text value in the form.
            try:
                main_window = MainWindow()
                main_window.load_the_selected_table_view()
                debug(str(list_of_selected_table_data[row_index][n]))
                list_of_line_edits[n].setText(str(list_of_selected_table_data[row_index][n]))
                temporary_var = npappend(temporary_var, list_of_line_edits[n].text())
                # Setting the text value of the save changes button
                self.save_changes_button.setText("Save Changes")

            # Instructing the application about what to do if the application fails to set text value of every single line edit widget in the form. That means row is out of index. And, user is trying to insert a row.
            except:
                main_window = MainWindow()
                main_window.load_the_selected_table_view()
                # Setting the line edit widgets' texts to empty strings
                list_of_line_edits[n].setText("")
                # Changing the saveChangesBtn's text to "Create"
                self.save_changes_button.setText("Create")

        debug(f'Temporary Values = {temporary_var}')


    def change_the_data(self):
        """A function which writes the new data/changes in to the database."""
        # Checking if the save_changes_button's text is "Create"
        if self.save_changes_button.text() == "Create":
            # Creating a variable called operation_id and setting it's value to "Insert"
            operation_id = "Insert"
        # Checking if the save_changes_button's text is not "Create"
        else:
            # Creating a variable called operation_id and setting it's value to "Update"
            operation_id = "Update"

        # Checking if the operation_id is equal to "Insert"
        if operation_id == "Insert":
            # Printing the operation id in debug mode.
            debug(f'Operation ID: {operation_id}')

            # Creating a empty array to store list of values.
            list_of_values = array([ list_of_line_edits[n].text() for n in range(len(list_of_line_edits)) ])

            # Creating a tuple from the list of values.
            tuple_of_values = tuple(list_of_values)

            # Creating a mysql command string
            mysql_command = f'INSERT INTO {selected_table_name} VALUES {tuple_of_values};'

            # Printing the mysql command in debug mode.
            debug(f'MySQL Command: {mysql_command}')

            # Trying to execute instructions below.
            try:
                # Creating a cursor to create a new row code
                mysql_insert_cursor = mysql_database_connection.cursor()

                # Executing the sql command
                mysql_insert_cursor.execute(mysql_command)

                # Commiting the changes
                mysql_database_connection.commit()

                # Setting the style sheet and text value of the info label.
                self.info_label.setStyleSheet(u"#info_label {color: lightgreen;}")
                self.info_label.setText(f'Row {row_index+1} has been created.')
                
                # Reloading the data in the main window.
                main_window = MainWindow()
                main_window.load_the_selected_table_view()

            # Instructing the computer, about what to do, if the application fails to execute instructions in the try block.
            except:
                # Displaying warning message in red color if the code fails to execute the mysql command.
                self.info_label.setStyleSheet(u"#info_label {color: red;}")
                self.info_label.setText("You don't have the required permissions!")

        # Checking the operation_id is equal to "Update"
        elif operation_id == "Update":
            # Creating a dictionary to store the values that are already exists in the initial instance of the row
            same_values_dictionary = {}
            # Creating a dictionary to store the values that are not exists in the initial instance of the row.
            new_values_dictionary = {}

            # Storing each line edit widget's value in the form to the list of values list.
            list_of_values = array([ list_of_line_edits[n].text() for n in range(len(list_of_line_edits)) ])

            # Looping through each column in the list of columns and looping through each value in teh list of values.
            for c, v in zip(list_of_columns, list_of_values):
                # Checking if the value is in the temporary_var list
                if v in temporary_var:
                    # Creating a key value pair the same_values_dictionary
                    same_values_dictionary[c] = v
                else:
                    # Creating a key value pair the new_values_dictionary
                    new_values_dictionary[c] = v

            # Printing the temporary_var list in debug mode.
            debug(f'Temporary Values = {temporary_var}')
            # Printing the same_values_dictionary in debug mode.
            debug(f'Same values: {same_values_dictionary}')
            # Printing the new_values_dictionary in debug mode.
            debug(f'New values: {new_values_dictionary}')

            # Creating an empty string caled conditional_string
            conditional_string = ''

            # Looping through each key and value in the same_values_dictionary
            for k,v in same_values_dictionary.items():
                # Checking if the value is not equal to None, "None" or "NULL"
                if v != None or v != 'None' or v != 'NULL':
                    debug(f'Key: {k} - Value: {v}')
                    conditional_string += f'{k} = \'{v}\' and '

            # Trimming the conditional_string
            conditional_string = conditional_string[0:-5]
            # Printing the conditional_string in debug mode.
            debug(f'Conditional String: {conditional_string}')
            
            # Looping through each permission the list_of_user_permissions.
            # Note Try to update the row for each and every new value. And when every it fails change the color of the line edit widget's border to red.
            for tp in list_of_user_permissions:
                # Checking if the permission statement is giving required permissions to the user to update the table.
                if 'UPDATE' in tp and f'`{database}`.*' in tp and f'`{host}`' in tp or 'UPDATE' in tp and f'`{database}`.`{selected_table_name}`' in tp and f'`{host}`' in tp  or 'ALL' in tp and f'`{database}`.*' in tp and f'`{host}`' in tp or 'ALL' in tp and f'`{database}`.`{selected_table_name}`' in tp and f'`{host}`' in tp:
                    # Setting the "UPDATE" key's value to True
                    mysql_permissions_dictionary['UPDATE'] = True

            # Checking if the UPDATE key's value is equal to True.
            if mysql_permissions_dictionary['UPDATE'] == True:
                # Looping through each key and value in the new_values_dictionary.
                for k, v in new_values_dictionary.items():
                    # Creating a string variable called column_values_string.
                    column_values_string = f'{k} = \'{v}\''
                    # Creating a mysql command string
                    mysql_command = f'UPDATE {selected_table_name} SET {column_values_string} WHERE {conditional_string};'
                    # Printing the mysql command string in debug mode.
                    debug(f'MySQL Command: {mysql_command}')
                    # Creating a QMessageBox widget
                    self.confirmation_dialog = QMessageBox()
                    # Setting the Message box's title
                    self.confirmation_dialog.setWindowTitle("Do you confirm your changes?")
                    # Setting the text of the message box.
                    self.confirmation_dialog.setText(mysql_command)
                    # Adding the a cancel button and a yes button to the message box
                    self.confirmation_dialog.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
                    # Adding an icon to the message box.
                    self.confirmation_dialog.setIcon(QMessageBox.Question)
                    # Showing the message box.
                    answer = self.confirmation_dialog.exec_()
                    # Creating a variable called column index.
                    col_index = -1

                    # Looping through each column in the list of columns.
                    for c in list_of_columns:
                        # Increasing the col_index's value by 1
                        col_index += 1
                        # Printing the column name in debug mode.
                        debug(f'Column Name: {c}')
                        # Checking if column's name is equal to the key 
                        if c == k:
                            # Breaking the loop
                            break
                    
                    # Checking if the user clicked to the yes button on the message box.
                    if answer == QMessageBox.Yes:
                        # Trying to execute the code inside try block.
                        try:
                            # Creating a cursor update the row 
                            mysql_update_cursor = mysql_database_connection.cursor()
                            # Executing the mysql command.
                            mysql_update_cursor.execute(mysql_command)
                            # Committing the changes.
                            mysql_database_connection.commit()
                            # Setting the style sheet of the line edit.
                            list_of_line_edits[col_index].setStyleSheet("")
                            # Setting the style sheet of the info_label.
                            self.info_label.setStyleSheet(u"#info_label {color: lightgreen;}")
                            # Setting the info label's text.
                            self.info_label.setText(f'Row {row_index+1} has been updated.')
                            # Reloadingthe seleted table view.
                            main_window = MainWindow()
                            main_window.load_the_selected_table_view()

                        except:
                            list_of_line_edits[col_index].setStyleSheet(u"#{col}line_edit_widget {{border: 2px solid red;}}".format(col=c))
                    
                    # Checking if the user didn't clicked to the Yes button.
                    else:
                        # Breaking the loop.
                        break

            # Checking if the user doesn't have the required permissions.
            else:
                # Setting the style sheet of the info_label
                self.info_label.setStyleSheet(u"#info_label {color: red;}")
                # Setting the info_label's text.
                self.info_label.setText("You don't have the required permissions!")

    def delete_row(self):
        """A function which deletes the row."""
        # Creating a dictionary to store the values that are already exists in the initial instance of the row
        same_values_dictionary = {}
        # Creating a dictionary to store the values that are not exists in the initial instance of the row.
        new_values_dictionary = {}
        # Creating an empty string to store the list of values
        list_of_values = array([ list_of_line_edits[n].text() for n in range(len(list_of_line_edits)) ])

        # Looping through each column in list of columns and for each value in list of values. 
        for c, v in zip(list_of_columns, list_of_values):
            # Checking if the value is in the temporary_var list.
            if v in temporary_var:
                # Creating a key value pair the the same_values_dictionary.
                same_values_dictionary[c] = v
            # Checking if the value is not in the temporary_var list.
            else:
                # Creating a key value pair in the new values dictionary.
                new_values_dictionary[c] = v

        # Printing the temporary_var list in debug mode.
        debug(f'Temporary Values = {temporary_var}')
        # Printing the list of values list in debug mode.
        debug(f'List of values: {list_of_values}')
        # Printing the new_values_dictioanry in debug mode.
        debug(f'New values: {new_values_dictionary}')

        # Creating a variable called conditional string.
        conditional_string = ''

        # Looping through each key and value in the same_values_dictionary.
        for k,v in same_values_dictionary.items():
            # Checking if the value is equal to None, "None" or "NULL" 
            if v != None or v != 'None' or v != 'NULL':
                # Printiing the key-value pair in debug mode.
                debug(f'Key: {k} - Value: {v}')
                # Creating a new conditional string by concatenating other sub strings. 
                conditional_string += f'{k} = \'{v}\' and '

        # Trimming the conditional_string
        conditional_string = conditional_string[0:-5]
        # Printing the conditional string in debug mode.
        debug(f'Conditional String: {conditional_string}')

        # Note Try to update the row for each and every new value. And when every it fails change the color of the line edit widget's border to red.
        # Looping through each permission statement in the list_of_user_permissions 
        for tp in list_of_user_permissions:
            # Checking if the user has the required permissions.
            if 'DELETE' in tp and f'`{database}`.*' in tp and f'`{host}`' in tp or 'DELETE' in tp and f'`{database}`.`{selected_table_name}`' in tp and f'`{host}`' in tp  or 'ALL' in tp and f'`{database}`.*' in tp and f'`{host}`' in tp or 'ALL' in tp and f'`{database}`.`{selected_table_name}`' in tp and f'`{host}`' in tp:
                # Seeting the "DELETE" key's value to True
                mysql_permissions_dictionary['DELETE'] = True

        # Checking if the "DELETE" key's value is equal to True.
        if mysql_permissions_dictionary['DELETE'] == True:
            # Creaing a mysql command to delete the row.
            mysql_command = f'DELETE FROM {selected_table_name} WHERE {conditional_string};'
            # Printing the mysql_command in debug mode.
            debug(f'MySQL Command: {mysql_command}')
            # Creating a message box.
            self.confirmationDialog = QMessageBox()
            # Setting the message box's title
            self.confirmationDialog.setWindowTitle("Do you confirm the statement below?")
            # Setting the message box's text.
            self.confirmationDialog.setText(mysql_command)
            # Adding Cancel and Yes buttons to the message box.
            self.confirmationDialog.setStandardButtons(QMessageBox.Cancel | QMessageBox.Yes)
            # Adding icon to the message box.
            self.confirmationDialog.setIcon(QMessageBox.Question)
            # Showing the message box.
            answer = self.confirmationDialog.exec_()
            # Creating a variable called column_index.
            column_index = -1

            # Checking if the user pressed to the yes button.
            if answer == QMessageBox.Yes:
                # Trying to execute all the code inside try block
                try:
                    # Creating a cursor to delete the row.
                    mysql_delete_row_cursor = mysql_database_connection.cursor()
                    # Executing the mysql command.
                    mysql_delete_row_cursor.execute(mysql_command)
                    # Commiting the changes.
                    mysql_database_connection.commit()
                    # Setting the style sheet of the info_label object
                    self.info_label.setStyleSheet(u"#info_label {color: lightgreen;}")
                    # Setting the text of the info_label
                    self.info_label.setText(f'Row {row_index+1} has been deleted.')
                    # Reloading the selected table view.
                    main_window = MainWindow()
                    main_window.load_list_of_tables_view()

                # Instructing the computer about what to do if the application fails to execute all the code inside the try block.
                except:
                    # Setting the style sheet of the info_label widget.
                    self.info_label.setStyleSheet(u"#info_label {color: red;}")
                    # Setting the text of the info_label widget.
                    self.info_label.setText("Something went wrong contact with your administrator!")

        # Checking if the user doesn't have the required permissions.
        else:
            # Setting the info_label widget's style sheet.
            self.info_label.setStyleSheet(u"#info_label {color: red;}")
            # Setting the text of the info_label.
            self.info_label.setText("You don't have the required permissions!")
 
# Self contained main window class.
class MainWindow(QMainWindow, Ui_MainWindow):
    # Initialize the main window to make it self contained.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Load the GUI
        self.setupUi(self)

        # Loading the list of tables data model's data
        self.load_list_of_tables_view()

        # Setting the username label's text.
        self.username_label.setText(user)

        # Connecting the list view widget with the display_the_selected_table function as it will trigger with a clicked signal
        self.list_of_tables_view.clicked.connect(self.display_the_selected_table)

        # Connecting the show_user_permissions_dialog function with the show_permissions_action_button
        self.show_permissions_action_button.triggered.connect(self.show_user_permissions_dialog)

        # Connecting the show_modify_database_dialog function with the modify_the_database_button as the function will going to trigger with a press signal.
        self.modify_the_database_button.pressed.connect(self.show_modify_database_dialog)

        # Connecting the show_password_changing_dialog function with the change_password_action_button action button as the function will trigger with a trigger signal.
        self.change_password_action_button.triggered.connect(self.show_password_changing_dialog)

        # Connecting the show_credits_dialog function with the credits_action_button button as the function will trigger with a trigger signal.
        self.credits_action_button.triggered.connect(self.show_credits_dialog)

        # Connecting the open control the data dialog function with the modify_the_database_button
        self.modify_the_data_button.pressed.connect(self.show_modify_the_data_dialog)

        # Creating the selected table view's sorting filter
        self.selected_table_view_proxy_model = QSortFilterProxyModel()

        # Connecting the selected_table_data_filter line edit with the self.selected_table_view_proxy_model.setFilterFixedString function as the function will going to trigger with a text change signal.
        self.selected_table_data_filter.textChanged.connect(self.selected_table_view_proxy_model.setFilterFixedString)

        # Connecting the list_of_tables_filter with the self.list_of_tables_view_proxy_model.setFilterFixedString function as the function will going to trigger with a text change signal.
        self.list_of_tables_filter.textChanged.connect(self.list_of_tables_view_proxy_model.setFilterFixedString)

        # creating a cursor to show grants
        mysql_show_grants_cursor = mysql_database_connection.cursor()

        # Executing show grants sql command using python
        mysql_show_grants_cursor.execute(f'SHOW GRANTS FOR {user}@"%";')

        # Fetching all the data which is generated with the cursor execution
        global list_of_user_permissions
        
        list_of_user_permissions = [ str(permission[0]) for permission in mysql_show_grants_cursor.fetchall() ]

        # Creating global dictionary for all of the mysql permissons in the euler database manager.
        global mysql_permissions_dictionary

        mysql_permissions_dictionary = {
            # List of all permissions with explanations -> https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#priv_insert
            ## All permission -> These privilege specifiers are shorthand for “all privileges available at a given privilege level” (except GRANT OPTION).
            'ALL': False,
            ## Create role permission -> Similar to create user but you can only use to create user accounts.
            'CREATE ROLE': False,
            ## Create User Permission -> Enables use of the ALTER USER, CREATE ROLE, CREATE USER, DROP ROLE, DROP USER, RENAME USER, and REVOKE ALL PRIVILEGES statements.
            'CREATE USER': False,
            ## Drop role permissions -> Similar to drop but you can only use it delete user accounts.
            'DROP ROLE': False,
            ## Select User Permission -> Required permission to display user accounts. This is a select permission on mysql.user table.
            'select_user_permission': False,
            ## Alter table permission -> Enables use of the ALTER TABLE statement to change the structure of tables. ALTER TABLE also requires the CREATE and INSERT privileges. Renaming a table requires ALTER and DROP on the old table, CREATE, and INSERT on the new table.
            'ALTER': False,
            ## Create table permission -> Enables use of statements that create new databases and tables.
            'CREATE': False,
            ## Drop permission -> Enables use of statements that drop (remove) existing databases, tables, and views. The DROP privilege is required to use the ALTER TABLE ... DROP PARTITION statement on a partitioned table. The DROP privilege is also required for TRUNCATE TABLE.
            'DROP': False,
            ## Grant option permission -> Enables you to grant to or revoke from other users those privileges that you yourself possess.
            'GRANT OPTION': False,
            ## Index permission -> to create data structures that imporves the speed of operations in a table.
            'INDEX': False,
            ## Insert permission -> Enables rows to be inserted into tables in a database. INSERT is also required for the ANALYZE TABLE, OPTIMIZE TABLE, and REPAIR TABLE table-maintenance statements.
            'INSERT': False,
            ## References permission -> Creation of a foreign key constraint requires the REFERENCES privilege for the parent table.
            'REFERENCES': False,
            ## Select permission -> Enables rows to be selected from tables in a database. SELECT statements require the SELECT privilege only if they actually access tables. Some SELECT statements do not access tables and can be executed without permission for any database.
            'SELECT': False,
            ## Update permission -> Enables rows to be updated in tables in a database.
            'UPDATE': False,
            ## Delete table permission -> Enables rows to be deleted from tables in a database.
            'DELETE': False,
        }

        # Creating a global variable called mysql_permissions_key_str8ings
        global mysql_permissions_keys_string
        # Creating an object called list_of_mysql_permission_keys from the mysql_permissions_dictionary's keys.
        list_of_mysql_permission_keys = list(mysql_permissions_dictionary.keys())
        # Removing the select_user_permission key value pair from the dictionary.
        list_of_mysql_permission_keys.remove('select_user_permission')
        # Creating a string from by joining each key in the list_of_mysql_permissions_keys with to one another wtih a '|'  
        mysql_permissions_keys_string = '|'.join(list_of_mysql_permission_keys)

        # Looping through each permission in the list of the user's permissions
        for tp in list_of_user_permissions:
            # Checking if the user has the select permission on mysql.user or if the user has all permissions on mysql.user table
            if 'SELECT' in tp and 'mysql' in tp and 'user' in tp or 'ALL' in tp and 'mysql' in tp and 'user' in tp:
                mysql_permissions_dictionary['select_user_permission'] = True


        # Checking if the user has the selectUserPerm(select permission on mysql.user)
        if mysql_permissions_dictionary['select_user_permission'] != True:
            self.account_control_button.setDisabled(False)

        # Checking if the user doesn't have the 
        else:
            # Connecting show_account_control_dialog function with the account_control_button as the function will going to trigger with a press signal.
            self.account_control_button.pressed.connect(self.show_account_control_dialog)

    def show_modify_database_dialog(self):
        """A function which shows the modify the database dialog."""
        dialog = ModifyTheDBDialog()
        dialog.exec_()

    def show_password_changing_dialog(self):
        """A function which opens the password changing window."""
        dialog = PasswordChangingDialog(self)
        dialog.exec_()

    def show_credits_dialog(self):
        """A function which opens the credits dialog"""
        dialog = CreditsDialog(self)
        dialog.exec_()

    # Creating a contex menu.
    def contextMenuEvent(self, e): # Hint: In order to create a context menu, using this name is mandatory.
        self.context_menu = QMenu()
        self.refresh_button = QAction("Refresh")
        self.refresh_button.triggered.connect(self.refresh_the_views)
        self.context_menu.addAction(self.refresh_button)
        self.context_menu.exec_(e.globalPos())

    def refresh_the_views(self):
        """A function which refreshes the list and table views in the main window."""
        # Reloading the list of tables view.
        self.load_list_of_tables_view()

        # Creating a variable to validate if the user selected a table from the list of tables list view.
        table_selection_status = False

        # Validating if selecteTableName variable is defined or not.
        try:
            selected_table_name
            # Setting the status to True if the variable is defined.
            table_selection_status = True

        except NameError:
            debug("Name Error: \"selected_table_name\" variable isn't defined")

        else:
            debug("Variable is defined.")
            table_selection_status = True

        if table_selection_status == True:
            # Reloading the selected table.
            self.load_the_selected_table_view()

    def show_modify_the_data_dialog(self):
        """A function which opens the modify the data dialog window."""
        # Creating a variable to validate if the user selected a table from the list of tables list view.
        table_selection_status = False

        # Validating if selecteTableName variable is defined or not.
        try:
            selected_table_name
            debug(f'Selected Table: {selected_table_name}')
            # Setting the status to True if the variable is defined.
            table_selection_status = True

        except NameError:
            debug("Name Error: \"selected_table_name\" variable isn't defined")

        if table_selection_status == True:
            modify_the_data_dialog = ModifyTheDataDialog()
            modify_the_data_dialog.exec_()
        else:
            self.warning_label.setText("You must select a table first!")


    def show_user_permissions_dialog(self):
        """A function which opens the permissions dialog window"""
        permissions_dialog = PermissionsDialog(self)
        permissions_dialog.exec_()

    def show_account_control_dialog(self):
        """A function which opens the control user accounts dialog window"""
        account_control_dialog = ControlUserAccsDialog()
        account_control_dialog.exec_()

    def load_the_selected_table_view(self):
        """A function which loads the selected table."""
        # Creating a cursor to get all the data from the selecting
        mysql_selected_table_data_cursor = mysql_database_connection.cursor()

        # Executing select sql command using python
        mysql_selected_table_data_cursor.execute(f'SELECT * FROM {selected_table_name}')

        # Fetching all the selected_table_data
        selected_table_data = mysql_selected_table_data_cursor.fetchall()

        # Organize the list of columns
        global list_of_columns
        list_of_columns = return_list_of_column_names(selected_table_name)

        # Creating a global variable
        global list_of_row_indexes
        # Initializing the list_of_row_indexes
        list_of_row_indexes = [ int(row_num) for row_num in range(1, len(selected_table_data)+1) ]

        # Creating a global variable called list_of_selected_table_data
        global list_of_selected_table_data
        list_of_selected_table_data = []

        # Looping through each of in the list_of_selected_table_data
        for row in selected_table_data:
            # Creating an empty list called list_of_row_data
            list_of_row_data = []
            # Appending the row data to the list_of_selected_table_data  
            list_of_selected_table_data.append(list_of_row_data)

            # Looping through each column in the row
            for col in row:
                # Appending the column data to the list_of_row_data 
                list_of_row_data.append(col)

        # Creating the selected table's result datas using pandas module
        selected_table_data_frame = pd.DataFrame(selected_table_data,columns=list_of_columns,index=list_of_row_indexes,)

        # Create a model for the table view widget
        self.selected_table_data_model = SelectedTableDataModel(selected_table_data_frame)

        # Setting the source model of the selected table view's proxy model
        self.selected_table_view_proxy_model.setSourceModel(self.selected_table_data_model)

        # Setting the filter as it will going to filter all columns
        self.selected_table_view_proxy_model.setFilterKeyColumn(-1)  # all columns

        # Setting the selected table view's model using selected table view's proxy model
        self.selected_table_view.setModel(self.selected_table_view_proxy_model)

    def load_list_of_tables_view(self):
        """A function which loads the list of tables list view widget's data."""
        # Create a mysql initial connection cursor to execute sql commands
        mysql_initial_connection_cursor = mysql_database_connection.cursor()

        # Execute show tables sql command using python
        mysql_initial_connection_cursor.execute("SHOW TABLES")

        # Put all the data to listOfTables variable
        global list_of_table_names
        list_of_table_names = [ str(table_name[0]) for table_name in mysql_initial_connection_cursor.fetchall()]

        # Initalizing the list of tables data model's data.
        self.list_of_tables_data_model = DataModelFLV(list_of_table_names)

        # Creating the list of table's data model
        self.list_of_tables_view_proxy_model = QSortFilterProxyModel()

        # Setting the source model of the selected table view's proxy model
        self.list_of_tables_view_proxy_model.setSourceModel(self.list_of_tables_data_model)

        # Setting the filter as it will going to filter all columns
        self.list_of_tables_view_proxy_model.setFilterKeyColumn(-1)  # all columns

        # Setting the selected table view's model using selected table view's proxy model
        self.list_of_tables_view.setModel(self.list_of_tables_view_proxy_model)

    def display_the_selected_table(self):
        """A function which displays the selected table in the table view widget"""
        indexes = self.list_of_tables_view.selectedIndexes()
        if indexes:
            # Indexes is a single-item list in single-select mode.
            index = indexes[0]
            global selected_table_name
            selected_table_name = self.list_of_tables_data_model.list_of_all_tables[index.row()]

        self.load_the_selected_table_view()


# Self contained login window class.
class LogInWindow(QMainWindow, Ui_LogInWindow):
    # Initializing the window to make it self contained.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loading the GUI
        self.setupUi(self)
        # Connecting the log_in function with the log_in_button as the function  will going to trigger with a press signal.
        self.log_in_button.pressed.connect(self.log_in)

    def log_in(self):
        """A function which logs in to the database"""

        # Creating a global variables called mysql_database_connection
        global mysql_database_connection

        # Creating a variable identify if the connection is succesful.
        connection_status = False

        # Try to connect to the database, except errors and if code fails set the connectionStatus to False
        try:
            # Creating the global variables that are required to connect to a mysql database
            global host, database, user, password
            host=self.hostname_line_edit.text()
            database=self.database_line_edit.text()
            user=self.username_line_edit.text()
            password=self.password_line_edit.text()

            # Creating fast log in credentials
            # host = "localhost"
            # database = "online_portfolio"
            # user = "testuser1"
            # password = "password12345"

            # Connecting to a mysql database
            mysql_database_connection = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password,
            )
            # Setting the connection_status to True if connection is succesful.
            connection_status = True

        # Instructing computer about what to do if the application fails to connect to the database.
        except:
            # Setting the connection status to False.
            connection_status = False

        # Checking if the connection status is True.
        if connection_status == True:

            # Creating a mysql initial connection cursor to execute sql commands
            mysql_initial_connection_cursor = mysql_database_connection.cursor()

            # Executing show tables sql command using python
            mysql_initial_connection_cursor.execute("SHOW TABLES")

            # Fetching all the data and storing them in list_of_table_names variable
            list_of_table_names = [ str(table_name[0]) for table_name in mysql_initial_connection_cursor.fetchall()]
            
            # Printing the list_of_table_names list in debug mode.
            debug(f'List of table names: {list_of_table_names}')

            QApplication.closeAllWindows()

            # Show the Main Window (The Database Manager GUI)
            ## Note: You can put self in but then the app doesn't close when the user closes the window
            main_window = MainWindow()
            main_window.show().exec_()


        # Displaying the warning message in the connetion status label
        else:
            self.connection_status_label.setText('Error! Make sure you are allowed in this database and did\'t entered your username and password wrong!')

def return_list_of_column_names(table_name):
    """A function which returns list of column names from a mysql database"""

    # Creating a cursor to query column names.
    mysql_query_column_names_cursor = mysql_database_connection.cursor()
    
    # Creating a sql command.
    mysql_command1 = f'SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME="{table_name}" ORDER BY ORDINAL_POSITION'

    # Executing the sql command.
    mysql_query_column_names_cursor.execute(mysql_command1)

    # Fetching all the data from the commands out put.
    column_names = mysql_query_column_names_cursor.fetchall()

    # Creating a list for the table's columns' names.
    list_of_the_table_column_names = array([ str(col[0]) for col in column_names ])

    # Returning the list_of_the_table_column_names
    return list_of_the_table_column_names

# Evaluate if the source is being run on its own or being imported somewhere else. With this conditional in place, your code can not be imported somewhere else.
if __name__ == '__main__':
    main()
