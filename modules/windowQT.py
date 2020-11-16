#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from modules.snake import *



import sys


class Popup(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def interface_Game_Over(self):

        self.setWindowTitle("Snake Menu")
        label = QLabel("You Lose", self)
        label.setStyleSheet("QLabel {color:red;font: bold 30px;padding: 6px;text-align:center;padding-left:175px;}")

        layout = QGridLayout()

        #Buttons
        auto_play_Button = QPushButton("&Auto Play", self)
        retry_Button = QPushButton("&Retry", self)
        exit_Button = QPushButton("&Exit", self)

        layout.addWidget(label,0,0)
        layout.addWidget(auto_play_Button)
        layout.addWidget(retry_Button)
        layout.addWidget(exit_Button)

        self.setGeometry(700,440 ,500 ,300)
        self.setLayout(layout)

        retry_Button.clicked.connect(self.runer)
        exit_Button.clicked.connect(self.my_Exit)

        self.show()

    def interface_Start_Game(self):

        self.setWindowTitle("Snake Menu")
        label = QLabel("Snake ", self)
        label.setStyleSheet("QLabel {color:red;font: bold 30px;padding: 6px;text-align:center;padding-left:175px;}")

        layout = QGridLayout()

        #Buttons
        auto_play_Button = QPushButton("&Auto Play", self)
        play_Button = QPushButton("&Play", self)
        exit_Button = QPushButton("&Exit", self)

        layout.addWidget(label,0,0)
        layout.addWidget(auto_play_Button)
        layout.addWidget(play_Button)
        layout.addWidget(exit_Button)

        self.setGeometry(700,440 ,500 ,300)
        self.setLayout(layout)

        play_Button.clicked.connect(self.runer)
        exit_Button.clicked.connect(self.my_Exit)

        self.show()

    def runer(self):
        self.a = Snake()
        self.my_Exit()
        self.a.update_window()

    def my_Exit(self):
        self.close()
