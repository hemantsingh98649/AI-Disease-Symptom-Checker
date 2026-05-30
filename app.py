
import groq
from flask import Flask, request, jsonify
from flask_cors import CORS
from pyngrok import ngrok
import threading

API_KEY = "your_groq_key_here"

client = groq.Groq(api_key=API_KEY)
app = Flask(__name__)
CORS(app)
