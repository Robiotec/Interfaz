from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTimer

from control import Control  # Ventana Control
from config.credenciales import CORRECT_USERNAME, CORRECT_PASSWORD

from PyQt5.QtGui import QImage, QPixmap, QIcon, QMovie
from PyQt5.QtWidgets import QGraphicsScene

from conect import SocketClient

from multiprocessing import Process, cpu_count
# import cv2

class LoginBack(QtWidgets.QWidget):
    def __init__(self, main_windows, username=None, password=None):
        super().__init__()
        self.main_windows = main_windows
        self.username = username or ""
        self.password = password or ""
    
    #* Muestra o no el password del login
    def toggle_password_visibility(self, checkbox, password_field):
        if checkbox.isChecked():
            password_field.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            password_field.setEchoMode(QtWidgets.QLineEdit.Password)
            
    #* Valida las credenciales
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
    
    #* Muestra el mensaje
    def show_message(self, l_mensaj, message, color):
        l_mensaj.setText(message)
        l_mensaj.setStyleSheet(f"color: {color};")
        l_mensaj.setVisible(True)
        # Ocultar el mensaje después de 3 segundos
        QtCore.QTimer.singleShot(3000, lambda: l_mensaj.setVisible(False))
    
    #* Redirige a la ventana de control y cerra la ventana actual.
    def redirect_to_control(self):
        self.control_window = ControlWindow()
        self.control_window.show()
        self.main_windows.close()


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
        
        self.system_active = False
        self.mode_active = 0
        self.selected_valve = None
        # self.beta = False
        # self.caja = False
        self.select = 0
        
        
        #* Conección con el servidor
        self.client = SocketClient("192.168.1.100", 5000)
        self.client.connect()
        
        # Variables para mover la ventana
        self.is_dragging = False
        self.offset = QtCore.QPoint()
        
        # Configuración del frame_cabecera para mover la ventana
        self.ui.frame_cabecera.mousePressEvent = self.mousePressEvent
        self.ui.frame_cabecera.mouseMoveEvent = self.mouseMoveEvent
        self.ui.frame_cabecera.mouseReleaseEvent = self.mouseReleaseEvent
        
        self.ui.PB_EMER.clicked.connect(self.emergencia)
        
        self.ui.PB_ciclo.clicked.connect(self.process_ciclos_valve) # Activa las valvulas por ciclo
        
        for i in range(1, 100):  # Del 1 al 99
            button = getattr(self.ui, f'PB_{i}')  # Obtiene el botón usando getattr
            button.clicked.connect(self.activate_valve_individual)

        
        self.ui.CB_Camaras.clicked.connect(self.toggle_camera)
        
        # Variables para manejar la captura y temporizador
        self.capture = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        
        # self.ui.PB_beta.clicked.connect(self.bt_beta)
        self.ui.PB_beta.clicked.connect(self.beta_caja)
        self.ui.PB_caja.clicked.connect(self.beta_caja)
        # self.ui.PB_caja.clicked.connect(self.bt_caja)
        
#TODO: ================================= Obtener el Json =================================================================
    
    def obtener_json_base(self, device_type, additional_params=None):
        base_json = {
            "device": device_type,
        }
        if additional_params:
            base_json.update(additional_params)
        return base_json
            
    def activate_valve_individual(self):
        valve_mode = 3
        
        button = self.sender()
        button_number = int(button.objectName().split('_')[1])
        
        valve_number = (button_number - 1) // 9 + 1
        output_number = (button_number - 1) % 9 + 1
        
        individual_valves = f"V{valve_number}/{output_number}"

        json_data = {"valve_mode": valve_mode, "individual_valves": individual_valves}
        json = self.obtener_json_base("valve", json_data)
        self.client.send_json(json)
        # Realiza la acción deseada dependiendo del botón presionado
        print(f'Activando válvula para el botón {valve_number}: {output_number}')
        # Aquí puedes agregar el código para activar la válvula correspondiente

