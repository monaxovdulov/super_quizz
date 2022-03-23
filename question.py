class Question:
    def __init__(self, question: str, answer: int, category: str, score: int, options: list):
        self.question = question
        self.answer = answer
        self.category = category
        self.score = score
        self.options = options

    def check_answer(self, answer: int) -> bool:
        return self.answer == answer
