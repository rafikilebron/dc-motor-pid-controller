# PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QTimer

# Python
import sys
import serial
import serial.tools.list_ports
from gui import Ui_MainWindow
from threads import SerialReaderThread


class MainWindow(QMainWindow):
    """
    ---- COMMAND GUIDE ----
    
    PC:
        $PID,kp,ki,kd
        $PID,REQUEST
        $MOTOR,angle
        $MOTOR,STOP

    MICROCONTROLLER:
        $TEL,position
        $PID,kp;ki;kd
    
    """

    # region ---------- CONSTRUCTOR ----------
    def __init__(self):
        super().__init__()

        self.w = Ui_MainWindow()
        self.w.setupUi(self)

        self.setup()
    
    #endregion

    # region ---------- GUI SETUP ----------
    def setup(self):
        self.init_widgets()
        self.init_flags()
        self.init_system_variables()
        self.init_signal_connections()

    def init_widgets(self):
        """Widgets Initialization"""
        self.w.baudComboBox.addItems([
            "9600",
            "19200",
            "38400",
            "57600",
            "115200"
        ])

        if self.w.baudComboBox.count() > 0:
            self.w.baudComboBox.setCurrentIndex(
            self.w.baudComboBox.count() - 1
            )

    def init_flags(self):
        self.connected = False

    def init_system_variables(self):
        self.serial         = None
        self.com            = None
        self.serial_thread  = None
        self.angle          = 0
        self.comTimer       = QTimer(self)

    def init_signal_connections(self):
        self.connect_uart_signals()
        self.connect_pid_signals()
        self.connect_motor_signals()   

    def connect_uart_signals(self):
        self.w.connectUartButton.clicked.connect(self.connectUART)
        self.w.disconnectUartButton.clicked.connect(self.disconnectUART)
        self.comTimer.timeout.connect(self.refreshPorts)
        self.comTimer.start(500)

    def connect_pid_signals(self):
        self.w.updatePidButton.clicked.connect(self.updatePID)

    def connect_motor_signals(self):
        self.w.moveMotorButton.clicked.connect(self.moveMotor)
        self.w.stopMotorButton.clicked.connect(self.stopMotor)
    
    # endregion

    # region ---------- GENERAL METHODS ----------
    def show_information(self, window_title, text):
        msg = QMessageBox(self)
        msg.setWindowTitle(window_title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.exec()

    def security_question(self, window_title, text):
        msg = QMessageBox(self)
        msg.setWindowTitle(window_title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Question)

        msg.setStandardButtons(
            QMessageBox.Yes | QMessageBox.No
        )

        msg.setDefaultButton(QMessageBox.No)

        return msg.exec() == QMessageBox.Yes
    
    def show_status(self, message):
        self.statusBar().showMessage(message)

    # endregion

    # region ---------- UART ----------
    def refreshPorts(self):
        current = self.w.comComboBox.currentText()

        ports = [port.device for port in serial.tools.list_ports.comports()]

        combo = [
            self.w.comComboBox.itemText(i)
            for i in range(self.w.comComboBox.count())
        ]

        if ports != combo:

            self.w.comComboBox.blockSignals(True)

            self.w.comComboBox.clear()
            self.w.comComboBox.addItems(ports)

            if current in ports:
                self.w.comComboBox.setCurrentText(current)

            self.w.comComboBox.blockSignals(False)

    def connectUART(self):
        if self.connected and (self.com == self.w.comComboBox.currentText()):
            self.show_information("UART Connection", f"Port {self.com} is connected already.")
            return

        port = self.w.comComboBox.currentText()
        baud = int(self.w.baudComboBox.currentText())

        try:
            self.serial = serial.Serial(
                port=port,
                baudrate=baud,
                timeout=1
            )

            self.connected = True
            self.com = port

            self.serial_thread = SerialReaderThread(self.serial)
            self.serial_thread.data_signal.connect(self.processReceivedData)
            self.serial_thread.start()

            self.sendCommand("$PID,REQUEST")

            self.w.statusStateLabel.setText("Connected")
            self.show_status(f"UART: connected to {self.com}")

            self.show_information(
                "UART Connection",
                f"Connection to {self.com} successful"
            )

        except serial.SerialException as e:
            self.serial = None
            self.connected = False
            self.w.statusStateLabel.setText("Disconnected")

            self.show_status("UART: Failed to connect to {}")

            self.show_information(
                "UART Connection",
                f"Connection failed"
            )

        except ValueError as e:
            self.serial = None
            self.connected = False

            self.show_information(
                "UART Connection",
                f"Invalid configuration:\n\n{e}"
            )

        except Exception as e:
            self.serial = None
            self.connected = False

            self.show_information(
                "UART Connection",
                f"An unknown error has occurred:\n\n{e}"
            )

    def disconnectUART(self):
        if not self.security_question("UART connection", f"Do you want to disconnect from {self.com}?"):
            return 

        if self.serial is not None:
            self.serial.close()
            self.serial = None

        if self.serial_thread is not None:
            self.serial_thread.stop()
            self.serial_thread = None
        
        self.connected  = False   
        self.com = None       

        self.w.statusStateLabel.setText("Disconnected")
        self.show_status("UART: connection closed")

    def sendCommand(self, command):
        if not self.connected:
            self.show_information(
                "UART Communication",
                "UART connection not available."
            )
            return False

        try:
            message = command + "\n"

            self.serial.write(message.encode("utf-8"))

            print(f"TX: {message.strip()}")

            return True

        except Exception as e:
            self.show_information(
                "UART Error",
                str(e)
            )

            return False                  

    def processReceivedData(self, data):
        if data.startswith("$TEL"):

            values = data.split(",")
            
            if len(values) == 2:

                position = float(values[1])
                error = abs(float(self.angle) - position)

                self.updatePosition(position)
                self.w.errorInfoValueLabel.setText(f"{error:.2f}°")

        elif data.startswith("$PID"):

            values = data.split(",")

            if len(values) == 4:

                kp = float(values[1])
                ki = float(values[2])
                kd = float(values[3])

                self.w.kpSpinBox.setValue(kp)
                self.w.kiSpinBox.setValue(ki)
                self.w.kdSpinBox.setValue(kd)

    #endregion

    # region ---------- PID ----------
    def updatePID(self):
        kp = self.w.kpSpinBox.value()
        ki = self.w.kiSpinBox.value()
        kd = self.w.kdSpinBox.value()

        command = f"$PID,{kp},{ki},{kd}"

        self.sendCommand(command)
    
    # endregion

    # region ---------- MOTOR ----------
    def moveMotor(self):

        self.angle = self.w.motorTargetAngleSpinBox.value()

        command = f"$MOTOR,{self.angle}"

        self.sendCommand(command)

        self.w.motorInfoStateLabel.setText("Enabled")

    def stopMotor(self):
        command = f"$MOTOR,STOP"

        self.sendCommand(command)

        self.w.motorInfoStateLabel.setText("Disabled")
    
    # endregion

    # region ---------- PLOT ----------
    def updatePosition(self, position):
        self.w.plotWidget.addPosition(position)
        self.w.positionInfoAngleLabel.setText(f"{position:.2f}°")
    
    # endregion


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())