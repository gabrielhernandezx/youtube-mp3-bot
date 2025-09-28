# youtube-mp3-bot

Bot en Python que automatiza la descarga de audio en formato MP3 desde videos de YouTube mediante Selenium.

## 📋 Funcionalidades

- Lee enlaces de YouTube desde un archivo `.txt`
- Extrae el ID del video
- Usa un sitio de conversión (por ejemplo `utomp3.com`) y maneja clics automáticos para convertir y descargar el MP3
- Guarda los archivos en carpeta de salida

## 🛠 Requisitos

- Python 3.7+
- Selenium (`pip install -r requirements.txt`)
- Chromedriver (o WebDriver compatible) en tu PATH

## 🚀 Uso

```bash
python youtube_mp3_bot.py enlaces_youtube.txt
````

*Ejemplo de enlaces_youtube.txt:*

```
https://www.youtube.com/watch?v=abcd1234
https://youtu.be/wxyz5678
```

## ⚠️ Advertencia legal

Este proyecto es solo con fines educativos. El descargado de contenido de YouTube puede violar los términos de servicio. Usa esta herramienta bajo tu propia responsabilidad y respetando derechos de autor.
