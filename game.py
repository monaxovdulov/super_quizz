from question import Question


class Game:
    def __init__(self, questions: list[Question]):
        self.questions = questions
        self.score = 0
        self.current_question = 0

    def get_current_question(self):
        return self.questions[self.current_question]

    def answer(self, answer: int):
        self.questions[self.current_question].check_answer(answer)

    def start(self):
        pass
