from PyQt5 import uic
from config import *
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from orm.db import Employee
from orm.db_helper import save, opendb

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load the .ui file
        uic.loadUi(os.path.join(ui_folder, 'main.ui'), self)
        self.startBtn.clicked.connect(self.launch_login)

    def launch_login(self):
        self.open_login()  # Call the method to open the login screen
        self.close()  # Close the window

    def open_login(self):
        self.login = LoginWindow()
        self.login.show()


# login screen
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(ui_folder, 'login.ui'), self)
        self.loginBtn.clicked.connect(self.authenticate)

    def authenticate(self):
        username = self.username_input.text()
        password = self.password_input.text()

        db = opendb()

        # Check if the provided username and password match an employee record
        employee = db.query(Employee).filter_by(username=username, password=password).first()
        db.close()

        if employee:
            self.status_label.setText('Login successful')
            self.open_dashboard()  # Call the method to open the dashboard
            self.close()  # Close the login window
        else:
            self.status_label.setText('Login failed')
    
    def open_dashboard(self):
        self.dashboard = DashboardWindow()
        self.dashboard.show()

class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('dashboard.ui', self)

# dont write below this -------------------------------------------------------------------------------->
def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
