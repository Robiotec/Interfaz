from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


class Control(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 654)
        # TODO: Eliminar bordes y botones del sistema
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        MainWindow.setMinimumSize(QtCore.QSize(1024, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
        MainWindow.setStyleSheet(self.stylos())  # * Inyect los Estylos
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_cabecera = QtWidgets.QFrame(self.centralwidget)
        self.frame_cabecera.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_cabecera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cabecera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cabecera.setObjectName("frame_cabecera")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_cabecera)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.frame_cabecera)
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PB_menu = QtWidgets.QPushButton(self.frame)
        self.PB_menu.setMinimumSize(QtCore.QSize(60, 0))
        self.PB_menu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.PB_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("src/icons/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.PB_menu.setIcon(icon)
        self.PB_menu.setIconSize(QtCore.QSize(20, 20))
        self.PB_menu.setObjectName("PB_menu")
        self.horizontalLayout_2.addWidget(self.PB_menu)
        self.horizontalLayout.addWidget(self.frame)
        spacerItem = QtWidgets.QSpacerItem(
            475, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.horizontalLayout.addItem(spacerItem)
        self.frame_2 = QtWidgets.QFrame(self.frame_cabecera)
        self.frame_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PB_minim = QtWidgets.QPushButton(self.frame_2)
        self.PB_minim.setMaximumSize(QtCore.QSize(50, 16777215))
        self.PB_minim.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_minim.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("src/icons/Minimizar.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.PB_minim.setIcon(icon1)
        self.PB_minim.setObjectName("PB_minim")
        self.horizontalLayout_3.addWidget(self.PB_minim)
        self.PB_maxim = QtWidgets.QPushButton(self.frame_2)
        self.PB_maxim.setMaximumSize(QtCore.QSize(50, 16777215))
        self.PB_maxim.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_maxim.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("src/icons/Maximizar.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.PB_maxim.setIcon(icon2)
        self.PB_maxim.setObjectName("PB_maxim")
        self.horizontalLayout_3.addWidget(self.PB_maxim)
        self.PB_cerrar = QtWidgets.QPushButton(self.frame_2)
        self.PB_cerrar.setMaximumSize(QtCore.QSize(50, 16777215))
        self.PB_cerrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_cerrar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("src/icons/Cerrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.PB_cerrar.setIcon(icon3)
        self.PB_cerrar.setObjectName("PB_cerrar")
        self.horizontalLayout_3.addWidget(self.PB_cerrar)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 8)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addWidget(self.frame_cabecera)
        self.frame_cuerpo = QtWidgets.QFrame(self.centralwidget)
        self.frame_cuerpo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cuerpo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cuerpo.setObjectName("frame_cuerpo")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_cuerpo)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_menucontroles = QtWidgets.QFrame(self.frame_cuerpo)
        self.frame_menucontroles.setMinimumSize(QtCore.QSize(198, 0))
        self.frame_menucontroles.setMaximumSize(QtCore.QSize(198, 16777215))
        self.frame_menucontroles.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menucontroles.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menucontroles.setObjectName("frame_menucontroles")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_menucontroles)
        self.verticalLayout_7.setContentsMargins(2, 0, 3, 0)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.PB_logo2 = QtWidgets.QPushButton(self.frame_menucontroles)
        self.PB_logo2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.PB_logo2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap("src/icons/LoogoBlanco.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.PB_logo2.setIcon(icon4)
        self.PB_logo2.setIconSize(QtCore.QSize(180, 180))
        self.PB_logo2.setObjectName("PB_logo2")
        self.verticalLayout_7.addWidget(self.PB_logo2)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 79, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_7.addItem(spacerItem1)
        self.PB_produc = QtWidgets.QPushButton(self.frame_menucontroles)
        self.PB_produc.setMinimumSize(QtCore.QSize(0, 50))
        self.PB_produc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap("src/icons/Home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.PB_produc.setIcon(icon5)
        self.PB_produc.setObjectName("PB_produc")
        self.verticalLayout_7.addWidget(self.PB_produc)
        self.PB_test = QtWidgets.QPushButton(self.frame_menucontroles)
        self.PB_test.setMinimumSize(QtCore.QSize(0, 50))
        self.PB_test.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap("src/icons/Test.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.PB_test.setIcon(icon6)
        self.PB_test.setObjectName("PB_test")
        self.verticalLayout_7.addWidget(self.PB_test)
        self.PB_config = QtWidgets.QPushButton(self.frame_menucontroles)
        self.PB_config.setMinimumSize(QtCore.QSize(0, 50))
        self.PB_config.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap("src/icons/Config.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.PB_config.setIcon(icon7)
        self.PB_config.setObjectName("PB_config")
        self.verticalLayout_7.addWidget(self.PB_config)
        self.PB_ayuda = QtWidgets.QPushButton(self.frame_menucontroles)
        self.PB_ayuda.setMinimumSize(QtCore.QSize(0, 50))
        self.PB_ayuda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap("src/icons/Ayuda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.PB_ayuda.setIcon(icon8)
        self.PB_ayuda.setObjectName("PB_ayuda")
        self.verticalLayout_7.addWidget(self.PB_ayuda)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 76, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_7.addItem(spacerItem2)
        self.PB_apagar = QtWidgets.QPushButton(self.frame_menucontroles)
        self.PB_apagar.setMinimumSize(QtCore.QSize(0, 50))
        self.PB_apagar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_apagar.setStyleSheet("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap("src/icons/1x/Apagar_3.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.PB_apagar.setIcon(icon9)
        self.PB_apagar.setIconSize(QtCore.QSize(120, 30))
        self.PB_apagar.setObjectName("PB_apagar")
        self.verticalLayout_7.addWidget(self.PB_apagar)
        self.horizontalLayout_4.addWidget(self.frame_menucontroles)
        self.frame_4 = QtWidgets.QFrame(self.frame_cuerpo)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 380))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_izquierdo = QtWidgets.QFrame(self.frame_3)
        self.frame_izquierdo.setMaximumSize(QtCore.QSize(62, 16777215))
        self.frame_izquierdo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_izquierdo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_izquierdo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_izquierdo.setObjectName("frame_izquierdo")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_izquierdo)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 153, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_5.addItem(spacerItem3)
        self.PB_left = QtWidgets.QPushButton(self.frame_izquierdo)
        self.PB_left.setMinimumSize(QtCore.QSize(50, 50))
        self.PB_left.setMaximumSize(QtCore.QSize(62, 62))
        self.PB_left.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_left.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PB_left.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(
            QtGui.QPixmap("src/icons/flecha_izquierda.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.PB_left.setIcon(icon10)
        self.PB_left.setObjectName("PB_left")
        self.verticalLayout_5.addWidget(self.PB_left)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 153, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_5.addWidget(self.frame_izquierdo)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        #self.frame_7.setStyleSheet("border: 1px solid orange;")
        self.video_area = QtWidgets.QVBoxLayout(self.frame_7)
        self.video_area.setContentsMargins(0, 0, 0, 0)
        self.video_area.setSpacing(0)
        self.video_area.setObjectName("video_area")
        self.label = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.video_area.addWidget(self.label)
        self.graphicsView = QtWidgets.QGraphicsView(self.frame_7)

        # * Creacion e insercion de video
        self.media_player = QMediaPlayer()
        self.video_widget = QVideoWidget()
        self.media_player.setVideoOutput(self.video_widget)
        self.video_widget.setStyleSheet("border: 1px solid orange;")

        self.graphicsView.setObjectName("graphicsView")
        self.video_widget.hide()

        self.video_area.addWidget(self.graphicsView)
        self.video_area.addWidget(self.video_widget)

        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.video_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.video_widget.setAspectRatioMode(QtCore.Qt.IgnoreAspectRatio)

        background_color = QtGui.QColor(
            38, 38, 38
        )  # Color gris claro (ajustalo como desees)
        self.graphicsView.setStyleSheet(f"background-color: {background_color.name()};")
        self.scene = QtWidgets.QGraphicsScene(self.graphicsView)
        self.graphicsView.setScene(self.scene)
        self.movie = QtGui.QMovie("src/icons/MaX2.gif")
        self.gif_item = QtWidgets.QGraphicsPixmapItem()
        self.scene.addItem(self.gif_item)
        self.gif_item.setVisible(False)
        self.movie.frameChanged.connect(self.update_gif)
        self.movie.start()
        self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)

        self.horizontalLayout_5.addWidget(self.frame_7)
        self.frame_derecho = QtWidgets.QFrame(self.frame_3)
        self.frame_derecho.setMaximumSize(QtCore.QSize(62, 16777215))
        self.frame_derecho.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_derecho.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_derecho.setObjectName("frame_derecho")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_derecho)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 153, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_6.addItem(spacerItem5)
        self.PB_right = QtWidgets.QPushButton(self.frame_derecho)
        self.PB_right.setMinimumSize(QtCore.QSize(50, 50))
        self.PB_right.setMaximumSize(QtCore.QSize(62, 62))
        self.PB_right.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_right.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(
            QtGui.QPixmap("src/icons/flecha_derecha.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.PB_right.setIcon(icon11)
        self.PB_right.setObjectName("PB_right")
        self.verticalLayout_6.addWidget(self.PB_right)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 153, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_6.addItem(spacerItem6)
        self.horizontalLayout_5.addWidget(self.frame_derecho)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 12)
        self.horizontalLayout_5.setStretch(2, 1)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.page)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_22 = QtWidgets.QFrame(self.frame_5)
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.label_8 = QtWidgets.QLabel(self.frame_22)
        self.label_8.setGeometry(QtCore.QRect(30, 20, 241, 20))
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.frame_22)
        self.label_11.setGeometry(QtCore.QRect(90, 110, 91, 20))
        self.label_11.setObjectName("label_11")
        self.PB_caja = QtWidgets.QPushButton(self.frame_22)
        self.PB_caja.setGeometry(QtCore.QRect(10, 150, 61, 61))
        self.PB_caja.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(
            QtGui.QPixmap("src/icons/Caja.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.PB_caja.setIcon(icon12)
        self.PB_caja.setIconSize(QtCore.QSize(50, 50))
        self.PB_caja.setObjectName("PB_caja")
        self.PB_caja.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_9 = QtWidgets.QLabel(self.frame_22)
        self.label_9.setGeometry(QtCore.QRect(90, 70, 111, 20))
        self.label_9.setObjectName("label_9")
        self.PB_beta = QtWidgets.QPushButton(self.frame_22)
        self.PB_beta.setGeometry(QtCore.QRect(10, 70, 61, 61))
        self.PB_beta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_beta.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(
            QtGui.QPixmap("src/icons/Beta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.PB_beta.setIcon(icon13)
        self.PB_beta.setIconSize(QtCore.QSize(50, 50))
        self.PB_beta.setObjectName("PB_beta")
        self.label_10 = QtWidgets.QLabel(self.frame_22)
        self.label_10.setGeometry(QtCore.QRect(90, 150, 111, 20))
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.frame_22)
        self.label_12.setGeometry(QtCore.QRect(90, 190, 91, 20))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.frame_22)
        self.frame_20 = QtWidgets.QFrame(self.frame_5)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_20)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 180, 121, 40))
        self.checkBox_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.cb_video_grab = QtWidgets.QCheckBox(self.frame_20)
        self.cb_video_grab.setGeometry(QtCore.QRect(10, 60, 121, 40))
        self.cb_video_grab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cb_video_grab.setText("")
        self.cb_video_grab.setObjectName("CB_Camaras")
        self.cb_valves = QtWidgets.QCheckBox(self.frame_20)
        self.cb_valves.setGeometry(QtCore.QRect(10, 120, 121, 40))
        font = QtGui.QFont()
        font.setBold(False)
        self.cb_valves.setFont(font)
        self.cb_valves.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cb_valves.setText("")
        self.cb_valves.setObjectName("cb_valves")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_20)
        self.checkBox_4.setGeometry(QtCore.QRect(140, 60, 121, 40))
        self.checkBox_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame_20)
        self.checkBox_6.setGeometry(QtCore.QRect(140, 180, 121, 40))
        self.checkBox_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_20)
        self.checkBox_5.setGeometry(QtCore.QRect(140, 120, 121, 40))
        self.checkBox_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.label_13 = QtWidgets.QLabel(self.frame_20)
        self.label_13.setGeometry(QtCore.QRect(70, 20, 171, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_20)
        self.label_14.setGeometry(QtCore.QRect(60, 70, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: black;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_20)
        self.label_15.setGeometry(QtCore.QRect(60, 130, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: black;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_20)
        self.label_16.setGeometry(QtCore.QRect(60, 190, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: black;")
        self.label_16.setObjectName("label_16")
        self.label_21 = QtWidgets.QLabel(self.frame_20)
        self.label_21.setGeometry(QtCore.QRect(190, 70, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: black;")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_20)
        self.label_22.setGeometry(QtCore.QRect(190, 130, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: black;")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_20)
        self.label_23.setGeometry(QtCore.QRect(190, 190, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: black;")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_7.addWidget(self.frame_20)
        self.frame_21 = QtWidgets.QFrame(self.frame_5)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.PB_EMER = QtWidgets.QPushButton(self.frame_21)
        self.PB_EMER.setGeometry(QtCore.QRect(10, 10, 251, 221))
        self.PB_EMER.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_EMER.setStyleSheet("background-color: transparent;")
        self.PB_EMER.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(
            QtGui.QPixmap("src/icons/Start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.PB_EMER.setIcon(icon14)
        self.PB_EMER.setIconSize(QtCore.QSize(200, 200))
        self.PB_EMER.setObjectName("PB_EMER")
        self.horizontalLayout_7.addWidget(self.frame_21)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setGeometry(QtCore.QRect(310, 390, 251, 101))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.page_4)
        self.pushButton.setGeometry(QtCore.QRect(140, 20, 621, 361))
        self.pushButton.setStyleSheet("background-color: transparent;")
        self.pushButton.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(
            QtGui.QPixmap("src/icons/Robiotec.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.pushButton.setIcon(icon15)
        self.pushButton.setIconSize(QtCore.QSize(350, 350))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page_4)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(2)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_16 = QtWidgets.QFrame(self.page_3)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_17 = QtWidgets.QFrame(self.frame_16)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_15.setSpacing(2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_24 = QtWidgets.QFrame(self.frame_17)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_6.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame_24)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.PB_grid = QtWidgets.QPushButton(self.frame_24)
        self.PB_grid.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setBold(True)
        self.PB_grid.setFont(font)
        self.PB_grid.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_grid.setObjectName("PB_grid")
        self.horizontalLayout_6.addWidget(self.PB_grid)
        self.verticalLayout_15.addWidget(self.frame_24)
        self.frame_19 = QtWidgets.QFrame(self.frame_17)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.GV_camara1 = QtWidgets.QGraphicsView(self.frame_19)
        self.GV_camara1.setObjectName("GV_camara1")
        self.verticalLayout_18.addWidget(self.GV_camara1)
        self.verticalLayout_15.addWidget(self.frame_19)
        self.frame_23 = QtWidgets.QFrame(self.frame_17)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.GV_camara2 = QtWidgets.QGraphicsView(self.frame_23)
        self.GV_camara2.setObjectName("GV_camara2")
        self.verticalLayout_17.addWidget(self.GV_camara2)
        self.verticalLayout_15.addWidget(self.frame_23)
        self.verticalLayout_15.setStretch(0, 1)
        self.verticalLayout_15.setStretch(1, 5)
        self.verticalLayout_15.setStretch(2, 5)
        self.verticalLayout_11.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.frame_16)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_fondo = QtWidgets.QFrame(self.frame_18)
        self.frame_fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fondo.setObjectName("frame_fondo")
        self.label_6 = QtWidgets.QLabel(self.frame_fondo)
        self.label_6.setGeometry(QtCore.QRect(100, 30, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_fondo)
        self.label_7.setGeometry(QtCore.QRect(140, 160, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.QS_iluminacion = QtWidgets.QSlider(self.frame_fondo)
        self.QS_iluminacion.setGeometry(QtCore.QRect(70, 180, 201, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.QS_iluminacion.setFont(font)
        self.QS_iluminacion.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QS_iluminacion.setStyleSheet("")
        self.QS_iluminacion.setMaximum(100)
        self.QS_iluminacion.setPageStep(5)
        self.QS_iluminacion.setOrientation(QtCore.Qt.Horizontal)
        self.QS_iluminacion.setObjectName("QS_iluminacion")
        self.PB_fondo = QtWidgets.QPushButton(self.frame_fondo)
        self.PB_fondo.setGeometry(QtCore.QRect(260, 78, 71, 45))
        self.PB_fondo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_fondo.setObjectName("PB_fondo")
        self.L_iluminacion = QtWidgets.QLabel(self.frame_fondo)
        self.L_iluminacion.setGeometry(QtCore.QRect(280, 180, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.L_iluminacion.setFont(font)
        self.L_iluminacion.setObjectName("L_iluminacion")
        self.SB_1 = QtWidgets.QSpinBox(self.frame_fondo)
        self.SB_1.setGeometry(QtCore.QRect(50, 80, 61, 41))
        self.SB_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SB_1.setMaximum(255)
        self.SB_1.setObjectName("SB_1")
        self.SB_2 = QtWidgets.QSpinBox(self.frame_fondo)
        self.SB_2.setGeometry(QtCore.QRect(120, 80, 61, 41))
        self.SB_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SB_2.setMaximum(255)
        self.SB_2.setObjectName("SB_2")
        self.SB_3 = QtWidgets.QSpinBox(self.frame_fondo)
        self.SB_3.setGeometry(QtCore.QRect(190, 80, 61, 41))
        self.SB_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SB_3.setMinimum(0)
        self.SB_3.setMaximum(255)
        self.SB_3.setObjectName("SB_3")
        self.L_iluminacion_2 = QtWidgets.QLabel(self.frame_fondo)
        self.L_iluminacion_2.setGeometry(QtCore.QRect(280, 210, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.L_iluminacion_2.setFont(font)
        self.L_iluminacion_2.setObjectName("L_iluminacion_2")
        self.QS_iluminacion_2 = QtWidgets.QSlider(self.frame_fondo)
        self.QS_iluminacion_2.setGeometry(QtCore.QRect(70, 210, 201, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.QS_iluminacion_2.setFont(font)
        self.QS_iluminacion_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QS_iluminacion_2.setStyleSheet("")
        self.QS_iluminacion_2.setMaximum(100)
        self.QS_iluminacion_2.setPageStep(5)
        self.QS_iluminacion_2.setOrientation(QtCore.Qt.Horizontal)
        self.QS_iluminacion_2.setObjectName("QS_iluminacion_2")
        self.L_iluminacion_3 = QtWidgets.QLabel(self.frame_fondo)
        self.L_iluminacion_3.setGeometry(QtCore.QRect(280, 240, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.L_iluminacion_3.setFont(font)
        self.L_iluminacion_3.setObjectName("L_iluminacion_3")
        self.QS_iluminacion_3 = QtWidgets.QSlider(self.frame_fondo)
        self.QS_iluminacion_3.setGeometry(QtCore.QRect(70, 240, 201, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.QS_iluminacion_3.setFont(font)
        self.QS_iluminacion_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QS_iluminacion_3.setStyleSheet("")
        self.QS_iluminacion_3.setMaximum(100)
        self.QS_iluminacion_3.setPageStep(5)
        self.QS_iluminacion_3.setOrientation(QtCore.Qt.Horizontal)
        self.QS_iluminacion_3.setObjectName("QS_iluminacion_3")
        self.L_iluminacion_4 = QtWidgets.QLabel(self.frame_fondo)
        self.L_iluminacion_4.setGeometry(QtCore.QRect(280, 270, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.L_iluminacion_4.setFont(font)
        self.L_iluminacion_4.setObjectName("L_iluminacion_4")
        self.QS_iluminacion_4 = QtWidgets.QSlider(self.frame_fondo)
        self.QS_iluminacion_4.setGeometry(QtCore.QRect(70, 270, 201, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.QS_iluminacion_4.setFont(font)
        self.QS_iluminacion_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QS_iluminacion_4.setStyleSheet("")
        self.QS_iluminacion_4.setMaximum(100)
        self.QS_iluminacion_4.setPageStep(5)
        self.QS_iluminacion_4.setOrientation(QtCore.Qt.Horizontal)
        self.QS_iluminacion_4.setObjectName("QS_iluminacion_4")
        self.horizontalLayout_8.addWidget(self.frame_fondo)
        self.frame_banda = QtWidgets.QFrame(self.frame_18)
        self.frame_banda.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_banda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_banda.setObjectName("frame_banda")
        self.label_17 = QtWidgets.QLabel(self.frame_banda)
        self.label_17.setGeometry(QtCore.QRect(112, 30, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.PB_banda = QtWidgets.QPushButton(self.frame_banda)
        self.PB_banda.setGeometry(QtCore.QRect(231, 80, 80, 31))
        self.PB_banda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_banda.setObjectName("PB_banda")
        self.label_18 = QtWidgets.QLabel(self.frame_banda)
        self.label_18.setGeometry(QtCore.QRect(60, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_20 = QtWidgets.QLabel(self.frame_banda)
        self.label_20.setGeometry(QtCore.QRect(105, 190, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.SB_saranda = QtWidgets.QSpinBox(self.frame_banda)
        self.SB_saranda.setGeometry(QtCore.QRect(120, 240, 101, 41))
        self.SB_saranda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SB_saranda.setObjectName("SB_saranda")
        self.label_24 = QtWidgets.QLabel(self.frame_banda)
        self.label_24.setGeometry(QtCore.QRect(80, 244, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.PB_saranda = QtWidgets.QPushButton(self.frame_banda)
        self.PB_saranda.setGeometry(QtCore.QRect(229, 247, 71, 31))
        self.PB_saranda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_saranda.setObjectName("PB_saranda")
        self.SP_banda = QtWidgets.QSpinBox(self.frame_banda)
        self.SP_banda.setGeometry(QtCore.QRect(120, 80, 101, 31))
        self.SP_banda.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SP_banda.setObjectName("SP_banda")
        self.horizontalLayout_8.addWidget(self.frame_banda)
        self.verticalLayout_11.addWidget(self.frame_18)
        self.verticalLayout_11.setStretch(0, 3)
        self.verticalLayout_11.setStretch(1, 4)
        self.verticalLayout_16.addWidget(self.frame_16)
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_6 = QtWidgets.QFrame(self.page_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_10 = QtWidgets.QFrame(self.frame_6)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_14.setSpacing(2)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_2 = QtWidgets.QLabel(self.frame_10)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_14.addWidget(self.label_2)
        self.verticalLayout_9.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_14 = QtWidgets.QFrame(self.frame_9)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.pb_cycle = QtWidgets.QPushButton(self.frame_14)
        self.pb_cycle.setMinimumSize(QtCore.QSize(0, 120))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.pb_cycle.setFont(font)
        self.pb_cycle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon16 = QtGui.QIcon()
        icon16.addPixmap(
            QtGui.QPixmap("src/icons/Ciclo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.pb_cycle.setIcon(icon16)
        self.pb_cycle.setCheckable(False)
        self.pb_cycle.setAutoRepeat(False)
        self.pb_cycle.setObjectName("pb_cycle")
        self.verticalLayout_12.addWidget(self.pb_cycle)
        self.gridLayout.addWidget(self.frame_14, 1, 0, 1, 1)
        self.frame_13 = QtWidgets.QFrame(self.frame_9)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.PB_todas = QtWidgets.QPushButton(self.frame_13)
        self.PB_todas.setMinimumSize(QtCore.QSize(0, 120))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.PB_todas.setFont(font)
        self.PB_todas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon17 = QtGui.QIcon()
        icon17.addPixmap(
            QtGui.QPixmap("src/icons/Todas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        self.PB_todas.setIcon(icon17)
        self.PB_todas.setObjectName("PB_todas")
        self.verticalLayout_13.addWidget(self.PB_todas)
        self.gridLayout.addWidget(self.frame_13, 0, 0, 1, 1)
        self.frame_15 = QtWidgets.QFrame(self.frame_9)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PB_58 = QtWidgets.QPushButton(self.frame_15)
        self.PB_58.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_58.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_58.setObjectName("PB_58")
        self.gridLayout_2.addWidget(self.PB_58, 6, 3, 1, 1)
        self.PB_29 = QtWidgets.QPushButton(self.frame_15)
        self.PB_29.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_29.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_29.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_29.setObjectName("PB_29")
        self.gridLayout_2.addWidget(self.PB_29, 3, 1, 1, 1)
        self.PB_78 = QtWidgets.QPushButton(self.frame_15)
        self.PB_78.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_78.setMaximumSize(QtCore.QSize(80, 16777215))
        self.PB_78.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_78.setObjectName("PB_78")
        self.gridLayout_2.addWidget(self.PB_78, 9, 5, 1, 1)
        self.PB_81 = QtWidgets.QPushButton(self.frame_15)
        self.PB_81.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_81.setMaximumSize(QtCore.QSize(80, 16777215))
        self.PB_81.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_81.setObjectName("PB_81")
        self.gridLayout_2.addWidget(self.PB_81, 9, 8, 1, 1)
        self.PB_34 = QtWidgets.QPushButton(self.frame_15)
        self.PB_34.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_34.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_34.setObjectName("PB_34")
        self.gridLayout_2.addWidget(self.PB_34, 3, 6, 1, 1)
        self.PB_42 = QtWidgets.QPushButton(self.frame_15)
        self.PB_42.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_42.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_42.setObjectName("PB_42")
        self.gridLayout_2.addWidget(self.PB_42, 4, 5, 1, 1)
        self.PB_55 = QtWidgets.QPushButton(self.frame_15)
        self.PB_55.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_55.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_55.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_55.setObjectName("PB_55")
        self.gridLayout_2.addWidget(self.PB_55, 6, 0, 1, 1)
        self.PB_17 = QtWidgets.QPushButton(self.frame_15)
        self.PB_17.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_17.setObjectName("PB_17")
        self.gridLayout_2.addWidget(self.PB_17, 1, 7, 1, 1)
        self.PB_10 = QtWidgets.QPushButton(self.frame_15)
        self.PB_10.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_10.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_10.setObjectName("PB_10")
        self.gridLayout_2.addWidget(self.PB_10, 1, 0, 1, 1)
        self.PB_35 = QtWidgets.QPushButton(self.frame_15)
        self.PB_35.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_35.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_35.setObjectName("PB_35")
        self.gridLayout_2.addWidget(self.PB_35, 3, 7, 1, 1)
        self.PB_77 = QtWidgets.QPushButton(self.frame_15)
        self.PB_77.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_77.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_77.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_77.setObjectName("PB_77")
        self.gridLayout_2.addWidget(self.PB_77, 9, 4, 1, 1)
        self.PB_57 = QtWidgets.QPushButton(self.frame_15)
        self.PB_57.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_57.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_57.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_57.setObjectName("PB_57")
        self.gridLayout_2.addWidget(self.PB_57, 6, 2, 1, 1)
        self.PB_38 = QtWidgets.QPushButton(self.frame_15)
        self.PB_38.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_38.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_38.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_38.setObjectName("PB_38")
        self.gridLayout_2.addWidget(self.PB_38, 4, 1, 1, 1)
        self.PB_48 = QtWidgets.QPushButton(self.frame_15)
        self.PB_48.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_48.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_48.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_48.setObjectName("PB_48")
        self.gridLayout_2.addWidget(self.PB_48, 5, 2, 1, 1)
        self.PB_60 = QtWidgets.QPushButton(self.frame_15)
        self.PB_60.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_60.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_60.setObjectName("PB_60")
        self.gridLayout_2.addWidget(self.PB_60, 6, 5, 1, 1)
        self.PB_18 = QtWidgets.QPushButton(self.frame_15)
        self.PB_18.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_18.setObjectName("PB_18")
        self.gridLayout_2.addWidget(self.PB_18, 1, 8, 1, 1)
        self.PB_83 = QtWidgets.QPushButton(self.frame_15)
        self.PB_83.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_83.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_83.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_83.setObjectName("PB_83")
        self.gridLayout_2.addWidget(self.PB_83, 10, 1, 1, 1)
        self.PB_45 = QtWidgets.QPushButton(self.frame_15)
        self.PB_45.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_45.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_45.setObjectName("PB_45")
        self.gridLayout_2.addWidget(self.PB_45, 4, 8, 1, 1)
        self.PB_12 = QtWidgets.QPushButton(self.frame_15)
        self.PB_12.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_12.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_12.setObjectName("PB_12")
        self.gridLayout_2.addWidget(self.PB_12, 1, 2, 1, 1)
        self.PB_25 = QtWidgets.QPushButton(self.frame_15)
        self.PB_25.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_25.setObjectName("PB_25")
        self.gridLayout_2.addWidget(self.PB_25, 2, 6, 1, 1)
        self.PB_41 = QtWidgets.QPushButton(self.frame_15)
        self.PB_41.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_41.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_41.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_41.setObjectName("PB_41")
        self.gridLayout_2.addWidget(self.PB_41, 4, 4, 1, 1)
        self.PB_89 = QtWidgets.QPushButton(self.frame_15)
        self.PB_89.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_89.setMaximumSize(QtCore.QSize(80, 16777215))
        self.PB_89.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_89.setObjectName("PB_89")
        self.gridLayout_2.addWidget(self.PB_89, 10, 7, 1, 1)
        self.PB_7 = QtWidgets.QPushButton(self.frame_15)
        self.PB_7.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_7.setObjectName("PB_7")
        self.gridLayout_2.addWidget(self.PB_7, 0, 6, 1, 1)
        self.PB_40 = QtWidgets.QPushButton(self.frame_15)
        self.PB_40.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_40.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_40.setObjectName("PB_40")
        self.gridLayout_2.addWidget(self.PB_40, 4, 3, 1, 1)
        self.PB_27 = QtWidgets.QPushButton(self.frame_15)
        self.PB_27.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_27.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_27.setObjectName("PB_27")
        self.gridLayout_2.addWidget(self.PB_27, 2, 8, 1, 1)
        self.PB_79 = QtWidgets.QPushButton(self.frame_15)
        self.PB_79.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_79.setMaximumSize(QtCore.QSize(80, 16777215))
        self.PB_79.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_79.setObjectName("PB_79")
        self.gridLayout_2.addWidget(self.PB_79, 9, 6, 1, 1)
        self.PB_50 = QtWidgets.QPushButton(self.frame_15)
        self.PB_50.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_50.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_50.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_50.setObjectName("PB_50")
        self.gridLayout_2.addWidget(self.PB_50, 5, 4, 1, 1)
        self.PB_72 = QtWidgets.QPushButton(self.frame_15)
        self.PB_72.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_72.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_72.setObjectName("PB_72")
        self.gridLayout_2.addWidget(self.PB_72, 8, 8, 1, 1)
        self.PB_66 = QtWidgets.QPushButton(self.frame_15)
        self.PB_66.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_66.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_66.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_66.setObjectName("PB_66")
        self.gridLayout_2.addWidget(self.PB_66, 8, 2, 1, 1)
        self.PB_16 = QtWidgets.QPushButton(self.frame_15)
        self.PB_16.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_16.setObjectName("PB_16")
        self.gridLayout_2.addWidget(self.PB_16, 1, 6, 1, 1)
        self.PB_22 = QtWidgets.QPushButton(self.frame_15)
        self.PB_22.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_22.setObjectName("PB_22")
        self.gridLayout_2.addWidget(self.PB_22, 2, 3, 1, 1)
        self.PB_31 = QtWidgets.QPushButton(self.frame_15)
        self.PB_31.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_31.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_31.setObjectName("PB_31")
        self.gridLayout_2.addWidget(self.PB_31, 3, 3, 1, 1)
        self.PB_80 = QtWidgets.QPushButton(self.frame_15)
        self.PB_80.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_80.setMaximumSize(QtCore.QSize(80, 16777215))
        self.PB_80.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_80.setObjectName("PB_80")
        self.gridLayout_2.addWidget(self.PB_80, 9, 7, 1, 1)
        self.PB_47 = QtWidgets.QPushButton(self.frame_15)
        self.PB_47.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_47.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_47.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_47.setObjectName("PB_47")
        self.gridLayout_2.addWidget(self.PB_47, 5, 1, 1, 1)
        self.PB_1 = QtWidgets.QPushButton(self.frame_15)
        self.PB_1.setEnabled(True)
        self.PB_1.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_1.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_1.setObjectName("PB_1")
        self.gridLayout_2.addWidget(self.PB_1, 0, 0, 1, 1)
        self.PB_5 = QtWidgets.QPushButton(self.frame_15)
        self.PB_5.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_5.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_5.setObjectName("PB_5")
        self.gridLayout_2.addWidget(self.PB_5, 0, 4, 1, 1)
        self.PB_11 = QtWidgets.QPushButton(self.frame_15)
        self.PB_11.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_11.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_11.setObjectName("PB_11")
        self.gridLayout_2.addWidget(self.PB_11, 1, 1, 1, 1)
        self.PB_74 = QtWidgets.QPushButton(self.frame_15)
        self.PB_74.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_74.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_74.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_74.setObjectName("PB_74")
        self.gridLayout_2.addWidget(self.PB_74, 9, 1, 1, 1)
        self.PB_69 = QtWidgets.QPushButton(self.frame_15)
        self.PB_69.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_69.setMaximumSize(QtCore.QSize(80, 16777215))
        self.PB_69.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_69.setObjectName("PB_69")
        self.gridLayout_2.addWidget(self.PB_69, 8, 5, 1, 1)
        self.PB_32 = QtWidgets.QPushButton(self.frame_15)
        self.PB_32.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_32.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_32.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_32.setObjectName("PB_32")
        self.gridLayout_2.addWidget(self.PB_32, 3, 4, 1, 1)
        self.PB_9 = QtWidgets.QPushButton(self.frame_15)
        self.PB_9.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_9.setObjectName("PB_9")
        self.gridLayout_2.addWidget(self.PB_9, 0, 8, 1, 1)
        self.PB_13 = QtWidgets.QPushButton(self.frame_15)
        self.PB_13.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_13.setObjectName("PB_13")
        self.gridLayout_2.addWidget(self.PB_13, 1, 3, 1, 1)
        self.PB_49 = QtWidgets.QPushButton(self.frame_15)
        self.PB_49.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_49.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_49.setObjectName("PB_49")
        self.gridLayout_2.addWidget(self.PB_49, 5, 3, 1, 1)
        self.PB_21 = QtWidgets.QPushButton(self.frame_15)
        self.PB_21.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_21.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_21.setObjectName("PB_21")
        self.gridLayout_2.addWidget(self.PB_21, 2, 2, 1, 1)
        self.PB_8 = QtWidgets.QPushButton(self.frame_15)
        self.PB_8.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_8.setObjectName("PB_8")
        self.gridLayout_2.addWidget(self.PB_8, 0, 7, 1, 1)
        self.PB_39 = QtWidgets.QPushButton(self.frame_15)
        self.PB_39.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_39.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_39.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_39.setObjectName("PB_39")
        self.gridLayout_2.addWidget(self.PB_39, 4, 2, 1, 1)
        self.PB_46 = QtWidgets.QPushButton(self.frame_15)
        self.PB_46.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_46.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_46.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_46.setObjectName("PB_46")
        self.gridLayout_2.addWidget(self.PB_46, 5, 0, 1, 1)
        self.PB_76 = QtWidgets.QPushButton(self.frame_15)
        self.PB_76.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_76.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_76.setObjectName("PB_76")
        self.gridLayout_2.addWidget(self.PB_76, 9, 3, 1, 1)
        self.PB_61 = QtWidgets.QPushButton(self.frame_15)
        self.PB_61.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_61.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_61.setObjectName("PB_61")
        self.gridLayout_2.addWidget(self.PB_61, 6, 6, 1, 1)
        self.PB_3 = QtWidgets.QPushButton(self.frame_15)
        self.PB_3.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_3.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_3.setObjectName("PB_3")
        self.gridLayout_2.addWidget(self.PB_3, 0, 2, 1, 1)
        self.PB_82 = QtWidgets.QPushButton(self.frame_15)
        self.PB_82.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_82.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_82.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_82.setObjectName("PB_82")
        self.gridLayout_2.addWidget(self.PB_82, 10, 0, 1, 1)
        self.PB_65 = QtWidgets.QPushButton(self.frame_15)
        self.PB_65.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_65.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_65.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_65.setObjectName("PB_65")
        self.gridLayout_2.addWidget(self.PB_65, 8, 1, 1, 1)
        self.PB_71 = QtWidgets.QPushButton(self.frame_15)
        self.PB_71.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_71.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_71.setObjectName("PB_71")
        self.gridLayout_2.addWidget(self.PB_71, 8, 7, 1, 1)
        self.PB_64 = QtWidgets.QPushButton(self.frame_15)
        self.PB_64.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_64.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_64.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_64.setObjectName("PB_64")
        self.gridLayout_2.addWidget(self.PB_64, 8, 0, 1, 1)
        self.PB_63 = QtWidgets.QPushButton(self.frame_15)
        self.PB_63.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_63.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_63.setObjectName("PB_63")
        self.gridLayout_2.addWidget(self.PB_63, 6, 8, 1, 1)
        self.PB_73 = QtWidgets.QPushButton(self.frame_15)
        self.PB_73.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_73.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_73.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_73.setObjectName("PB_73")
        self.gridLayout_2.addWidget(self.PB_73, 9, 0, 1, 1)
        self.PB_87 = QtWidgets.QPushButton(self.frame_15)
        self.PB_87.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_87.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_87.setObjectName("PB_87")
        self.gridLayout_2.addWidget(self.PB_87, 10, 5, 1, 1)
        self.PB_19 = QtWidgets.QPushButton(self.frame_15)
        self.PB_19.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_19.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_19.setObjectName("PB_19")
        self.gridLayout_2.addWidget(self.PB_19, 2, 0, 1, 1)
        self.PB_14 = QtWidgets.QPushButton(self.frame_15)
        self.PB_14.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_14.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_14.setObjectName("PB_14")
        self.gridLayout_2.addWidget(self.PB_14, 1, 4, 1, 1)
        self.PB_51 = QtWidgets.QPushButton(self.frame_15)
        self.PB_51.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_51.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_51.setObjectName("PB_51")
        self.gridLayout_2.addWidget(self.PB_51, 5, 5, 1, 1)
        self.PB_68 = QtWidgets.QPushButton(self.frame_15)
        self.PB_68.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_68.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_68.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_68.setObjectName("PB_68")
        self.gridLayout_2.addWidget(self.PB_68, 8, 4, 1, 1)
        self.PB_85 = QtWidgets.QPushButton(self.frame_15)
        self.PB_85.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_85.setMaximumSize(QtCore.QSize(80, 16777215))
        self.PB_85.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_85.setObjectName("PB_85")
        self.gridLayout_2.addWidget(self.PB_85, 10, 3, 1, 1)
        self.PB_86 = QtWidgets.QPushButton(self.frame_15)
        self.PB_86.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_86.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_86.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_86.setObjectName("PB_86")
        self.gridLayout_2.addWidget(self.PB_86, 10, 4, 1, 1)
        self.PB_33 = QtWidgets.QPushButton(self.frame_15)
        self.PB_33.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_33.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_33.setObjectName("PB_33")
        self.gridLayout_2.addWidget(self.PB_33, 3, 5, 1, 1)
        self.PB_62 = QtWidgets.QPushButton(self.frame_15)
        self.PB_62.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_62.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_62.setObjectName("PB_62")
        self.gridLayout_2.addWidget(self.PB_62, 6, 7, 1, 1)
        self.PB_4 = QtWidgets.QPushButton(self.frame_15)
        self.PB_4.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_4.setObjectName("PB_4")
        self.gridLayout_2.addWidget(self.PB_4, 0, 3, 1, 1)
        self.PB_88 = QtWidgets.QPushButton(self.frame_15)
        self.PB_88.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_88.setMaximumSize(QtCore.QSize(80, 16777215))
        self.PB_88.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_88.setObjectName("PB_88")
        self.gridLayout_2.addWidget(self.PB_88, 10, 6, 1, 1)
        self.PB_2 = QtWidgets.QPushButton(self.frame_15)
        self.PB_2.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_2.setObjectName("PB_2")
        self.gridLayout_2.addWidget(self.PB_2, 0, 1, 1, 1)
        self.PB_30 = QtWidgets.QPushButton(self.frame_15)
        self.PB_30.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_30.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_30.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_30.setObjectName("PB_30")
        self.gridLayout_2.addWidget(self.PB_30, 3, 2, 1, 1)
        self.PB_28 = QtWidgets.QPushButton(self.frame_15)
        self.PB_28.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_28.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_28.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_28.setObjectName("PB_28")
        self.gridLayout_2.addWidget(self.PB_28, 3, 0, 1, 1)
        self.PB_37 = QtWidgets.QPushButton(self.frame_15)
        self.PB_37.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_37.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_37.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_37.setObjectName("PB_37")
        self.gridLayout_2.addWidget(self.PB_37, 4, 0, 1, 1)
        self.PB_56 = QtWidgets.QPushButton(self.frame_15)
        self.PB_56.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_56.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_56.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_56.setObjectName("PB_56")
        self.gridLayout_2.addWidget(self.PB_56, 6, 1, 1, 1)
        self.PB_36 = QtWidgets.QPushButton(self.frame_15)
        self.PB_36.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_36.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_36.setObjectName("PB_36")
        self.gridLayout_2.addWidget(self.PB_36, 3, 8, 1, 1)
        self.PB_44 = QtWidgets.QPushButton(self.frame_15)
        self.PB_44.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_44.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_44.setObjectName("PB_44")
        self.gridLayout_2.addWidget(self.PB_44, 4, 7, 1, 1)
        self.PB_53 = QtWidgets.QPushButton(self.frame_15)
        self.PB_53.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_53.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_53.setObjectName("PB_53")
        self.gridLayout_2.addWidget(self.PB_53, 5, 7, 1, 1)
        self.PB_59 = QtWidgets.QPushButton(self.frame_15)
        self.PB_59.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_59.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_59.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_59.setObjectName("PB_59")
        self.gridLayout_2.addWidget(self.PB_59, 6, 4, 1, 1)
        self.PB_52 = QtWidgets.QPushButton(self.frame_15)
        self.PB_52.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_52.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_52.setObjectName("PB_52")
        self.gridLayout_2.addWidget(self.PB_52, 5, 6, 1, 1)
        self.PB_70 = QtWidgets.QPushButton(self.frame_15)
        self.PB_70.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_70.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_70.setObjectName("PB_70")
        self.gridLayout_2.addWidget(self.PB_70, 8, 6, 1, 1)
        self.PB_90 = QtWidgets.QPushButton(self.frame_15)
        self.PB_90.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_90.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_90.setObjectName("PB_90")
        self.gridLayout_2.addWidget(self.PB_90, 10, 8, 1, 1)
        self.PB_15 = QtWidgets.QPushButton(self.frame_15)
        self.PB_15.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_15.setObjectName("PB_15")
        self.gridLayout_2.addWidget(self.PB_15, 1, 5, 1, 1)
        self.PB_20 = QtWidgets.QPushButton(self.frame_15)
        self.PB_20.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_20.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_20.setObjectName("PB_20")
        self.gridLayout_2.addWidget(self.PB_20, 2, 1, 1, 1)
        self.PB_75 = QtWidgets.QPushButton(self.frame_15)
        self.PB_75.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_75.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_75.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_75.setObjectName("PB_75")
        self.gridLayout_2.addWidget(self.PB_75, 9, 2, 1, 1)
        self.PB_54 = QtWidgets.QPushButton(self.frame_15)
        self.PB_54.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_54.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_54.setObjectName("PB_54")
        self.gridLayout_2.addWidget(self.PB_54, 5, 8, 1, 1)
        self.PB_67 = QtWidgets.QPushButton(self.frame_15)
        self.PB_67.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_67.setMaximumSize(QtCore.QSize(80, 16777215))
        self.PB_67.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_67.setObjectName("PB_67")
        self.gridLayout_2.addWidget(self.PB_67, 8, 3, 1, 1)
        self.PB_84 = QtWidgets.QPushButton(self.frame_15)
        self.PB_84.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_84.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_84.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_84.setObjectName("PB_84")
        self.gridLayout_2.addWidget(self.PB_84, 10, 2, 1, 1)
        self.PB_24 = QtWidgets.QPushButton(self.frame_15)
        self.PB_24.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_24.setObjectName("PB_24")
        self.gridLayout_2.addWidget(self.PB_24, 2, 5, 1, 1)
        self.PB_23 = QtWidgets.QPushButton(self.frame_15)
        self.PB_23.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_23.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_23.setObjectName("PB_23")
        self.gridLayout_2.addWidget(self.PB_23, 2, 4, 1, 1)
        self.PB_26 = QtWidgets.QPushButton(self.frame_15)
        self.PB_26.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_26.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_26.setObjectName("PB_26")
        self.gridLayout_2.addWidget(self.PB_26, 2, 7, 1, 1)
        self.PB_43 = QtWidgets.QPushButton(self.frame_15)
        self.PB_43.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_43.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_43.setObjectName("PB_43")
        self.gridLayout_2.addWidget(self.PB_43, 4, 6, 1, 1)
        self.PB_92 = QtWidgets.QPushButton(self.frame_15)
        self.PB_92.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_92.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_92.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_92.setObjectName("PB_92")
        self.gridLayout_2.addWidget(self.PB_92, 12, 1, 1, 1)
        self.PB_6 = QtWidgets.QPushButton(self.frame_15)
        self.PB_6.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_6.setObjectName("PB_6")
        self.gridLayout_2.addWidget(self.PB_6, 0, 5, 1, 1)
        self.PB_91 = QtWidgets.QPushButton(self.frame_15)
        self.PB_91.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_91.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_91.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_91.setObjectName("PB_91")
        self.gridLayout_2.addWidget(self.PB_91, 12, 0, 1, 1)
        self.PB_93 = QtWidgets.QPushButton(self.frame_15)
        self.PB_93.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_93.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_93.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_93.setObjectName("PB_93")
        self.gridLayout_2.addWidget(self.PB_93, 12, 2, 1, 1)
        self.PB_94 = QtWidgets.QPushButton(self.frame_15)
        self.PB_94.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_94.setMaximumSize(QtCore.QSize(80, 16777215))
        self.PB_94.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_94.setObjectName("PB_94")
        self.gridLayout_2.addWidget(self.PB_94, 12, 3, 1, 1)
        self.PB_95 = QtWidgets.QPushButton(self.frame_15)
        self.PB_95.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_95.setMaximumSize(QtCore.QSize(75, 16777215))
        self.PB_95.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_95.setObjectName("PB_95")
        self.gridLayout_2.addWidget(self.PB_95, 12, 4, 1, 1)
        self.PB_96 = QtWidgets.QPushButton(self.frame_15)
        self.PB_96.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_96.setMaximumSize(QtCore.QSize(80, 16777215))
        self.PB_96.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_96.setObjectName("PB_96")
        self.gridLayout_2.addWidget(self.PB_96, 12, 5, 1, 1)
        self.PB_97 = QtWidgets.QPushButton(self.frame_15)
        self.PB_97.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_97.setMaximumSize(QtCore.QSize(80, 16777215))
        self.PB_97.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_97.setObjectName("PB_97")
        self.gridLayout_2.addWidget(self.PB_97, 12, 6, 1, 1)
        self.PB_98 = QtWidgets.QPushButton(self.frame_15)
        self.PB_98.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_98.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_98.setObjectName("PB_98")
        self.gridLayout_2.addWidget(self.PB_98, 12, 7, 1, 1)
        self.PB_99 = QtWidgets.QPushButton(self.frame_15)
        self.PB_99.setMinimumSize(QtCore.QSize(0, 35))
        self.PB_99.setMaximumSize(QtCore.QSize(80, 16777215))
        self.PB_99.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PB_99.setObjectName("PB_99")
        self.gridLayout_2.addWidget(self.PB_99, 12, 8, 1, 1)
        self.gridLayout.addWidget(self.frame_15, 0, 1, 2, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.verticalLayout_9.addWidget(self.frame_9)
        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 8)
        self.verticalLayout_8.addWidget(self.frame_6)
        self.frame_8 = QtWidgets.QFrame(self.page_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_3 = QtWidgets.QLabel(self.frame_11)
        self.label_3.setGeometry(QtCore.QRect(390, 10, 63, 20))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_10.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.frame_8)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.frame_12.setStyleSheet("QFrame#frame_12 { border: 2px solid orange; }")

 


 

        # 
 

        layout = QtWidgets.QHBoxLayout(self.frame_12)
 


 

        self.button_run = QtWidgets.QPushButton("RUN", self.frame_12)
 

        self.button_run.setCursor(QtCore.Qt.PointingHandCursor)
 

        self.button_run.setFixedHeight(40)
 

        self.button_run.setStyleSheet("""
 

            QPushButton {
 

                background-color: white;  # Color de fondo
 

                color: black;  # Color del texto
 

                font-size: 16px;  # Tamaño de la fuente
 

                border-radius: 10px;  # Bordes redondeados
 

            }
 

            QPushButton:hover {
 

                background-color: #f0f0f0;  # Color de fondo cuando el mouse está encima
 

            }
 

        """)
 

        layout.addWidget(self.button_run)
 


 

        direction_group = QtWidgets.QGroupBox("CAMBIAR DIRECCIÓN", self.frame_12)
 

        direction_group.setStyleSheet("QGroupBox { color: white; }")
 

        direction_layout = QtWidgets.QHBoxLayout()
 


 

        self.button_left = QtWidgets.QPushButton("←", self.frame_12)
 

        self.button_left.setCursor(QtCore.Qt.PointingHandCursor)
 

        self.button_left.setFixedSize(60, 60)
 

        self.button_left.setStyleSheet("""
 

            QPushButton {
 

                background-color: white;
 

                color: black;
 

                font-size: 20px;
 

                border-radius: 10px;
 

            }
 

            QPushButton:hover {
 

                background-color: #f0f0f0;
 

            }
 

        """)
 


 

        self.button_right = QtWidgets.QPushButton("→", self.frame_12)
 

        self.button_right.setCursor(QtCore.Qt.PointingHandCursor)
 

        self.button_right.setFixedSize(60, 60)
 

        self.button_right.setStyleSheet("""
 

            QPushButton {
 

                background-color: white;
 

                color: black;
 

                font-size: 20px;
 

                border-radius: 10px;
 

            }
 

            QPushButton:hover {
 

                background-color: #f0f0f0;
 

            }
 

        """)
 


 

        direction_layout.addWidget(self.button_left)
 

        direction_layout.addWidget(self.button_right)
 


 

        direction_group.setLayout(direction_layout)
 


 

        layout.addWidget(direction_group)
 


 

        speed_group = QtWidgets.QGroupBox("CAMBIAR VELOCIDAD", self.frame_12)
 

        speed_group.setStyleSheet("QGroupBox { color: white; }")
 

        speed_layout = QtWidgets.QHBoxLayout()
 


 

        self.button_low_speed = QtWidgets.QPushButton("BAJA", self.frame_12)
 

        self.button_low_speed.setCursor(QtCore.Qt.PointingHandCursor)
 

        self.button_low_speed.setFixedSize(100, 40)
 

        self.button_low_speed.setStyleSheet("""
 

            QPushButton {
 

                background-color: white;
 

                color: black;
 

                font-size: 14px;
 

                border-radius: 10px;
 

            }
 

            QPushButton:hover {
 

                background-color: #f0f0f0;
 

            }
 

        """)
 


 

        self.button_medium_speed = QtWidgets.QPushButton("MEDIA", self.frame_12)
 

        self.button_medium_speed.setCursor(QtCore.Qt.PointingHandCursor)
 

        self.button_medium_speed.setFixedSize(100, 40)
 

        self.button_medium_speed.setStyleSheet("""
 

            QPushButton {
 

                background-color: white;
 

                color: black;
 

                font-size: 14px;
 

                border-radius: 10px;
 

            }
 

            QPushButton:hover {
 

                background-color: #f0f0f0;
 

            }
 

        """)
 


 

        self.button_high_speed = QtWidgets.QPushButton("ALTA", self.frame_12)
 

        self.button_high_speed.setCursor(QtCore.Qt.PointingHandCursor)
 

        self.button_high_speed.setFixedSize(100, 40)
 

        self.button_high_speed.setStyleSheet("""
 

            QPushButton {
 

                background-color: white;
 

                color: black;
 

                font-size: 14px;
 

                border-radius: 10px;
 

            }
 

            QPushButton:hover {
 

                background-color: #f0f0f0;
 

            }
 

        """)
 


 

        speed_layout.addWidget(self.button_low_speed)
 

        speed_layout.addWidget(self.button_medium_speed)
 

        speed_layout.addWidget(self.button_high_speed)
 


 

        speed_group.setLayout(speed_layout)
 


 

        layout.addWidget(speed_group)
 


 

        layout.setSpacing(10)
 

        layout.setAlignment(QtCore.Qt.AlignTop)
        self.verticalLayout_10.addWidget(self.frame_12)
        self.verticalLayout_10.setStretch(0, 2)
        self.verticalLayout_10.setStretch(1, 10)
        self.verticalLayout_8.addWidget(self.frame_8)
        self.verticalLayout_8.setStretch(0, 3)
        self.verticalLayout_8.setStretch(1, 2)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.horizontalLayout_4.setStretch(0, 2)
        self.verticalLayout.addWidget(self.frame_cuerpo)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 12)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PB_produc.setText(_translate("MainWindow", " Producción"))
        self.PB_test.setText(_translate("MainWindow", " Testeo"))
        self.PB_config.setText(_translate("MainWindow", " Configuración"))
        self.PB_ayuda.setText(_translate("MainWindow", " Ayuda"))
        self.PB_apagar.setText(_translate("MainWindow", "  APAGAR"))
        self.label.setText(_translate("MainWindow", "Camara #1"))
        self.label_8.setText(
            _translate("MainWindow", "Selecciona lo que quieres procesar")
        )
        self.label_11.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "# de Betas:"))
        self.label_10.setText(_translate("MainWindow", "# de Cajas:"))
        self.label_12.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "Activaciones Individuales"))
        self.label_14.setText(_translate("MainWindow", "Grabar"))
        self.label_15.setText(_translate("MainWindow", "Valvulas"))
        self.label_16.setText(_translate("MainWindow", "Banda"))
        self.label_21.setText(_translate("MainWindow", "Saranda"))
        self.label_22.setText(_translate("MainWindow", "Alimentad"))
        self.label_23.setText(_translate("MainWindow", "Rampa"))
        self.label_5.setText(_translate("MainWindow", "Ayuda"))
        self.label_4.setText(_translate("MainWindow", "Alineaciòn de las camaras"))
        self.PB_grid.setText(_translate("MainWindow", "Grid"))
        self.label_6.setText(_translate("MainWindow", "Color de Fondo (RGB)"))
        self.label_7.setText(_translate("MainWindow", "Iluminación"))
        self.PB_fondo.setText(_translate("MainWindow", "Cargar"))
        self.L_iluminacion.setText(_translate("MainWindow", "0%"))
        self.L_iluminacion_2.setText(_translate("MainWindow", "0%"))
        self.L_iluminacion_3.setText(_translate("MainWindow", "0%"))
        self.L_iluminacion_4.setText(_translate("MainWindow", "0%"))
        self.label_17.setText(_translate("MainWindow", "Velocidad de la Banda"))
        self.PB_banda.setText(_translate("MainWindow", "Cargar"))
        self.label_18.setText(_translate("MainWindow", "RPM:"))
        self.label_20.setText(_translate("MainWindow", "Velocidad de la Saranda"))
        self.label_24.setText(_translate("MainWindow", "Hz:"))
        self.PB_saranda.setText(_translate("MainWindow", "Cargar"))
        self.label_2.setText(_translate("MainWindow", "Valvulas"))
        self.pb_cycle.setText(_translate("MainWindow", "Ciclo"))
        self.PB_todas.setText(_translate("MainWindow", "Todas"))
        self.PB_58.setText(_translate("MainWindow", "Sal. 58"))
        self.PB_29.setText(_translate("MainWindow", "Sal. 29"))
        self.PB_78.setText(_translate("MainWindow", "Sal. 78"))
        self.PB_81.setText(_translate("MainWindow", "Sal. 81"))
        self.PB_34.setText(_translate("MainWindow", "Sal. 34"))
        self.PB_42.setText(_translate("MainWindow", "Sal. 42"))
        self.PB_55.setText(_translate("MainWindow", "Sal. 55"))
        self.PB_17.setText(_translate("MainWindow", "Sal. 17"))
        self.PB_10.setText(_translate("MainWindow", "Sal. 10"))
        self.PB_35.setText(_translate("MainWindow", "Sal. 35"))
        self.PB_77.setText(_translate("MainWindow", "Sal. 77"))
        self.PB_57.setText(_translate("MainWindow", "Sal. 57"))
        self.PB_38.setText(_translate("MainWindow", "Sal. 38"))
        self.PB_48.setText(_translate("MainWindow", "Sal. 48"))
        self.PB_60.setText(_translate("MainWindow", "Sal. 60"))
        self.PB_18.setText(_translate("MainWindow", "Sal. 18"))
        self.PB_83.setText(_translate("MainWindow", "Sal. 83"))
        self.PB_45.setText(_translate("MainWindow", "Sal. 45"))
        self.PB_12.setText(_translate("MainWindow", "Sal. 12"))
        self.PB_25.setText(_translate("MainWindow", "Sal. 25"))
        self.PB_41.setText(_translate("MainWindow", "Sal. 41"))
        self.PB_89.setText(_translate("MainWindow", "Sal. 89"))
        self.PB_7.setText(_translate("MainWindow", "Sal. 7"))
        self.PB_40.setText(_translate("MainWindow", "Sal. 40"))
        self.PB_27.setText(_translate("MainWindow", "Sal. 27"))
        self.PB_79.setText(_translate("MainWindow", "Sal. 79"))
        self.PB_50.setText(_translate("MainWindow", "Sal. 50"))
        self.PB_72.setText(_translate("MainWindow", "Sal. 72"))
        self.PB_66.setText(_translate("MainWindow", "Sal. 66"))
        self.PB_16.setText(_translate("MainWindow", "Sal. 16"))
        self.PB_22.setText(_translate("MainWindow", "Sal. 22"))
        self.PB_31.setText(_translate("MainWindow", "Sal. 31"))
        self.PB_80.setText(_translate("MainWindow", "Sal. 80"))
        self.PB_47.setText(_translate("MainWindow", "Sal. 47"))
        self.PB_1.setText(_translate("MainWindow", "Sal. 1"))
        self.PB_5.setText(_translate("MainWindow", "Sal. 5"))
        self.PB_11.setText(_translate("MainWindow", "Sal. 11"))
        self.PB_74.setText(_translate("MainWindow", "Sal. 74"))
        self.PB_69.setText(_translate("MainWindow", "Sal. 69"))
        self.PB_32.setText(_translate("MainWindow", "Sal. 32"))
        self.PB_9.setText(_translate("MainWindow", "Sal. 9"))
        self.PB_13.setText(_translate("MainWindow", "Sal. 13"))
        self.PB_49.setText(_translate("MainWindow", "Sal. 49"))
        self.PB_21.setText(_translate("MainWindow", "Sal. 21"))
        self.PB_8.setText(_translate("MainWindow", "Sal. 8"))
        self.PB_39.setText(_translate("MainWindow", "Sal. 39"))
        self.PB_46.setText(_translate("MainWindow", "Sal. 46"))
        self.PB_76.setText(_translate("MainWindow", "Sal. 76"))
        self.PB_61.setText(_translate("MainWindow", "Sal. 61"))
        self.PB_3.setText(_translate("MainWindow", "Sal. 3"))
        self.PB_82.setText(_translate("MainWindow", "Sal. 82"))
        self.PB_65.setText(_translate("MainWindow", "Sal. 65"))
        self.PB_71.setText(_translate("MainWindow", "Sal. 71"))
        self.PB_64.setText(_translate("MainWindow", "Sal. 64"))
        self.PB_63.setText(_translate("MainWindow", "Sal. 63"))
        self.PB_73.setText(_translate("MainWindow", "Sal. 73"))
        self.PB_87.setText(_translate("MainWindow", "Sal. 87"))
        self.PB_19.setText(_translate("MainWindow", "Sal. 19"))
        self.PB_14.setText(_translate("MainWindow", "Sal. 14"))
        self.PB_51.setText(_translate("MainWindow", "Sal. 51"))
        self.PB_68.setText(_translate("MainWindow", "Sal. 68"))
        self.PB_85.setText(_translate("MainWindow", "Sal. 85"))
        self.PB_86.setText(_translate("MainWindow", "Sal. 86"))
        self.PB_33.setText(_translate("MainWindow", "Sal. 33"))
        self.PB_62.setText(_translate("MainWindow", "Sal. 62"))
        self.PB_4.setText(_translate("MainWindow", "Sal. 4"))
        self.PB_88.setText(_translate("MainWindow", "Sal. 88"))
        self.PB_2.setText(_translate("MainWindow", "Sal. 2"))
        self.PB_30.setText(_translate("MainWindow", "Sal. 30"))
        self.PB_28.setText(_translate("MainWindow", "Sal. 28"))
        self.PB_37.setText(_translate("MainWindow", "Sal. 37"))
        self.PB_56.setText(_translate("MainWindow", "Sal. 56"))
        self.PB_36.setText(_translate("MainWindow", "Sal. 36"))
        self.PB_44.setText(_translate("MainWindow", "Sal. 44"))
        self.PB_53.setText(_translate("MainWindow", "Sal. 53"))
        self.PB_59.setText(_translate("MainWindow", "Sal. 59"))
        self.PB_52.setText(_translate("MainWindow", "Sal. 52"))
        self.PB_70.setText(_translate("MainWindow", "Sal. 70"))
        self.PB_90.setText(_translate("MainWindow", "Sal. 90"))
        self.PB_15.setText(_translate("MainWindow", "Sal. 15"))
        self.PB_20.setText(_translate("MainWindow", "Sal. 20"))
        self.PB_75.setText(_translate("MainWindow", "Sal. 75"))
        self.PB_54.setText(_translate("MainWindow", "Sal. 54"))
        self.PB_67.setText(_translate("MainWindow", "Sal. 67"))
        self.PB_84.setText(_translate("MainWindow", "Sal. 84"))
        self.PB_24.setText(_translate("MainWindow", "Sal. 24"))
        self.PB_23.setText(_translate("MainWindow", "Sal. 23"))
        self.PB_26.setText(_translate("MainWindow", "Sal. 26"))
        self.PB_43.setText(_translate("MainWindow", "Sal. 43"))
        self.PB_92.setText(_translate("MainWindow", "Sal. 92"))
        self.PB_6.setText(_translate("MainWindow", "Sal. 6"))
        self.PB_91.setText(_translate("MainWindow", "Sal. 91"))
        self.PB_93.setText(_translate("MainWindow", "Sal. 93"))
        self.PB_94.setText(_translate("MainWindow", "Sal. 94"))
        self.PB_95.setText(_translate("MainWindow", "Sal. 95"))
        self.PB_96.setText(_translate("MainWindow", "Sal. 96"))
        self.PB_97.setText(_translate("MainWindow", "Sal. 97"))
        self.PB_98.setText(_translate("MainWindow", "Sal. 98"))
        self.PB_99.setText(_translate("MainWindow", "Sal. 99"))
        self.label_3.setText(_translate("MainWindow", "Motores"))

    def stylos(self):
        url = "src/style.qss"
        try:
            with open(url, "r", encoding="utf-8") as file:
                css = file.read()
                return css
        except:
            print("No cargo el archivo")
            return ""

    def update_gif(self):
        self.gif_item.setPixmap(self.movie.currentPixmap())

        self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsView.centerOn(self.gif_item)

    def set_gif_visibility(self, visible):
        self.gif_item.setVisible(visible)
        
        if visible:
            self.video_widget.hide()  # Ocultar el video cuando se muestra el gif
        else:
            self.video_widget.show()  # Mostrar el video cuando el gif está oculto

    def view_media_player(self, path):
        self.video_widget.show()
        self.media_content = QMediaContent(QtCore.QUrl.fromLocalFile(path))
        self.media_player.setMedia(self.media_content)
        self.media_player.play()
    
    def reiniciar_sistema_video(self):
        self.media_player.stop()

        try:
            self.media_player.setSource(QUrl())  # PyQt6
        except AttributeError:

            self.media_player.setMedia(QMediaContent())  # PyQt5

        if self.video_widget.parent():
            self.video_area.removeWidget(self.video_widget)
            self.video_widget.deleteLater()
        
        self.video_widget = QVideoWidget()
        self.video_area.addWidget(self.video_widget)
        self.video_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.video_widget.setAspectRatioMode(QtCore.Qt.IgnoreAspectRatio)
        self.media_player.setVideoOutput(self.video_widget)
        self.video_widget.show()

        self.video_widget.repaint()
        self.centralwidget.update()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Control()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
