import sys
import os  # Para apagar el dispositivo
import time
import serial

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication

from PyQt5.QtGui import QIcon
from views.lg import Login  # Ventana Login
from controllers.login import LoginHmi
from views.control import Control  # Ventana Control

from multiprocessing import Process, cpu_count

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Login()
        self.login_hmi = LoginHmi(self)
                
        self.ui.setupUi(self)
        self.ui.l_mensaj.setVisible(False) # Oculta el mensaje al iniciar

        self.ui.TE_contra.setEchoMode(QtWidgets.QLineEdit.Password) # Configura TE_contra
        # Conexion de lógica CB_mostrar
        self.ui.CB_mostrar.stateChanged.connect(lambda: self.login_hmi.toggle_password_visibility(self.ui.CB_mostrar, self.ui.TE_contra))
        # Conecta el botón iniciar sesión
        self.ui.PB_iniciar.clicked.connect(lambda: self.login_hmi.validate_credentials(self.ui.TE_usua, self.ui.TE_contra, self.ui.l_mensaj))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = MainWindow()
    # MainWindow.setWindowIcon(QIcon("icons/LogoSmpli.png")) # Cambiar el ícono de la aplicación
    login_window.show()
    # print(cpu_count())
    sys.exit(app.exec())