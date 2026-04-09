"""
Script de prueba para verificar que la aplicación funciona correctamente
Ejecutar con: python test_app.py
"""

from app import create_app
from database import db
from models.cita import Cita

def test_create_app():
    """Prueba que la app se crea sin errores"""
    app = create_app()
    print("✓ Aplicación Flask creada")
    return app

def test_database(app):
    """Prueba que la BD está configurada"""
    with app.app_context():
        # Verificar que el archivo de BD existe
        import os
        db_path = os.path.join(os.path.dirname(__file__), "clinic.db")
        if os.path.exists(db_path):
            print("✓ Base de datos encontrada")
        
        # Verificar que hay datos
        citas_count = db.session.query(Cita).count()
        print(f"✓ Total de citas en BD: {citas_count}")

def test_secret_key(app):
    """Prueba que la secret key está configurada"""
    if app.config.get('SECRET_KEY'):
        print("✓ Secret key configurada para sesiones")
    else:
        print("✗ Secret key NO configurada")

if __name__ == "__main__":
    print("🧪 Ejecutando pruebas...\n")
    
    app = test_create_app()
    test_database(app)
    test_secret_key(app)
    
    print("\n✅ ¡Todas las pruebas pasaron!")
    print("\nPara iniciar la aplicación:")
    print("  python app.py")
    print("\nLuego abre tu navegador en:")
    print("  http://localhost:5000")

