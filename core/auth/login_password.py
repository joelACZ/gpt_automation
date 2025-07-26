# core/auth/login_password.py

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from utils.waits import esperar_segundos


def ingresar_password(driver, password):
    """
    Localiza el input de contraseña, lo rellena y presiona Enter.
    """
    try:
        # Intentar encontrar el campo de contraseña por ID
        pwd_input = driver.find_element(By.ID, "password")
        pwd_input.clear()
        pwd_input.send_keys(password)
        esperar_segundos(1)
        pwd_input.send_keys(Keys.RETURN)
        print("[✓] Contraseña ingresada correctamente.")
    except NoSuchElementException:
        print("[✗] No se encontró el campo de contraseña.")
