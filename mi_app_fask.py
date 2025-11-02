from flask import Flask
import os

app = Flask(_name_)

@app.route('/')
def home():
    return "Hola, esta es mi red local de ejemplo!"

if _name_ == '_main_':
    # Usar el puerto que Render asigne, por defecto 5000 si no hay
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)