class Question:
    def __init__(self, question, answer, category, score):
        self.question = question
        self.answer = answer
        self.category = category
        self.score = score

    def is_correct_answer(self, answer_user):
        if self.answer == answer_user:
            return True
        return False
