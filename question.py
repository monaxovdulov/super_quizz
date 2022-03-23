class Question:
    def __init__(self, text: str, answer: int, category: str, score: int, options: dict):
        self.text = text
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
