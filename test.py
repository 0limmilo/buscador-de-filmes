from dotenv import load_dotenv
from flask import Flask, jsonify, request
import requests
import os

load_dotenv()
chave = os.getenv("CHAVE")

filme = "Spider-Man"

URL = f"https://www.omdbapi.com/?s={filme}&apikey={chave}"

ress = requests.get(URL)
date = ress.json()

print(date)