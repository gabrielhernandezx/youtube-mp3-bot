#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_codigo_video(url_youtube):
    patron = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]+)'
    match = re.search(patron, url_youtube)
    return match.group(1) if match else None

def procesar_enlaces(enlaces):
    for url_youtube in enlaces:
        codigo_video = obtener_codigo_video(url_youtube)

        if codigo_video:
            url_sitio_web = f"https://utomp3.com/es/youtube/{codigo_video}"
            print("Procesando enlace:", url_sitio_web)

            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            prefs = {'download.default_directory': os.getcwd()}
            options.add_experimental_option('prefs', prefs)
            driver = webdriver.Chrome(options=options)

            driver.get(url_sitio_web)

            try:
                boton_convertir = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//button[contains(@onclick,'convertFile(0)')]"))
                )
                boton_convertir.click()

                boton_descargar = WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.ID, "asuccess"))
                )
                boton_descargar.click()

                time.sleep(10)
            finally:
                driver.quit()
        else:
            print("❌ No se pudo obtener el código del video de la URL:", url_youtube)

def main():
    archivo_enlaces = 'enlaces_youtube.txt'
    if os.path.exists(archivo_enlaces):
        with open(archivo_enlaces, 'r') as file:
            enlaces = [line.strip() for line in file.readlines()]
        procesar_enlaces(enlaces)
    else:
        print(f"❗ El archivo '{archivo_enlaces}' no existe.")

if __name__ == "__main__":
    main()
