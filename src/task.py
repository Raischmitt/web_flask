from flask import (Blueprint, redirect, request, url_for)

from src.db import get_db

bp = Blueprint('tarefa', __name__, url_prefix='/tarefa')

@bp.route("/adicionar", methods=["POST"])
def adicionar():
    db = get_db()
    tarefa = request.form["item"]
    db.execute('INSERT INTO lista (tarefa) values (?)', (tarefa,))
    db.commit() 
    return redirect(url_for('index'))

@bp.route("/remover", methods=["POST"])
def remover():
    db = get_db()
    codigo_lista = request.form["item"]
    db.execute(f'DELETE FROM lista WHERE codigo_lista = {codigo_lista}')
    db.commit()
    return redirect(url_for('index'))