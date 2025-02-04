import sys
import os  # Para apagar el dispositivo
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QIcon
from lg import Login  # Ventana Login
from control import Control  # Ventana Control

# Credenciales
CORRECT_USERNAME = "Robiotec"
CORRECT_PASSWORD = "123456"

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Login()
        
        self.ui.setupUi(self)

        # Oculta el mensaje al iniciar
        self.ui.l_mensaj.setVisible(False)

        # Configura TE_contra
        self.ui.TE_contra.setEchoMode(QtWidgets.QLineEdit.Password)

        # Conexion de lógica CB_mostrar
        self.ui.CB_mostrar.stateChanged.connect(self.toggle_password_visibility)

        # Conecta el botón iniciar sesión
        self.ui.PB_iniciar.clicked.connect(self.validate_credentials)

    def toggle_password_visibility(self):
        """Muestra y Oculta la contraseña según el estado del checkbox."""
        if self.ui.CB_mostrar.isChecked():
            self.ui.TE_contra.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ui.TE_contra.setEchoMode(QtWidgets.QLineEdit.Password)

    def validate_credentials(self):
        """Valida las credenciales"""
        username = self.ui.TE_usua.text().strip()
        password = self.ui.TE_contra.text().strip()

        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            self.show_message("¡Acceso correcto!", "green")
            
            self.ui.TE_usua.clear()
            self.ui.TE_contra.clear()
            
            # redirige a la ventana de control
            QtCore.QTimer.singleShot(500, self.redirect_to_control)
        else:
            self.show_message("Acceoso incorrectos.", "red")
            self.ui.TE_usua.clear()
            self.ui.TE_contra.clear()
            QtCore.QTimer.singleShot(500, self.redirect_to_control)

    def show_message(self, message, color):
        """Mostrar un mensaje."""
        self.ui.l_mensaj.setText(message)
        self.ui.l_mensaj.setStyleSheet(f"color: {color};")
        self.ui.l_mensaj.setVisible(True)

        # Ocultar el mensaje después de 3 segundos
        QtCore.QTimer.singleShot(3000, lambda: self.ui.l_mensaj.setVisible(False))

    def redirect_to_control(self):
        """Redirige a la ventana de control y cerra la ventana actual."""
        self.control_window = ControlWindow()
        # self.control_window.showFullScreen()
        self.control_window.show()
        self.close()  # Cierra la ventana de login

class ControlWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Control()
        self.ui.setupUi(self)
        self.ui.PB_cerrar.clicked.connect(self.close)
        self.ui.PB_menu.clicked.connect(self.toggle_menu)
        self.ui.PB_minim.clicked.connect(self.showMinimized)
        # self.ui.PB_maxim.clicked.connect(self.toggle_maximization)
        
        self.ui.PB_produc.clicked.connect(self.produccion)
        self.ui.PB_test.clicked.connect(self.test)
        self.ui.PB_config.clicked.connect(self.configuracion)
        self.ui.PB_ayuda.clicked.connect(self.ayuda)
        self.ui.PB_apagar.clicked.connect(self.salir)
        
        # Variables para mover la ventana
        self.is_dragging = False
        self.offset = QtCore.QPoint()
        
        # Configuración del frame_cabecera para mover la ventana
        self.ui.frame_cabecera.mousePressEvent = self.mousePressEvent
        self.ui.frame_cabecera.mouseMoveEvent = self.mouseMoveEvent
        self.ui.frame_cabecera.mouseReleaseEvent = self.mouseReleaseEvent
        
        self.ui.PB_EMER.clicked.connect(self.emergencia)
        
        
    def mousePressEvent(self, event):
        """Detecta cuando el ratón es presionado sobre el frame de la cabecera."""
        if event.button() == QtCore.Qt.LeftButton:
            self.is_dragging = True
            self.offset = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        """Mueve la ventana solo cuando el ratón está presionado."""
        if self.is_dragging:
            self.move(event.globalPos() - self.offset)
            event.accept()

    def mouseReleaseEvent(self, event):
        """Deja de mover la ventana cuando se suelta el clic del ratón."""
        if event.button() == QtCore.Qt.LeftButton:
            self.is_dragging = False
            event.accept()

    def close(self):
        print("Cerrando ventana de control")
        super().close()
    
    def toggle_menu(self):
        """oculta el menú lateral"""
        current_width = self.ui.frame_menucontroles.width()
        # Alterna entre el ancho original y el ancho reducido
        new_width = 60 if current_width == self.ui.PB_menu.width() else self.ui.PB_menu.width()
        self.ui.frame_menucontroles.setFixedWidth(new_width)
        
    def minimize_window(self):
        """Función personalizada para minimizar la ventana"""
        self.setWindowState(self.windowState() | QtCore.Qt.WindowMinimized)

    def toggle_maximization(self):
        """Alterna entre maximizar y restaurar."""
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
            
    def produccion(self):
        # Cambia a la pagina de produccion
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def test(self):
        # Cambia a la pagina de Tests
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def configuracion(self):
        # Cambia a la pagina de Configuracion
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)

    def ayuda(self):
        # Cambia a la pagina de Ayuda
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)

    def salir(self):
        # Apagar el dispositivo (solo en sistemas operativos compatibles)
        if sys.platform == "win32":
            os.system("shutdown /s /t 1")  # Apagar en Windows
        elif sys.platform == "linux" or sys.platform == "darwin":
            os.system("shutdown now")  # Apagar en Linux/Mac
        else:
            print("Comando de apagado no compatible con este sistema operativo")
        QApplication.quit()  # Cierra la aplicación
        
        # self.ui.PB_apagar.style.backgroundColor = "red"
        
    def emergencia(self):
        # Definir la variable de estado en el constructor
        if not hasattr(self, 'emergency_active'):
            self.emergency_active = False

        # Alternar el estado del boton emergencia
        self.emergency_active = not self.emergency_active

        if self.emergency_active:
            print("Parado de emergencia activado")
            self.ui.PB_EMER.setIcon(QIcon("Iconos/Detener.png"))
        else:
            print("Parado de emergencia desactivado")
            self.ui.PB_EMER.setIcon(QIcon("Iconos/Start.png"))

        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login_window = MainWindow()
    # Cambiar el ícono de la aplicación
    # MainWindow.setWindowIcon(QIcon("Iconos/LogoSmpli.png"))
    login_window.show()
    sys.exit(app.exec())