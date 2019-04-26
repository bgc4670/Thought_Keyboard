import sys
import keyboard
import pyautogui
import threading
import msvcrt
from pylsl import StreamInlet, resolve_stream
from functools import partial
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QToolTip
"""
This program is the GUI for the Thought Keyboard project using PyQT5 and pyautogui
:Start Date: 2-22-2019
:language: Python 3.7
:author: Brenton Cousins
"""
text = ''
lsample = []
rsample = []


class Window(QWidget):

    def __init__(self, x, text):
        """
        Starts the processes to make a new window
        :param x: The current board (default 0)
        :param text: The current text (default '')
        """
        super().__init__()
        QWidget.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        size = pyautogui.size()
        xcord = size[0]
        ycord = size[1]
        self.setGeometry(0, ycord-320, xcord, ycord/4)
        self.setWindowTitle('Thought Keyboard')

        self.home(x, text)

    def home(self, x, text):
        """
        Holds the key libraries and creates the window with default settings
        :param x: The current board (default 0)
        :param text: The current text (default '')
        :return:
        """
        self.l = QLabel()
        self.l.setText(text)

        self.keys_sides = [
                    'Esc', 'Tab', 'Uppercase', 'Lowercase', 'Altcase'
                    ]

        self.keys_low = [
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', '1', '2', '3', 'h', 'i', 'j', 'k', 'l', 'm', 'n', '4', '5', '6',
                    'o', 'p', 'q', 'r', 's', 't', 'u', '7', '8', '9', 'v', 'w', 'x', 'y', 'z', chr(39), ',', '.', '0', 'Clear'
                    ]

        self.keys_high = [
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', '1', '2', '3', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '4', '5', '6',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U', '7', '8', '9', 'V', 'W', 'X', 'Y', 'Z', chr(39), ',', '.', '0', 'Clear'
                    ]

        self.keys_alt = [
                    '~', '`', '#', '$', '%', '^', '&', '1', '2', '3', '*', '(', ')', '_', '=', '+', '-', '4', '5', '6',
                    '<', '>', '{', '}', chr(47), '/', '@', '7', '8', '9', ':', ';', '"', '!', '?', chr(39), ',', '.', '0', 'Clear'
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
        """
        simulates a key press (currently not used)
        :param per: the given key
        :return:
        """
        pyautogui.press(per)

    def esc_press(self):
        """
        closes the window
        :return:
        """
        self.close()

    def caps_press(self):
        """
        changes the board to upper case letters and refreshes
        :return:
        """
        self.close()
        self.__init__(1, text)

    def shift_press(self):
        """
        changes the board to lower case characters and refreshes
        :return:
        """
        self.close()
        self.__init__(0, text)

    def alt_press(self):
        """
        Changes the board to alt characters and refreshes
        :return:
        """
        self.close()
        self.__init__(2, text)

    def make_sides(self, y):
        """
        Creates the sides side buttons
        :param y: The id for the current board
        :return:
        """
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
        """
        The center board with lower case letters
        :return:
        """
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
        """
        The center board with upper case letters
        :return:
        """
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
        """
        The center board with alternate symbols
        :return:
        """
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
        """
        Adds the given character to the global text
        :param y: The id for which board to refresh
        :param t: The text to add
        :return:
        """
        global text

        if (t == 'Clear'):
            text = ''
        else:
            text += t

        self.close()
        self.__init__(y, text)


    def remove_text(self, y):
        """
        Takes the global text and removes the last character
        :param y: The id for which board to refresh
        :return:
        """
        global text

        text = text[0:-1]

        self.close()
        self.__init__(y, text)


def move():
#    print("qwerty")

    while True:
        if msvcrt.getch() == 'w':
#           print("w")
            pyautogui.move(0, -10)
        elif msvcrt.getch() == 'a':
            pyautogui.move(-25, 0)
        elif msvcrt.getch() == 'd':
            pyautogui.move(25, 0)
        elif msvcrt.getch() == 's':
            pyautogui.move(0, 10)
        elif msvcrt.getch() == 'e':
            pyautogui.click()
        elif msvcrt.getch() == 'q':
            break


def eeg_in():

    global rsample
    global lsample

    # first resolve a LiSiLity stream on the lab network
    print('Looking for a LiSiLity stream...')
    streams = resolve_stream('type', 'LiSiLity.Angles')

    # create a new inlet to read from the stream
    inlet_left = StreamInlet(streams[0])
    inlet_right = StreamInlet(streams[1])

    while True:
        # get a new sample (you can also omit the timestamp part if you’re not
        # interested in it)
        lsample, ltimestamp = inlet_left.pull_sample()
        rsample, rtimestamp = inlet_right.pull_sample()
        for i in range(len(lsample)):
            lsample[i] = round(lsample[i], 2)
        for i in range(len(rsample)):
            rsample[i] = round(rsample[i], 2)
        print(round(ltimestamp, 0), lsample, rsample)


def run():
    app = QApplication(sys.argv)
    window = Window(0, '')
    sys.exit(app.exec_())


pyautogui.moveTo(50, pyautogui.size()[1] - 215)
thread2 = threading.Thread(None, eeg_in)
thread2.start()
thread3 = threading.Thread(None, move)
thread3.start()
run()