#TODO: ==================================== Control de Luces ====================================

        #* Conectar sliders para escuchar cambios en tiempo real
        self.ui.QS_iluminacion.valueChanged.connect(self.actualizar_intensidades)
        self.ui.QS_iluminacion_2.valueChanged.connect(self.actualizar_intensidades)
        self.ui.QS_iluminacion_3.valueChanged.connect(self.actualizar_intensidades)
        self.ui.QS_iluminacion_4.valueChanged.connect(self.actualizar_intensidades)

        #* Mostrar el porcentaje inicial de las Luces
        self.ui.L_iluminacion.setText(f'{self.ui.QS_iluminacion.value()} %')
        self.ui.L_iluminacion_2.setText(f'{self.ui.QS_iluminacion_2.value()} %')
        self.ui.L_iluminacion_3.setText(f'{self.ui.QS_iluminacion_3.value()} %')
        self.ui.L_iluminacion_4.setText(f'{self.ui.QS_iluminacion_4.value()} %')
        
    def actualizar_intensidades(self):
        """ Envía las intensidades a Arduino automáticamente al mover los sliders. """
        try:
            # Conectar al puerto serie de Arduino
            if not hasattr(self, 'arduino') or self.arduino.is_open == False:
                self.arduino = serial.Serial("COM4", 9600, timeout=1)

            # Leer los valores actuales de los sliders
            intensidad1 = self.ui.QS_iluminacion.value()
            intensidad2 = self.ui.QS_iluminacion_2.value()
            intensidad3 = self.ui.QS_iluminacion_3.value()
            intensidad4 = self.ui.QS_iluminacion_4.value()

            # Mostrar los valores actualizados en las etiquetas
            self.ui.L_iluminacion.setText(f'{intensidad1} %')
            self.ui.L_iluminacion_2.setText(f'{intensidad2} %')
            self.ui.L_iluminacion_3.setText(f'{intensidad3} %')
            self.ui.L_iluminacion_4.setText(f'{intensidad4} %')
            
            # Convertir los valores a un rango de 0 a 255
            intensidad1 = int((intensidad1 / 100) * 255)
            intensidad2 = int((intensidad2 / 100) * 255)
            intensidad3 = int((intensidad3 / 100) * 255)
            intensidad4 = int((intensidad4 / 100) * 255)

            # Crear el comando en formato CSV
            comando = f"{intensidad1},{intensidad2},{intensidad3},{intensidad4}\n"
            self.arduino.write(comando.encode())  # Enviar comando a Arduino

            # Leer confirmación del Arduino
            respuesta = self.arduino.readline().decode().strip()
            print(f"Respuesta de Arduino: {respuesta}")

        except serial.SerialException as e:
            print(f"Error al conectar con Arduino: {e}")

        
        
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
        elif sys.platform == "linux":
            os.system("sudo poweroff")  # Apagar en Linux
        elif sys.platform == "darwin":
            os.system("sudo shutdown -h now")  # Apagar en Mac
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
            self.ui.PB_EMER.setIcon(QIcon("src/Iconos/Detener.png"))
            self.ui.set_gif_visibility(True)
            
            self.ui.PB_beta.setEnabled(False)
            self.ui.PB_caja.setEnabled(False)
            self.ui.PB_left.setEnabled(False)
            self.ui.PB_right.setEnabled(False)
            self.ui.CB_Camaras.setEnabled(False)
            self.ui.checkBox_2.setEnabled(False)
            self.ui.checkBox_3.setEnabled(False)
            self.ui.checkBox_4.setEnabled(False)
            self.ui.checkBox_5.setEnabled(False)
            self.ui.checkBox_6.setEnabled(False)
            self.ui.PB_grid.setEnabled(False)
            self.ui.PB_fondo.setEnabled(False)
            self.ui.PB_banda.setEnabled(False)
            self.ui.PB_saranda.setEnabled(False)
            self.ui.PB_test.setEnabled(False)
            
            # Setear Beta Siempre
            
            json = self.obtener_json_base(
                "camera",
                {
                    # "camera_id": [0, 1],
                    # "is_grabbing": self.btn_grab_video.isChecked(),
                    # "is_gridding": self.btn_activate_grid.isChecked(),
                    # "is_ejecting": self.btn_activate_valves.isChecked(),
                    "selection": self.select,
                    "is_predicting": True,
                },
            )
            
            self.client.sendJSON(json)
                
            
        else:
            print("Parado de emergencia desactivado")
            self.ui.PB_EMER.setIcon(QIcon("src/Iconos/Start.png"))
            self.ui.set_gif_visibility(False)
            
            self.ui.PB_beta.setEnabled(True)
            self.ui.PB_caja.setEnabled(True)
            self.ui.PB_left.setEnabled(True)
            self.ui.PB_right.setEnabled(True)
            self.ui.CB_Camaras.setEnabled(True)
            self.ui.checkBox_2.setEnabled(True)
            self.ui.checkBox_3.setEnabled(True)
            self.ui.checkBox_4.setEnabled(True)
            self.ui.checkBox_5.setEnabled(True)
            self.ui.checkBox_6.setEnabled(True)
            self.ui.PB_grid.setEnabled(True)
            self.ui.PB_fondo.setEnabled(True)
            self.ui.PB_banda.setEnabled(True)
            self.ui.PB_saranda.setEnabled(True)
            self.ui.PB_test.setEnabled(True)
            
    def extraccion_video_player(self):
        print(" Activación de la camara ")
        
    def toggle_camera(self):
        # Al marcar o desmarcar el checkbox
        if self.ui.CB_Camaras.isChecked():
            print("Cámara activa")
            self.activate_camera()
        else:
            print("Cámara desactivada")
            self.deactivate_camera()
    
    def activate_camera(self):
        self.capture = cv2.VideoCapture(0)
        if not self.capture.isOpened():
            print("No se pudo acceder a la cámara.")
            return
        self.timer.start(30)
    
    def deactivate_camera(self):
        if self.capture:
            self.capture.release()
            self.capture = None
        self.timer.stop()

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            height, width, channels = frame_rgb.shape
            bytes_per_line = channels * width
            q_image = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
            
            pixmap = QPixmap.fromImage(q_image)
            scene = QGraphicsScene()
            scene.addPixmap(pixmap)
            self.ui.graphicsView.setScene(scene)
        
    def enviomessege(self, json):
        self.client.send_json(json)

        """ Activación de las valvulas individual """
    def process_todas_valve(self):        
        """ Activa todas las valvulas de golpe"""
    #* Proceso para la activación de todas las valvulas
    def process_ciclos_valve(self):
        self.mode_active = 1
        json = self.obtener_json_base("valve", {"valve_mode": 1})
        send_Json = Process(target=self.enviomessege, args=(json,))
        send_Json.start()
        send_Json.join()
        # self.send_json_async(json, "cycle")
        print("Proceso de activación de todas las valvulas")
    
    def select_valve(self, valve_index):
        self.selected_valve = valve_index
        self.toggle_valve_panel(True)
        
    def beta_caja(self):
        if self.select == 0:
            self.select = 1
            self.ui.PB_beta.setStyleSheet("background-color: #39FF14; border-radius: 5px;")
            self.ui.PB_caja.setStyleSheet("background-color: lightgray; border-radius: 3px;")
        else:
            self.select = 0
            self.ui.PB_caja.setStyleSheet("background-color: #39FF14; border-radius: 5px;")
            self.ui.PB_beta.setStyleSheet("background-color: lightgray; border-radius: 3px;")
        # return self.select
