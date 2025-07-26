# core/chatgpt/send_prompt.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from utils.waits import esperar_segundos


def enviar_prompt(driver, prompt):
    """
    Localiza el área de texto de ChatGPT, ingresa el prompt y envía con Enter.
    """
    try:
        # Esperar carga del textarea
        esperar_segundos(2)
        # Encontrar el textarea principal
        textarea = driver.find_element(By.TAG_NAME, "textarea")
        textarea.clear()
        textarea.send_keys(prompt)
        esperar_segundos(1)
        textarea.send_keys(Keys.ENTER)
        print("[✓] Prompt enviado correctamente.")
    except NoSuchElementException:
        print("[✗] No se encontró el área de texto para enviar el prompt.")
