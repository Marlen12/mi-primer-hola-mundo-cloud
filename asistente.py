import os
import subprocess
import json
from flask import Flask, request, render_template

app = Flask(__name__)

# Extraemos la llave de la variable de entorno del sistema
api_key = os.environ.get("API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    respuesta = None
    error = None

    if request.method == "POST":
        frase = request.form.get("frase")
        
        # Consulta estructurada con cURL hacia la API de producción estable v1
        comando = [
            'curl', '-s', '-X', 'POST',
            f'https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={api_key}',
            '-H', 'Content-Type: application/json',
            '-d', json.dumps({
                "contents": [{
                    "parts": [{"text": f"Explica de forma muy corta, divertida y en un solo párrafo qué significa la siguiente frase o palabra: '{frase}'"}]
                }]
            })
        ]

        try:
            resultado = subprocess.run(comando, capture_output=True, text=True)
            datos = json.loads(resultado.stdout)
            
            if 'candidates' in datos:
                respuesta = datos['candidates'][0]['content']['parts'][0]['text']
            else:
                error = f"El servidor de Google rechazó la petición: {datos.get('error', {}).get('message', 'Error desconocido')}"
        except Exception as e:
            error = f"Error en la conexión interna: {str(e)}"

    # Buscara de forma automática el archivo index.html dentro de la carpeta templates
    return render_template("index.html", respuesta=respuesta, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
