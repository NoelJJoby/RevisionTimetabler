import pickle
from typing import Self
from topic_class import Topic


class TopicIterator():
    def __init__(self, name, calender) -> None:
        # open old topics
        self.topics: list[Topic] = []
        with open(f"../data/{name}/{calender}/topics.pkl", "rb") as f:
            self.topics = pickle.load(f)

        self.name = name
        self.calender = calender

    def get_topic_name(self, pos: int) -> str | None:
        return None if pos > len(self.topics)-1 else self.topics[pos].name

    def get_topic_score(self, pos: int) -> float | None:
        return None if pos > len(self.topics)-1 else self.topics[pos].score

    def add_new_topics(self, name:str, difficulty:float) -> None:
        # add new topics
        self.topics.append(Topic(name, difficulty))
        self.topics.sort(key=lambda x: x.score)

    def schedule_topics(self) -> None:
        # calcuates each topics score
        for t in self.topics:
            t.calculate_score()

        # sorts the topics ascending by score
        self.topics.sort(key=lambda x: x.score)

    def save_scheduler(self) -> None:
        x.topics.sort(key=lambda x: x.score)
        with open(f"../data/{self.name}/{self.calender}/topics.pkl", "wb") as f:
            pickle.dump(self.topics, f)

# reset code
# import pickle
# from topic_class import Topic
# with open("../data/noel/GCSEs/topics.pkl", "wb") as f:
#     pickle.dump([], f)


if __name__ == "__main__":
    x: TopicIterator = TopicIterator("noel", "GCSEs")

    x.schedule_topics()
    while input("Add New Topics [Y/N]") == "Y":
        n: str = input("Enter New Topic Name::")
        d: float = float(input("Enter New Topic Difficulty::"))
        x.add_new_topics(n, d)

    cont: bool = input("Enter Y to display first topic [Y/N]") == "Y"
    for topic in x.topics:

        if not (cont):
            break

        print(topic)
        input("finished")
        topic.revise(float(input("New Difficulty 1-10 (10=easy):\n")))
        cont = input("Enter Y to display next topic [Y/N]") == "Y"


    input("close [ENTER]")
    x.save_scheduler()
