from PyQt5 import QtCore, QtGui, QtWidgets

class LoginView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 254)
        MainWindow.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Iconos/LoogoBlanco.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        # Estilos
        MainWindow.setStyleSheet("QMainWindow{\n"
                                    "    background-color: black;\n"
                                    "    color: white;\n"
                                    "}\n"
                                    "\n"
                                    "QCheckBox{\n"
                                    "    color: white;\n"
                                    "}\n"
                                    "\n"
                                    "QLabel{\n"
                                    "    color:white;\n"
                                    "}\n"
                                    "\n"
                                    "QTextEdit {\n"
                                    "    background-color: transparent; \n"
                                    "    border: none; /* Sin bordes */\n"
                                    "    border-bottom: 2px solid orange; \n"
                                    "    border-top-left-radius: 10px;\n"
                                    "    border-top-right-radius: 10px;\n"
                                    "    color: white;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit{\n"
                                    "    background-color: transparent; \n"
                                    "    border: none; /* Sin bordes */\n"
                                    "    border-bottom: 2px solid orange; \n"
                                    "    border-top-left-radius: 10px;\n"
                                    "    border-top-right-radius: 10px;\n"
                                    "    color: white;\n"
                                    "}\n"
                                    "\n"
                                    "QTextEdit:focus {\n"
                                    "    background: qlineargradient(\n"
                                    "        spread:pad, \n"
                                    "        x1:0, y1:0, x2:0, y2:1, \n"
                                    "        stop:0 rgba(40, 100, 94, 0.0), \n"
                                    "        stop:1 rgba(40, 100, 94, 0.2)  \n"
                                    "    );\n"
                                    "    border-top-left-radius: 10px;\n"
                                    "    border-top-right-radius: 10px;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:focus{\n"
                                    "    background: qlineargradient(\n"
                                    "        spread:pad, \n"
                                    "        x1:0, y1:0, x2:0, y2:1, \n"
                                    "        stop:0 rgba(40, 100, 94, 0.0), \n"
                                    "        stop:1 rgba(40, 100, 94, 0.2)  \n"
                                    "    );\n"
                                    "    border-top-left-radius: 10px;\n"
                                    "    border-top-right-radius: 10px;\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "#Logo{\n"
                                    "    background-color: transparent;\n"
                                    "}\n"
                                    "#Logo:hover{\n"
                                    "    background-color: transparent;\n"
                                    "}\n"
                                    "\n"
                                    ""
                                    )

        # Widgets principales
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)

        # Frame del logo
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.Logo = QtWidgets.QPushButton(self.frame)
        self.Logo.setGeometry(QtCore.QRect(10, 80, 151, 81))
        self.Logo.setIcon(icon)
        self.Logo.setIconSize(QtCore.QSize(130, 100))
        self.horizontalLayout.addWidget(self.frame)

        # Frame del formulario
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.label_usuario = QtWidgets.QLabel("Usuario:", self.frame_2)
        self.label_usuario.setGeometry(QtCore.QRect(30, 20, 63, 20))

        self.TE_usua = QtWidgets.QLineEdit(self.frame_2)
        self.TE_usua.setGeometry(QtCore.QRect(30, 50, 271, 28))

        self.label_contra = QtWidgets.QLabel("Contraseña:", self.frame_2)
        self.label_contra.setGeometry(QtCore.QRect(30, 100, 91, 20))

        self.TE_contra = QtWidgets.QLineEdit(self.frame_2)
        self.TE_contra.setGeometry(QtCore.QRect(30, 120, 271, 28))
        self.TE_contra.setEchoMode(QtWidgets.QLineEdit.Password)

        self.CB_mostrar = QtWidgets.QCheckBox("Mostrar contraseña", self.frame_2)
        self.CB_mostrar.setGeometry(QtCore.QRect(30, 160, 151, 26))

        self.PB_iniciar = QtWidgets.QPushButton("INICIAR", self.frame_2)
        self.PB_iniciar.setGeometry(QtCore.QRect(210, 190, 83, 29))

        self.l_mensaj = QtWidgets.QLabel("", self.frame_2)
        self.l_mensaj.setGeometry(QtCore.QRect(30, 190, 151, 31))

        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        # Centrar ventana
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry()
        window_geometry = MainWindow.geometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        MainWindow.move(x, y)
