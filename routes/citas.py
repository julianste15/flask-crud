from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from models.cita import Cita
from models.paciente import Paciente
from models.medico import Medico
from datetime import datetime

citas_bp = Blueprint('citas', __name__, url_prefix='/citas')

@citas_bp.route('/')
@citas_bp.route('/lista')
def lista():
    """Mostrar lista de todas las citas"""
    page = request.args.get('page', 1, type=int)
    citas = Cita.query.paginate(page=page, per_page=10)
    return render_template('citas/lista.html', citas=citas)

@citas_bp.route('/nueva', methods=['GET', 'POST'])
def nueva():
    """Crear una nueva cita"""
    if request.method == 'POST':
        try:
            paciente_id = request.form.get('paciente_id', type=int)
            medico_id = request.form.get('medico_id', type=int)
            fecha_str = request.form.get('fecha')
            hora_str = request.form.get('hora')
            motivo = request.form.get('motivo')
            
            # Validar que existan paciente y médico
            paciente = Paciente.query.get(paciente_id)
            medico = Medico.query.get(medico_id)
            
            if not paciente or not medico:
                flash('Paciente o Médico no encontrado', 'error')
                return redirect(url_for('citas.nueva'))
            
            # Convertir fecha y hora a datetime
            fecha_datetime = datetime.strptime(f"{fecha_str} {hora_str}", "%Y-%m-%d %H:%M")
            
            cita = Cita(
                paciente_id=paciente_id,
                medico_id=medico_id,
                fecha=fecha_datetime,
                motivo=motivo,
                estado='Pendiente'
            )
            
            db.session.add(cita)
            db.session.commit()
            
            flash('Cita creada exitosamente', 'success')
            return redirect(url_for('citas.lista'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear la cita: {str(e)}', 'error')
    
    pacientes = Paciente.query.all()
    medicos = Medico.query.all()
    return render_template('citas/nueva.html', pacientes=pacientes, medicos=medicos)

@citas_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    """Editar una cita existente"""
    cita = Cita.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            cita.paciente_id = request.form.get('paciente_id', type=int)
            cita.medico_id = request.form.get('medico_id', type=int)
            
            fecha_str = request.form.get('fecha')
            hora_str = request.form.get('hora')
            cita.fecha = datetime.strptime(f"{fecha_str} {hora_str}", "%Y-%m-%d %H:%M")
            
            cita.motivo = request.form.get('motivo')
            cita.estado = request.form.get('estado')
            cita.notas = request.form.get('notas')
            
            db.session.commit()
            flash('Cita actualizada exitosamente', 'success')
            return redirect(url_for('citas.lista'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar la cita: {str(e)}', 'error')
    
    pacientes = Paciente.query.all()
    medicos = Medico.query.all()
    estados = ['Pendiente', 'Confirmada', 'Cancelada', 'Completada']
    
    return render_template('citas/editar.html', cita=cita, pacientes=pacientes, medicos=medicos, estados=estados)

@citas_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    """Eliminar una cita"""
    cita = Cita.query.get_or_404(id)
    
    try:
        db.session.delete(cita)
        db.session.commit()
        flash('Cita eliminada exitosamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar la cita: {str(e)}', 'error')
    
    return redirect(url_for('citas.lista'))

@citas_bp.route('/detalles/<int:id>')
def detalles(id):
    """Ver detalles de una cita"""
    cita = Cita.query.get_or_404(id)
    return render_template('citas/detalles.html', cita=cita)

