# -- coding: utf-8 --
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QApplication
import ui_main
from Srt_video2audio import video2audio


class Launcher(QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('icons/logo.svg'))
        self.setWindowFlags(Qt.WindowType.WindowMinimizeButtonHint | Qt.WindowType.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.bind()

    def bind(self):
        self.pushButton_1.clicked.connect(self.methodFunc1)
        self.pushButton_2.clicked.connect(self.methodFunc2)

    def methodFunc1(self):
        self.methodWindow1 = video2audio.Video2Audio()
        self.methodWindow1.show()

    def methodFunc2(self):
        pass


if __name__ == "__main__":
    app = QApplication([])
    launcher = Launcher()
    launcher.show()
    sys.exit(app.exec())
