from flask import Flask, render_template
import os
from . import db
from . import task

def create_app():
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY="dev",
    DATABASE=os.path.join(app.instance_path, 'src.sqlite')
  )

  app.register_blueprint(task.bp)

  db.init_app(app)

  @app.route('/ping')
  def ping():
    return "pong"

  @app.route('/')
  def index():
    banco = db.get_db()
    data = banco.execute('SELECT codigo_lista, tarefa FROM lista')
    return render_template("home.html", data=data)
  
  return app