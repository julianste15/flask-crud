"""
Script para inicializar datos de prueba en la base de datos
Ejecutar con: python seed_database.py
"""

from app import create_app
from database import db
from models.paciente import Paciente
from models.medico import Medico
from models.cita import Cita
from datetime import datetime, timedelta

def seed_database():
    """Inicializa la base de datos con datos de ejemplo"""
    
    app = create_app()
    
    with app.app_context():
        # Limpiar datos existentes
        db.drop_all()
        db.create_all()
        
        # Crear pacientes de ejemplo
        pacientes = [
            Paciente(
                nombre="Juan",
                apellido="Pérez",
                cedula="123456789",
                email="juan.perez@email.com",
                telefono="555-0101",
                fecha_nacimiento=datetime(1985, 5, 15).date(),
                direccion="Calle Principal 123, Santiago"
            ),
            Paciente(
                nombre="María",
                apellido="García",
                cedula="987654321",
                email="maria.garcia@email.com",
                telefono="555-0102",
                fecha_nacimiento=datetime(1990, 3, 22).date(),
                direccion="Avenida Central 456, Santiago"
            ),
            Paciente(
                nombre="Carlos",
                apellido="Rodríguez",
                cedula="456789123",
                email="carlos.rodriguez@email.com",
                telefono="555-0103",
                fecha_nacimiento=datetime(1978, 8, 10).date(),
                direccion="Calle Secondary 789, Santiago"
            ),
        ]
        
        # Crear médicos de ejemplo
        medicos = [
            Medico(
                nombre="Antonio",
                apellido="Martínez",
                especialidad="Medicina General",
                cedula_profesional="MED001",
                email="a.martinez@clinica.com",
                telefono="555-1001",
                consultorio="101"
            ),
            Medico(
                nombre="Elena",
                apellido="López",
                especialidad="Cardiología",
                cedula_profesional="MED002",
                email="e.lopez@clinica.com",
                telefono="555-1002",
                consultorio="202"
            ),
            Medico(
                nombre="Diego",
                apellido="Sánchez",
                especialidad="Pediatría",
                cedula_profesional="MED003",
                email="d.sanchez@clinica.com",
                telefono="555-1003",
                consultorio="303"
            ),
        ]
        
        # Guardar pacientes y médicos
        for paciente in pacientes:
            db.session.add(paciente)
        for medico in medicos:
            db.session.add(medico)
        
        db.session.commit()
        
        # Crear citas de ejemplo
        ahora = datetime.now()
        citas = [
            Cita(
                paciente_id=1,
                medico_id=1,
                fecha=ahora + timedelta(days=1, hours=10),
                motivo="Consulta de rutina",
                estado="Pendiente",
                notas="Paciente sin antecedentes relevantes"
            ),
            Cita(
                paciente_id=2,
                medico_id=2,
                fecha=ahora + timedelta(days=2, hours=14),
                motivo="Revisión cardiaca",
                estado="Confirmada",
                notas="Control periódico"
            ),
            Cita(
                paciente_id=3,
                medico_id=3,
                fecha=ahora + timedelta(days=3, hours=9),
                motivo="Revisión de niño sano",
                estado="Pendiente"
            ),
        ]
        
        for cita in citas:
            db.session.add(cita)
        
        db.session.commit()
        
        print("✅ Base de datos inicializada correctamente!")
        print(f"✓ {len(pacientes)} pacientes creados")
        print(f"✓ {len(medicos)} médicos creados")
        print(f"✓ {len(citas)} citas creadas")

if __name__ == "__main__":
    seed_database()
