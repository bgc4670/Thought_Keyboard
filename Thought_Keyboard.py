import sys
import pyautogui
import threading
import time
from pylsl import StreamInlet, resolve_stream
from functools import partial
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QToolTip
"""
This program is the GUI for the Thought Keyboard project using PyQT5 and pyautogui
:Start Date: 2-22-2019
:language: Python 3.7
:author: Brenton Cousins
"""
text = ''
t = 0
lsample = 0
rsample = 0


class Window(QWidget):

    def __init__(self, x):
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

        self.home(x)

    def home(self, x):
        """
        Holds the key libraries and creates the window with default settings
        :param x: The current board (default 0)
        :param text: The current text (default '')
        :return:
        """
        self.l = QLabel()
        self.l.setText(text)

        self.keys_sides = [
                    'Shift+Tab', 'Tab', 'Case Shift', 'Altcase', 'Clear'
                    ]

        self.keys_low = [
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', '1', '2', '3', 'h', 'i', 'j', 'k', 'l', 'm', 'n', '4', '5', '6',
                    'o', 'p', 'q', 'r', 's', 't', 'u', '7', '8', '9', 'v', 'w', 'x', 'y', 'z', chr(39), ',', '.', '0', 'Enter'
                    ]

        self.keys_high = [
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', '1', '2', '3', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '4', '5', '6',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U', '7', '8', '9', 'V', 'W', 'X', 'Y', 'Z', chr(39), ',', '.', '0', 'Enter'
                    ]

        self.keys_alt = [
                    '~', '`', '#', '$', '%', '^', '&', '1', '2', '3', '*', '(', ')', '_', '=', '+', '-', '4', '5', '6',
                    '<', '>', '{', '}', chr(47), '/', '@', '7', '8', '9', ':', ';', '"', '!', '?', chr(39), ',', '.', '0', 'Enter'
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

    def btn_press(self, per, y):
        """
        simulates a key press (currently not used)
        :param per: the given key
        :return:
        """

        global text

        if per == "Shift+Tab":
            pyautogui.hotkey('Alt', 'Tab')
            pyautogui.hotkey('Shift', 'Tab')
        elif per == "Case Shift":
            if y == 1 or y == 2:
                self.close()
                self.__init__(0)
            elif y ==0:
                self.close()
                self.__init__(1)
        elif per == "Clear":
            text = ''
            self.close()
            self.__init__(y)

        elif per == "Altcase":
            self.close()
            self.__init__(2)
        elif per == "Enter":
            text += "\n"
            pyautogui.hotkey('Alt', 'Tab')
            pyautogui.press("enter")
            self.close()
            self.__init__(y)
        elif per == "Tab":
            text += "     "
            pyautogui.hotkey('Alt', 'Tab')
            pyautogui.press("tab")
            self.close()
            self.__init__(y)
        elif per == "backspace":
            text = text[0:-1]
            pyautogui.hotkey('Alt', 'Tab')
            pyautogui.press(per)
            self.close()
            self.__init__(y)
        elif per == "space":
            text += " "
            pyautogui.hotkey('Alt', 'Tab')
            pyautogui.press(per)
            self.close()
            self.__init__(y)
        else:
            text += per
            pyautogui.hotkey('Alt', 'Tab')
            pyautogui.press(per)
            self.close()
            self.__init__(y)

    def make_sides(self, y):
        """
        Creates the sides side buttons
        :param y: The id for the current board
        :return:
        """
        v_box = QVBoxLayout()

        for s in self.keys_sides:
            x = QPushButton(s, self)
            x.clicked.connect(partial(self.btn_press, s, y))
            v_box.addWidget(x, y)

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
            x.clicked.connect(partial(self.btn_press, self.keys_low[i], 0))
            h_box1.addWidget(x)
        for i in range(10, 20):
            x = QPushButton(self.keys_low[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_low[i], 0))
            h_box2.addWidget(x)
        for i in range(20, 30):
            x = QPushButton(self.keys_low[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_low[i], 0))
            h_box3.addWidget(x)
        for i in range(30, 40):
            x = QPushButton(self.keys_low[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_low[i], 0))
            h_box4.addWidget(x)

        b = QPushButton('<--Backspace', self)
        b.clicked.connect(partial(self.btn_press, 'backspace', 0))
        h_box5.addWidget(b)

        s = QPushButton('_Space_', self)
        s.clicked.connect(partial(self.btn_press, 'space', 0))
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
            x.clicked.connect(partial(self.btn_press, self.keys_high[i], 1))
            h_box1.addWidget(x)
        for i in range(10, 20):
            x = QPushButton(self.keys_high[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_high[i], 1))
            h_box2.addWidget(x)
        for i in range(20, 30):
            x = QPushButton(self.keys_high[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_high[i], 1))
            h_box3.addWidget(x)
        for i in range(30, 40):
            x = QPushButton(self.keys_high[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_high[i], 1))
            h_box4.addWidget(x)

        b = QPushButton('<--Backspace', self)
        b.clicked.connect(partial(self.btn_press, 'backspace', 1))
        h_box5.addWidget(b)

        s = QPushButton('_Space_', self)
        s.clicked.connect(partial(self.btn_press, 'space', 1))
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
            x.clicked.connect(partial(self.btn_press, self.keys_alt[i], 2))
            h_box1.addWidget(x)
        for i in range(10, 20):
            x = QPushButton(self.keys_alt[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_alt[i], 2))
            h_box2.addWidget(x)
        for i in range(20, 30):
            x = QPushButton(self.keys_alt[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_alt[i], 2))
            h_box3.addWidget(x)
        for i in range(30, 40):
            x = QPushButton(self.keys_alt[i], self)
            x.clicked.connect(partial(self.btn_press, self.keys_alt[i], 2))
            h_box4.addWidget(x)

        b = QPushButton('<--Backspace', self)
        b.clicked.connect(partial(self.btn_press, 'backspace', 2))
        h_box5.addWidget(b)

        s = QPushButton('_Space_', self)
        s.clicked.connect(partial(self.btn_press, 'space', 2))
        h_box5.addWidget(s)

        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)
        v_box.addLayout(h_box5)

        return v_box


def move():
    global t
    if lsample == 1:
        pyautogui.move(-1, 0)
    elif lsample == 2:
        pyautogui.move(1, 0)
    elif rsample == 1:
        pyautogui.move(0, -1)
    elif rsample == 2:
        pyautogui.move(0, 1)
    elif rsample or lsample == 3:
        if time.time()-t > 3:
            pyautogui.click()
            t = time.time()



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
        move()


def run():
    pyautogui.moveTo(50, pyautogui.size()[1] - 215)
    app = QApplication(sys.argv)
    window = Window(0)
    sys.exit(app.exec_())


thread1 = threading.Thread(None, eeg_in)
thread1.start()
thread2 = threading.Thread(None, move)
thread2.start()
thread3 = threading.Thread(None, run)
thread3.start()
