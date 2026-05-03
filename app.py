from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key="SUA_API_KEY_AQUI")

SYSTEM_PROMPT = """
Você é uma vendedora Especialista da Loja Desfrut.

Seu objetivo é vender de forma natural, elegante e envolvente.

Regras:
- Nunca responda seco
- Sempre faça uma pergunta
- Sempre tente sugerir produto
- Linguagem leve e sensual, nunca vulgar

Fluxo:
1. Entender cliente
2. Guiar
3. Sugerir
4. Estimular
5. Fechar
"""

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

if __name__ == "__main__":
    app.run()
