import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

__all__ = ["esperar_segundos", "esperar_por_elemento", "esperar_por_clickable"]


def esperar_segundos(segundos: int):
    """
    Pausa la ejecución de forma explícita.

    Parámetros:
    - segundos: segundos a esperar.
    """
    time.sleep(segundos)


def esperar_por_elemento(driver, by, selector, timeout=30):
    """
    Espera hasta que un elemento esté presente en el DOM y sea visible.

    Parámetros:
    - driver: instancia de WebDriver
    - by: estrategia de búsqueda (By.ID, By.XPATH, etc.)
    - selector: selector correspondiente
    - timeout: tiempo máximo de espera en segundos (default=30)

    Retorna:
    - WebElement encontrado o lanza TimeoutException
    """
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, selector))
    )


def esperar_por_clickable(driver, by, selector, timeout=30):
    """
    Espera hasta que un elemento sea clickable.

    Parámetros:
    - driver: instancia de WebDriver
    - by: estrategia de búsqueda
    - selector: selector correspondiente
    - timeout: tiempo máximo de espera (default=30)

    Retorna:
    - WebElement clickable o lanza TimeoutException
    """
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, selector))
    )
