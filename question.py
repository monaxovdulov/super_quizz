class Question:
    def __init__(self, question: str, answer: int, category: str, score: int, options: dict):
        self.question = question
        self.answer = answer
        self.category = category
        self.score = score
        self.options = options

    def check_answer(self, answer: int) -> bool:
        return self.answer == answer

    def get_correct_answer(self):
        return self.options[str(self.answer)]

    def get_answer_options(self):
        return self.options.values()
