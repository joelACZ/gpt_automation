# core/chatgpt/extract_response.py

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from utils.waits import esperar_segundos


def obtener_respuesta(driver, timeout=30, poll_interval=1):
    """
    Espera hasta que la respuesta de ChatGPT aparezca y luego la extrae.

    Parámetros:
    - driver: instancia de WebDriver
    - timeout: tiempo máximo de espera en segundos
    - poll_interval: intervalo de sondeo en segundos

    Retorna:
    - Texto completo de la respuesta generada
    """
    elapsed = 0
    last_html = ""
    while elapsed < timeout:
        try:
            # Encontrar todos los bloques de Markdown (respuestas)
            bloques = driver.find_elements(By.CLASS_NAME, "markdown")
            if bloques:
                # Extraer texto del último bloque
                respuesta = bloques[-1].text
                # Validar que haya cambios (respuesta terminada)
                if respuesta and respuesta != last_html:
                    last_html = respuesta
                else:
                    # Esperar siguiente poll
                    pass
                # Comprobar indicio de fin (puede variar según UI)
                if not driver.find_elements(By.CLASS_NAME, "typing"):
                    return last_html
        except NoSuchElementException:
            # continuar esperando
            pass
        esperar_segundos(poll_interval)
        elapsed += poll_interval

    print(f"[!] Tiempo de espera ({timeout}s) agotado al extraer respuesta.")
    return last_html
