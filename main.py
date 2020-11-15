#!/usr/bin/python3
# -*- coding: utf-8 -*-
from modules.windowQT import*
import sys

end = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Popup()
    window.interface_Start_Game()
    sys.exit(app.exec_())
