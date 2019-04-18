import sys
import keyboard
import pyautogui
import threading
from msvcrt import getch
from functools import partial
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QToolTip

text = ''


class Window(QWidget):

    def __init__(self, x, text):
        super().__init__()
        QWidget.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        size = pyautogui.size()
        xcord = size[0]
        ycord = size[1]
        self.setGeometry(0, ycord-320, xcord, ycord/4)
        self.setWindowTitle('Thought Keyboard')

        self.home(x, text)

    def home(self, x, text):

        self.l = QLabel()
        self.l.setText(text)

        self.keys_sides = [
                    'esc', 'tab', 'capslock', 'shift', 'alt'
                    ]

        self.keys_low = [
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', '1', '2', '3', 'h', 'i', 'j', 'k', 'l', 'm', 'n', '4', '5', '6',
                    'o', 'p', 'q', 'r', 's', 't', 'u', '7', '8', '9', 'v', 'w', 'x', 'y', 'z', chr(39), ',', '.', '0', 'Del'
                    ]

        self.keys_high = [
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', '1', '2', '3', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '4', '5', '6',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U', '7', '8', '9', 'V', 'W', 'X', 'Y', 'Z', chr(39), ',', '.', '0', 'Del'
                    ]

        self.keys_alt = [
                    '~', '`', '#', '$', '%', '^', '&', '1', '2', '3', '*', '(', ')', '_', '=', '+', '-', '4', '5', '6',
                    '<', '>', '{', '}', chr(47), '/', '@', '7', '8', '9', ':', ';', '"', '!', '?', chr(39), ',', '.', '0', 'Del'
                    ]

        v_box1 = QVBoxLayout()
        h_box1 = QHBoxLayout()

        v_box1.addWidget(self.l)

        h_box1.addLayout(self.make_sides(x))

        if x == 0:
            h_box1.addLayout(self.lower_case())
        elif x == 1:
            h_box1.addLayout(self.upper_case())
        elif x == 2:
            h_box1.addLayout(self.alt_case())

        h_box1.addLayout(self.make_sides(x))

        v_box1.addLayout(h_box1)

        self.setLayout(v_box1)

        self.show()

    def btn_press(self, per):
        pyautogui.press(per)

    def esc_press(self):
        self.close()

    def caps_press(self):
        self.close()
        self.__init__(1, text)

    def shift_press(self):
        self.close()
        self.__init__(0, text)

    def alt_press(self):
        self.close()
        self.__init__(2, text)

    def make_sides(self, y):

        v_box = QVBoxLayout()

        x = QPushButton(self.keys_sides[0], self)
        x.clicked.connect(self.esc_press)
        v_box.addWidget(x)

        x = QPushButton(self.keys_sides[1], self)
        x.clicked.connect(partial(self.btn_press, self.keys_sides[1]))
        x.clicked.connect(partial(self.add_text, y, '    '))
        v_box.addWidget(x)

        x = QPushButton(self.keys_sides[2], self)
        x.clicked.connect(self.caps_press)
        v_box.addWidget(x)

        x = QPushButton(self.keys_sides[3], self)
        x.clicked.connect(self.shift_press)
        v_box.addWidget(x)

        x = QPushButton(self.keys_sides[4], self)
        x.clicked.connect(self.alt_press)
        v_box.addWidget(x)

        return v_box

    def lower_case(self):

        h_box1 = QHBoxLayout()
        h_box2 = QHBoxLayout()
        h_box3 = QHBoxLayout()
        h_box4 = QHBoxLayout()
        h_box5 = QHBoxLayout()
        v_box = QVBoxLayout()

        for i in range(0, 10):
            x = QPushButton(self.keys_low[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_low[i]))
            x.clicked.connect(partial(self.add_text, 0, self.keys_low[i]))
            h_box1.addWidget(x)
        for i in range(10, 20):
            x = QPushButton(self.keys_low[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_low[i]))
            x.clicked.connect(partial(self.add_text, 0, self.keys_low[i]))
            h_box2.addWidget(x)
        for i in range(20, 30):
            x = QPushButton(self.keys_low[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_low[i]))
            x.clicked.connect(partial(self.add_text, 0, self.keys_low[i]))
            h_box3.addWidget(x)
        for i in range(30, 40):
            x = QPushButton(self.keys_low[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_low[i]))
            x.clicked.connect(partial(self.add_text, 0, self.keys_low[i]))
            h_box4.addWidget(x)

        b = QPushButton('<--Backspace', self)
        b.clicked.connect(partial(self.btn_press, 'backspace'))
        b.clicked.connect(partial(self.remove_text, 0))
        h_box5.addWidget(b)

        s = QPushButton('_Space_', self)
