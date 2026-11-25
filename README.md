# USM Tutor IA Agéntico

Prueba de Concepto desarrollada para el proyecto **Estrategia Institucional de IA para el Aprendizaje** de la Universidad Técnica Federico Santa María.

El objetivo es diseñar un tutor basado en Inteligencia Artificial que apoye el aprendizaje activo del estudiante, evitando entregar respuestas directas y utilizando preguntas, pistas y retroalimentación para guiar su razonamiento.

## Estado actual (Entrega Final PoC)

Actualmente la Prueba de Concepto incluye:

- **Interfaz de chat interactiva** desarrollada con **Streamlit**.
- **Integración con la API de Groq** con selección automática de modelos estables de baja latencia y control de tokens.
- **Academic RAG (Repositorio del Curso):** Carga, indexación y recuperación de fragmentos desde documentos oficiales (`PDF`, `TXT`, `MD`) para fundamentar las pistas en el material de la asignatura y mitigar alucinaciones.
- **Tutoría Socrática Activa:** Prompt de sistema orientado al aprendizaje activo que evalúa el razonamiento, entrega pistas progresivas y bloquea respuestas directas.
- **Arquitectura Híbrida Desacoplada:** Separación entre la gestión local de documentos/interfaz y el procesamiento externo mediante API.
- **Historial de conversación** persistente durante la sesión y delimitación explícita de capacidades y límites de la plataforma.

## Tecnologías

- Python
- Streamlit
- Groq API
- PyPDF (extracción y fragmentación de texto para RAG)
- Modelos de Lenguaje (LLM)

## Ejecución local

Instalar las dependencias:

```bash
pip install streamlit groq pypdf
```

Ejecutar la aplicación:

```bash
streamlit run app.py
```

Luego ingresar una API Key válida de Groq desde el panel lateral de la aplicación y, opcionalmente, cargar un apunte o guía del curso (`PDF`, `TXT` o `MD`) para activar el contexto RAG.

## Próximos Pasos (Fase 2 - Escalamiento Institucional)

- Integración nativa con plataformas educativas institucionales (Aula USM).
- Soporte multimodal (OCR y visión) para analizar diagramas y ejercicios manuscritos.
- Modelo persistente del estudiante para seguimiento de progreso y evaluación continua del razonamiento.
- Middleware institucional con anonimización automática de datos sensibles, *guardrails* avanzados y dashboard de métricas docentes.

## Objetivo Final

Construir un ecosistema institucional de IA donde el estudiante pueda utilizar Inteligencia Artificial como una herramienta de aprendizaje y acompañamiento, en lugar de utilizarla únicamente para obtener respuestas o realizar automáticamente sus tareas.

---
Proyecto académico — TEL342, Universidad Técnica Federico Santa María.

