# mi-primer-hola-mundo-cloud

# Taller Práctico: Mi Primer Hola Mundo con Inteligencia Artificial en la Nube

Este repositorio contiene la estructura completa de una aplicación web interactiva que funciona como un Traductor Inteligente de Modismos Regionales. Aprendemos a desplegar servidores en la nube y conectar modelos de Inteligencia Artificial en tiempo real.

## Conceptos Clave del Taller

* Computación en la Nube: Uso de infraestructura virtual (Google Cloud Shell) para ejecutar código sin depender de recursos locales.
* APIs y API Keys: Mecanismos de comunicación segura para consumir servicios externos.
* Modelos de Lenguaje: Implementación de Gemini 2.5 Flash para tareas de procesamiento de texto inmediato.

## Estructura del Proyecto

* asistente.py: Servidor lógico construido con el microframework Flask.
* templates/index.html: Interfaz web de usuario diseñada con HTML5 y estilos CSS integrados.

## Requisitos de Instalación

Dentro de la consola de Cloud Shell, se debe asegurar la instalación del entorno web ejecutando:

pip3 install flask

## Configuración y Despliegue

1. Generar una API Key gratuita en Google AI Studio seleccionando la opción de crear en un proyecto nuevo independiente.
2. Configurar la credencial en la consola del sistema operativo:
   export API_KEY='TU_LLAVE_AQUI'
3. Iniciar el servidor web de la aplicación:
   python3 asistente.py
4. Visualizar los resultados haciendo clic en el menú superior de Cloud Shell en la opción Vista previa en la Web usando el puerto 8080.
