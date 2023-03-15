# -*- coding: utf-8 -*-
import os
import sys
# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import time
import pyautogui
import threading
import keyboard
import json

from PySide6.QtCore import Qt
from PySide6.QtGui import QFontDatabase, QFont, QAction, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMenuBar, \
    QMainWindow, QMenu
from pynput import mouse

import CoordinateHandler

#TODO: rework actual bloons interface to run as a while-loop that interfaces with a json file full of data
#TODO: rework json file construction
#TODO: add functionality to the secondary windows to edit tower positions


class BloonsUIMain(QMainWindow):
    def __init__(self):
        super().__init__()
        # Main Window UI setup junk
        self.BloonsUI = QApplication([])
        self.setWindowTitle('Bloons Auto Farm')
        self.setGeometry(550, 250, 800, 600)
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.mainhboxtop = QHBoxLayout()
        self.mainhboxbot = QHBoxLayout()
        self.defhboxtop = QHBoxLayout()
        self.defhboxbot = QHBoxLayout()
        self.def2xhboxtop = QHBoxLayout()
        self.def2xhboxbot = QHBoxLayout()

        # Font setup
        self.font_id = QFontDatabase.addApplicationFont(self.resolve_path('LuckiestGuy-Regular.ttf'))
        self.font_name = QFontDatabase.applicationFontFamilies(self.font_id)[0]
        self.custom_font = QFont(self.font_name)

        # Add main window label widgets
        self.mainlabel = QLabel('Choose your desired farming method', parent=self.window)
        self.mainlabel.setFixedSize(600,50)
        self.custom_font.setPointSize(24)
        self.mainlabel.setFont(self.custom_font)

        self.deflationlabel = QLabel('Program is currently running Deflation farm', parent=self.window)
        self.deflationlabel.setFixedSize(618,50)
        self.custom_font.setPointSize(20)
        self.deflationlabel.setFont(self.custom_font)
        self.deflationlabel.hide()

        self.deflation2xlabel = QLabel('Program is currently running 2x Cash Deflation farm', parent=self.window)
        self.deflation2xlabel.setFixedSize(615,50)
        self.custom_font.setPointSize(17)
        self.deflation2xlabel.setFont(self.custom_font)
        self.deflation2xlabel.hide()

        # Add a menu bar
        self.menubar = QMenuBar()
        self.editmenu = QMenu("Edit", self.menubar)

        self.deflation_action = QAction('Deflation', self)
        self.editmenu.addAction(self.deflation_action)

        self.deflation2x_action = QAction('Deflation 2x Cash', self)
        self.editmenu.addAction(self.deflation2x_action)

        self.menubar.addMenu(self.editmenu)

        self.deflation_action.triggered.connect(self.editdeflation)
        self.deflation2x_action.triggered.connect(self.editdeflation2x)

        # Add button widgets to main window
        self.defbutton = QPushButton('Deflation', parent=self.window)
        self.defbutton.setFixedSize(200, 100)
        self.custom_font.setPointSize(20)
        self.defbutton.setFont(self.custom_font)
        self.defbutton.clicked.connect(self.deflationpress)

        self.def2xbutton = QPushButton('Deflation 2x Cash', parent=self.window)
        self.custom_font.setPointSize(15)
        self.def2xbutton.setFont(self.custom_font)
        self.def2xbutton.setFixedSize(200, 100)
        self.def2xbutton.clicked.connect(self.deflation2xpress)

        self.quitbutton = QPushButton('Quit to Menu', parent=self.window)
        self.quitbutton.hide()
        self.custom_font.setPointSize(20)
        self.quitbutton.setFont(self.custom_font)
        self.quitbutton.setFixedSize(200, 100)
        self.quitbutton.clicked.connect(self.quit)

        # Add Widgets and set up layout of main UI page
        self.mainhboxtop.addWidget(self.mainlabel)
        self.mainhboxbot.addWidget(self.defbutton)
        self.mainhboxbot.addWidget(self.def2xbutton)
        self.layout.addLayout(self.mainhboxtop)
        self.layout.addLayout(self.mainhboxbot)

        # Add Widgets and set up layout of Deflation/Deflation 2x Cash pages
        self.defhboxtop.addWidget(self.deflationlabel)
        self.layout.addLayout(self.defhboxtop)
        self.layout.addLayout(self.defhboxbot)

        self.def2xhboxtop.addWidget(self.deflation2xlabel)
        self.def2xhboxbot.addWidget(self.quitbutton)
        self.layout.addLayout(self.def2xhboxtop)
        self.layout.addLayout(self.def2xhboxbot)

        # Finalize UI setup and open the window
        self.window.setLayout(self.layout)
        self.setCentralWidget(self.window)
        self.setMenuBar(self.menubar)
        self.show()
        self.run()

        # Tower setup
        self.snipx = 0
        self.snipy = 0
        self.alchx = 0
        self.alchy = 0
        self.vilx = 0
        self.vily = 0
        self.nintopx = 0
        self.nintopy = 0
        self.ninbottomx = 0
        self.ninbottomy = 0
        self.alchtopx = 0
        self.alchtopy = 0
        self.alchbottomx = 0
        self.alchbottomy = 0

        # Reset Coordinates
        self.x = 0
        self.y = 0
        
        # Thread setup
        self.running = False

        # Make the json file

        


    # Separate methods to run in the buttons
    def deflation(self):
        try:
            with open("towerpos.json") as f:
                pass
        except FileNotFoundError:
            CoordinateHandler.main()
        self.coordinateHandler()
        width, height = pyautogui.size()
        x_fact = width / 1920
        y_fact = height / 1080

        while self.running:
            counter = 0
            while counter < 5:
                if not self.running:
                    print("We're not self.running anymore, exit!")
                    return
                else:
                    print(f"We're still self.running, keep sleeping... {counter + 1}/5")
                    time.sleep(1)
                    counter += 1
            pyautogui.click(x_fact * 837, y_fact * 933)
            time.sleep(0.5)
            pyautogui.click(x_fact * 1332, y_fact * 967)
            time.sleep(0.5)
            pyautogui.click(x_fact * 958, y_fact * 575)
            time.sleep(0.5)
            pyautogui.click(x_fact * 656, y_fact * 396)
            time.sleep(0.5)
            pyautogui.click(x_fact * 1253, y_fact * 446)
            counter = 0
            while counter < 10:
                if not self.running:
                    print("We're not self.running anymore, exit!")
                    return
                else:
                    print(f"We're still self.running, keep sleeping... {counter + 1}/10")
                    time.sleep(1)
                    counter += 1
            pyautogui.click(x_fact * 954, y_fact * 750)
            time.sleep(0.25)
            pyautogui.click(self.nintopx, self.nintopy)
            time.sleep(0.25)
            keyboard.press_and_release('d')
            time.sleep(0.25)
            pyautogui.click(self.nintopx, self.nintopy)
            time.sleep(0.25)
            pyautogui.click(self.nintopx, self.nintopy)
            for i in range(4):
                time.sleep(0.25)
                keyboard.press_and_release(',')
            for i in range(2):
                time.sleep(0.25)
                keyboard.press_and_release('/')
            time.sleep(0.25)
            pyautogui.click(self.alchtopx, self.alchtopy)
            time.sleep(0.25)
            keyboard.press_and_release('f')
            time.sleep(0.25)
            pyautogui.click(self.alchtopx, self.alchtopy)
            time.sleep(0.25)
            pyautogui.click(self.alchtopx, self.alchtopy)
            for i in range(4):
                time.sleep(0.25)
                keyboard.press_and_release(',')
            for i in range(2):
                time.sleep(0.25)
                keyboard.press_and_release('.')
            time.sleep(0.25)
            pyautogui.click(self.alchbottomx, self.alchbottomy)
            time.sleep(0.25)
            keyboard.press_and_release('f')
            time.sleep(0.25)
            pyautogui.click(self.alchbottomx, self.alchbottomy)
            time.sleep(0.25)
            pyautogui.click(self.alchbottomx, self.alchbottomy)
            for i in range(4):
                time.sleep(0.25)
                keyboard.press_and_release(',')
            for i in range(2):
                time.sleep(0.25)
                keyboard.press_and_release('.')
            time.sleep(0.25)
            pyautogui.click(self.ninbottomx, self.ninbottomy)
            time.sleep(0.25)
            keyboard.press_and_release('d')
            time.sleep(0.25)
            pyautogui.click(self.ninbottomx, self.ninbottomy)
            time.sleep(0.25)
            pyautogui.click(self.ninbottomx, self.ninbottomy)
            for i in range(4):
                time.sleep(0.25)
                keyboard.press_and_release(',')
            for i in range(2):
                time.sleep(0.25)
                keyboard.press_and_release('/')
            time.sleep(0.25)
            keyboard.press_and_release('space')
            time.sleep(0.25)
            keyboard.press_and_release('space')
            pyautogui.click(x_fact * 693, y_fact * 851)
            counter = 0
            while counter < 330:
                if not self.running:
                    print("We're not self.running anymore, exit!")
                    return
                else:
                    print(f"We're still self.running, keep sleeping... {counter + 1}/330")
                    time.sleep(1)
                    counter += 1
            pyautogui.click(x_fact * 956, y_fact * 904)
            time.sleep(0.5)
            pyautogui.click(x_fact * 693, y_fact * 851)
            print("Done with the loop!")

    def deflation2x(self):
        try:
            with open("towerpos.json") as f:
                pass
        except FileNotFoundError:
            CoordinateHandler.main()
        self.coordinateHandler()
        width, height = pyautogui.size()
        x_fact = width / 1920
        y_fact = height / 1080

        while self.running:
            counter = 0
            while counter < 5:
                if not self.running:
                    print("We're not self.running anymore, exit!")
                    return
                else:
                    print(f"We're still self.running, keep sleeping... {counter + 1}/5")
                    time.sleep(1)
                    counter += 1
            pyautogui.click(x_fact * 837, y_fact * 933)
            time.sleep(0.5)
            pyautogui.click(x_fact * 1332, y_fact * 967)
            time.sleep(0.5)
            pyautogui.click(x_fact * 958, y_fact * 575)
            time.sleep(0.5)
            pyautogui.click(x_fact * 656, y_fact * 396)
            time.sleep(0.5)
            pyautogui.click(x_fact * 1253, y_fact * 446)
            counter = 0
            while counter < 10:
                if not self.running:
                    print("We're not self.running anymore, exit!")
                    return
                else:
                    print(f"We're still self.running, keep sleeping... {counter + 1}/10")
                    time.sleep(1)
                    counter += 1
            pyautogui.click(x_fact * 954, y_fact * 750)
            time.sleep(0.25)
            pyautogui.click(self.snipx, self.snipy)
            time.sleep(0.25)
            keyboard.press_and_release('z')
            time.sleep(0.25)
            pyautogui.click(self.snipx, self.snipy)
            time.sleep(0.25)
            pyautogui.click(self.snipx, self.snipy)
            for i in range(2):
                time.sleep(0.25)
                keyboard.press_and_release(',')
            for i in range(5):
                time.sleep(0.25)
                keyboard.press_and_release('/')
            time.sleep(0.25)
            pyautogui.click(self.alchx, self.alchy)
            time.sleep(0.25)
            keyboard.press_and_release('f')
            time.sleep(0.25)
            pyautogui.click(self.alchx, self.alchy)
            time.sleep(0.25)
            pyautogui.click(self.alchx, self.alchy)
            for i in range(4):
                time.sleep(0.25)
                keyboard.press_and_release(',')
            for i in range(2):
                time.sleep(0.25)
                keyboard.press_and_release('.')
            time.sleep(0.25)
            pyautogui.click(self.vilx, self.vily)
            time.sleep(0.25)
            keyboard.press_and_release('k')
            time.sleep(0.25)
            pyautogui.click(self.vilx, self.vily)
            time.sleep(0.25)
            pyautogui.click(self.vilx, self.vily)
            for i in range(2):
                time.sleep(0.25)
                keyboard.press_and_release(',')
            for i in range(3):
                time.sleep(0.25)
                keyboard.press_and_release('.')
            time.sleep(0.25)
            keyboard.press_and_release('space')
            time.sleep(0.25)
            keyboard.press_and_release('space')
            pyautogui.click(x_fact * 693, y_fact * 851)
            counter = 0
            while counter < 303:
                if not self.running:
                    print("We're not self.running anymore, exit!")
                    return
                else:
                    print(f"We're still self.running, keep sleeping... {counter + 1}/303")
                    time.sleep(1)
                    counter += 1
            pyautogui.click(x_fact * 956, y_fact * 904)
            time.sleep(0.5)
            pyautogui.click(x_fact * 693, y_fact * 851)

    # Define menu functionality
    def editdeflation(self):
        defsubwin = BloonsUISub("Deflation",["Top Ninja Pos", "Bottom Ninja Pos", "Top Alchemist Pos", "Bottom Alchemist Pos"])
        defsubwin.show()
        defsubwin.raise_()

    def editdeflation2x(self):
        def2xsubwin = BloonsUISub("Deflation 2x Cash", ["Sniper Pos", "Alchemist Pos", "Village Pos"])
        def2xsubwin.show()
        def2xsubwin.raise_()

    # Define button functionality for main window
    def deflationpress(self):
        self.running = True
        self.deflationlabel.show()
        self.quitbutton.show()
        self.mainlabel.hide()
        self.defbutton.hide()
        self.def2xbutton.hide()
        self.thread = threading.Thread(target=self.deflation, daemon=True)
        self.thread.start()

    def deflation2xpress(self):
        self.running = True
        self.deflation2xlabel.show()
        self.quitbutton.show()
        self.mainlabel.hide()
        self.defbutton.hide()
        self.def2xbutton.hide()
        self.thread = threading.Thread(target=self.deflation2x, daemon=True)
        self.thread.start()

    def quit(self):
        self.running = False
        self.deflation2xlabel.hide()
        self.deflationlabel.hide()
        self.quitbutton.hide()
        self.mainlabel.show()
        self.defbutton.show()
        self.def2xbutton.show()
        self.thread.join()

    # Writing and handling tower coordinates
    def coordinateHandler(self):
        with open('towerpos.json', 'r') as f:
            pos = json.load(f)
        self.snipx, self.snipy = pos['sniper_pos']
        self.alchx, self.alchy = pos['alchemist_pos']
        self.vilx, self.vily= pos['village_pos']
        self.nintopx, self.nintopy = pos['top_ninja_pos']
        self.ninbottomx, self.ninbottomy = pos['bottom_ninja_pos']
        self.alchtopx, self.alchtopy = pos['top_alchemist_pos']
        self.alchbottomx, self.alchbottomy = pos['bottom_alchemist_pos']

    # Finding file path for assets
    def resolve_path(self, path):
        if getattr(sys, "frozen", False):
            # If the 'frozen' flag is set, we are in bundled-app mode!
            resolved_path = os.path.abspath(os.path.join(sys._MEIPASS, path))
        else:
            # Normal development mode. Use os.getcwd() or __file__ as appropriate in your case...
            resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))

        return resolved_path

    # Run program
    def run(self):
        sys.exit(self.BloonsUI.exec())

