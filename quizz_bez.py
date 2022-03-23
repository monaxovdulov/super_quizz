import json

from game import Game
from question import Question


def main():
    # read json file
    with open('quizz.json') as json_file:
        data = json.load(json_file)
    questions = []
    for q in data:
        questions.append(Question(q['text'], q['correct'], q['category'], q['score'], q['options']))
    game = Game(questions)
    game.start()


if __name__ == '__main__':
    main()
