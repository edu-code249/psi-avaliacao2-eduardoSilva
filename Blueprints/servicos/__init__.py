from flask import Blueprint

servicos_bp = Blueprint("servicos", __name__, template_folder="templates")

from blueprint.servicos import routes