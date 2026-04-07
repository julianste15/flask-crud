from flask import Blueprint, render_template

citas_bp = Blueprint('citas', __name__, url_prefix='/citas')

# Mock data para demostración
MOCK_CITAS = [
    {'id': 1, 'paciente': 'Juan Pérez', 'medico': 'Dr. House', 'fecha': '2026-04-10', 'estado': 'Pendiente'},
    {'id': 2, 'paciente': 'Maria García', 'medico': 'Dra. Quinn', 'fecha': '2026-04-12', 'estado': 'Confirmada'},
]

@citas_bp.route('/')
def lista():
    return render_template('citas/lista.html', citas=MOCK_CITAS)

@citas_bp.route('/nueva')
def nueva():
    return render_template('citas/nueva.html')

@citas_bp.route('/editar/<int:id>')
def editar(id):
    # In a real app we'd fetch the cita by id
    cita = next((c for c in MOCK_CITAS if c['id'] == id), None)
    return render_template('citas/editar.html', cita=cita)
