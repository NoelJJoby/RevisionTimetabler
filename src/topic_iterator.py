import pickle
from typing import Self
from topic_class import Topic


class TopicIterator():
    def __init__(self, name, calender) -> None:
        # open old topics
        self.topics: list[Topic] = []
        with open(f"../data/{name}/{calender}/topics.pkl", "rb") as f:
            self.topics = pickle.load(f)

    def __iter__(self) -> Self:
        self.pos: int = -1
        return self

    def __next__(self) -> Topic:
        """
        Iterates over each topic
        at each iteration calls that topic's revise func.
        """
        self.topics.sort(key=lambda x: x.score)
        if self.pos == len(self.topics) - 1:  # 2
            self.topics[self.pos].revise(
                float(input("New Difficulty 1-10 (10=easy):\n")))
            raise StopIteration

        if self.pos != -1:
            self.topics[self.pos].revise(
                float(input("New Difficulty 1-10 (10=easy):\n")))

        self.pos += 1
        return self.topics[self.pos]

    def add_new_topics(self) -> None:
        # add new topics
        while True:
            name: str = input("Next Topic: [STOP/name]\n")
            if name == "STOP":
                break
            difficulty: float = float(input("Difficulty 1-10 (10=easy):\n"))
            self.topics.append(Topic(name, difficulty))

    def schedule_topics(self) -> None:
        # calcuates each topics score
        for t in self.topics:
            t.calculate_score()

        # sorts the topics ascending by score
        self.topics.sort(key=lambda x: x.score)

    def close_scheduler(self) -> None:
        with open("../data.pkl", "wb") as f:
            pickle.dump(self.topics, f)
