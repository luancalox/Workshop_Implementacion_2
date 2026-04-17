import os
from dotenv import load_dotenv
from openai import OpenAI
from retriever import retrieve_chunks

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
CHAT_MODEL = "gpt-4o-mini"

def answer_question(question: str, top_k: int = 6, threshold: float = 0.70):

    # 🔎 1) Retrieval
    chunks = retrieve_chunks(question, top_k=top_k, threshold=threshold)

    if not chunks:
        return "No encontré información relevante en la base de conocimiento."

    # 📚 2) Construir contexto
    context = "\n\n---\n\n".join([c["content"] for c in chunks])

    # 🤖 3) Llamar al LLM
    messages = [
        {
            "role": "system",
            "content": (
                "Responde únicamente usando el contexto proporcionado. "
                "Si no encuentras la respuesta en el contexto, indícalo claramente."
            )
        },
        {
            "role": "user",
            "content": f"CONTEXTO:\n{context}\n\nPREGUNTA:\n{question}"
        }
    ]

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=messages,
        temperature=0.2
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    pregunta = input("Haz tu pregunta: ")
    respuesta = answer_question(pregunta)

    print("\n=== RESPUESTA ===\n")
    print(respuesta)