if __name__ == "__main__":
    BloonsUI = BloonsUIMain()
    BloonsUI.run()

class BloonsUISub(QMainWindow):
    def __init__(self, title, button_labels):
        super().__init__()
        # Secondary Window UI setup junk
        self.subwindowUI = QApplication()
        self.setWindowTitle(title)
        self.setGeometry(550, 250, 400, 300)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.sub = QWidget()
        self.sublayout = QHBoxLayout()
        self.subvbox = QVBoxLayout()

        # Font setup
        self.font_id = QFontDatabase.addApplicationFont(self.resolve_path('LuckiestGuy-Regular.ttf'))
        self.font_name = QFontDatabase.applicationFontFamilies(self.font_id)[0]
        self.custom_font = QFont(self.font_name)

        # Add sub window label widgets
        self.subwinlab = QLabel("Select a tower to change it's position:", parent=self)
        self.custom_font.setPointSize(15)
        self.subwinlab.setFont(self.custom_font)

        # Add Widgets and set up layout of sub windows
        self.sublayout.addLayout(self.subvbox)
        self.subvbox.addWidget(self.subwinlab)

        # Create sub window buttons and add them to layout
        self.buttons = []
        for labels, i in enumerate(button_labels):
            self.buttons[i] = QPushButton(labels, parent=self)
            self.buttons[i].setFixedSize(200, 50)
            self.custom_font.setPointSize(15)
            self.buttons[i].setFont(self.custom_font)
            self.buttons[i].clicked.connect(self.resetPos)
            self.subvbox.addWidget(self.buttons[i])

        # Finalize and setup of sub windows
        self.sub.setLayout(self.sublayout)
        self.setCentralWidget(self.sub)

    # Function for finding file path for assets
    def resolve_path(self, path):
        if getattr(sys, "frozen", False):
            # If the 'frozen' flag is set, we are in bundled-app mode!
            resolved_path = os.path.abspath(os.path.join(sys._MEIPASS, path))
        else:
            # Normal development mode. Use os.getcwd() or __file__ as appropriate in your case...
            resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))

        return resolved_path

    # Function for resetting tower positions
    def resetPos(self):
        try:
            with open('towerpos.json') as f:
                def on_click(self,x,y,button,pressed):
                    self.x = x
                    self.y = y
                    if pressed:
                        return False

                button_name = self.sender().text().lower().replace(' ', '_')
                with open('towerpos.json', 'r+') as f:
                    pos = json.load(f)
                    pos[button_name] = self.x
                    pos[button_name] = self.y
                    f.seek(0)
                    json.dump(pos)

                with mouse.Listener(on_click=on_click) as listener:
                    listener.join()
        except FileNotFoundError:
            error = BloonsUIError("No File Found", "Error! coordinate file not found! (Run one of the default farms first)")
            error.show()


