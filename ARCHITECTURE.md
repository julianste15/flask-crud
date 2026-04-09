# 📋 Sistema de Gestión de Citas - Clínica Piedrazul

## 🏗️ Arquitectura MVC adaptada en Flask

Este proyecto implementa una arquitectura **Modelo-Vista-Controlador (MVC)** adaptada para Flask, demostrando cómo organizar una aplicación web moderna siguiendo principios de separación de responsabilidades.

### Estructura del Proyecto

```
Flask-crud/
├── app.py                    # Punto de entrada y configuración
├── models/                   # CAPA DE DATOS
│   ├── __init__.py
│   ├── paciente.py          # Modelo SQLAlchemy - Paciente
│   ├── medico.py            # Modelo SQLAlchemy - Médico
│   └── cita.py              # Modelo SQLAlchemy - Cita
├── routes/                   # CAPA DE CONTROL (Controladores)
│   ├── __init__.py
│   ├── main.py              # Rutas principales (inicio)
│   └── citas.py             # Controlador CRUD de citas
├── templates/                # CAPA DE PRESENTACIÓN (Vistas)
│   ├── base.html            # Plantilla base con navegación
│   ├── index.html           # Página de inicio
│   └── citas/
│       ├── lista.html       # Listado de citas
│       ├── nueva.html       # Formulario para crear cita
│       ├── editar.html      # Formulario para editar cita
│       └── detalles.html    # Vista de detalles de cita
├── static/
│   └── css/
│       └── style.css        # Estilos globales
├── requirements.txt         # Dependencias Python
├── seed_database.py         # Script para datos de prueba
└── README.md               # Este archivo
```

---

## 🔄 Flujo de Arquitectura MVC

### 1. **MODELOS (Models)** - Capa de Datos
Definen la estructura de datos y la interacción con la base de datos.

- **`paciente.py`**: Define el modelo `Paciente` con SQLAlchemy
  - Atributos: nombre, apellido, cédula, email, teléfono, fecha_nacimiento, dirección
  - Relación: Un paciente puede tener múltiples citas

- **`medico.py`**: Define el modelo `Medico`
  - Atributos: nombre, apellido, especialidad, cédula_profesional, email, teléfono, consultorio
  - Relación: Un médico puede tener múltiples citas

- **`cita.py`**: Define el modelo `Cita`
  - Atributos: paciente_id, medico_id, fecha, motivo, estado, notas
  - Relaciones: Vinculado a Paciente y Médico mediante foreign keys

### 2. **CONTROLADORES (Routes)** - Capa de Control
Manejan las peticiones HTTP, procesan datos y coordinan entre modelos y vistas.

**`routes/citas.py`** - Implementa operaciones CRUD:

#### GET /citas/ - Listar citas
```python
@citas_bp.route('/')
def lista():
    page = request.args.get('page', 1, type=int)
    citas = Cita.query.paginate(page=page, per_page=10)
    return render_template('citas/lista.html', citas=citas)
```

#### GET /citas/nueva - Mostrar formulario
```python
@citas_bp.route('/nueva', methods=['GET', 'POST'])
def nueva():
    if request.method == 'POST':
        # Procesar datos del formulario
        # Crear nueva cita en BD
        # Redirigir a lista
    # Mostrar formulario con pacientes y médicos
```

#### POST /citas/nueva - Crear cita
El mismo endpoint maneja GET y POST
- Lee datos del formulario
- Valida que existan paciente y médico
- Crea objeto Cita
- Guarda en BD
- Redirige a lista con mensaje de éxito

#### GET /citas/editar/<id> - Editar cita
- Carga la cita por ID
- Muestra formulario con datos precargados
- POST actualiza los datos y guarda cambios

#### POST /citas/eliminar/<id> - Eliminar cita
- Busca la cita por ID
- La elimina de la BD
- Redirige a lista

#### GET /citas/detalles/<id> - Ver detalles
- Muestra información completa de la cita
- Incluye paciente y médico relacionados

---

## 🎨 VISTAS (Templates) - Capa de Presentación
HTML con Jinja2 templating engine que renderizan datos dinámicamente.

### Plantillas Principales:

**`base.html`** - Plantilla base
- Navegación
- Sistema de alertas (success/error)
- Estilos globales
- Estructura HTML común

**`index.html`** - Página de inicio
- Información sobre MVC
- Botones de acceso rápido
- Descripción del proyecto

**`citas/lista.html`** - Listado de citas
- Tabla con todas las citas
- Paginación
- Botones de acción (ver, editar, eliminar)
- Badges de estado con colores
- Estado vacío cuando no hay citas

**`citas/nueva.html`** - Crear nueva cita
- Selector de paciente
- Selector de médico
- Campos de fecha y hora
- Campo de motivo
- Información importante

