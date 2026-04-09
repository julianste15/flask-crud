# Sistema de Gestión de Citas Médicas - Flask CRUD

Este proyecto es una aplicación web desarrollada con **Flask** utilizando el patrón de arquitectura **Modelo-Vista-Controlador (MVC)**. Ha sido diseñado para gestionar citas médicas de manera eficiente con un enfoque en una interfaz de usuario premium y responsiva.

## Características Principales

*   **Arquitectura Modular**: Uso de Blueprints para organizar las rutas de forma escalable.
*   **Interfaz Premium**: Diseño moderno con efectos de glassmorphism, modo oscuro y tipografía Inter.
*   **Vistas de Gestión (CRUD)**:
    *   **Listado**: Visualización clara de citas con estados diferenciados por colores.
    *   **Creación**: Formulario intuitivo para añadir nuevas citas.
    *   **Edición**: Capacidad de modificar registros existentes con carga de datos dinámica.
*   **Arquitectura MVC Real**: Integración completa con base de datos SQLite usando SQLAlchemy ORM.

## Estructura del Proyecto

```text
Flask-crud/
├── app.py              # Punto de entrada de la aplicación (Factory Pattern)
├── routes/             # Controladores y lógica de ruteo (Blueprints)
│   ├── main.py         # Rutas generales e inicio
│   └── citas.py        # Rutas específicas para el módulo de citas
├── models/             # Estructura para modelos de datos (SQLAlchemy)
├── static/             # Archivos estáticos (CSS, imágenes)
│   └── css/style.css   # Estilos premium personalizados
└── templates/          # Vistas (Jinja2)
    ├── base.html       # Plantilla base con navegación
    ├── index.html      # Página de inicio
    └── citas/          # Módulo de citas (lista, nueva, editar)
```

## Requisitos e Instalación

Para ejecutar este proyecto localmente, asegúrate de tener Python instalado y sigue estos pasos:

1.  **Instala las dependencias**:
    ```bash
    pip install flask
    ```

2.  **Inicia el servidor**:
    ```bash
    python app.py
    ```

3.  **Accede a la aplicación**:
    Abre tu navegador en [http://127.0.0.1:5000](http://127.0.0.1:5000).

---
**Documentación adicional**:
- [ARCHITECTURE.md](ARCHITECTURE.md): Detalle de la arquitectura MVC.
- [EXPLICACION_FRONTEND.md](EXPLICACION_FRONTEND.md): Guía sobre el uso de Jinja2 y componentes visuales.
- [QUICKSTART.md](QUICKSTART.md): Guía rápida para ejecutar el proyecto.
