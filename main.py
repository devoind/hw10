from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def main():
    """
    Функция, которая выводит на главную страницу список кандидатов

    :return: возвращаем список кандидатов
    """
    candidates_list = utils.get_candidates('candidates.json')

    return utils.format_candidates(candidates_list)


@app.route("/candidates/<int:candidate_id>")
def name_candidates(candidate_id):
    """
    Функция, которая выводит кандидата по номеру позиции

    :param candidate_id: номер позиции кандидата
    :return: возвращает информацию о кандидате, который соответсвует указанной позиции
    """
    candidates_list = utils.get_candidates('candidates.json')
    candidate = utils.get_candidate_from_id(candidates_list, candidate_id)
    result = f'<img src = "{candidate["picture"]}">'
    return result + utils.format_candidates([candidate])


@app.route("/skills/<skill>")
def skills_candidates(skill):
    """
    Функция, которая выводит кандидатов в зависимости от указанного навыка (skill)

    :param skill: навык кандидата
    :return: возвращает список кандидатов, у которых имеются соответствующие навыки
    """
    candidates_list = utils.get_candidates('candidates.json')

    return utils.format_candidates(utils.get_candidate_from_skills(candidates_list, skill))


app.run()
