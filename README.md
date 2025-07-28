# youtube-mp3-bot

🎵 Script en Python que automatiza la descarga de audio MP3 desde enlaces de YouTube usando Selenium.

## ¿Qué hace?

- Lee enlaces de un archivo `.txt`
- Extrae automáticamente el ID de cada video
- Abre un sitio web de conversión (`utomp3.com`)
- Automatiza clics para convertir y descargar el audio
- Guarda el MP3 en la carpeta del proyecto

## Tecnologías usadas

- Python 🐍
- Selenium (automatización de navegador)
- Regex para extraer IDs de YouTube
- WebDriver (Chrome)

## Requisitos

- Python 3.7 o superior
- `chromedriver` disponible en tu PATH
- Instala dependencias con:

```bash
pip install -r requirements.txt