#        s.clicked.connect(partial(self.btn_press, 'space'))
        s.clicked.connect(partial(self.add_text, 0, ' '))
        h_box5.addWidget(s)

        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box5)

        return v_box

    def upper_case(self):

        h_box1 = QHBoxLayout()
        h_box2 = QHBoxLayout()
        h_box3 = QHBoxLayout()
        h_box4 = QHBoxLayout()
        h_box5 = QHBoxLayout()
        v_box = QVBoxLayout()

        for i in range(0, 10):
            x = QPushButton(self.keys_high[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_high[i]))
            x.clicked.connect(partial(self.add_text, 1, self.keys_high[i]))
            h_box1.addWidget(x)
        for i in range(10, 20):
            x = QPushButton(self.keys_high[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_high[i]))
            x.clicked.connect(partial(self.add_text, 1, self.keys_high[i]))
            h_box2.addWidget(x)
        for i in range(20, 30):
            x = QPushButton(self.keys_high[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_high[i]))
            x.clicked.connect(partial(self.add_text, 1, self.keys_high[i]))
            h_box3.addWidget(x)
        for i in range(30, 40):
            x = QPushButton(self.keys_high[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_high[i]))
            x.clicked.connect(partial(self.add_text, 1, self.keys_high[i]))
            h_box4.addWidget(x)

        b = QPushButton('<--Backspace', self)
        b.clicked.connect(partial(self.btn_press, 'backspace'))
        b.clicked.connect(partial(self.remove_text, 1))
        h_box5.addWidget(b)

        s = QPushButton('_Space_', self)
#        s.clicked.connect(partial(self.btn_press, 'space'))
        s.clicked.connect(partial(self.add_text, 1, ' '))
        h_box5.addWidget(s)

        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box5)

        return v_box

    def alt_case(self):

        h_box1 = QHBoxLayout()
        h_box2 = QHBoxLayout()
        h_box3 = QHBoxLayout()
        h_box4 = QHBoxLayout()
        h_box5 = QHBoxLayout()
        v_box = QVBoxLayout()

        for i in range(0, 10):
            x = QPushButton(self.keys_alt[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_alt[i]))
            x.clicked.connect(partial(self.add_text, 2, self.keys_alt[i]))
            h_box1.addWidget(x)
        for i in range(10, 20):
            x = QPushButton(self.keys_alt[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_alt[i]))
            x.clicked.connect(partial(self.add_text, 2, self.keys_alt[i]))
            h_box2.addWidget(x)
        for i in range(20, 30):
            x = QPushButton(self.keys_alt[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_alt[i]))
            x.clicked.connect(partial(self.add_text, 2, self.keys_alt[i]))
            h_box3.addWidget(x)
        for i in range(30, 40):
            x = QPushButton(self.keys_alt[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_alt[i]))
            x.clicked.connect(partial(self.add_text, 2, self.keys_alt[i]))
            h_box4.addWidget(x)

        b = QPushButton('<--Backspace', self)
        b.clicked.connect(partial(self.btn_press, 'backspace'))
        b.clicked.connect(partial(self.remove_text, 2))
        h_box5.addWidget(b)

        s = QPushButton('_Space_', self)
#        s.clicked.connect(partial(self.btn_press, 'space'))
        s.clicked.connect(partial(self.add_text, 2, ' '))
        h_box5.addWidget(s)

        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box5)

        return v_box

    def add_text(self, y, t):

        global text

        text += t

        self.close()
        self.__init__(y, text)

    def remove_text(self, y):

        global text

        text = text[0:-1]

        self.close()
        self.__init__(y, text)


def mouse():
    pyautogui.moveTo(50, pyautogui.size()[1]-300)
    while True:
        e = getch()
        if e.lower() == 'w':
            pyautogui.move(0, -10)
        elif e.lower() == 'a':
            pyautogui.move(-25, 0)
        elif e.lower() == 'd':
            pyautogui.move(25, 0)
        elif e.lower() == 's':
            pyautogui.move(0, 10)
        elif e.lower() == 'e':
            pyautogui.click()
        elif e.lower() == 'q':
            break


def run():
    app = QApplication(sys.argv)
    window = Window(0, '')

    sys.exit(app.exec_())


run()
thread2 = threading.Thread(None, mouse, (0,))
thread2.start()