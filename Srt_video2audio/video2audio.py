# -- coding: utf-8 --
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget

from . import ui_video2audio


class Video2Audio(QWidget, ui_video2audio.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('icons/logo.svg'))
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.WindowMinimizeButtonHint | Qt.WindowType.WindowCloseButtonHint)
        self.setFixedSize(self.width(), self.height())
