#####################IMPORTS#############################
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from PyQt5.QtCore import *
import sys

from selenium import webdriver
from access_client_master import parse_client_excel_file_and_return_dict, generate_data_for_clientName_drop_down
from login_on_gst_portal import login_on_GSTPortal
###########################DATA HANDLING##############################
with open(r'db\db_path.txt','r') as file:
    excel_file = file.read()

client_master_excel_file = excel_file
client_dict = parse_client_excel_file_and_return_dict(client_master_excel_file)
#print(client_dict)
client_name_list = generate_data_for_clientName_drop_down("", client_dict)
####################APP CLASS & METHODS################################
class Client_Master_and_Login_Window(QDialog):
    def __init__(self):
        super(Client_Master_and_Login_Window, self).__init__()
        loadUi("GSTAutoLogin.ui", self)

        #set login button out of focus
        self.login_button.setFocusPolicy(Qt.NoFocus)

        #set window Icon
        self.setWindowIcon(QIcon(QPixmap('N.ico')))
        #set client value
        self.client_name_combo_box.addItems(client_name_list)
        #signal handling of search
        self.search_le.editingFinished.connect(self.update_client_name_list)
        #signal handling when particular client got selected
        self.client_name_combo_box.currentIndexChanged.connect(self.update_client_master_data)
        #signal handling on login button click
        self.login_button.clicked.connect(self.login_button_clicked)
        #signal handling for show password radio button
        self.radio_showPwd.toggled.connect(self.show_password_radio_clicked)

    def update_client_name_list(self):
        search = self.search_le.text()
        client_name_list = generate_data_for_clientName_drop_down(search, client_dict)
        self.client_name_combo_box.clear()
        self.client_name_combo_box.addItems(client_name_list)
        #delete all current data into LEs

    def update_client_master_data(self):
        client_name = self.client_name_combo_box.currentText()
        #retrive data from dict and set to LE
        if not client_name == "":
            client_data = client_dict[client_name]
            self.user_id_le.setText(str(client_data['User_id']))
            self.password_le.setText(str(client_data['Password']))
            self.gstin_le.setText(str(client_data['GSTIN']))
            self.org_type_le.setText(str(client_data['Organization_Type']))
            self.contact_person_le.setText(str(client_data['Contact_Person']))
            contact_number = client_data['Contact_Number']
            if contact_number != "":
                if type(contact_number) is float:
                    self.contact_number_le.setText(str(int(contact_number)))
                else:
                    self.contact_number_le.setText(client_data['Contact_Number'])  
            self.email_id_le.setText(str(client_data['Email_ID']))
            self.client_status_le.setText(str(client_data['Client_Status']))
            self.reg_type_le.setText(str(client_data['Registration_Type']))

    def login_button_clicked(self):
        user_id = self.user_id_le.text()
        password = self.password_le.text()
        if user_id != "" and password != "":
            login_on_GSTPortal(user_id, password)

    def show_password_radio_clicked(self, rb_stat):
        if rb_stat == False:
            self.password_le.setEchoMode(QLineEdit.Password)
        else:
            self.password_le.setEchoMode(QLineEdit.Normal)