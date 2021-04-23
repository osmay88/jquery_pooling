from flask import Flask


def setup_blueprints(app: Flask):
    from jquery_pooling.blueprints import main_view_bp, pooling_view_bp
    app.register_blueprint(main_view_bp)
    app.register_blueprint(pooling_view_bp)


def init_app():
    app = Flask(__name__)
    setup_blueprints(app)
    return app