import streamlit as st
from groq import Groq

# Configuración de la página
st.title("USM - Tutor IA Agéntico")
st.subheader("Prueba de Concepto - Arquitectura Híbrida")

api_key = st.sidebar.text_input("Ingresa API Key de Groq", type="password")

modelo_seleccionado = None

# Si hay API Key, consultamos directamente al servidor qué modelos están activos hoy
if api_key:
    try:
        client = Groq(api_key=api_key)
        modelos_servidor = client.models.list()
        # Filtramos modelos de audio (whisper) o moderación (guard) para dejar solo los de chat
        lista_modelos = [
            m.id for m in modelos_servidor.data 
            if "whisper" not in m.id.lower() and "guard" not in m.id.lower() and "tts" not in m.id.lower()
        ]
        modelo_seleccionado = st.sidebar.selectbox("Modelo activo en el servidor:", lista_modelos)
        st.sidebar.success("Conectado al servidor de Groq")
    except Exception as e:
        st.sidebar.error(f"Error al validar la llave: {e}")

if "mensajes" not in st.session_state:
    # System Prompt que define el comportamiento del agente
    st.session_state.mensajes = [
        {
            "role": "system",
            "content": (
                "Eres un tutor académico de la USM. Tu objetivo es ayudar al estudiante a razonar "
                "y aprender de forma activa. NUNCA entregues la respuesta directa a un problema. "
                "En su lugar, identifica qué sabe el alumno, detecta dónde está la dificultad, "
                "da pistas conceptuales y haz preguntas socráticas para guiarlo."
            )
        }
    ]

# Mostrar el historial del chat
for msg in st.session_state.mensajes:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# Interfaz de entrada
if prompt := st.chat_input("Escribe tu duda aquí..."):
    with st.chat_message("user"):
        st.write(prompt)
    
    st.session_state.mensajes.append({"role": "user", "content": prompt})
    
    if api_key and modelo_seleccionado:
        try:
            respuesta = client.chat.completions.create(
                model=modelo_seleccionado, # Usa el modelo real que entregó el servidor
                messages=st.session_state.mensajes,
                temperature=0.3
            )
            
            msg_respuesta = respuesta.choices[0].message.content
            with st.chat_message("assistant"):
                st.write(msg_respuesta)
            
            st.session_state.mensajes.append({"role": "assistant", "content": msg_respuesta})
        except Exception as e:
            # Si el primer modelo de la lista no es de chat, te avisa sin romper la página
            st.error(f"Este modelo específico ({modelo_seleccionado}) no admite chat directo. Selecciona otro en la lista de la izquierda. Detalle: {e}")
            st.session_state.mensajes.pop() # Limpia el mensaje fallido para no bloquear el historial
    else:
        st.warning("Por favor, ingresa una API Key válida en el panel lateral.")