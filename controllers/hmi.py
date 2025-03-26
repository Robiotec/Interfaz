import os
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize, QTimer
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsScene, QApplication
import serial
import time

#from pymodbus.client import ModbusSerialClient

from views.control import Control
from services.connect import SocketClient


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

        self.script_dir =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.system_active = False
        self.mode_active = 0
        self.selected_valve = None
        self.selection = 0

        # * Conección con el servidors
        self.client = SocketClient("192.168.1.100", 5000)
        self.client.connect()

        self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        time.sleep(2)   

        # Variables para mover la ventana
        self.is_dragging = False
        self.offset = QtCore.QPoint()

        # Configuración del frame_cabecera para mover la ventana
        self.ui.frame_cabecera.mousePressEvent = self.mousePressEvent
        self.ui.frame_cabecera.mouseMoveEvent = self.mouseMoveEvent
        self.ui.frame_cabecera.mouseReleaseEvent = self.mouseReleaseEvent

        self.ui.pb_sys.clicked.connect(self.toggle_system_operation)
        self.ui.pb_cycle.clicked.connect(self.cycles_valves)

        for i in range(1, 100):  # Del 1 al 99
            button = getattr(self.ui, f"PB_{i}")  # Obtiene el botón usando getattr
            button.clicked.connect(self.activate_valve_individual)

        # Variables para manejar la captura y temporizador
        #self.capture = None
        #self.timer = QTimer(self)
        #self.timer.timeout.connect(self.update_frame)
        self.ui.PB_beta.clicked.connect(self.beta_caja)
        self.ui.PB_caja.clicked.connect(self.beta_caja)
        self.ui.button_run.clicked.connect(self.toggleRun)
        self.ui.button_left.clicked.connect(self.leftMotor)
        self.ui.button_right.clicked.connect(self.rightMotor)
        self.ui.button_low_speed.clicked.connect(self.lowSpeed)
        self.ui.button_high_speed.clicked.connect(self.highSpeed)
        self.ui.button_medium_speed.clicked.connect(self.mediumSpeed)
        #self.ui.checkBox_3.clicked.connect(self.checkBox_3_toggled)

        # Configuración del cliente Modbus
        #self.modbus_client = ModbusSerialClient(
        #    method='rtu',
        #    port='COM3',  # Reemplaza con tu puerto COM
        #    baudrate=9600,  # Reemplaza con la velocidad de baudios
        #    parity='N',
        #    stopbits=1,
        #    bytesize=8,
        #    timeout=1
        #)
        #self.modbus_connection = self.modbus_client.connect()

    def toggleRun(self):
        if self.ui.button_run.styleSheet() == "background-color: orange;":
            self.ui.button_run.setStyleSheet("background-color: none;")
            self.sendToSerial("D/RUN")
        else:
            self.ui.button_run.setStyleSheet("background-color: orange;")
            self.sendToSerial("A/RUN")
            self.readFromSerial()
            #self.deactivateDirectionButtons()
            #self.deactivateSpeedButtons()

    def leftMotor(self):
        if self.ui.button_left.styleSheet() == "background-color: orange;":
            self.ui.button_left.setStyleSheet("background-color: none;")
            self.sendToSerial("D/DIRECTION")
        else:
            self.ui.button_left.setStyleSheet("background-color: orange;")
            self.sendToSerial("A/DIRECTION")
            self.deactivateRightMotor()

    def rightMotor(self):
        if self.ui.button_right.styleSheet() == "background-color: orange;":
            self.ui.button_right.setStyleSheet("background-color: none;")
            self.sendToSerial("D/DIRECTION")
        else:
            self.ui.button_right.setStyleSheet("background-color: orange;")
            self.sendToSerial("A/DIRECTION")
            self.deactivateLeftMotor()

    def lowSpeed(self):
        if self.ui.button_low_speed.styleSheet() == "background-color: orange;":
            self.ui.button_low_speed.setStyleSheet("background-color: none;")
            self.sendToSerial("D/BAJA")
        else:
            self.ui.button_low_speed.setStyleSheet("background-color: orange;")
            self.sendToSerial("A/BAJA")
            self.deactivateSpeedButtonsExcept("low")

    def mediumSpeed(self):
        if self.ui.button_medium_speed.styleSheet() == "background-color: orange;":
            self.ui.button_medium_speed.setStyleSheet("background-color: none;")
            self.sendToSerial("D/MEDIA")
        else:
            self.ui.button_medium_speed.setStyleSheet("background-color: orange;")
            self.sendToSerial("A/MEDIA")
            self.deactivateSpeedButtonsExcept("medium")

    def highSpeed(self):
        if self.ui.button_high_speed.styleSheet() == "background-color: orange;":
            self.ui.button_high_speed.setStyleSheet("background-color: none;")
            self.sendToSerial("D/ALTA")
        else:
            self.ui.button_high_speed.setStyleSheet("background-color: orange;")
            self.sendToSerial("A/ALTA")
            self.deactivateSpeedButtonsExcept("high")

    def deactivateDirectionButtons(self):
        self.ui.button_left.setStyleSheet("background-color: none;")
        self.ui.button_right.setStyleSheet("background-color: none;")

    def deactivateSpeedButtons(self):
        self.ui.button_low_speed.setStyleSheet("background-color: none;")
        self.ui.button_medium_speed.setStyleSheet("background-color: none;")
        self.ui.button_high_speed.setStyleSheet("background-color: none;")

    def deactivateSpeedButtonsExcept(self, active_speed):
        if active_speed != "low":
            self.ui.button_low_speed.setStyleSheet("background-color: none;")
        if active_speed != "medium":
            self.ui.button_medium_speed.setStyleSheet("background-color: none;")
        if active_speed != "high":
            self.ui.button_high_speed.setStyleSheet("background-color: none;")

    def deactivateLeftMotor(self):
        self.ui.button_left.setStyleSheet("background-color: none;")
        
    def deactivateRightMotor(self):
        self.ui.button_right.setStyleSheet("background-color: none;")
        
    def sendToSerial(self, command):
        try:
            print(f"Enviando comando: {command}")
            command_with_newline = command + "\n"
            self.ser.write(command_with_newline.encode())  # Envía el comando
            time.sleep(0.1)
        except serial.SerialException as e:
            print(f"Error al enviar el comando: {e}")

    def readFromSerial(self):
        try:
            response = self.ser.readline().decode('utf-8').strip()  # Lee la respuesta de Arduino
            if response:
                print(f"Respuesta de Arduino: {response}")  # Muestra la respuesta en Python
        except serial.SerialException as e:
            print(f"Error al leer del puerto serial: {e}")



    # TODO: ================================= Obtener el Json =================================================================
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
        button_number = int(button.objectName().split("_")[1])

        valve_number = (button_number - 1) // 9 + 1
        output_number = (button_number - 1) % 9 + 1

        individual_valves = f"V{valve_number}/{output_number}"

        json_data = {"valve_mode": valve_mode, "individual_valves": individual_valves}
        json = self.obtener_json_base("valve", json_data)
        self.client.send_json(json)
        print(individual_valves)

        # TODO: ==================================== Control de Luces ====================================
        # * Conectar sliders para escuchar cambios en tiempo real
        self.ui.QS_iluminacion.valueChanged.connect(self.actualizar_intensidades)
        self.ui.QS_iluminacion_2.valueChanged.connect(self.actualizar_intensidades)
        self.ui.QS_iluminacion_3.valueChanged.connect(self.actualizar_intensidades)
        self.ui.QS_iluminacion_4.valueChanged.connect(self.actualizar_intensidades)

        # # * Mostrar el porcentaje inicial de las Luces
        self.ui.L_iluminacion.setText(f"{self.ui.QS_iluminacion.value()} %")
        self.ui.L_iluminacion_2.setText(f"{self.ui.QS_iluminacion_2.value()} %")
        self.ui.L_iluminacion_3.setText(f"{self.ui.QS_iluminacion_3.value()} %")
        self.ui.L_iluminacion_4.setText(f"{self.ui.QS_iluminacion_4.value()} %")

    def actualizar_intensidades(self):
        """Envía las intensidades a Arduino automáticamente al mover los sliders."""
        try:
            # Conectar al puerto serie de Arduino
            if not hasattr(self, "arduino") or self.arduino.is_open == False:
                self.arduino = serial.Serial("COM4", 9600, timeout=1)
            # Leer los valores actuales de los sliders
            intensidad1 = self.ui.QS_iluminacion.value()
            intensidad2 = self.ui.QS_iluminacion_2.value()
            intensidad3 = self.ui.QS_iluminacion_3.value()
            intensidad4 = self.ui.QS_iluminacion_4.value()
            # Mostrar los valores actualizados en las etiquetas
            self.ui.L_iluminacion.setText(f"{intensidad1} %")
            self.ui.L_iluminacion_2.setText(f"{intensidad2} %")
            self.ui.L_iluminacion_3.setText(f"{intensidad3} %")
            self.ui.L_iluminacion_4.setText(f"{intensidad4} %")
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

    # * Detecta cuando el ratón es presionado sobre el frame de la cabecera
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.is_dragging = True
            self.offset = event.globalPos() - self.pos()
            event.accept()

    # * Mueve la ventana solo cuando el ratón está presionado
    def mouseMoveEvent(self, event):
        if self.is_dragging:
            self.move(event.globalPos() - self.offset)
            event.accept()

    # * Deja de mover la ventana cuando se suelta el clic del ratón
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.is_dragging = False
            event.accept()

    def close(self):
        super().close()

    # * oculta el menú lateral
    def toggle_menu(self):
        current_width = self.ui.frame_menucontroles.width()
        # Alterna entre el ancho original y el ancho reducido
        new_width = (
            60 if current_width == self.ui.PB_menu.width() else self.ui.PB_menu.width()
        )
        self.ui.frame_menucontroles.setFixedWidth(new_width)
        if new_width == 60:
            self.ui.PB_logo2.setIcon(QIcon("src/icons/logoSimplificadoC.png"))
            self.ui.PB_logo2.setIconSize(QSize(30, 30))
        else:
            self.ui.PB_logo2.setIcon(QIcon("src/icons/LoogoBlanco.png"))
            self.ui.PB_logo2.setIconSize(QSize(180, 180))

    def minimize_window(self):
        """Función personalizada para minimizar la ventana"""
        self.setWindowState(self.windowState() | QtCore.Qt.WindowMinimized)

    # * Alterna entre maximizar y restaurar
    def toggle_maximization(self):
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

    def handle_video_response(self, response):
        print(f"Video response from server: {response}")

        if response == "sended_videos":
            print("Todos los videos han sido recibidos con éxito.")
            video_path = os.path.join(
                self.script_dir, "src","videos", "camara_recived_2.mp4"
            )
            self.ui.view_media_player(video_path)

    def handle_cycle_response(self, response):
        print(f"Response from server: {response}")

    def set_enable_buttons(self, enable):
        self.ui.PB_beta.setEnabled(enable)
        self.ui.PB_caja.setEnabled(enable)
        self.ui.PB_left.setEnabled(enable)
        self.ui.PB_right.setEnabled(enable)
        self.ui.cb_video_grab.setEnabled(enable)
        self.ui.cb_valves.setEnabled(enable)
        self.ui.checkBox_3.setEnabled(enable)
        self.ui.checkBox_4.setEnabled(enable)
        self.ui.checkBox_5.setEnabled(enable)
        self.ui.checkBox_6.setEnabled(enable)
        self.ui.PB_grid.setEnabled(enable)
        self.ui.PB_fondo.setEnabled(enable)
        self.ui.PB_banda.setEnabled(enable)
        self.ui.PB_saranda.setEnabled(enable)
        self.ui.PB_test.setEnabled(enable)

    def toggle_system_operation(self):
        if not self.system_active:
            self.ui.pb_sys.setIcon(QIcon("src/icons/Detener.png"))
            self.ui.set_gif_visibility(True)
            self.set_enable_buttons(False)

            if self.ui.cb_video_grab.isChecked():
                self.ui.reiniciar_sistema_video()
                self.ui.label.setText("Modo: Grabar Video Activado...")
                self.ui.video_widget.hide()
                self.ui.set_gif_visibility(True)
            else:
                self.ui.label.setText("Modo: Tiempo Real Activado...")
                self.ui.set_gif_visibility(True)

            json = self.obtener_json_base(
                "camera",
                {
                    "is_grabbing": self.ui.cb_video_grab.isChecked(),
                    "is_predicting": True,
                    "is_ejecting": True,
                    "selection": self.selection,
                }
            )
            # self.client.send_json(json)

        else:
            self.ui.pb_sys.setIcon(QIcon("src/icons/Start.png"))
            self.ui.set_gif_visibility(False)
            self.set_enable_buttons(True)

            if self.ui.label.text() == "Modo: Tiempo Real Activado...":
                self.ui.label.setText("Modo: Tiempo Real Desactivado...")
            elif self.ui.label.text() == "Modo: Grabar Video Activado...":
                self.ui.label.setText("Modo: Grabar Video Desactivado")

            json = self.obtener_json_base(
                "stop_camera",
                {"is_grabbing": False, "is_gridding": False, "is_predicting": False},
            )
            print("Sending stop camera request...")
            # self.client.send_json(json)
            
            if self.ui.cb_video_grab.isChecked():
                # self.client.send_json_async(
                #     hmi=self, 
                #     json_data=json, 
                #     handle="stop_video", 
                #     handle_videos=True
                # )
                # QTimer.singleShot(500, self.ui.reiniciar_sistema_video)
                self.handle_video_response("sended_videos")

            # else:
            #     print("No se recibieron videos.")
            #     self.ui.reiniciar_sistema_video()
            #     self.ui.media_player.stop()
            #     if self.ui.video_widget.parent():
            #         self.ui.video_area.removeWidget(self.ui.video_widget)
            #         self.ui.video_widget.hide()
        self.system_active = not self.system_active
        
    def handle_start_complete(self, response):
        """Callback para cuando se completa el inicio de la operación"""
        print(f"Operación de inicio completada: {response}")
        self.operacion_en_curso = False

    def handle_stop_complete(self, response):
        """Callback para cuando se completa la detención de la operación"""
        print(f"Operación de detención completada: {response}")
        self.operacion_en_curso = False

    def enviomessege(self, json):
        self.client.send_json(json)

    def cycles_valves(self):
        self.mode_active = 1
        json = self.obtener_json_base("valve", {"valve_mode": 1})
        print("Activando todas las valvulas..." + str(json))
        self.client.send_json_async(
            hmi=self, json_data=json, handle="cycle", handle_videos=False
        )

    def select_valve(self, valve_index):
        self.selected_valve = valve_index
        self.toggle_valve_panel(True)

    def beta_caja(self):
        if self.selection == 0:
            self.selection = 1
            self.ui.PB_beta.setStyleSheet(
                "background-color: #ff7400; border-radius: 5px;"
            )
            self.ui.PB_caja.setStyleSheet(
                "background-color: lightgray; border-radius: 3px;"
            )
        else:
            self.selection = 0
            self.ui.PB_caja.setStyleSheet(
                "background-color: #ff7400; border-radius: 5px;"
            )
            self.ui.PB_beta.setStyleSheet(
                "background-color: lightgray; border-radius: 3px;"
            )
        # return self.select
    def handle_stop_button(self):
        if hasattr(self, "worker") and self.worker.isRunning():
            self.worker.cancel()
            self.worker.finished.connect(self.on_worker_finished)
            self.worker.wait()
            print("El trabajador ha sido cancelado y detenido.")
            
    def on_worker_finished(self):
        print("El trabajador ha terminado su ejecución.")

    #def checkBox_3_toggled(self):
    #    if self.ui.checkBox_3.isChecked():
    #        # Acción cuando el checkBox está marcado
    #        print("El checkbox está marcado")
    #    else:
    #        # Acción cuando el checkBox está desmarcado
    #        print("El checkbox está desmarcado")

    #def write_modbus_register(self, address, value):
    #    if self.modbus_connection:
    #        result = self.modbus_client.write_register(address, value, unit=1)
    #        if result.isError():
    #            print(f"Error al escribir en el registro {address}: {result}")
    #    else:
    #        print("No hay conexión Modbus.")
