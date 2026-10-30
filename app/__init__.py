from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    # Registro de los blueprints (modulos)
    from app.usuarios.routes import usuarios_bp
    from app.producto.routes import producto_bp
    from app.admin.routes import admin_bp
    from app.blog.routes import blog_bp

    app.register_blueprint(usuarios_bp)
    app.register_blueprint(producto_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(blog_bp)

# Pagina de inicio con el menu
    @app.route('/')
    def inicio():
        return render_template('inicio.html')

    return app