class BloonsUIError(QMainWindow):
    def __init__(self, title, errormessage):
        super().__init__()
        # Error Window setup junk
        self.errorwindowUI = QApplication()
        self.setWindowTitle(title)
        self.setGeometry(550, 250, 300, 100)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.errorwindow = QWidget()
        self.errorlayout = QVBoxLayout()
        self.errorhbox = QHBoxLayout()

        # Font setup
        self.font_id = QFontDatabase.addApplicationFont(self.resolve_path('LuckiestGuy-Regular.ttf'))
        self.font_name = QFontDatabase.applicationFontFamilies(self.font_id)[0]
        self.custom_font = QFont(self.font_name)

        # Add error window label widget
        self.errorlabel = QLabel(errormessage, parent=self)
        self.custom_font.setPointSize(10.5)
        self.errorlabel.setFont(self.custom_font)

        # Add Widgets and set up layout of error window
        self.errorhbox.addWidget(self.errorlabel)
        self.errorlayout.addLayout(self.errorhbox)

    # Finding file path for assets
    def resolve_path(self, path):
        if getattr(sys, "frozen", False):
            # If the 'frozen' flag is set, we are in bundled-app mode!
            resolved_path = os.path.abspath(os.path.join(sys._MEIPASS, path))
        else:
            # Normal development mode. Use os.getcwd() or __file__ as appropriate in your case...
            resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))

        return resolved_path