**`citas/editar.html`** - Editar cita
- Todos los campos editables
- Selector de estado
- Campo de notas
- Información de creación y actualización

**`citas/detalles.html`** - Ver detalles
- Información completa de la cita
- Datos del paciente
- Datos del médico
- Historial de cambios
- Botones para editar o eliminar

---

## 🚀 Instalación y Uso

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Inicializar base de datos con datos de prueba
```bash
python seed_database.py
```

Salida esperada:
```
✅ Base de datos inicializada correctamente!
✓ 3 pacientes creados
✓ 3 médicos creados
✓ 3 citas creadas
```

### 3. Ejecutar la aplicación
```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

---

## 📊 Flujo de una Petición

### Ejemplo: Crear una nueva cita

```
1. USUARIO hace clic en "Nueva Cita"
   ↓
2. Flask ROUTER (routes/citas.py) intercepta GET /citas/nueva
   ↓
3. CONTROLADOR (nueva()) consulta MODELOS por pacientes y médicos
   ↓
4. MODELOS (Paciente.query.all(), Medico.query.all()) ejecutan SQL
   ↓
5. VISTA (nueva.html) con Jinja2 procesa los datos y renderiza HTML
   ↓
6. NAVEGADOR recibe página con opciones de pacientes y médicos
   ↓
7. USUARIO llena el formulario y hace clic en "Agendar Cita"
   ↓
8. Flask ROUTER intercepta POST /citas/nueva
   ↓
9. CONTROLADOR procesa request.form y crea objeto Cita()
   ↓
10. MODELO Cita.add() y db.commit() guardan en SQLite
    ↓
11. CONTROLADOR redirige a GET /citas/
    ↓
12. VISTA lista.html renderiza con datos actualizados incluyendo la nueva cita
```

---

## 🗄️ Base de Datos

SQLAlchemy con SQLite proporciona:
- **ORM (Object-Relational Mapping)**: Los modelos Python mapean a tablas SQL
- **Relaciones**: Foreign keys entre Paciente-Cita y Médico-Cita
- **Validaciones**: Campos obligatorios y únicos
- **Timestamps**: Fechas de creación y actualización automáticas

### Relaciones:
```
Paciente (1 ---> N) Cita
Médico   (1 ---> N) Cita
```

Una cita SIEMPRE tiene:
- Un paciente
- Un médico
- Una fecha
- Un motivo
- Un estado (Pendiente, Confirmada, Cancelada, Completada)

---

## 🎯 Características Implementadas

✅ **CRUD Completo**
- Create (Crear citas)
- Read (Ver listado y detalles)
- Update (Editar citas)
- Delete (Eliminar citas)

✅ **Interfaz Moderna**
- Diseño glassmorphismo
- Tema oscuro
- Responsive (mobile-friendly)
- Animaciones suaves

✅ **Validación y Seguridad**
- Confirmación antes de eliminar
- Validación de datos en servidor
- Manejo de errores con mensajes flash

✅ **Paginación**
- Listado de citas paginado (10 por página)
- Navegación fácil

✅ **Estados de Cita**
- Pendiente (naranja)
- Confirmada (verde)
- Cancelada (rojo)
- Completada (azul)

---

## 💡 Ventajas de esta Arquitectura MVC

### Separación de Responsabilidades
- **Modelos**: Solo datos y lógica de BD
- **Controladores**: Lógica de negocio
- **Vistas**: Presentación al usuario

### Mantenibilidad
- Cambios en diseño no afectan lógica
- Cambios en BD no requieren actualizar vistas
- Fácil de debuggear

### Escalabilidad
- Agregar nuevas funcionalidades es simple
- Reutilizar modelos en múltiples vistas
- Compartir controladores

### Testabilidad
- Cada capa se puede probar independientemente
- Modelos sin dependencias de vistas
- Controladores fáciles de testear

---

## 🔐 Mejoras Futuras

- [ ] Autenticación de usuarios
- [ ] Confirmación por email
- [ ] Calendario interactivo
- [ ] Búsqueda avanzada de citas
- [ ] Reportes y estadísticas
- [ ] API REST
- [ ] Notificaciones
- [ ] Historial del paciente
- [ ] Recetas médicas generadas
- [ ] Integración con sistemas de pago

---

## 📝 Notas Técnicas

- **Framework**: Flask >= 3.0.0
- **ORM**: SQLAlchemy >= 3.1.1
- **Base de Datos**: SQLite
- **Templating**: Jinja2
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Python**: 3.8+

---

## 🤝 Contribuciones

Este proyecto es educativo y está diseñado para demostrar la arquitectura MVC adaptada a Flask.

---

**Creado por**: GitHub Copilot
**Fecha**: 2026
**Licencia**: MIT
