# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

from plot_widget import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QSize(1080, 720))
        MainWindow.setMaximumSize(QSize(1080, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.actionsFrame = QFrame(self.centralwidget)
        self.actionsFrame.setObjectName(u"actionsFrame")
        self.actionsFrame.setGeometry(QRect(10, 10, 260, 660))
        self.actionsFrame.setMinimumSize(QSize(260, 660))
        self.actionsFrame.setMaximumSize(QSize(260, 660))
        self.actionsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.actionsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.actionsFrame)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 5, -1, -1)
        self.uartFrame = QFrame(self.actionsFrame)
        self.uartFrame.setObjectName(u"uartFrame")
        self.uartFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.uartFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.uartFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.uartLabel = QLabel(self.uartFrame)
        self.uartLabel.setObjectName(u"uartLabel")
        self.uartLabel.setMinimumSize(QSize(220, 25))
        self.uartLabel.setMaximumSize(QSize(220, 25))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.uartLabel.setFont(font)
        self.uartLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.uartLabel)

        self.uartParametersFrame = QFrame(self.uartFrame)
        self.uartParametersFrame.setObjectName(u"uartParametersFrame")
        self.uartParametersFrame.setMinimumSize(QSize(220, 35))
        self.uartParametersFrame.setMaximumSize(QSize(220, 35))
        self.uartParametersFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.uartParametersFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.uartParametersFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comLabel = QLabel(self.uartParametersFrame)
        self.comLabel.setObjectName(u"comLabel")
        self.comLabel.setMinimumSize(QSize(50, 20))
        self.comLabel.setMaximumSize(QSize(50, 20))
        self.comLabel.setSizeIncrement(QSize(0, 0))
        self.comLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.comLabel)

        self.baudLabel = QLabel(self.uartParametersFrame)
        self.baudLabel.setObjectName(u"baudLabel")
        self.baudLabel.setMinimumSize(QSize(90, 20))
        self.baudLabel.setMaximumSize(QSize(90, 20))
        self.baudLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.baudLabel)

        self.uartStatusLabel = QLabel(self.uartParametersFrame)
        self.uartStatusLabel.setObjectName(u"uartStatusLabel")
        self.uartStatusLabel.setMinimumSize(QSize(50, 20))
        self.uartStatusLabel.setMaximumSize(QSize(50, 20))
        self.uartStatusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.uartStatusLabel)


        self.verticalLayout.addWidget(self.uartParametersFrame)

        self.uartInWidgetsFrame = QFrame(self.uartFrame)
        self.uartInWidgetsFrame.setObjectName(u"uartInWidgetsFrame")
        self.uartInWidgetsFrame.setMinimumSize(QSize(230, 45))
        self.uartInWidgetsFrame.setMaximumSize(QSize(230, 45))
        self.uartInWidgetsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.uartInWidgetsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.uartInWidgetsFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comComboBox = QComboBox(self.uartInWidgetsFrame)
        self.comComboBox.setObjectName(u"comComboBox")
        self.comComboBox.setMinimumSize(QSize(65, 25))
        self.comComboBox.setMaximumSize(QSize(65, 25))

        self.horizontalLayout_2.addWidget(self.comComboBox)

        self.baudComboBox = QComboBox(self.uartInWidgetsFrame)
        self.baudComboBox.setObjectName(u"baudComboBox")
        self.baudComboBox.setMinimumSize(QSize(70, 25))
        self.baudComboBox.setMaximumSize(QSize(70, 25))

        self.horizontalLayout_2.addWidget(self.baudComboBox)

        self.statusStateLabel = QLabel(self.uartInWidgetsFrame)
        self.statusStateLabel.setObjectName(u"statusStateLabel")
        self.statusStateLabel.setMinimumSize(QSize(75, 25))
        self.statusStateLabel.setMaximumSize(QSize(75, 25))
        self.statusStateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.statusStateLabel)


        self.verticalLayout.addWidget(self.uartInWidgetsFrame)

        self.uartOutWidgetsFrame = QFrame(self.uartFrame)
        self.uartOutWidgetsFrame.setObjectName(u"uartOutWidgetsFrame")
        self.uartOutWidgetsFrame.setMinimumSize(QSize(220, 75))
        self.uartOutWidgetsFrame.setMaximumSize(QSize(220, 75))
        self.uartOutWidgetsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.uartOutWidgetsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.uartOutWidgetsFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.connectUartButton = QPushButton(self.uartOutWidgetsFrame)
        self.connectUartButton.setObjectName(u"connectUartButton")

        self.verticalLayout_6.addWidget(self.connectUartButton)

        self.disconnectUartButton = QPushButton(self.uartOutWidgetsFrame)
        self.disconnectUartButton.setObjectName(u"disconnectUartButton")

        self.verticalLayout_6.addWidget(self.disconnectUartButton)


        self.verticalLayout.addWidget(self.uartOutWidgetsFrame)


        self.verticalLayout_4.addWidget(self.uartFrame)

        self.pidFrame = QFrame(self.actionsFrame)
        self.pidFrame.setObjectName(u"pidFrame")
        self.pidFrame.setMinimumSize(QSize(240, 190))
        self.pidFrame.setMaximumSize(QSize(240, 190))
        self.pidFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.pidFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.pidFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pidLabel = QLabel(self.pidFrame)
        self.pidLabel.setObjectName(u"pidLabel")
        self.pidLabel.setMinimumSize(QSize(220, 25))
        self.pidLabel.setMaximumSize(QSize(220, 25))
        self.pidLabel.setFont(font)
        self.pidLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.pidLabel)

        self.pidParametersFrame = QFrame(self.pidFrame)
        self.pidParametersFrame.setObjectName(u"pidParametersFrame")
        self.pidParametersFrame.setMinimumSize(QSize(220, 45))
        self.pidParametersFrame.setMaximumSize(QSize(220, 45))
        self.pidParametersFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.pidParametersFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.pidParametersFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.kpLabel = QLabel(self.pidParametersFrame)
        self.kpLabel.setObjectName(u"kpLabel")
        self.kpLabel.setMinimumSize(QSize(50, 20))
        self.kpLabel.setMaximumSize(QSize(50, 20))
        self.kpLabel.setSizeIncrement(QSize(0, 0))
        self.kpLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.kpLabel)

        self.kiLabel = QLabel(self.pidParametersFrame)
        self.kiLabel.setObjectName(u"kiLabel")
        self.kiLabel.setMinimumSize(QSize(90, 20))
        self.kiLabel.setMaximumSize(QSize(90, 20))
        self.kiLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.kiLabel)

        self.kdLabel = QLabel(self.pidParametersFrame)
        self.kdLabel.setObjectName(u"kdLabel")
        self.kdLabel.setMinimumSize(QSize(50, 20))
        self.kdLabel.setMaximumSize(QSize(50, 20))
        self.kdLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.kdLabel)


        self.verticalLayout_2.addWidget(self.pidParametersFrame)

        self.pidParametersWidgets = QFrame(self.pidFrame)
        self.pidParametersWidgets.setObjectName(u"pidParametersWidgets")
        self.pidParametersWidgets.setMinimumSize(QSize(220, 45))
        self.pidParametersWidgets.setMaximumSize(QSize(220, 45))
        self.pidParametersWidgets.setFrameShape(QFrame.Shape.StyledPanel)
        self.pidParametersWidgets.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.pidParametersWidgets)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.kpSpinBox = QDoubleSpinBox(self.pidParametersWidgets)
        self.kpSpinBox.setObjectName(u"kpSpinBox")
        self.kpSpinBox.setDecimals(5)
        self.kpSpinBox.setMaximum(99.999989999999997)

        self.horizontalLayout_4.addWidget(self.kpSpinBox)

        self.kiSpinBox = QDoubleSpinBox(self.pidParametersWidgets)
        self.kiSpinBox.setObjectName(u"kiSpinBox")
        self.kiSpinBox.setDecimals(5)
        self.kiSpinBox.setMaximum(100.000000000000000)

        self.horizontalLayout_4.addWidget(self.kiSpinBox)

        self.kdSpinBox = QDoubleSpinBox(self.pidParametersWidgets)
        self.kdSpinBox.setObjectName(u"kdSpinBox")
        self.kdSpinBox.setDecimals(5)
        self.kdSpinBox.setMaximum(100.000000000000000)

        self.horizontalLayout_4.addWidget(self.kdSpinBox)


        self.verticalLayout_2.addWidget(self.pidParametersWidgets)

        self.updatePidFrame = QFrame(self.pidFrame)
        self.updatePidFrame.setObjectName(u"updatePidFrame")
        self.updatePidFrame.setMinimumSize(QSize(220, 45))
        self.updatePidFrame.setMaximumSize(QSize(220, 45))
        self.updatePidFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.updatePidFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.updatePidFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.updatePidButton = QPushButton(self.updatePidFrame)
        self.updatePidButton.setObjectName(u"updatePidButton")

        self.horizontalLayout_5.addWidget(self.updatePidButton)


        self.verticalLayout_2.addWidget(self.updatePidFrame)


        self.verticalLayout_4.addWidget(self.pidFrame)

        self.motorFrame = QFrame(self.actionsFrame)
        self.motorFrame.setObjectName(u"motorFrame")
        self.motorFrame.setMinimumSize(QSize(240, 200))
        self.motorFrame.setMaximumSize(QSize(240, 150))
        self.motorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.motorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.motorFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.motorLabel = QLabel(self.motorFrame)
        self.motorLabel.setObjectName(u"motorLabel")
        self.motorLabel.setMinimumSize(QSize(220, 25))
        self.motorLabel.setMaximumSize(QSize(220, 25))
        self.motorLabel.setFont(font)
        self.motorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.motorLabel)

        self.motorInWidgetsFrame = QFrame(self.motorFrame)
        self.motorInWidgetsFrame.setObjectName(u"motorInWidgetsFrame")
        self.motorInWidgetsFrame.setMinimumSize(QSize(220, 45))
        self.motorInWidgetsFrame.setMaximumSize(QSize(220, 45))
        self.motorInWidgetsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.motorInWidgetsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.motorInWidgetsFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.motorTargetAngleSpinBox = QSpinBox(self.motorInWidgetsFrame)
        self.motorTargetAngleSpinBox.setObjectName(u"motorTargetAngleSpinBox")
        self.motorTargetAngleSpinBox.setMinimumSize(QSize(50, 30))
        font1 = QFont()
        font1.setPointSize(14)
        self.motorTargetAngleSpinBox.setFont(font1)
        self.motorTargetAngleSpinBox.setMinimum(-360)
        self.motorTargetAngleSpinBox.setMaximum(360)

        self.horizontalLayout_7.addWidget(self.motorTargetAngleSpinBox)

        self.motorInAngleRangeLabel = QLabel(self.motorInWidgetsFrame)
        self.motorInAngleRangeLabel.setObjectName(u"motorInAngleRangeLabel")
        font2 = QFont()
        font2.setPointSize(10)
        self.motorInAngleRangeLabel.setFont(font2)
        self.motorInAngleRangeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.motorInAngleRangeLabel)


        self.verticalLayout_3.addWidget(self.motorInWidgetsFrame)

        self.motorOutWidgetsFrame = QFrame(self.motorFrame)
        self.motorOutWidgetsFrame.setObjectName(u"motorOutWidgetsFrame")
        self.motorOutWidgetsFrame.setMinimumSize(QSize(220, 100))
        self.motorOutWidgetsFrame.setMaximumSize(QSize(220, 100))
        self.motorOutWidgetsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.motorOutWidgetsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.motorOutWidgetsFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.moveMotorButton = QPushButton(self.motorOutWidgetsFrame)
        self.moveMotorButton.setObjectName(u"moveMotorButton")

        self.verticalLayout_5.addWidget(self.moveMotorButton)

        self.stopMotorButton = QPushButton(self.motorOutWidgetsFrame)
        self.stopMotorButton.setObjectName(u"stopMotorButton")

        self.verticalLayout_5.addWidget(self.stopMotorButton)


        self.verticalLayout_3.addWidget(self.motorOutWidgetsFrame)


        self.verticalLayout_4.addWidget(self.motorFrame)

        self.statusFrame = QFrame(self.centralwidget)
        self.statusFrame.setObjectName(u"statusFrame")
        self.statusFrame.setGeometry(QRect(280, 560, 790, 110))
        self.statusFrame.setMinimumSize(QSize(790, 110))
        self.statusFrame.setMaximumSize(QSize(790, 110))
        self.statusFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.statusFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.statusFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.statusLabel = QLabel(self.statusFrame)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setMinimumSize(QSize(220, 25))
        self.statusLabel.setMaximumSize(QSize(220, 75))
        self.statusLabel.setFont(font)
        self.statusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.statusLabel)

        self.statusInfoFrame = QFrame(self.statusFrame)
        self.statusInfoFrame.setObjectName(u"statusInfoFrame")
        self.statusInfoFrame.setMinimumSize(QSize(540, 95))
        self.statusInfoFrame.setMaximumSize(QSize(540, 95))
        self.statusInfoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.statusInfoFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.statusInfoFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.positionInfoFrame = QFrame(self.statusInfoFrame)
        self.positionInfoFrame.setObjectName(u"positionInfoFrame")
        self.positionInfoFrame.setMinimumSize(QSize(250, 40))
        self.positionInfoFrame.setMaximumSize(QSize(250, 40))
        self.positionInfoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.positionInfoFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.positionInfoFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.positionInfoLabel = QLabel(self.positionInfoFrame)
        self.positionInfoLabel.setObjectName(u"positionInfoLabel")
        self.positionInfoLabel.setMinimumSize(QSize(112, 20))
        self.positionInfoLabel.setMaximumSize(QSize(112, 20))

        self.horizontalLayout_8.addWidget(self.positionInfoLabel)

        self.positionInfoAngleLabel = QLabel(self.positionInfoFrame)
        self.positionInfoAngleLabel.setObjectName(u"positionInfoAngleLabel")
        self.positionInfoAngleLabel.setMinimumSize(QSize(112, 20))
        self.positionInfoAngleLabel.setMaximumSize(QSize(112, 20))
        self.positionInfoAngleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.positionInfoAngleLabel)


        self.gridLayout.addWidget(self.positionInfoFrame, 0, 0, 1, 1)

        self.errorInfoFrame = QFrame(self.statusInfoFrame)
        self.errorInfoFrame.setObjectName(u"errorInfoFrame")
        self.errorInfoFrame.setMinimumSize(QSize(250, 40))
        self.errorInfoFrame.setMaximumSize(QSize(250, 40))
        self.errorInfoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.errorInfoFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.errorInfoFrame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.errorInfoLabel = QLabel(self.errorInfoFrame)
        self.errorInfoLabel.setObjectName(u"errorInfoLabel")
        self.errorInfoLabel.setMinimumSize(QSize(112, 20))
        self.errorInfoLabel.setMaximumSize(QSize(112, 20))

        self.horizontalLayout_12.addWidget(self.errorInfoLabel)

        self.errorInfoValueLabel = QLabel(self.errorInfoFrame)
        self.errorInfoValueLabel.setObjectName(u"errorInfoValueLabel")
        self.errorInfoValueLabel.setMinimumSize(QSize(112, 20))
        self.errorInfoValueLabel.setMaximumSize(QSize(112, 20))
        self.errorInfoValueLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.errorInfoValueLabel)


        self.gridLayout.addWidget(self.errorInfoFrame, 0, 1, 1, 1)

        self.motorInfoFrame = QFrame(self.statusInfoFrame)
        self.motorInfoFrame.setObjectName(u"motorInfoFrame")
        self.motorInfoFrame.setMinimumSize(QSize(250, 40))
        self.motorInfoFrame.setMaximumSize(QSize(250, 40))
        self.motorInfoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.motorInfoFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.motorInfoFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.motorInfoLabel = QLabel(self.motorInfoFrame)
        self.motorInfoLabel.setObjectName(u"motorInfoLabel")
        self.motorInfoLabel.setMinimumSize(QSize(112, 20))
        self.motorInfoLabel.setMaximumSize(QSize(112, 20))

        self.horizontalLayout_9.addWidget(self.motorInfoLabel)

        self.motorInfoStateLabel = QLabel(self.motorInfoFrame)
        self.motorInfoStateLabel.setObjectName(u"motorInfoStateLabel")
        self.motorInfoStateLabel.setMinimumSize(QSize(112, 20))
        self.motorInfoStateLabel.setMaximumSize(QSize(112, 20))
        self.motorInfoStateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.motorInfoStateLabel)


        self.gridLayout.addWidget(self.motorInfoFrame, 1, 0, 1, 1)

        self.pidInfoFrame = QFrame(self.statusInfoFrame)
        self.pidInfoFrame.setObjectName(u"pidInfoFrame")
        self.pidInfoFrame.setMinimumSize(QSize(250, 40))
        self.pidInfoFrame.setMaximumSize(QSize(250, 40))
        self.pidInfoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.pidInfoFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.pidInfoFrame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pidInfoLabel = QLabel(self.pidInfoFrame)
        self.pidInfoLabel.setObjectName(u"pidInfoLabel")
        self.pidInfoLabel.setMinimumSize(QSize(112, 20))
        self.pidInfoLabel.setMaximumSize(QSize(112, 20))

        self.horizontalLayout_13.addWidget(self.pidInfoLabel)

        self.pidInfoValueLabel = QLabel(self.pidInfoFrame)
        self.pidInfoValueLabel.setObjectName(u"pidInfoValueLabel")
        self.pidInfoValueLabel.setMinimumSize(QSize(112, 20))
        self.pidInfoValueLabel.setMaximumSize(QSize(112, 20))
        self.pidInfoValueLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.pidInfoValueLabel)


        self.gridLayout.addWidget(self.pidInfoFrame, 1, 1, 1, 1)


        self.horizontalLayout_6.addWidget(self.statusInfoFrame)

        self.plotWidget = PlotWidget(self.centralwidget)
        self.plotWidget.setObjectName(u"plotWidget")
        self.plotWidget.setGeometry(QRect(280, 10, 790, 541))
        self.plotWidget.setMinimumSize(QSize(790, 541))
        self.plotWidget.setMaximumSize(QSize(790, 541))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.uartLabel.setText(QCoreApplication.translate("MainWindow", u"UART", None))
        self.comLabel.setText(QCoreApplication.translate("MainWindow", u"COM", None))
        self.baudLabel.setText(QCoreApplication.translate("MainWindow", u"BAUD", None))
        self.uartStatusLabel.setText(QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.statusStateLabel.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
        self.connectUartButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.disconnectUartButton.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.pidLabel.setText(QCoreApplication.translate("MainWindow", u"PID", None))
        self.kpLabel.setText(QCoreApplication.translate("MainWindow", u"Kp", None))
        self.kiLabel.setText(QCoreApplication.translate("MainWindow", u"Ki", None))
        self.kdLabel.setText(QCoreApplication.translate("MainWindow", u"Kd", None))
        self.updatePidButton.setText(QCoreApplication.translate("MainWindow", u"Update PID", None))
        self.motorLabel.setText(QCoreApplication.translate("MainWindow", u"MOTOR", None))
        self.motorInAngleRangeLabel.setText(QCoreApplication.translate("MainWindow", u"(-360\u00b0 to 360\u00b0)", None))
        self.moveMotorButton.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.stopMotorButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"STATUS", None))
        self.positionInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Position: ", None))
        self.positionInfoAngleLabel.setText("")
        self.errorInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Error:", None))
        self.errorInfoValueLabel.setText("")
        self.motorInfoLabel.setText(QCoreApplication.translate("MainWindow", u"Motor:", None))
        self.motorInfoStateLabel.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.pidInfoLabel.setText("")
        self.pidInfoValueLabel.setText("")
    # retranslateUi

