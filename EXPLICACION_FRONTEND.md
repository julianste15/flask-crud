# 🎨 Documentación del Frontend - Clínica Piedrazul

Esta guía explica cómo está construido el frontend del sistema de **Gestión de Citas**, detallando el uso de plantillas, lógica de Jinja2 y la interacción con el backend.

---

## 🔧 1. Uso de Jinja2 (Motor de Plantillas)

Jinja2 permite que el HTML sea dinámico. En este proyecto se utiliza para:

### **A. Herencia de Plantillas**
Para no repetir el código del menú y el pie de página, usamos un archivo base:
- `{% extends "base.html" %}`: Indica que la página hereda la estructura de `base.html`.
- `{% block content %}`: Define el espacio donde cada página (Inicio, Lista, Nueva) inserta su propio contenido.

### **B. Generación de URLs Dinámicas**
Usamos `url_for` para que Flask genere las rutas automáticamente, evitando errores de enlaces rotos:
- `<a href="{{ url_for('citas.lista') }}">`: Enlace a la página de listado.
- `<form action="{{ url_for('citas.nueva') }}">`: Destino del formulario de creación.

### **C. Estructuras de Control**
- **Ciclos (For)**: Para mostrar las citas en la tabla:
  ```jinja
  {% for cita in citas.items %}
      <tr>
          <td>{{ cita.paciente.nombre }}</td>
          <td>{{ cita.fecha }}</td>
      </tr>
  {% endfor %}
  ```
- **Condicionales (If)**: Para mostrar estados diferentes o mensajes si no hay datos:
  ```jinja
  {% if citas.items %}
      <!-- Mostrar tabla -->
  {% else %}
      <p>No hay citas agendadas.</p>
  {% endif %}
  ```

---

## 📝 2. Formularios y Captura de Datos

El sistema cuenta con formularios modernos vinculados directamente a la base de datos:

### **Formulario de Nueva Cita (`nueva.html`)**
- **Campos**: Selectores para Paciente y Médico (cargados dinámicamente desde la BD), fecha, hora y motivo.
- **Método POST**: Los formularios envían la información de forma segura al servidor usando `method="POST"`.
- **Validación**: Atributos como `required` en los inputs aseguran que no se envíen campos vacíos.

### **Formulario de Edición (`editar.html`)**
- **Precarga**: Usa Jinja2 para rellenar los campos con la información actual de la cita: 
  `value="{{ cita.motivo }}"`.
- **Estado**: Incluye un selector para cambiar el estado de la cita (Pendiente, Confirmada, Cancelada, Completada).

---

## 🔘 3. Botones y Llamadas a la Acción

Se han definido estilos consistentes para facilitar la navegación:

- **`.btn-primary`**: Botones principales (color verde/clínico) para "Agendar" o "Guardar".
- **`.btn-secondary`**: Botones de "Cancelar" o "Volver" con colores más tenues.
- **`.btn-action`**: Iconos pequeños en la tabla para acciones rápidas:
    - 👁️ (Ver detalles)
    - ✏️ (Editar)
    - 🗑️ (Eliminar - incluye una alerta de confirmación en JS).

---

## 🛣️ 4. Rutas y Enlaces entre Páginas

El flujo de navegación está diseñado para ser intuitivo (Navegación Circular):

| Origen | Acción/Botón | Destino | Propósito |
| :--- | :--- | :--- | :--- |
| **Inicio** | "Agendar Cita" | `/citas/nueva` | Crear una nueva entrada. |
| **Inicio** | "Ver Citas" | `/citas/` | Listado general. |
| **Listado** | 👁️ (Detalles) | `/citas/detalles/<id>` | Ver info completa de una cita. |
| **Listado** | ✏️ (Editar) | `/citas/editar/<id>` | Modificar una cita existente. |
| **Formularios** | "Cancelar" | `/citas/` | Volver al listado sin cambios. |

---

## 💎 5. Estética y Diseño (Glassmorphism)

El frontend utiliza **Vanilla CSS** con un diseño "Glassmorphism" (efecto cristal):
- **Transparencias**: Uso de `rgba(255, 255, 255, 0.1)` y `backdrop-filter: blur()`.
- **Iconografía**: Uso de emojis para una interfaz más amigable y clara.
- **Responsividad**: El diseño se ajusta automáticamente para ser usable en computadoras y celulares.

---
**Nota:** El sistema ha sido renombrado recientemente a **Clínica Piedrazul**, reflejando este cambio en el título y el pie de página de todas las vistas.
