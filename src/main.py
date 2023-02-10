import sys
from datetime import datetime

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


from topic_iterator import TopicIterator

TITLEFONT: QFont = QFont("Helvetica", 32, 4, False)
DATEFONT: QFont = QFont("Helvetica", 24, 4, False)
SYSTEMFONT: QFont = QFont("Helvetica", 16, 2, False)
NAME: str = "noel"
CALENDER: str = "GCSEs"


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setWindowTitle("Retrospective Calender App")
        self.setMinimumSize(600, 500)

        self.scheduler: TopicIterator = TopicIterator(NAME, CALENDER)

        left_col_cont: QWidget = self.create_left_col()
        main_col_cont: QWidget = self.create_main_col()

        main_topic_label: QLabel = self.create_main_topic_label()

        self.glayout: QGridLayout = QGridLayout()
        self.glayout.addWidget(self.create_date_box(), 0, 0)
        self.glayout.addWidget(main_topic_label, 0, 1)
        self.glayout.addWidget(left_col_cont, 1, 0)
        self.glayout.addWidget(main_col_cont, 1, 1)

        container: QWidget = QWidget()
        container.setLayout(self.glayout)
        self.setCentralWidget(container)

    def create_date_box(self) -> QLabel:
        today: datetime = datetime.now()
        date_box: QLabel = QLabel(today.strftime("%A %d\n%B\n%Y"), self)
        date_box.setFont(DATEFONT)
        date_box.setFixedSize(200, 200)
        return date_box

    def create_main_topic_label(self) -> QLabel:
        # if self.scheduler.get_topic_name(0) )
        label: QLabel = QLabel("No Topic")
        label.setFont(TITLEFONT)
        label.setContentsMargins(20, 5, 20, 5)
        label.setFixedHeight(100)

        label.adjustSize()
        return label

    def create_main_col(self) -> QWidget:  # sourcery skip: class-extract-method
        main_col_layout: QVBoxLayout = QVBoxLayout()

        difficulty_label: QLabel = QLabel("New Difficulty")
        difficulty_label.setFont(SYSTEMFONT)
        self.difficulty_s: QDoubleSpinBox = QDoubleSpinBox()
        self.difficulty_s.setMaximum(10)
        self.difficulty_s.setMinimum(1)

        self.done_b: QPushButton = QPushButton("Done", self)

        main_col_layout.addWidget(difficulty_label)
        main_col_layout.addWidget(self.difficulty_s)
        main_col_layout.addWidget(self.done_b)

        main_col_cont: QWidget = QWidget()
        main_col_cont.setLayout(main_col_layout)

        return main_col_cont

    def create_left_col(self) -> QWidget:
        left_col_layout: QVBoxLayout = QVBoxLayout()

        top_label: QLabel = QLabel("Top 9 Topics")
        top_label.setFont(TITLEFONT)
        top_label.adjustSize()
        left_col_layout.addWidget(top_label)

        left_col_topics: list[QLabel] = []

        for i in range(9):
            name: str | None = self.scheduler.get_topic_name(i)
            score: float | None = self.scheduler.get_topic_score(i)

            if name is None:
                break
            text: str = f"{name.capitalize()} --- {score}"

            label_box: QLabel = QLabel(text)
            label_box.setFont(SYSTEMFONT)
            label_box.adjustSize()

            left_col_topics.append(label_box)
            left_col_layout.addWidget(label_box)

        left_col_cont: QWidget = QWidget()
        left_col_cont.setLayout(left_col_layout)

        return left_col_cont


App: QApplication = QApplication(sys.argv)
main_win: MainWindow = MainWindow()
main_win.show()
App.exec()
