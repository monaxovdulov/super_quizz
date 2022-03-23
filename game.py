from question import Question

FLAG_GAME_CREATED = 'game_created'
FLAG_GAME_STARTED = 'game_started'
FLAG_GAME_FINISHED = 'game_finished'


class Game:
    def __init__(self, questions: list[Question]):
        self.questions = questions
        self.score = 0
        self.current_question = 0
        self.status = FLAG_GAME_CREATED

    def get_current_question(self):
        return self.questions[self.current_question]

    def answer(self, answer: int):
        question = self.questions[self.current_question]

        # check correctness
        is_answer_correct = question.check_answer(answer)
        if is_answer_correct:
            self.score += question.score

        # move to next question
        self.current_question += 1

        # check if game is finished
        if self.current_question == len(self.questions):
            self.finish()
        return is_answer_correct

    def start(self):
        self.status = FLAG_GAME_STARTED

    def finish(self):
        self.status = FLAG_GAME_FINISHED
