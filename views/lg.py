
from PyQt5 import QtCore, QtGui, QtWidgets


class Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 254)
        #* Elimina el boton maximizar
        MainWindow.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/icons/LoogoBlanco.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(self.styleSheet())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Logo = QtWidgets.QPushButton(self.frame)
        self.Logo.setGeometry(QtCore.QRect(10, 80, 151, 81))
        self.Logo.setText("")
        self.Logo.setIcon(icon)
        self.Logo.setIconSize(QtCore.QSize(130, 100))
        self.Logo.setObjectName("Logo")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(30, 20, 63, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 91, 20))
        self.label_2.setObjectName("label_2")
        self.PB_iniciar = QtWidgets.QPushButton(self.frame_2)
        self.PB_iniciar.setGeometry(QtCore.QRect(210, 190, 83, 29))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.PB_iniciar.setFont(font)
        self.PB_iniciar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_iniciar.setObjectName("PB_iniciar")
        self.CB_mostrar = QtWidgets.QCheckBox(self.frame_2)
        self.CB_mostrar.setGeometry(QtCore.QRect(30, 160, 151, 26))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.CB_mostrar.setFont(font)
        self.CB_mostrar.setObjectName("CB_mostrar")
        self.l_mensaj = QtWidgets.QLabel(self.frame_2)
        self.l_mensaj.setGeometry(QtCore.QRect(30, 190, 151, 31))
        self.l_mensaj.setObjectName("l_mensaj")
        self.TE_contra = QtWidgets.QLineEdit(self.frame_2)
        self.TE_contra.setGeometry(QtCore.QRect(30, 120, 271, 28))
        self.TE_contra.setObjectName("TE_contra")
        self.TE_usua = QtWidgets.QLineEdit(self.frame_2)
        self.TE_usua.setGeometry(QtCore.QRect(30, 50, 271, 28))
        self.TE_usua.setObjectName("TE_usua")
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Centrar ventana
        screen_geometry = QtWidgets.QApplication.primaryScreen().availableGeometry()
        window_geometry = MainWindow.geometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        MainWindow.move(x, y)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robiotec"))
        self.label.setText(_translate("MainWindow", "Usuario:"))
        self.label_2.setText(_translate("MainWindow", "Contraseña:"))
        self.PB_iniciar.setText(_translate("MainWindow", "INICIAR"))
        self.CB_mostrar.setText(_translate("MainWindow", "Mostrar contraseña"))
        self.l_mensaj.setText(_translate("MainWindow", "TextLabel"))
        
    def styleSheet(self):
        url = "src/stylelg.qss"
        try:
            with open(url, "r", encoding="utf-8") as file:
                css = file.read()
                return css
        except FileNotFoundError:
            print(f"Archivo de estilo no encontrado: {url}")
            return "/* Estilo por defecto */"
        except Exception as e:
            print(f"Error al cargar la hoja de estilo: {e}")
            return "/* Error al cargar el estilo */"



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_sesion = QtWidgets.QMainWindow()
    ui = Login()
    ui.setupUi(login_sesion)
    login_sesion.show()
    sys.exit(app.exec_())
