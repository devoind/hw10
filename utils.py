import json


def get_candidates(path):
    """
    
    :param path: 
    :return: 
    """""
    with open(path, 'r', encoding='utf-8') as candidates:
        return json.load(candidates)


def format_candidates(candidates_list):
    """

    :param candidates_list:
    :return:
    """
    result = '<pre>'
    for candidate in candidates_list:
        result += (
            f"Имя кандидата №{candidate['id']} - {candidate['name']}\n"
            f"Позиция кандидата: {candidate['position']}\n"
            f"Навыки через запятую: {candidate['skills']}\n"
            '\n'
        )

    result += '<pre>'
    return result


def get_candidate_from_id(candidate_list, candidate_id):
    """

    :param candidate_list:
    :param candidate_id:
    :return:
    """
    for candidate in candidate_list:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidate_from_skills(candidate_list, candidate_skill):
    result = []
    for candidate in candidate_list:
        candidate_skills = candidate['skills'].lower().split(', ')
        if candidate_skill.lower() in candidate_skills:
            result.append(candidate)

    return result
