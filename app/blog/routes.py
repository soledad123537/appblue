from flask import Blueprint, render_template, abort

blog_bp = Blueprint('blog', __name__, template_folder='templates')

# Entradas de ejemplo: id -> titulo
ENTRADAS = {
    1: "Mi primera entrada",
    2: "Aprendiendo Flask",
    3: "Blueprints y plantillas",
}


# /entrada/1
@blog_bp.route("/entrada/<int:id>")
def entrada(id):
    titulo = ENTRADAS.get(id)
    if titulo is None:
        abort(404)
    return render_template('entrada.html', titulo=titulo)
