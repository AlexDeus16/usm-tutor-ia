# USM Tutor IA Agéntico

Prueba de Concepto desarrollada para el proyecto **Estrategia Institucional de IA para el Aprendizaje** de la Universidad Técnica Federico Santa María.

El objetivo es diseñar un tutor basado en Inteligencia Artificial que apoye el aprendizaje activo del estudiante, evitando entregar respuestas directas y utilizando preguntas, pistas y retroalimentación para guiar su razonamiento.

## Estado actual

Actualmente la PoC incluye:

- Interfaz de chat desarrollada con **Streamlit**.
- Integración con la API de **Groq**.
- Selección dinámica de modelos disponibles.
- Historial de conversación durante la sesión.
- Prompt de sistema orientado al aprendizaje activo.
- Comportamiento de tutor basado en preguntas y pistas en lugar de respuestas directas.

## Tecnologías

- Python
- Streamlit
- Groq API
- Modelos de Lenguaje (LLM)

## Ejecución local

Instalar las dependencias:

```bash
pip install streamlit groq
```

Ejecutar la aplicación:

```bash
streamlit run app.py
```

Luego ingresar una API Key válida de Groq desde el panel lateral de la aplicación.

## Próximos pasos

El proyecto continuará incorporando progresivamente:

- Modelo del estudiante.
- Evaluación del razonamiento.
- Sistema RAG con contenido académico institucional.
- Guardrails y mitigación de prompt injection.
- Integración con plataformas educativas.
- Gestión segura de datos académicos.
- Evaluación de arquitectura cloud/híbrida.
- Métricas y trazabilidad de aprendizaje.

## Objetivo final

Construir un ecosistema institucional de IA donde el estudiante pueda utilizar Inteligencia Artificial como una herramienta de aprendizaje y acompañamiento, en lugar de utilizarla únicamente para obtener respuestas o realizar automáticamente sus tareas.

---

Proyecto académico — TEL342, Universidad Técnica Federico Santa María.
