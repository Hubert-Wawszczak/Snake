#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout


import sys


class Popup(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


    def interface_Game_Over(self):

        self.setWindowTitle("Snake Menu")
        label = QLabel("Game Over", self)
        layout = QGridLayout()

        #Buttons
        auto_play_Button = QPushButton("&Auto Play", self)
        retry_Button = QPushButton("&Retry", self)
        exit_Button = QPushButton("&Exit", self)

        layout.addWidget(label, 0,0)
        layout.addWidget(auto_play_Button)
        layout.addWidget(retry_Button)
        layout.addWidget(exit_Button)


        self.setGeometry(700,440 ,500 ,300)
        self.setLayout(layout)

        self.show()

    def interface_Start_Game(self):
        self.resize(500, 300)
        self.setWindowTitle("Snake Menu")
        label = QLabel("Snake", self)
        self.show()
