# выбирается режим игры либо с компом либо с игроками
# создаются игроки у кажого есть имя и очки
#


questions_dict = {
    1: {
        "text": "В каком году началась первая мировая война?",
        "options": ("1909", "1914", "1919"),
        "correct": "1914",

    },
    2: {
        "text": "Какой страны не было в Антанте во время ПМВ?",
        "options": ("Российская империя", "Япония", "Болгарское царство"),
        "correct": "Болгарское царство"
    },
    3: {
        "text": "Какая страна не сохраняла нейтралитет в ПМВ?",
        "options": ("Испания", "Швейцария", "Сербия", "Швеция"),
        "correct": "Сербия"
    },
}


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


class Game:
    pass


