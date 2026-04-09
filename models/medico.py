from database import db
from datetime import datetime

class Medico(db.Model):
    __tablename__ = 'medicos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    cedula_profesional = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    consultorio = db.Column(db.String(50))
    horario_entrada = db.Column(db.Time)
    horario_salida = db.Column(db.Time)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    citas = db.relationship('Cita', backref='medico', lazy=True)
    
    def __repr__(self):
        return f'<Medico Dr. {self.nombre} {self.apellido}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'especialidad': self.especialidad,
            'cedula_profesional': self.cedula_profesional,
            'email': self.email,
            'telefono': self.telefono,
            'consultorio': self.consultorio,
            'horario_entrada': self.horario_entrada.isoformat() if self.horario_entrada else None,
            'horario_salida': self.horario_salida.isoformat() if self.horario_salida else None,
        }
