from flask_cors import CORS
from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Você é uma vendedora especialista da loja Desfrut.

Seu objetivo é vender de forma natural, elegante e envolvente.

Regras:
- Nunca responda seco
- Sempre faça uma pergunta
- Sempre tente sugerir produto
- Linguagem leve e sensual, nunca vulgar
"""

@app.route("/")
def home():
    return "IA Desfrut online"

@app.route("/perguntar", methods=["POST"])
def perguntar():
    data = request.json
    pergunta = data.get("pergunta")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": pergunta}
        ]
    )

    resposta = response.choices[0].message.content

    return jsonify({"resposta": resposta})
