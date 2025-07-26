# core/auth/login_email.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from utils.waits import esperar_segundos


def ingresar_email(driver, email):
    """
    Localiza el input de email, lo rellena y presiona Enter.
    """
    try:
        # Intentar encontrar el campo por ID
        email_input = driver.find_element(By.ID, "username")
        email_input.clear()
        email_input.send_keys(email)
        esperar_segundos(1)
        email_input.send_keys(Keys.RETURN)
        print("[✓] Email ingresado correctamente.")
    except NoSuchElementException:
        print("[✗] No se encontró el campo de email.")
