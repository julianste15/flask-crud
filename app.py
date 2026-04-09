from flask import Flask
import os
from datetime import datetime
from database import db

def create_app():
    app = Flask(__name__)
    
    # Secret Key Configuration (required for sessions and CSRF protection)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'clinica-piedrazul-dev-key-2026')
    
    # Database Configuration
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "clinic.db")}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    
    # Register Blueprints
    from routes.main import main_bp
    from routes.citas import citas_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(citas_bp)
    
    # Context processors - Variables disponibles en todas las plantillas
    @app.context_processor
    def inject_now():
        return {'now': datetime.now()}
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

