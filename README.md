# Guía Paso a Paso: Mi Primer Hola Mundo con Inteligencia Artificial en la Nube

Este repositorio contiene la guía de aprendizaje para construir un Traductor Inteligente de Modismos utilizando la infraestructura global de Google Cloud y los modelos de Inteligencia Artificial de Gemini. 

El objetivo de este taller es aprender a desplegar servidores web en la nube y conectar servicios de IA mediante APIs de manera 100% gratuita.

---

## 1. Conceptos Fundamentales

Antes de iniciar, es importante comprender las tres herramientas que utilizaremos hoy:

* Computación en la Nube: Uso de infraestructura virtual (Google Cloud Shell) para ejecutar código en servidores remotos sin depender de los recursos o la configuración de tu computadora local.
* APIs y API Keys: Mecanismos de comunicación segura para consumir servicios externos. La llave actúa como una contraseña digital que nos identifica ante Google.
* Gemini 2.5 Flash: El modelo de lenguaje de Google optimizado para tareas de alta velocidad y respuestas contextuales inmediatas.

---

## 2. Ruta Completa de Implementación

Sigue cada uno de los siguientes pasos en orden cronológico para construir y desplegar tu aplicación.

### Paso 1: Iniciar Sesión en la Plataforma de la Nube
1. Abre tu navegador e ingresa al portal de administración oficial: https://console.cloud.google.com/
2. Inicia sesión utilizando tu cuenta personal de Gmail.
3. Si es tu primera vez en la plataforma, selecciona tu país de residencia, acepta los términos de servicio del ecosistema de Google y confirma para continuar.

### Paso 2: Creación de un Proyecto de Trabajo
Para mantener tus aplicaciones organizadas, Google requiere estructurar todo dentro de proyectos independientes.
1. En la barra superior azul de la consola de Google Cloud, haz clic en el menú desplegable de proyectos (junto al texto "Google Cloud").
2. En la esquina superior derecha de la ventana emergente, selecciona el botón Proyecto nuevo.
3. En el campo de nombre del proyecto, escribe: taller-ia-cloud
4. Deja las demás opciones por defecto y haz clic en el botón azul Crear.
5. Espera unos segundos a que la notificación del sistema indique que el proyecto está listo. Vuelve a hacer clic en el menú desplegable superior y asegúrate de seleccionar taller-ia-cloud para empezar a trabajar en él.

### Paso 3: Generación de la Credencial de Inteligencia Artificial
Para consumir los servicios de Gemini de forma gratuita sin activar tarjetas de crédito ni sistemas de facturación, debemos generar una llave limpia.
1. Abre una nueva pestaña en tu navegador e ingresa al entorno de desarrollo de IA: https://aistudio.google.com/
2. Haz clic en el botón azul del menú lateral izquierdo que dice Create API key (Crear llave API).
3. Punto Crucial: Selecciona la opción "Create API key in new project" (Crear llave API en un proyecto nuevo). Esto forzará al sistema a mantenerte dentro de los límites del Plan Gratuito puro.
4. Una vez generado el código alfanumérico largo, haz clic en el botón Copy (Copiar) y mantenlo guardado temporalmente.

### Paso 4: Activación de la Terminal Virtual (Cloud Shell)
1. Regresa a la pestaña del navegador donde tienes abierta la Consola de Google Cloud.
2. En la barra de herramientas de la esquina superior derecha, busca y haz clic en el icono de Activar Cloud Shell (identificado con el símbolo gráfico >_).
3. En el panel inferior que se despliega, haz clic en Continuar. El sistema tardará unos segundos en encender y conectarte a una máquina virtual Linux completamente equipada de forma gratuita.

### Paso 5: Configuración de Variables de Envorno
Para que tu código de programación pueda usar la credencial de IA sin exponerla públicamente dentro del archivo de texto, la guardaremos en la memoria de la terminal.
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
3. Abre el archivo asistente.py recién creado y añade la lógica de control de Flask que se encarga de recibir los datos del formulario, realizar la petición HTTP mediante cURL hacia la API v1 de producción de Gemini usando el modelo gemini-2.5-flash, y renderizar la plantilla.
4. Ahora, expande la carpeta llamada templates en el menú izquierdo, haz clic derecho dentro de ella y genera un nuevo archivo llamado index.html
5. Añade dentro de templates/index.html la estructura HTML5 con el formulario de envío, las variables dinámicas de Flask para mostrar las respuestas de la IA o los errores, y los estilos CSS responsivos.

### Paso 8: Lanzamiento y Despliegue de la Web
1. Haz clic en el botón Open Terminal (Abrir terminal) en la barra superior para enfocarte de nuevo en la consola negra de comandos.
2. Enciende el servidor de desarrollo web ejecutando el intérprete de Python:
   python3 asistente.py
3. El sistema te indicará en texto que la aplicación ya se encuentra escuchando peticiones en el puerto 8080.
4. Dirígete a la barra superior del entorno de Cloud Shell, ubica el icono de Vista previa en la Web (representado por una pantalla con una lupa o flecha interna) y haz clic en él.
5. Selecciona la opción Vista previa en el puerto 8080.

El entorno abrirá una pestaña independiente en tu navegador web mostrando tu aplicación corriendo en internet. Escribe cualquier término regional, presiona el botón de envío y observa cómo la inteligencia artificial procesa los datos en tiempo real.

---

## 3. Instrucciones de Carga hacia GitHub

Una vez que compruebes que todo el sistema funciona sin errores, puedes subir tu código a tu cuenta personal de GitHub directamente desde la misma consola negra de Cloud Shell.

1. Detén el servidor web de desarrollo presionando la combinación de teclas Control + C.
2. Inicializa el gestor de versiones Git dentro de la carpeta del proyecto:
   git init
3. Configura tus datos básicos de firma de código (reemplaza los valores por tus credenciales de usuario de GitHub):
   git config --global user.email "tu-correo-registrado@gmail.com"
   git config --global user.name "TuNombreDeUsuarioDeGitHub"
4. Vincula tu terminal local con un repositorio remoto en la web de GitHub. Crea previamente un repositorio vacío en tu perfil web de GitHub llamado mi-primer-hola-mundo-ia, copia su dirección URL y ejecútalo en la terminal:
   git remote add origin https://github.com/TuNombreDeUsuarioDeGitHub/mi-primer-hola-mundo-ia.git
   git branch -M main
5. Prepara, empaqueta y confirma todos los archivos locales creados para el envío masivo:
   git add .
   git commit -m "Versión final del taller web de IA con Flask y HTML estructurado"
6. Empuja todo tu avance directamente hacia los servidores de GitHub:
   git push -u origin main
   (Nota de seguridad: Si la terminal te solicita la contraseña de acceso, debes ingresar tu Token de Acceso Personal de GitHub (PAT), ya que los servidores de Git no admiten el uso de contraseñas de texto plano tradicionales).
