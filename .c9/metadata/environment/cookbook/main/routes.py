{"filter":false,"title":"routes.py","tooltip":"/cookbook/main/routes.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["from flask import Blueprint, render_template","","# Blueprint instance to main route","main = Blueprint(\"main\", __name__)","","","'''","INDEX ROUTE","'''","","","@main.route('/')","def index():","    return render_template(\"index.html\")",""],"id":3}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1565723007133,"hash":"87f93a540b32bafc86baabe3e848088f5ff3c9c9"}