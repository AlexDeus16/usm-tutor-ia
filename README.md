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

  ## Funcionalidades Implementadas (Entrega Final PoC)

* **Tutoría Socrática Activa:** Guía paso a paso mediante preguntas y pistas conceptuales, bloqueando la entrega de respuestas directas.
* **Academic RAG (Repositorio del Curso):** Indexación y recuperación de fragmentos desde documentos oficiales (`PDF`, `TXT`, `MD`) para acotar las respuestas al material de la asignatura y mitigar alucinaciones.
* **Arquitectura Híbrida Desacoplada:** Interfaz local en Streamlit conectada a servicios LLM externos vía API de Groq con selección automática de modelos de baja latencia.

## Próximos Pasos (Fase 2 - Escalamiento Institucional)

* Integración nativa con plataformas educativas institucionales (Aula USM).
* Soporte multimodal (OCR y visión) para analizar diagramas y ejercicios manuscritos.
* Modelo persistente del estudiante para seguimiento de progreso y evaluación continua del razonamiento.
* Middleware institucional con anonimización automática de datos sensibles, *guardrails* avanzados y dashboard de métricas docentes.

## Objetivo Final

Construir un ecosistema institucional de IA donde el estudiante pueda utilizar Inteligencia Artificial como una herramienta de aprendizaje y acompañamiento, en lugar de utilizarla únicamente para obtener respuestas o realizar automáticamente sus tareas.

---
Proyecto académico — TEL342, Universidad Técnica Federico Santa María.

## Objetivo final

Construir un ecosistema institucional de IA donde el estudiante pueda utilizar Inteligencia Artificial como una herramienta de aprendizaje y acompañamiento, en lugar de utilizarla únicamente para obtener respuestas o realizar automáticamente sus tareas.

---

Proyecto académico — TEL342, Universidad Técnica Federico Santa María.
