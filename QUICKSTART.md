# 🚀 Guía Rápida de Inicio

## Inicio Rápido en 3 Pasos

### Paso 1: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 2: Inicializar la base de datos
```bash
python seed_database.py
```

Esto crea:
- 3 pacientes de prueba
- 3 médicos de prueba  
- 3 citas de prueba

### Paso 3: Ejecutar la aplicación
```bash
python app.py
```

Luego abre tu navegador en: **http://localhost:5000**

---

## ✨ Funcionalidades Principales

### 📋 Gestión de Citas
- **Ver todas las citas** en http://localhost:5000/citas/
- **Crear nueva cita** en http://localhost:5000/citas/nueva
- **Editar cita** haciendo clic en el ícono ✏️
- **Eliminar cita** haciendo clic en el ícono 🗑️
- **Ver detalles** haciendo clic en 👁️

### 🎨 Interfaz
- Tema oscuro moderno
- Responsive (funciona en móviles)
- Animaciones suaves
- Mensajes de éxito/error

---

## 📚 Estructura Aprendida

Esta aplicación demuestra:

### 1. **MODELOS** (models/)
- SQLAlchemy ORM
- Relaciones entre tablas
- Validaciones de datos

### 2. **CONTROLADORES** (routes/)
- Flask Blueprints
- Operaciones CRUD
- Manejo de formularios
- Redirecciones y flash messages

### 3. **VISTAS** (templates/)
- Templates Jinja2
- Renderizado dinámico
- Herencia de plantillas
- CSS moderno

---

## 🐛 Solución de Problemas

### Error: "No module named 'flask'"
```bash
pip install flask>=3.0.0
```

### Error: "No module named 'flask_sqlalchemy'"
```bash
pip install flask-sqlalchemy>=3.1.1
```

### Error: "clinic.db not found"
```bash
python seed_database.py
```

### Puerto 5000 ya está en uso
```bash
python app.py --port 5001
```

---

## 📖 Documentación Completa

Para entender la arquitectura MVC detalladamente, lee:
- [ARCHITECTURE.md](ARCHITECTURE.md) - Guía completa de arquitectura
- [EXPLICACION_FRONTEND.md](EXPLICACION_FRONTEND.md) - Guía detallada del Frontend
- [README.md](README.md) - Información general del proyecto

---

## 🔗 Rutas Importantes

| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Página de inicio |
| `/citas/` | GET | Listado de citas (paginado) |
| `/citas/nueva` | GET/POST | Crear nueva cita |
| `/citas/editar/<id>` | GET/POST | Editar cita |
| `/citas/eliminar/<id>` | POST | Eliminar cita |
| `/citas/detalles/<id>` | GET | Ver detalles de cita |

---

## 💾 Base de Datos

La base de datos SQLite se crea automáticamente:
- **Archivo**: `clinic.db` (en la raíz del proyecto)
- **Tablas**: pacientes, médicos, citas
- **Relaciones**: Foreign keys automáticas

---

## 🎯 Próximos Pasos

Después de entender el código básico, prueba agregar:

1. **Validación avanzada**: Fecha/hora mínima, máxima
2. **Búsqueda**: Filtrar citas por paciente o médico
3. **Autenticación**: Login de usuarios
4. **Email**: Confirmación de citas por email
5. **API**: Endpoints JSON para aplicaciones móviles

---

¡Felicidades! 🎉 Ahora tienes un sistema CRUD completo con arquitectura MVC.
