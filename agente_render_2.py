import requests

# 🔗 URL de tu servicio en Render
API_URL = "https://rag-render-i9mk.onrender.com/chat"

def answer_question(question: str, top_k: int = 6, threshold: float = 0.70):
    
    payload = {
        "question": question,
        "top_k": top_k,
        "threshold": threshold
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=60)

        if response.status_code != 200:
            return f"Error {response.status_code}: {response.text}"

        return response.json().get("answer")

    except Exception as e:
        return f"Error conectando con la API: {str(e)}"


if __name__ == "__main__":
    pregunta = input("Haz tu pregunta: ")
    respuesta = answer_question(pregunta)

    print("\n=== RESPUESTA DESDE RENDER ===\n")
    print(respuesta)