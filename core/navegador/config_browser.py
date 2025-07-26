# core/navegador/config_browser.py

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# === Configuración personalizada del navegador Brave ===

BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
DRIVER_PATH = (
    r"C:\Users\Ozmothz\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
)


def get_browser_config():
    """
    Devuelve los objetos configurados Options y Service
    para iniciar el navegador Brave vía ChromeDriver.
    """
    # Configuración de opciones del navegador
    options = Options()
    options.binary_location = BRAVE_PATH

    # (Opcional) Configuración adicional
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Inicialización del servicio ChromeDriver
    service = Service(executable_path=DRIVER_PATH)

    return options, service
