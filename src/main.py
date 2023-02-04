import sys
from datetime import datetime

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


from topic_iterator import TopicIterator

SYSTEMFONT: str = "Helvetica"
NAME: str = "noel"
CALENDER: str = "GCSEs"


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setWindowTitle("Retrospective Calender App")
        self.setMinimumSize(600, 500)

        self.scheduler: TopicIterator = TopicIterator(NAME, CALENDER)

        left_col_layout: QVBoxLayout = QVBoxLayout()
        for topic_label in self.create_left_col():
            left_col_layout.addWidget(topic_label)
        left_col_cont: QWidget = QWidget()
        left_col_cont.setLayout(left_col_layout)

        self.glayout: QGridLayout = QGridLayout()
        self.glayout.addWidget(self.create_date_box(), 0, 0)
        self.glayout.addWidget(left_col_cont, 1, 0)

        container: QWidget = QWidget()
        container.setLayout(self.glayout)
        self.setCentralWidget(container)

    def create_date_box(self) -> QLabel:
        today: datetime = datetime.now()
        date_box: QLabel = QLabel(today.strftime("%A %d\n%B\n%Y"), self)
        date_box.setFont(QFont(SYSTEMFONT, 16, 2, False))
        date_box.adjustSize()
        return date_box

    def create_left_col(self) -> list[QLabel]:
        left_col: list[QLabel] = []

        for i in range(9):
            name: str | None = self.scheduler.get_topic_name(i)
            score: float | None = self.scheduler.get_topic_score(i)

            if name is None:
                break
            text: str = f"{name.capitalize()} --- {score}"

            label_box: QLabel = QLabel(text)
            label_box.setFont(QFont(SYSTEMFONT, 16, 1, False))
            label_box.adjustSize()
            left_col.append(label_box)
        return left_col


App: QApplication = QApplication(sys.argv)
main_win: MainWindow = MainWindow()
main_win.show()
App.exec()
