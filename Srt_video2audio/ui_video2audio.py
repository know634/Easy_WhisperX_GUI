# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video2audio.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(735, 450)
        self.pushButton_file = QPushButton(Form)
        self.pushButton_file.setObjectName(u"pushButton_file")
        self.pushButton_file.setGeometry(QRect(110, 140, 120, 35))
        font = QFont()
        font.setFamilies([u"\u971e\u9e5c\u6587\u6977\u7b49\u5bbd"])
        font.setPointSize(12)
        self.pushButton_file.setFont(font)
        self.textEdit_name = QTextEdit(Form)
        self.textEdit_name.setObjectName(u"textEdit_name")
        self.textEdit_name.setGeometry(QRect(110, 30, 120, 100))
        self.textEdit_name.setFont(font)
        self.textEdit_dir = QTextEdit(Form)
        self.textEdit_dir.setObjectName(u"textEdit_dir")
        self.textEdit_dir.setGeometry(QRect(240, 230, 450, 35))
        self.textEdit_dir.setFont(font)
        self.pushButton_folder = QPushButton(Form)
        self.pushButton_folder.setObjectName(u"pushButton_folder")
        self.pushButton_folder.setGeometry(QRect(110, 180, 120, 35))
        self.pushButton_folder.setFont(font)
        self.pushButton_folder.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.pushButton_dir = QPushButton(Form)
        self.pushButton_dir.setObjectName(u"pushButton_dir")
        self.pushButton_dir.setGeometry(QRect(110, 230, 120, 35))
        self.pushButton_dir.setFont(font)
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(110, 390, 121, 35))
        self.pushButton_4.setFont(font)
        self.textEdit_out = QTextEdit(Form)
        self.textEdit_out.setObjectName(u"textEdit_out")
        self.textEdit_out.setGeometry(QRect(110, 280, 120, 100))
        self.textEdit_out.setFont(font)
        self.textEdit_show = QTextEdit(Form)
        self.textEdit_show.setObjectName(u"textEdit_show")
        self.textEdit_show.setGeometry(QRect(240, 30, 450, 180))
        self.textEdit_show.setFont(font)
        self.label_1 = QLabel(Form)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(20, 30, 80, 100))
        font1 = QFont()
        font1.setFamilies([u"\u971e\u9e5c\u6587\u6977\u7b49\u5bbd"])
        font1.setPointSize(14)
        self.label_1.setFont(font1)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 280, 80, 100))
        self.label_2.setFont(font1)
        self.textEdit_res = QTextEdit(Form)
        self.textEdit_res.setObjectName(u"textEdit_res")
        self.textEdit_res.setGeometry(QRect(240, 280, 450, 145))
        self.textEdit_res.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Know634：视频音频提取（可批量）", None))
        self.pushButton_file.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.pushButton_folder.setText(QCoreApplication.translate("Form", u"\u62e9\u6587\u4ef6\u5939", None))
        self.pushButton_dir.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa\u8def\u5f84", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u89c6\u9891<br/>\u8def\u5f84</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">\u97f3\u9891<br/>\u8def\u5f84</p></body></html>", None))
    # retranslateUi

