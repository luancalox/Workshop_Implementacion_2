import requests
import streamlit as st

API_URL = "https://rag-y0fr.onrender.com/chat"

TOP_K = 5
THRESHOLD = 0.6

st.set_page_config(page_title="RAG Chat", page_icon="💬")
st.title("💬 Agente Conversacional con RAG")

# Input del usuario (desde la interfaz)
user_question = st.text_input("Escribe tu pregunta:")

if st.button("Enviar") and user_question.strip():

    with st.spinner("Procesando pregunta..."):
        try:
            payload = {
                "question": user_question,
                "top_k": TOP_K,
                "threshold": THRESHOLD
            }

            response = requests.post(API_URL, json=payload, timeout=90)

            if response.status_code == 200:
                answer = response.json().get("answer", "")
                st.success("Respuesta:")
                st.write(answer)
            else:
                st.error(f"Error {response.status_code}: {response.text}")

        except Exception as e:
            st.error(f"Error conectando con la API: {e}")