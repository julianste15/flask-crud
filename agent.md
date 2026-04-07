# Agente de Desarrollo - Antigravity

Este documento describe el rol y las decisiones tomadas por el asistente de IA durante el desarrollo de la estructura de este proyecto.

## Rol del Agente
Actué como un desarrollador de software experto, aplicando buenas prácticas de arquitectura (MVC) y diseño web moderno (Premium UI con Glassmorphism). Mi objetivo fue facilitar la creación de una base sólida y escalable para el sistema de Citas Médicas.

## Decisiones Arquitectónicas
1.  **Patrón MVC**: Se implementó una clara separación de responsabilidades:
    *   **Modelos**: Ubicados en `models/` para futura integración con bases de datos.
    *   **Vistas**: Utilizando Jinja2 en `templates/` con herencia de plantilla base.
    *   **Controladores**: Implementados mediante `Blueprints` en `routes/` para un ruteo modular.
2.  **Organización de Paquetes**: Uso de `__init__.py` para asegurar que el código sea tratable como módulos de Python.
3.  **Frontend Independiente**: Se diseñó el frontend para ser funcional y estéticamente superior antes de completar el backend, permitiendo la previsualización de datos mediante objetos *mock*.

## Stack Tecnológico Utilizado
*   **Lenguaje**: Python 3.x
*   **Backend**: Flask
*   **Frontend**: HTML5, CSS3 (Vanilla), Jinja2
*   **Tipografía**: Inter (Google Fonts)

## Compromiso con la Calidad
Cada archivo fue creado siguiendo estándares de limpieza de código (Clean Code) y optimizado para una experiencia de usuario (UX) fluida y atractiva.
