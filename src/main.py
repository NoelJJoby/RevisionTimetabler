from topic_iterator import TopicIterator
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys
from datetime import datetime


SYSTEMFONT: str = "Helvetica"


class Colour(QWidget):
    def __init__(self, color) -> None:
        super(Colour, self).__init__()
        self.setAutoFillBackground(True)

        palette: QPalette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setWindowTitle("Retrospective Calender App")
        self.setMinimumSize(600, 500)

        today: datetime = datetime.now()
        date_box: QLabel = QLabel(today.strftime("%A %d\n%B\n%Y"), self)
        date_box.setFont(QFont(SYSTEMFONT, 16, 2, False))
        date_box.adjustSize()

        layout: QGridLayout = QGridLayout()
        layout.addWidget(date_box, 0, 0)

        container: QWidget = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


App: QApplication = QApplication(sys.argv)

main_win: MainWindow = MainWindow()

main_win.show()
App.exec()


# reset code
# import pickle
# from topic_class import Topic
# with open("../data/noel/GCSEs/topics.pkl", "wb") as f:
#     pickle.dump([], f)


# x: TopicIterator = TopicIterator("noel", "GCSEs")

# x.add_new_topics()
# x.schedule_topics()
# for topic in x:
#     print(topic)
#     input("Press enter to display next topic")

# input("close [ENTER]")
# x.close_scheduler()
