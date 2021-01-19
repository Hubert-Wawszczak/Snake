#!/usr/bin/python3
# -*- coding: utf-8 -*-
from modules.windowQT import*
import sys
from modules.snake import *
end = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = Snake()
    window = Popup(a)
    window.my_Exit()
    window.interface_Start_Game()
    window.my_Exit()
    while end == True:
        window.interface_Game_Over()
        sys.exit(app.exec_())
