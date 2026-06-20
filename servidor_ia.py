import os
import subprocess
import json
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Recuperamos la llave gratuita que guardamos en la terminal
api_key = os.environ.get("API_KEY")

# Diseño visual de la página web (HTML + CSS limpio en un solo lugar)
PAGINA_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Primer Hola Mundo en la Nube</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; background-color: #f4f6f9; margin: 0; padding: 40px; text-align: center; }
        .container { max-width: 600px; background: white; margin: 0 auto; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h1 { color: #1a73e8; margin-bottom: 10px; }
        p.sub { color: #5f6368; margin-bottom: 30px; }
        input[type="text"] { width: 80%; padding: 12px; border: 2px solid #dadce0; border-radius: 8px; font-size: 16px; outline: none; transition: 0.3s; }
        input[type="text"]:focus { border-color: #1a73e8; }
        button { background-color: #1a73e8; color: white; border: none; padding: 12px 24px; font-size: 16px; border-radius: 8px; margin-top: 15px; cursor: pointer; transition: 0.3s; }
        button:hover { background-color: #1557b0; }
        .resultado { margin-top: 30px; padding: 20px; background-color: #e8f0fe; border-left: 5px solid #1a73e8; border-radius: 4px; text-align: left; }
        .error { margin-top: 30px; padding: 20px; background-color: #fce8e6; border-left: 5px solid #d93025; border-radius: 4px; color: #a51d24; text-align: left; }
    </style>
</head>
<body>
    <div class="container">
        <h1>¡Hola Mundo desde la Nube!</h1>
        <p class="sub">Taller en Build With AI Tarija</p>
        
        <form method="POST">
            <input type="text" name="frase" placeholder="Escribe un modismo (ej. saice, qué churo)..." required>
            <br>
            <button type="submit">Preguntar a Gemini IA</button>
        </form>

        {% if respuesta %}
            <div class="resultado">
                <strong>Respuesta de la IA:</strong>
                <p>{{ respuesta }}</p>
            </div>
        {% endif %}

        {% if error %}
            <div class="error">
                <strong>Detalle del inconveniente:</strong>
                <p>{{ error }}</p>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    respuesta = None
    error = None

    if request.method == "POST":
        frase = request.form.get("frase")
        
        # Conexión directa a la API v1 de Gemini con el modelo 2.5-flash
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

    return render_template_string(PAGINA_HTML, respuesta=respuesta, error=error)

if __name__ == "__main__":
    # Encendemos el servidor web en el puerto 8080 oficial de Google Cloud Shell
    app.run(host="0.0.0.0", port=8080)
