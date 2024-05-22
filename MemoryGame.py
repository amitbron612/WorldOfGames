import random

class MemoryGame:
    def __init__(self, difficulty, sequence=None):
        self.difficulty = int(difficulty)
        self.sequence = sequence if sequence is not None else self.generate_sequence()

    def generate_sequence(self):
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def is_list_equal(self, list1, list2):
        return list1 == list2

    def play(self, user_list):
        result = self.is_list_equal(self.sequence, user_list)
        return result, self.sequence
