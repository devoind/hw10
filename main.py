from flask import Flask
import utils

app = Flask(__name__)


@app.route("/")
def main():
    """
    :return:
    """
    candidates_list = utils.get_candidates('candidates.json')

    return utils.format_candidates(candidates_list)


@app.route("/candidates/<int:candidate_id>")
def name_candidates(candidate_id):
    """
    :param candidate_id:
    :return:
    """
    candidates_list = utils.get_candidates('candidates.json')
    candidate = utils.get_candidate_from_id(candidates_list, candidate_id)
    result = f'<img src = "{candidate["picture"]}">'
    return result + utils.format_candidates([candidate])


@app.route("/skills/<skill>")
def skills_candidates(skill):
    """
    :param skill:
    :return:
    """
    candidates_list = utils.get_candidates('candidates.json')

    return utils.format_candidates(utils.get_candidate_from_skills(candidates_list, skill))


app.run()
