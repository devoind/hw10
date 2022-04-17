import json


def get_candidates(path):
    """
    Функция для получения списка кандидатов из json-файла

    :param path: получает json-файл
    :return: возвращает список кандидатов из json-файла
    """
    with open(path, 'r', encoding='utf-8') as candidates:
        return json.load(candidates)


def format_candidates(candidates_list):
    """
    Функция для формирования списка кандидатов по шаблону

    :param candidates_list: получает список кандидатов
    :return: возвращает информацию о кандидате согласно шаблону
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
    Функция для формирования информации о кандидате по шаблону в зависимости от выбранной позиции

    :param candidate_list: получает список кандидатов
    :param candidate_id: получает номер позиции кандидата
    :return: возвращает информацию о кандидате
    """
    for candidate in candidate_list:
        if candidate['id'] == candidate_id:
            return candidate


def get_candidate_from_skills(candidate_list, candidate_skill):
    """
    Функция для формирования списка кандидатов по шаблону в зависимости от выбранных навыков

    :param candidate_list: получает список кандидатов
    :param candidate_skill: получает навык кандидата
    :return: возвращает список кандидатов по указанным навыкам
    """
    result = []
    for candidate in candidate_list:
        candidate_skills = candidate['skills'].lower().split(', ')
        if candidate_skill.lower() in candidate_skills:
            result.append(candidate)

    return result
