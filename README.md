# Guía Paso a Paso: Mi Primer Hola Mundo con Inteligencia Artificial en la Nube

Este repositorio contiene el código y la guía de aprendizaje para construir un Traductor Inteligente de Modismos utilizando la infraestructura global de Google Cloud y los modelos de última generación de Gemini. 

El objetivo de este taller es aprender a desplegar servidores web en la nube y conectar servicios de Inteligencia Artificial mediante APIs de manera 100% gratuita.

---

## 1. Conceptos Fundamentales

Antes de iniciar, es importante comprender las tres herramientas que utilizaremos:

* Computación en la Nube: En lugar de instalar programas en tu computadora, alquilamos una máquina virtual con sistema Linux directamente en los servidores de Google a través del navegador.
* API y API Key: Una API es un puente de comunicación entre dos aplicaciones. La API Key funciona como una contraseña digital que nos identifica ante Google para usar sus modelos de IA.
* Gemini 2.5 Flash: El modelo de lenguaje de Google optimizado para tareas de alta velocidad y respuestas contextuales inmediatas.

---

## 2. Ruta Completa de Implementación

Sigue cada uno de los siguientes pasos en orden cronológico para construir y desplegar tu aplicación en la nube.

### Paso 1: Iniciar Sesión en la Plataforma de la Nube
1. Abre tu navegador e ingresa al portal oficial de administración: https://console.cloud.google.com/
2. Inicia sesión utilizando tu cuenta personal de Gmail.
3. Si es la primera vez que ingresas, el sistema te mostrará una ventana de bienvenida. Selecciona tu país de residencia, acepta los términos del servicio y haz clic en el botón de confirmación para continuar.

### Paso 2: Creación de un Proyecto de Trabajo
Para mantener tus aplicaciones organizadas, Google requiere estructurar todo dentro de proyectos independientes.
1. En la barra superior azul de la consola, haz clic en el menú desplegable de proyectos (se encuentra justo al lado del texto que dice Google Cloud).
2. En la esquina superior derecha de la ventana emergente, haz clic en el botón Proyecto nuevo.
3. En el campo de nombre del proyecto, escribe: taller-ia-cloud
4. Deja las demás opciones por defecto y haz clic en el botón azul Crear.
5. Espera unos segundos a que la notificación del sistema indique que el proyecto está listo. Vuelve a hacer clic en el menú desplegable superior y selecciona tu nuevo proyecto de la lista: taller-ia-cloud.

### Paso 3: Generación de la Credencial de Inteligencia Artificial
Para consumir los servicios de Gemini de forma gratuita sin activar tarjetas de crédito ni sistemas de facturación prepago, debemos generar una llave limpia.
1. Abre una nueva pestaña en tu navegador e ingresa directamente al entorno de desarrollo de inteligencia artificial: https://aistudio.google.com/
2. Haz clic en el botón azul del menú lateral izquierdo que dice Create API key (Crear llave API).
3. Punto Crucial: Verás una opción que dice "Create API key in new project" (Crear llave API en un proyecto nuevo). Haz clic en ella. Esto forzará al sistema a mantenerte dentro de los límites del Plan Gratuito puro.
4. Una vez generado el código alfanumérico largo, haz clic en el botón Copy (Copiar) y mantenlo guardado en tu portapapeles.

### Paso 4: Activación de la Terminal Virtual (Cloud Shell)
1. Regresa a la pestaña del navegador donde tienes abierta la Consola de Google Cloud.
2. En la barra de herramientas de la esquina superior derecha, busca y haz clic en el icono de Activar Cloud Shell (tiene el símbolo gráfico >_).
3. En el panel inferior que se despliega, haz clic en Continuar. El sistema tardará unos segundos en encender y conectarte a una máquina virtual Linux completamente equipada de forma gratuita.

### Paso 5: Configuración de Variables de Entorno
Para que tu código de programación pueda usar la credencial de IA sin exponerla públicamente dentro del archivo de texto, la guardaremos en la memoria temporal de la terminal.
1. En la consola negra de Cloud Shell, escribe el siguiente comando, asegurándote de reemplazar el texto genérico por tu código largo copiado de AI Studio (mantén las comillas simples):
   export API_KEY='TU_LLAVE_DE_AI_STUDIO'
2. Presiona la tecla Enter para confirmar la variable en el sistema operativo.

### Paso 6: Estructuración y Descarga de Dependencias
Para transformar un script simple en una página web interactiva utilizaremos Flask, un microframework de desarrollo web para Python.
1. Ejecuta el gestor de paquetes de Python en la terminal para descargar la librería oficial:
   pip3 install flask
2. Crea la estructura ordenada de carpetas necesaria para separar el diseño visual de la lógica del servidor:
   mkdir -p templates

### Paso 7: Creación de los Archivos del Proyecto
Utilizaremos el Editor de Código integrado en la consola para una gestión visual y cómoda de los archivos.
1. En la barra superior de Cloud Shell, haz clic en el botón Open Editor (Abrir editor). Esto dividirá tu pantalla para mostrar un explorador visual de archivos en la parte superior.
2. En el panel izquierdo del explorador de archivos, localiza tu directorio raíz de trabajo. Haz clic derecho y selecciona la opción de crear un nuevo archivo de texto. Nómbralo: asistente.py
3. Abre el archivo asistente.py recién creado y pega el siguiente código lógico de Python:

```python
import os
import subprocess
import json
from flask import Flask, request, render_template

app = Flask(__name__)

# Extraemos de forma segura la credencial guardada en la terminal
api_key = os.environ.get("API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    respuesta = None
    error = None

    if request.method == "POST":
        frase = request.form.get("frase")
        
        # Generamos la llamada directa por consola usando el protocolo seguro cURL
        # Apuntamos a la ruta de producción v1 y al modelo estable gemini-2.5-flash
        comando = [
            'curl', '-s', '-X', 'POST',
            f'[https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key=](https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key=){api_key}',
            '-H', 'Content-Type: application/json',
            '-d', json.dumps({
                "contents": [{
                    "parts": [{"text": f"Explica de forma muy corta, divertida y en un solo párrafo qué significa la siguiente frase o palabra: '{frase}'"}]
                }]
            })
        ]

        try:
            # Ejecutamos el subproceso en el sistema operativo Linux subyacente
            resultado = subprocess.run(comando, capture_output=True, text=True)
            datos = json.loads(resultado.stdout)
            
            if 'candidates' in datos:
                respuesta = datos['candidates'][0]['content']['parts'][0]['text']
            else:
                error = f"El servidor de Google rechazó la petición: {datos.get('error', {}).get('message', 'Error de cuota o configuración')}"
        except Exception as e:
            error = f"Error interno del sistema: {str(e)}"

    return render_template("index.html", respuesta=respuesta, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
