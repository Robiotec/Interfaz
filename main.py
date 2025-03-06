import sys

from PyQt5 import QtWidgets
from views.lg import Login  # Ventana Login
from controllers.login import LoginHmi


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Login()
        self.login_hmi = LoginHmi(self)
                
        self.ui.setupUi(self)
        self.ui.l_mensaj.setVisible(False) # Oculta el mensaje al iniciar
        self.ui.TE_contra.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.CB_mostrar.stateChanged.connect(self.toggle_password_visibility)
        self.ui.PB_iniciar.clicked.connect(self.validate_credentials)

    def toggle_password_visibility(self):
        self.login_hmi.toggle_password_visibility(self.ui.CB_mostrar, self.ui.TE_contra)

    def validate_credentials(self):
        self.login_hmi.validate_credentials(self.ui.TE_usua, self.ui.TE_contra, self.ui.l_mensaj)
        
if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        login_window = MainWindow()
        # MainWindow.setWindowIcon(QIcon("icons/LogoSmpli.png")) # Cambiar el ícono de la aplicación
        login_window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Error al cargar la aplicación: {e}")
        sys.exit(1)