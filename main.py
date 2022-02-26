from flask import Flask

from utils import get_candidate_id, get_candidate_skill, data_load

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = data_load()
    page_content = ""
    for candidate in candidates:
        page_content += candidate["name"] + "\n" + candidate["position"] + "\n" + candidate["skills"] + "\n\n"

    return "<pre>" + page_content + "</pre>"


@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    candidate = get_candidate_id(uid)

    page_content = f'<img src={candidate["picture"]}>\n<pre>{candidate["name"]}\n{candidate["position"]}\n{candidate["skills"]}<pre>'

    return page_content


@app.route("/skill/<skill_name>")
def page_skill(skill_name):
    candidates = get_candidate_skill(skill_name)

    page_content = ""

    for candidate in candidates:
        page_content += candidate["name"] + "\n" + candidate["position"] + "\n" + candidate["skills"] + "\n\n"

    return "<pre>" + page_content + "</pre>"


app.run()
