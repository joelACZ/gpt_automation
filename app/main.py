# app/main.py
import sys
from pathlib import Path

# ✅ Agrega raíz del proyecto al sys.path ANTES de los imports
sys.path.append(str(Path(__file__).resolve().parent.parent))

from core.navegador.launch_browser import launch_browser
from core.auth.login_email import ingresar_email
from core.auth.login_password import ingresar_password
from core.chatgpt.send_prompt import enviar_prompt
from core.chatgpt.extract_response import obtener_respuesta
from utils.waits import esperar_segundos


def main():
    # 1. Lanzar navegador Brave
    driver = launch_browser()

    # 2. Navegar a ChatGPT login
    driver.get("https://auth.openai.com/log-in")
    esperar_segundos(20)

    # 3. Ingreso de credenciales
    email = "tu_email@example.com"
    password = "tu_contraseña_segura"

    ingresar_email(driver, email)
    esperar_segundos(3)

    ingresar_password(driver, password)
    esperar_segundos(10)

    # 4. Enviar prompt a ChatGPT
    prompt = "¿Qué es la inteligencia artificial?"
    enviar_prompt(driver, prompt)
    esperar_segundos(15)

    # 5. Extraer respuesta
    respuesta = obtener_respuesta(driver)
    print("\nRespuesta generada:\n")
    print(respuesta)

    # Mantener navegador abierto
    input("\nPresiona Enter para cerrar el navegador...")
    driver.quit()


if __name__ == "__main__":
    main()
