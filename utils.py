import json


def data_load():
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
        return candidates


def get_candidate_id(uid):
    candidates = data_load()
    for candidate in candidates:
        if candidate["id"] == uid:
            return candidate


def get_candidate_skill(skill):
    candidates = data_load()
    skill_lower = skill.lower()
    skill_candidates = []

    for candidate in candidates:
        if skill_lower in candidate["skills"].lower().split(", "):
            skill_candidates.append(candidate)

    return skill_candidates


print(get_candidate_skill("python"))