#
    #def read_modbus_register(self, address, count):
    #    if self.modbus_connection:
    #        result = self.modbus_client.read_holding_registers(address, count, unit=1)
    #        if result.isError():
    #            print(f"Error al leer el registro {address}: {result}")
    #        return result
    #    else:
    #        print("No hay conexión Modbus.")
    #        return None
#
    #def checkBox_3_toggled(self, checked):
    #    
    #    if checked:
    #        # Habilitar el servomotor y ponerlo en marcha
    #        self.write_modbus_register(0x0001, 1)  # Ejemplo: Registro de habilitación
    #        time.sleep(0.1)
    #        self.write_modbus_register(0x0002, 1)  # Ejemplo: Registro de arranque
    #        time.sleep(0.1)
    #        self.write_modbus_register(0x0003, 1000) # Ejemplo: Registro de velocidad, 1000 es valor de ejemplo.
    #    else:
    #        # Detener el servomotor y deshabilitarlo
    #        self.write_modbus_register(0x0002, 0)  # Ejemplo: Registro de parada
    #        time.sleep(0.1)
    #        self.write_modbus_register(0x0001, 0)  # Ejemplo: Registro de deshabilitación
#
    ## ... (resto de tus métodos) ...
#
    #def closeEvent(self, event):
    #    # Asegúrate de cerrar la conexión Modbus al cerrar la aplicación
    #    if self.modbus_connection:
    #        self.modbus_client.close()
    #    event.accept()
