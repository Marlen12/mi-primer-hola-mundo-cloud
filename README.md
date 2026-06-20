# Guía: Mi Primer Hola Mundo en la Nube

Guía práctica para desplegar un Traductor Inteligente de Modismos en la nube usando Flask y Gemini 2.5 Flash de forma gratuita.

---

## 1. Ruta de Implementación Paso a Paso

### Paso 1: Iniciar Sesión
1. Entra a la [Consola de Google Cloud](https://console.cloud.google.com/).
2. Inicia sesión con tu cuenta de Gmail.
3. Acepta los términos de servicio si es tu primera vez.

### Paso 2: Crear el Proyecto
1. Haz clic en el menú desplegable de proyectos en la barra superior azul.
2. Selecciona **Proyecto nuevo**.
3. Ponle como nombre: `hola-mundo-cloud` y haz clic en **Crear**.
4. En el mismo menú superior, selecciona el proyecto `hola-mundo-cloud` para activar tu entorno de trabajo.

### Paso 3: Activar Cloud Shell
1. Regresa a la Consola de Google Cloud.
2. Haz clic en el icono **Activar Cloud Shell** (`>_`) en la esquina superior derecha.
3. Selecciona **Continuar** y espera a que conecte la terminal.
4. Crea una carpeta: mkdir mi-pagina-web
5. Ingresa a la carpeta: cd mi-pagina-web
6. copia lo siguiente en la terminal:
```
echo '<html><body><h1>¡Hola Mundo desde Google Cloud!</h1><p>Mi primer taller en la nube completado :).</p></body></html>' > index.html
```
   
8. Enciende el servidor con:
```
python3 -m http.server 8080
```

##HOLA MUNDO con IA
### Paso 4: Obtener la API Key de Gemini
1. Entra a [Google AI Studio](https://aistudio.google.com/).
2. Haz clic en **Create API key** en el menú izquierdo.
3. Selecciona **"Create API key in new project"** para asegurar el Plan Gratuito.
4. Copia la clave alfanumérica generada.


### Paso 5: Configurar la Llave en la Terminal
1. En la terminal negra de abajo, guarda tu clave ejecutando:
```
export API_KEY='TU_LLAVE_DE_AI_STUDIO'
```

### Paso 6: Instalar Librerías y Crear el Código con Nano
1. Instala Flask corriendo este comando en la terminal:
```
pip3 install flask
```

2. Abre un archivo nuevo con el editor de terminal corriendo:
```
nano asistente.py
```
4. Pega todo el código del proyecto (el cual ya incluye tanto la lógica de Python como la interfaz de usuario en formato de texto plano).
5. Guarda y cierra presionando Control + O, luego Enter y finalmente Control + X.

### Paso 7: Desplegar la Web
1. Enciende el servidor ejecutando en tu terminal:
```
python3 asistente.py
```

2. En la barra superior de Cloud Shell, haz clic en Vista previa en la Web (icono de pantalla con lupa).
3. Selecciona Vista previa en el puerto 8080 para abrir tu página web en internet.
