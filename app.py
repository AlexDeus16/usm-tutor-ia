import streamlit as st
from groq import Groq
from pypdf import PdfReader
import re

# Configuración de la página
st.set_page_config(page_title="USM - Tutor IA Agéntico", page_icon="🎓")
st.title("USM - Tutor IA Agéntico")
st.subheader("Prueba de Concepto - Arquitectura Híbrida con Academic RAG")

MODELOS_ESTABLES = [
    "openai/gpt-oss-20b",
    "llama-3.1-8b-instant",
    "llama-3.3-70b-versatile",
    "openai/gpt-oss-120b"
]

def fragmentar_texto(texto, tamano_fragmento=700, solapamiento=100):
    """Divide el texto extraído del documento en fragmentos manejables."""
    palabras = texto.split()
    fragmentos = []
    paso = tamano_fragmento - solapamiento
    for i in range(0, len(palabras), paso):
        fragmento = " ".join(palabras[i:i + tamano_fragmento])
        if fragmento.strip():
            fragmentos.append(fragmento)
    return fragmentos

def recuperar_contexto(pregunta, fragmentos, top_k=2):
    """Recupera los fragmentos más relevantes o un panorama inicial si piden resumen."""
    if not fragmentos:
        return ""
    
    pregunta_lower = pregunta.lower()
    if any(p in pregunta_lower for p in ["resumen", "trata", "leer", "leíste", "subí", "archivo", "pdf", "documento"]):
        return "\n---\n".join(fragmentos[:3])

    palabras_clave = set(re.findall(r"\b\w{4,}\b", pregunta_lower))
    if not palabras_clave:
        return "\n---\n".join(fragmentos[:top_k])

    puntuados = []
    for frag in fragmentos:
        frag_lower = frag.lower()
        puntaje = sum(1 for palabra in palabras_clave if palabra in frag_lower)
        puntuados.append((puntaje, frag))

    puntuados.sort(key=lambda x: x[0], reverse=True)
    mejores = [frag for puntaje, frag in puntuados[:top_k] if puntaje > 0]
    if not mejores:
        mejores = fragmentos[:2]
    return "\n---\n".join(mejores)

# --- PANEL LATERAL ---
api_key = st.sidebar.text_input("Ingresa API Key de Groq", type="password")
modelo_activo = None

if api_key:
    try:
        client = Groq(api_key=api_key)
        modelos_disponibles = [m.id for m in client.models.list().data]
        for modelo in MODELOS_ESTABLES:
            if modelo in modelos_disponibles:
                modelo_activo = modelo
                break
        if modelo_activo:
            st.sidebar.success("Conectado al servidor de Groq")
        else:
            st.sidebar.error("No se encontró un modelo de chat disponible.")
    except Exception as e:
        st.sidebar.error(f"Error al validar la llave: {e}")

st.sidebar.divider()
st.sidebar.markdown("### Repositorio Académico (RAG)")
archivo_subido = st.sidebar.file_uploader(
    "Sube un apunte o guía del curso (PDF, TXT, MD)",
    type=["pdf", "txt", "md"]
)

if "fragmentos_rag" not in st.session_state:
    st.session_state.fragmentos_rag = []
    st.session_state.nombre_archivo = None

if archivo_subido is not None:
    if st.session_state.nombre_archivo != archivo_subido.name:
        try:
            texto_completo = ""
            if archivo_subido.name.lower().endswith(".pdf"):
                lector = PdfReader(archivo_subido)
                for pagina in lector.pages:
                    extraido = pagina.extract_text()
                    if extraido:
                        texto_completo += extraido + "\n"
            else:
                texto_completo = archivo_subido.read().decode("utf-8", errors="ignore")

            st.session_state.fragmentos_rag = fragmentar_texto(texto_completo)
            st.session_state.nombre_archivo = archivo_subido.name
        except Exception as e:
            st.sidebar.error(f"No se pudo leer el archivo: {e}")

    if st.session_state.fragmentos_rag:
        st.sidebar.info(
            f"Documento indexado: {st.session_state.nombre_archivo} "
            f"({len(st.session_state.fragmentos_rag)} fragmentos)"
        )
else:
    st.session_state.fragmentos_rag = []
    st.session_state.nombre_archivo = None

# --- HISTORIAL DE CONVERSACIÓN ---
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

for msg in st.session_state.mensajes:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --- ENTRADA DEL ESTUDIANTE ---
if prompt := st.chat_input("Escribe tu duda aquí..."):
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.mensajes.append({"role": "user", "content": prompt})

    if api_key and modelo_activo:
        contexto_recuperado = recuperar_contexto(prompt, st.session_state.fragmentos_rag)

        capacidades_plataforma = (
            "Capacidades y límites de esta plataforma USM: El estudiante SÍ puede subir apuntes o guías "
            "en formato PDF, TXT o MD usando el panel lateral izquierdo ('Repositorio Académico (RAG)'). "
            "Sin embargo, esta Prueba de Concepto NO soporta imágenes, audio ni videos (solo texto extraído de documentos). "
            "Si te preguntan si pueden subir archivos o imágenes, explica exactamente estas capacidades y límites."
        )

        if contexto_recuperado:
            instruccion_sistema = (
                f"Eres un tutor académico de la USM. {capacidades_plataforma}\n"
                "Actualmente el estudiante YA subió un documento y el sistema RAG extrajo su contenido abajo. "
                "Reglas pedagógicas: Ayuda al estudiante a razonar activamente. NUNCA entregues respuestas "
                "directas a ejercicios ni hagas el trabajo completo por él. Basa tus pistas y orientaciones "
                "EXCLUSIVAMENTE en el siguiente material oficial del curso para evitar alucinaciones, "
                "haciendo preguntas socráticas para guiarlo.\n\n"
                f"CONTENIDO EXTRAÍDO DEL DOCUMENTO ({st.session_state.nombre_archivo}):\n{contexto_recuperado}"
            )
        else:
            instruccion_sistema = (
                f"Eres un tutor académico de la USM. {capacidades_plataforma}\n"
                "Actualmente no hay ningún documento cargado en el panel lateral. Si el alumno quiere trabajar "
                "sobre un apunte específico, invítalo a subir su PDF, TXT o MD a la izquierda. "
                "Reglas pedagógicas: Ayuda al estudiante a razonar activamente. NUNCA entregues la respuesta "
                "directa a un problema; identifica qué sabe, da pistas conceptuales y haz preguntas socráticas."
            )

        mensajes_api = [{"role": "system", "content": instruccion_sistema}] + st.session_state.mensajes

        try:
            respuesta = client.chat.completions.create(
                model=modelo_activo,
                messages=mensajes_api,
                temperature=0.3,
                max_tokens=600
            )

            msg_respuesta = respuesta.choices[0].message.content
            with st.chat_message("assistant"):
                if contexto_recuperado:
                    st.caption(f"Fuente consultada (RAG): {st.session_state.nombre_archivo}")
                st.write(msg_respuesta)

            st.session_state.mensajes.append({"role": "assistant", "content": msg_respuesta})
        except Exception as e:
            st.error(f"Error de conexión con el servidor: {e}")
            st.session_state.mensajes.pop()
    else:
        st.warning("Por favor, ingresa una API Key válida en el panel lateral.")