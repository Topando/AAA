import random
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup, QLabel, QGridLayout
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor, QBrush
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5 import QtCore

qp = QPainter()


class StartMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        qp.begin(self)

        self.pushButton.clicked.connect(self.click)

    def click(self):
        self.update()

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        # Начинаем процесс рисования
        qp.begin(self)

        self.draw_flag(qp)
        # Завершаем рисование
        qp.end()

    def draw_flag(self, qp):
        # Задаем кисть
        if True:
            # Рисуем прямоугольник заданной кистью
            qp.setBrush(QColor(255, 255, 0))
            R = random.randint(0, 200)
            X = random.randint(0, 400)
            Y = random.randint(0, 200)

            print(R)
            qp.drawEllipse(X, Y, R, R)

