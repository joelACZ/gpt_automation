# core/navegador/launch_browser.py

from selenium import webdriver
from core.navegador.config_browser import get_browser_config


def launch_browser():
    """
    Inicializa y devuelve una instancia del navegador Brave,
    configurada mediante opciones y servicio definidos previamente.
    """
    options, service = get_browser_config()
    driver = webdriver.Chrome(service=service, options=options)
    return driver
