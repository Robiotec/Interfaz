from PyQt5 import QtCore, QtWidgets
from config.credentials import CORRECT_USERNAME, CORRECT_PASSWORD
from controllers.hmi import ControlWindow

class LoginHmi(QtWidgets.QWidget):
    def __init__(self, main_windows, username=None, password=None):
        super().__init__()
        self.main_windows = main_windows
        self.username = username or ""
        self.password = password or ""
    
    def toggle_password_visibility(self, checkbox, password_field):
        if checkbox.isChecked():
            password_field.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            password_field.setEchoMode(QtWidgets.QLineEdit.Password)
            
    def validate_credentials(self, username_field, password_field, l_mensaj):
        username = username_field.text().strip()
        password = password_field.text().strip()

        if self.is_valid_user(username, password):
            self.show_message(l_mensaj, "¡Acceso correcto!", "green")
            username_field.clear()
            password_field.clear()
            self.redirect_to_control()
        else:
            self.show_message(l_mensaj, "Accesos incorrectos.", "red")
            username_field.clear()
            password_field.clear()
            self.redirect_to_control()
            
    def is_valid_user(self, username, password):
        return username == CORRECT_USERNAME and password == CORRECT_PASSWORD
    
    def show_message(self, l_mensaj, message, color):
        l_mensaj.setText(message)
        l_mensaj.setStyleSheet(f"color: {color};")
        l_mensaj.setVisible(True)
        QtCore.QTimer.singleShot(3000, lambda: l_mensaj.setVisible(False))
    
    def redirect_to_control(self):
        self.control_window = ControlWindow()
        # self.control_window.showFullScreen()
        self.control_window.show()
        self.main_windows.close()