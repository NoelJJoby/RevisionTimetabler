import datetime

DIFF_MOD: int = 5
# Multiplier Effects
# 10 -> 2
# 5  -> 1
# 1  -> 0.2


class Topic():
    def __init__(self, name: str, difficulty: float) -> None:
        self.name: str = name
        self.difficulty: float = difficulty / DIFF_MOD
        self.last: int = int(datetime.datetime.now().strftime("%j"))
        self.total: int = 0
        self.score: float = 0

    def __str__(self) -> str:
        return f"""
        {self.name.capitalize()}
        Diff. -- {self.difficulty*DIFF_MOD}
        Last  -- {self.last}
        Total -- {self.total}
        ~~~~~~~~~~~~~~~~~~~~~
        Score -- {self.score}
        """

    def calculate_score(self) -> None:
        today: int = int(datetime.datetime.now().strftime("%j"))
        self.score += today - self.last

        self.score += self.total
        self.score *= self.difficulty

    def revise(self, difficulty: float) -> None:
        self.last = int(datetime.datetime.now().strftime("%j"))
        self.total += 1
        self.score += 1
        self.difficulty = difficulty / DIFF_MOD
