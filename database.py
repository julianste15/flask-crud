"""
Inicialización de SQLAlchemy desacoplada de la aplicación Flask
para evitar circular imports
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
