from flask import Flask, jsonify, request
import requests
import os

from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

app.json.sort_keys = False

chave = os.getenv("CHAVE")

@app.route("/filme")
def buscar_filme():
    filme = request.args.get("name")

    if not filme:
        return jsonify({"erro": "Envie o nome do filme"}), 400

    url = f"https://www.omdbapi.com/?t={filme}&apikey={chave}"
    ress = requests.get(url)
    date = ress.json()
    
    title = f"{date["Title"]}"
    genre = f"{date["Genre"]}"
    img = f"{date["Poster"]}"
    rating = f"{date["Ratings"][0]["Source"]} : { date["Ratings"][0]["Value"]}"

    return jsonify({
        "titulo": title,
        "genero": genre,
        "Imagem": img,
        "avaliacao": rating
    })
    
        

if __name__ == "__main__":
    app.run(debug=True)