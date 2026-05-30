from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

historique = []

@app.route("/")
def accueil():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("message", "")
    system = data.get("system", "Tu es EduBot, assistant pedagogique pour etudiants ingenieurs. Reponds en francais.")

    historique.append({"role": "user", "content": question})

    reponse = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3.2:1b",
            "messages": [
                {"role": "system", "content": system},
                *historique
            ],
            "stream": False
        },
        timeout=60
    )

    texte = reponse.json()["message"]["content"]
    historique.append({"role": "assistant", "content": texte})
    return jsonify({"reponse": texte})

if __name__ == "__main__":
    app.run(debug=True)