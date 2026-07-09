from PySide6.QtCore import QThread, Signal

class SerialReaderThread(QThread):
    data_signal    = Signal(str)
    error_signal   = Signal(str)

    def __init__(self, serial_obj):
        super().__init__()

        self.serial = serial_obj
        self.running = True

    def run(self):

        while self.running:
            try:
                self.read()

            except Exception as e:
                self.error_signal.emit(e)
                break

    def read(self):
        if self.serial.in_waiting:

            data = (
                self.serial
                .readline()
                .decode("utf-8")
                .strip()
            )

            if data:
                self.data_signal.emit(data)

    def stop(self):
        self.running = False
        self.quit()
        self.wait()