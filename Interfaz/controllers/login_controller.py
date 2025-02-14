from PyQt5.QtWidgets import QMessageBox
from views.login_view import LoginView

class LoginController(LoginView):
    def __init__(self):
        super().__init__()

        # Conectar eventos
        self.PB_iniciar.clicked.connect(self.verificar_credenciales)
        self.CB_mostrar.stateChanged.connect(self.mostrar_contrasena)

    def verificar_credenciales(self):
        usuario = self.TE_usua.text()
        contrasena = self.TE_contra.text()

        # Simulación de credenciales correctas
        if usuario == "admin" and contrasena == "1234":
            self.l_mensaj.setText("Inicio exitoso")
            self.l_mensaj.setStyleSheet("color: green;")
        else:
            self.l_mensaj.setText("Acceso incorrecto")
            self.l_mensaj.setStyleSheet("color: red;")

    def mostrar_contrasena(self):
        if self.CB_mostrar.isChecked():
            self.TE_contra.setEchoMode(self.TE_contra.Normal)
        else:
            self.TE_contra.setEchoMode(self.TE_contra.Password)
