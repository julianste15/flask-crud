from database import db
from datetime import datetime

class Cita(db.Model):
    __tablename__ = 'citas'
    
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    motivo = db.Column(db.String(255), nullable=False)
    estado = db.Column(db.String(20), default='Pendiente', nullable=False)  # Pendiente, Confirmada, Cancelada, Completada
    notas = db.Column(db.Text)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Cita {self.id} - {self.estado}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'paciente_id': self.paciente_id,
            'paciente': f"{self.paciente.nombre} {self.paciente.apellido}" if self.paciente else None,
            'medico_id': self.medico_id,
            'medico': f"Dr. {self.medico.nombre} {self.medico.apellido}" if self.medico else None,
            'fecha': self.fecha.isoformat(),
            'motivo': self.motivo,
            'estado': self.estado,
            'notas': self.notas,
        }
